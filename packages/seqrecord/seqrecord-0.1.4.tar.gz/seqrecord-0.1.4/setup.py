from setuptools import setup, find_packages

setup(
    name="seqrecord",
    version="0.1.4",
    description="fix more bugs in writing frames",
    author_email="shuhang0chen@gmail.com",
    maintainer_email="shuhang0chen@gmail.com",
    packages=find_packages(),
    install_requires=["numpy", "torch"],
)
