"""Iterative datapipes toread weather dataset in seqrecord format"""

from typing import Callable, Dict, List, Optional, Tuple

import numpy as np
import torch
import torchdata.datapipes as dp
from tqdm import tqdm

from .wseqrecord import WSeqRecord
from .constants import VAR_LEVEL_TO_NAME_LEVEL


@dp.functional_datapipe("weather_datapipe")
class WeatherDatapipeFromWSeqRecord(dp.iter.IterDataPipe):
    """A torch datapiple class that iteratively read frame pairs from weather dataset (encoded by WSeqRecord)."""

    def __init__(
        self,
        record: WSeqRecord,
        input_features: List[str],
        target_features: List[str],
        max_pred_steps: int,
    ) -> None:
        super().__init__()
        self.record = record
        self.input_features = input_features
        self.target_features = target_features
        self.max_pred_steps = max_pred_steps

    def __iter__(self):
        # naive iterate
        # yield from self.record.iterate_frame_pairs(
        #     self.input_features, self.target_features, self.max_pred_steps
        # )
        # prefetech
        yield from self.record.async_iterate_frame_pairs(
            self.input_features, self.target_features, self.max_pred_steps
        )


def collate_fn(batch: List[Dict[str, np.ndarray]]) -> Dict[str, torch.Tensor]:
    collated_batch: Dict[str, torch.Tensor] = {}
    collated_batch["input"] = torch.from_numpy(
        np.stack([batch[i]["input"] for i in range(len(batch))], axis=0)
    ).unsqueeze(1)
    collated_batch["target"] = torch.from_numpy(
        np.stack([batch[i]["target"] for i in range(len(batch))], axis=0)
    )
    collated_batch["lookahead_steps"] = torch.from_numpy(
        np.stack([batch[i]["lookahead_steps"] for i in range(len(batch))], axis=0)
    ).to(collated_batch["input"].dtype)
    # todo: scale it: predict_ranges= hrs_each_step * predict_ranges / 100
    # we can put them in weather datapipe
    for feature in ["input_features", "target_features"]:
        collated_batch[feature] = [
            VAR_LEVEL_TO_NAME_LEVEL[v] for v in batch[0][feature]
        ]
    return collated_batch


def build_datapipes(
    datapipe: dp.iter.IterDataPipe,
    shuffle_buffer_size: Optional[int],
    batch_size: int,
    mappings: List[Callable],
) -> dp.iter.IterDataPipe:
    """Iteratively apply operations to datapipe: shuffle, sharding, map, batch, collator

    Args:
        datapipe (dp.datapipe.IterDataPipe): entry datapipe
        shuffle_buffer_size (Optional[int]): buffer size for pseudo-shuffle
        batch_size (int):
        mappings (List[Callable]): a list of transforms applied to datapipe, between sharding and batch

    Returns:
        dp.datapipe.IterDataPipe: transformed datapipe ready to be sent to dataloader
    """
    # Shuffle will happen as long as you do NOT set `shuffle=False` later in the DataLoader
    # https://pytorch.org/data/main/tutorial.html#working-with-dataloader
    if shuffle_buffer_size is not None:
        datapipe = datapipe.shuffle(buffer_size=shuffle_buffer_size)
    # sharding: Place ShardingFilter (datapipe.sharding_filter) as early as possible in the pipeline,
    # especially before expensive operations such as decoding, in order to avoid repeating these expensive operations across worker/distributed processes.
    datapipe = datapipe.sharding_filter()
    for i, mapping in enumerate(mappings):
        datapipe = datapipe.map(fn=mapping)
    # Note that if you choose to use Batcher while setting batch_size > 1 for DataLoader,
    # your samples will be batched more than once. You should choose one or the other.
    # https://pytorch.org/data/main/tutorial.html#working-with-dataloader
    datapipe = datapipe.batch(batch_size=batch_size, drop_last=True)
    datapipe = datapipe.collate(collate_fn=collate_fn)
    return datapipe
