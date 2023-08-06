"""A package for encoding and decoding weather dataset."""

import asyncio
import copy
import io
import os
import pickle
import random
import threading
import time
from collections import deque
from functools import partial
from time import perf_counter
from typing import (
    Any,
    BinaryIO,
    Deque,
    Dict,
    Generator,
    List,
    Optional,
    Tuple,
    TypeVar,
    Union,
)

import aiofiles
import numpy as np
import yaml

from seqrecord.utils import (
    CONSUMER_SLEEP_INTERVAL,
    PRODUCER_SLEEP_INTERVAL,
    FileManager,
    LRUCache,
    TimeTracker,
    WriterBuffer,
)

MAX_RECORDFILE_SIZE = 1e9  # 1e8, 100 mb, maximum size of a single record file

WSR = TypeVar("WSR", bound="WSeqRecord")

# todo: record file size and write buffer size, how to choose it, and tune it
# todo: test effect of caching


# todo: use azure uri and manage sources of storage account by ourselves (replica of dataset)
# todo: MISSING, some transform work, subsample etc. Need to make sure data is same as produced by existing dataset


def recordfileidx2path(recorddir: str, file_idx: int) -> str:
    return os.path.join(recorddir, f"record_{file_idx}.bin")


class _PrefetchData:
    def __init__(self, source_data_generator, buffer_size: int):
        self.run_prefetcher = True
        # python deque is thread safe for appends and pops from opposite sides.
        # ref: https://stackoverflow.com/questions/8554153/is-this-deque-thread-safe-in-python
        self.prefetch_buffer: Deque = deque()
        self.buffer_size: int = buffer_size
        self.source_data_generator = source_data_generator


class WSeqRecord:
    """A serialization protocal that stores a single continuous long sequence of weather data into record files, while provides metadata of each frame to enable efficient random access of frames."""

    def __init__(
        self,
        recorddir: str,
    ) -> None:
        """_summary_

        Args:
            recorddir (str): directory record files is placed
        """
        # folder that stores data in a separate directory (subfolder)
        self.recorddir: str = recorddir
        os.makedirs(self.recorddir, exist_ok=True)
        self.features_written = None
        self.num_bytes: int = 0  # number of bytes in current file
        # track the frame idx endpoints for each record file, [[start_idx, end_idx)], includes start, exclusive on end
        self.idx_range_of_files: List[Tuple[int, int]] = []
        # file object for current record file
        self.file_desc: Optional[BinaryIO] = None
        # serialization proto info of each data item
        self.metadata: Dict[int, dict] = {}
        # index of current data item to be processed
        self.frame_idx: int = 0

        # write buffer # todo: determine the size of write buffer
        self.write_buffer = WriterBuffer()
        self.timer = TimeTracker()

    # todo add append_item(), add new frames to existing dataset (probably saved already)
    # todo add preput worker
    def write_item(
        self,
        frame: Dict[str, np.ndarray],
    ) -> None:
        """write one frame data dict(feature->np.ndarray) into byte repr and write bytes into
        current file. It has to be called by users in a sequential order. Every key,value in frame will
        be written into file.

        #todo: add default settings, where features are all features in metadata[idx]

        Args:
            frame (Dict[str, np.ndarray]): feature to data (np.ndarray)
        """
        if self.features_written is None:
            self.features_written = [key for key in frame]
        file_idx = len(self.idx_range_of_files) - 1
        if self.num_bytes == 0:
            # new file
            self.idx_range_of_files.append([self.frame_idx])
            file_idx += 1
            self.file_desc = open(
                recordfileidx2path(self.recorddir, file_idx),
                mode="wb",
            )
            # todo: check here if we are appending, if it is, we need to open a new file

        # get file name and start position for frame
        self.metadata[self.frame_idx] = {
            "frame_idx": self.frame_idx,
            "file_idx": file_idx,
            "bytes_offset": self.num_bytes,
        }
        num_bytes_in_frame = 0
        for feature, data in frame.items():
            self.metadata[self.frame_idx][feature] = {
                "is_none": (
                    data.dtype == np.dtype("O") and data == None
                ),  # this feature is essentially missing, and
                "dtype": data.dtype,
                "shape": data.shape,
                "bytes_offset": num_bytes_in_frame,
                "nbytes": data.nbytes,
            }
            self.write_buffer.write(data.tobytes())
            num_bytes_in_frame += data.nbytes

        self.metadata[self.frame_idx]["nbytes"] = num_bytes_in_frame
        self.num_bytes += num_bytes_in_frame
        self.frame_idx += 1

        # if self.write_buffer.is_full():
        #     self.file_desc.write(self.write_buffer.getbuffer())
        #     self.write_buffer.clear()
        #     self.file_desc.flush()

        if self.num_bytes > MAX_RECORDFILE_SIZE:
            # current file is big enough
            self.num_bytes = 0
            self.idx_range_of_files[-1].append(self.frame_idx)
            self.file_desc.write(self.write_buffer.getbuffer())
            self.write_buffer.clear()
            self.file_desc.flush()
            self.file_desc.close()
        return

    def close_recordfile(self):
        """Close opened file descriptor!

        This needs to be called by user when finishes scanning over the dataset.
        """
        if len(self.idx_range_of_files[-1]) == 1:
            # the last record file has not reached maximum file size
            self.idx_range_of_files[-1].append(self.frame_idx)

            # write what's left in self.writer buffer
            self.file_desc.write(self.write_buffer.getbuffer())
            self.write_buffer.close()

        self.file_desc.close()
        self.write_buffer = None
        self.file_desc = None
        self.num_frames = self.frame_idx
        self.num_files = len(self.idx_range_of_files)

    def recordfile_generator(self, frame_generator: callable):
        try:
            write_buffer = WriterBuffer()
            num_bytes = 0
            self.idx_range_of_files = []
            frame_idx = 0
            file_idx = 0
            for frame in frame_generator:
                if self.features_written is None:
                    self.features_written = [key for key in frame]
                if num_bytes == 0:
                    # new file
                    self.idx_range_of_files.append([frame_idx])
                self.metadata[frame_idx] = {
                    "frame_idx": frame_idx,
                    "file_idx": file_idx,
                    "bytes_offset": num_bytes,
                }
                num_bytes_in_frame = 0
                for feature, data in frame.items():
                    self.metadata[frame_idx][feature] = {
                        "is_none": (
                            data.dtype == np.dtype("O") and data == None
                        ),  # this feature is essentially missing, and
                        "dtype": data.dtype,
                        "shape": data.shape,
                        "bytes_offset": num_bytes_in_frame,
                        "nbytes": data.nbytes,
                    }
                    write_buffer.write(data.tobytes())
                    num_bytes_in_frame += data.nbytes

                self.metadata[frame_idx]["nbytes"] = num_bytes_in_frame
                frame_idx += 1
                num_bytes += num_bytes_in_frame
                if num_bytes > MAX_RECORDFILE_SIZE:
                    # current file is big enough
                    num_bytes = 0
                    self.idx_range_of_files[-1].append(frame_idx)
                    write_buffer.clear()
                    yield (file_idx, write_buffer.getvalue())
                    file_idx += 1

            if len(self.idx_range_of_files[-1]) == 1:
                # there is content left in the write_buffer
                self.idx_range_of_files[-1].append(frame_idx)
                yield (file_idx, write_buffer.getvalue())
        finally:
            write_buffer.close()
            self.num_files = len(self.idx_range_of_files)
            self.num_frames = frame_idx

    def put_frame(self, frame_generator: callable, prefetch_buffer_size: int = 5):
        # should be only adding frames here
        # two threads this function keep writing and send them to buffer
        # a separate thread writes the buffer to files as long as the buffer is non-empty
        try:
            prefetch_data = _PrefetchData(
                self.recordfile_generator(frame_generator=frame_generator),
                prefetch_buffer_size,
            )
            thread = threading.Thread(
                target=WSeqRecord.prefetch_thread_worker,
                args=(prefetch_data,),
                daemon=True,
            )
            thread.start()
            while prefetch_data.run_prefetcher:
                if len(prefetch_data.prefetch_buffer) > 0:
                    file_idx, content = prefetch_data.prefetch_buffer.popleft()
                    with open(recordfileidx2path(self.recorddir, file_idx), "wb") as f:
                        f.write(content)
                else:
                    # TODO: Calculate sleep interval based on previous availability speed
                    time.sleep(CONSUMER_SLEEP_INTERVAL)
        finally:
            prefetch_data.run_prefetcher = False
            if thread is not None:
                thread.join()
                thread = None

    def read_frame(
        self,
        file_desc: Union[io.BufferedReader, BinaryIO],
        metadata_frame: Dict[str, Union[int, dict]],
        features: List[str],
    ) -> Dict[str, np.ndarray]:
        """Given record file descriptor and serialization proto of a single frame, return the
        decoded dictionary(feature->data(np.ndarray)) of the item.

        Args:
            file_desc (io.BufferedReader): python file object of the record file (required by numpy)
            metadata_frame (Dict[str, Any]): dict that contains meta info of a specific frame
            features (List[str]):  features requested for frame
        Returns:
            Dict[str, np.ndarray]: data
        """
        frame = {}
        frame_offset = metadata_frame["bytes_offset"]
        for feature in features:
            frame[feature] = np.memmap(
                file_desc,
                dtype=metadata_frame[feature]["dtype"],
                mode="r",
                offset=frame_offset + metadata_frame[feature]["bytes_offset"],
                shape=metadata_frame[feature]["shape"],
            )
        return frame

    def iterate_frames(
        self, features: List[str]
    ) -> Generator[Dict[str, np.ndarray], None, None]:
        """Iterate sequentially over frames in the dataset

        Args:
            features (List[str]): a list of feature names requested from frames

        Returns:
            _type_: _description_

        Yields:
            Generator[Dict[str, np.ndarray], None, None]: generates one-frame data
        """
        assert all(
            len(endpoints) == 2 for endpoints in self.idx_range_of_files
        ), "Record file endpoints are not complete!"

        for file_idx in range(self.num_files):
            file_desc = open(
                recordfileidx2path(self.recorddir, file_idx=file_idx), mode="rb"
            )
            endpoints = self.idx_range_of_files[file_idx]
            for idx in range(endpoints[0], endpoints[1]):
                frame = self.read_frame(file_desc, self.metadata[idx], features)

                yield {feature: frame[feature] for feature in features}
            file_desc.close()

    # todoL add prefetch using threads or asyncio
    # todo: test effect of caching on real data
    def iterate_frame_pairs(
        self,
        input_features: List[str],
        target_features: List[str],
        max_pred_steps: int,
        filedesc_cache_cap: int = 10,
        frame_cache_cap: int = 20,
    ) -> Generator[Dict[str, np.ndarray], None, None]:
        """Iterate frames over the whole dataset

        # todo: to think about, if we don't shuffle files, then cache based on frame idx is convenient and effective.
        Args:
            input_features [List[str]]: a list of features requested for input
            target_features [List[str]]: a list of features requested for target
            max_pred_steps [int]: maximum number of leap steps for predictive frame
        Yields:
            Generator[Dict[str, np.ndarray], None, None]: data item [feature->data]. All data items are being returned sequentially
        """
        file_manager = FileManager(
            fileidx2path=partial(recordfileidx2path, recorddir=self.recorddir),
            cache_capacity=filedesc_cache_cap,
        )
        # given that, input and target features do not overlap, we only cache target frame
        # LRU might not be suitable, evicting based on idx seems better
        frame_cache = LRUCache(frame_cache_cap)
        assert all(
            len(endpoints) == 2 for endpoints in self.idx_range_of_files
        ), "Record file endpoints are not complete!"
        num_frames = len(self.metadata)  # or self.num_frames
        for fileidx4input in range(self.num_files):
            filedesc4input = file_manager.open_file(file_idx=fileidx4input)
            endpoints = self.idx_range_of_files[fileidx4input]
            # no target frame to predict for the last frame
            for frameidx4input in range(
                endpoints[0],
                min(endpoints[1], num_frames - 1),  # self.num_frames
            ):
                input_frame = self.read_frame(
                    filedesc4input, self.metadata[frameidx4input], input_features
                )
                # get the target frame for prediction, both start, stop inclusive
                lookahead_steps = min(
                    random.randint(1, max_pred_steps),
                    num_frames - 1 - frameidx4input,
                )
                frameidx4target = frameidx4input + lookahead_steps
                target_frame = frame_cache.get(frameidx4target)
                if target_frame is None:
                    fileidx4target = self.metadata[frameidx4target]["file_idx"]
                    filedesc4target = file_manager.open_file(fileidx4target)
                    target_frame = self.read_frame(
                        filedesc4target,
                        self.metadata[frameidx4target],
                        target_features,
                    )
                # colllate input and target frames so that input and target frame are np.ndarray
                input_frame = np.vstack(
                    [input_frame[feature] for feature in input_features]
                )
                target_frame = np.vstack(
                    [target_frame[feature] for feature in target_features]
                )
                # print(self.timer.summarize())
                yield {
                    "input": input_frame,
                    "target": target_frame,
                    "lookahead_steps": np.asarray(lookahead_steps),
                    "input_features": input_features,
                    "target_features": target_features,
                }
        file_manager.close_all_files()

    def async_iterate_frame_pairs(
        self,
        input_features: List[str],
        target_features: List[str],
        max_pred_steps: int,
        filedesc_cache_cap: int = 10,
    ) -> Generator[Dict[str, np.ndarray], None, None]:
        """Asyncly read two frames from (possibly) two files.

        Notes:
            No frame cache

        Returns:
            _type_: _description_

        Yields:
            _type_: _description_
        """
        # setup a single event loop for async read
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # file_desc_cache is only used for target frame, since we are iterating for the input frame,
        file_desc_cache = LRUCache(capacity=filedesc_cache_cap)
        # given that, input and target features do not overlap, we only cache target frame
        # LRU might not be suitable, evicting based on idx seems better
        assert all(
            len(endpoints) == 2 for endpoints in self.idx_range_of_files
        ), "Record file endpoints are not complete!"

        num_frames = len(self.metadata)
        # read two frames using asyn io
        # file cache should only be used for future frames, since base file desc is used continuously
        try:
            for fileidx4input in range(self.num_files):
                filedesc4input = None
                endpoints = self.idx_range_of_files[fileidx4input]

                # no target frame to predict for the last frame
                for frameidx4input in range(
                    endpoints[0], min(endpoints[1], num_frames - 1)
                ):
                    lookahead_steps = min(
                        random.randint(1, max_pred_steps),
                        num_frames - 1 - frameidx4input,
                    )
                    frameidx4target = frameidx4input + lookahead_steps
                    fileidx4target = self.metadata[frameidx4target]["file_idx"]

                    filedesc4target = file_desc_cache.get(fileidx4target)
                    if filedesc4input is None and filedesc4target is None:
                        # both files need to be opened
                        file_descs = loop.run_until_complete(
                            asyncio.gather(
                                async_open_file(fileidx4input, None, self.recorddir),
                                async_open_file(
                                    fileidx4target, file_desc_cache, self.recorddir
                                ),
                            )
                        )
                        # order of return values are preserved. Ref: https://stackoverflow.com/questions/54668701/asyncio-gather-scheduling-order-guarantee
                        filedesc4input, filedesc4target = file_descs[0], file_descs[1]
                    elif filedesc4input is None:
                        # only need files for input frame
                        file_descs = loop.run_until_complete(
                            async_open_file(fileidx4input, None, self.recorddir)
                        )
                        filedesc4input = file_descs
                    elif filedesc4target is None:
                        # only need files for target frame
                        file_descs = loop.run_until_complete(
                            async_open_file(
                                fileidx4target, file_desc_cache, self.recorddir
                            )
                        )
                        filedesc4target = file_descs

                    start_time = perf_counter()
                    frame_pairs = loop.run_until_complete(
                        asyncio.gather(
                            async_read_frame(
                                filedesc4input,
                                self.metadata[frameidx4input],
                                input_features,
                            ),
                            async_read_frame(
                                filedesc4target,
                                self.metadata[frameidx4target],
                                target_features,
                            ),
                        )
                    )
                    end_time = perf_counter()
                    self.timer.add(
                        end_time - start_time,
                        frame_pairs[0].nbytes + frame_pairs[1].nbytes,
                    )
                    # print(self.timer.summarize())
                    yield {
                        "input": frame_pairs[0],
                        "target": frame_pairs[1],
                        "lookahead_steps": np.asarray(lookahead_steps),
                        "input_features": input_features,
                        "target_features": target_features,
                    }
                # close file descriptor for

                if filedesc4input is not None:
                    loop.run_until_complete(close_aiofile(filedesc4input))
        finally:
            # close open files
            loop.run_until_complete(close_files_in_cache(file_desc_cache))

            # wrap up async works
            loop.run_until_complete(loop.shutdown_asyncgens())
            loop.close()

    @staticmethod
    def prefetch_thread_worker(prefetch_data):
        # Lazily import to prevent circular import
        # shc: not sure what this is for?
        from torchdata.dataloader2 import communication

        itr = iter(prefetch_data.source_data_generator)
        stop_iteration = False
        while prefetch_data.run_prefetcher:
            if (
                len(prefetch_data.prefetch_buffer) < prefetch_data.buffer_size
                and not stop_iteration
            ):
                try:
                    item = next(itr)
                    prefetch_data.prefetch_buffer.append(item)
                except StopIteration:
                    stop_iteration = True
                # shc: probably not necessary for now
                except communication.iter.InvalidStateResetRequired:
                    stop_iteration = True
                except communication.iter.TerminateRequired:
                    prefetch_data.run_prefetcher = False
            elif stop_iteration and len(prefetch_data.prefetch_buffer) == 0:
                prefetch_data.run_prefetcher = False
            else:  # Buffer is full, waiting for main thread to consume items
                # TODO: Calculate sleep interval based on previous consumption speed
                time.sleep(PRODUCER_SLEEP_INTERVAL)

    def fetch_frame_pairs(
        self,
        input_features: List[str],
        target_features: List[str],
        max_pred_steps: int,
        prefetch_buffer_size: int = 10,
    ):

        if prefetch_buffer_size < 1:
            yield from self.iterate_frame_pairs(
                input_features, target_features, max_pred_steps
            )
        else:
            # ref: https://github.com/pytorch/data/blob/main/torchdata/datapipes/iter/util/prefetcher.py
            # preftech using a separate thread
            try:
                prefetch_data = _PrefetchData(
                    self.iterate_frame_pairs(
                        input_features, target_features, max_pred_steps
                    ),
                    prefetch_buffer_size,
                )
                thread = threading.Thread(
                    target=WSeqRecord.prefetch_thread_worker,
                    args=(prefetch_data,),
                    daemon=True,
                )
                thread.start()
                while prefetch_data.run_prefetcher:
                    if len(prefetch_data.prefetch_buffer) > 0:
                        yield prefetch_data.prefetch_buffer.popleft()
                    else:
                        # TODO: Calculate sleep interval based on previous availability speed
                        time.sleep(CONSUMER_SLEEP_INTERVAL)
            finally:
                prefetch_data.run_prefetcher = False
                if thread is not None:
                    thread.join()
                    thread = None

    def dump(self) -> None:
        """save attributes of instance of record into a pickled file and yaml file for visual inspection.

        Note:
        saving attribute dict instead of pickled class: pickling class and loading it is a mess because of
        path issues.
        """
        dic = copy.deepcopy(self.__dict__)
        # do not want to pickle a python module
        dic["file_desc"] = None
        with open(os.path.join(self.recorddir, "record.dict"), mode="wb") as f:
            pickle.dump(dic, file=f)

        # save some attributes of the seqrecord to yaml for human inspection
        dic["idx_range_of_files"] = None
        # transform some features to make them readable in yaml
        for key, val in dic["metadata"].items():
            for feature in dic["features_written"]:
                val[feature]["dtype"] = val[feature]["dtype"].str
                val[feature]["shape"] = list(val[feature]["shape"])
        with open(os.path.join(self.recorddir, "record_dict.yaml"), mode="w") as f:
            f.write("# Configs for human inspection only!\n")
            f.write(yaml.dump(dic))

    @classmethod
    def load_record_from_dict(cls, recorddir: str) -> WSR:
        """return an instance of sequence record from file that stores attributes of record as a
        dict (stored at path).

        Args:
            path (str): path to the file that stores dict of attributes of seqrecord

        Returns:
            WSR: an instance of record
        """

        file_path = os.path.join(recorddir, "record.dict")
        with open(file_path, mode="rb") as f:
            obj_dict = pickle.load(f)
        obj = cls(
            recorddir=recorddir,
        )
        obj_dict.pop("recorddir", None)
        for key, value in obj_dict.items():
            setattr(obj, key, value)
        return obj


async def async_open_file(file_idx: int, file_desc_cache: Optional[LRUCache], dir: str):
    file_desc = await aiofiles.open(recordfileidx2path(dir, file_idx), "rb")
    if file_desc_cache is not None:
        evicted = file_desc_cache.put(file_idx, file_desc)
        if evicted is not None:
            await evicted.close()
    return file_desc


async def close_files_in_cache(file_desc_cache: LRUCache) -> None:
    for key in file_desc_cache.keys():
        await file_desc_cache.pop(key).close()
    return None


async def close_aiofile(file_desc: io.BufferedReader) -> None:
    await file_desc.close()
    return


# notes: have to use file manager (instead of an lru function since we need to close files)
#        how to verify we are doing async?
# other approaches to be compared with:
#           1. read the whole frame and extract feature data (since reading small pieces of data multiple times is probably slow)
#           2. no async at all
async def async_read_frame(
    file_desc: io.BufferedReader, metadata_frame: dict, features: List[str]
) -> np.ndarray:
    """Given frame metadata and file object that contain frame data, read features from the frame data
    according to features

    Args:
        file_desc (io.BufferedReader): file object that contains the frame data (file object returned by aiofiles) is a subtype of BufferedReader
        metadata_frame (dict): _description_
        features (List[str]): _description_

    Returns:
        np.ndarray: _description_
    """
    await file_desc.seek(metadata_frame["bytes_offset"])
    data_bytes = await file_desc.read(metadata_frame["nbytes"])
    frame = {}
    # read the whole chunk or we read each file separately
    for feature in features:
        # b = file_desc.read(metadata[feature]["nbytes"])
        # array1d = np.frombuffer(
        #     bytes,
        #     dtype=metadata[feature]["dtype"],
        # )
        # frame[feature] = array1d
        # `await` halts `async_read_frame` and gives control back
        start = metadata_frame[feature]["bytes_offset"]
        end = start + metadata_frame[feature]["nbytes"]
        frame[feature] = np.frombuffer(
            data_bytes[start:end],
            dtype=metadata_frame[feature]["dtype"],
        ).reshape(metadata_frame[feature]["shape"])

    frame_array = np.vstack([frame[feature] for feature in features])
    return frame_array
