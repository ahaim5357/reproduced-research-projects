## Setup Instructions

A NVIDIA Graphics Card is necessary to make full use of the models provided in this codebase. Additionally, this makes use of the [CUDA Toolkit][cuda] 11.3 and [cuDNN][cudnn] 8.2.0. You can follow the instructions on how to setup on [their website][cuda_docs]. It is highly recommended, and sometimes required, to use a Linux distribution for use with any implementations of the CUDA Toolkit in other software.

### Method 1: Docker

This project contains the necessary files needed to setup a [docker container][docker] with the [NVIDIA Container Toolkit runtime][nvidia_docker]. Make sure you have both Docker and the NVIDIA runtime installed before attempting anything below. 

To build the docker container, navigate to this directory and run the following command:

```sh
docker build -t <image_name> .
```

`image_name` should be replaced with whatever name you would like to refer to the docker container as. It will take around 30 minutes to an hour to build the image.

From there, you can load into the terminal via:

```sh
docker run --rm --runtime=nvidia --gpus all -it <image_name> sh
```

Once in the docker terminal, you can run the Python script via:

```sh
python3 EDM2022\ CLO.py
python3 Multi-Label.py
```

You can look through the terminal output and compare the numbers within the paper.

### Method 2: Local Setup

This project uses the Python package `jammies[all]` to setup and fix any issues in the codebase. For instructions on how to download and generate the project from this directory, see the [`jammies`][jammies] repository.

The following instructions have been reproduced using [Python][python] 3.9.18. This project does not make any guarantees that this will work outside of the specified version. Make sure you have Python, along with gcc for Cython, before attempting anything below.

First, you will need to navigate to the generated `src` directory. You will need to install the required dependencies into the global Python instance or a virtual environment via:

```sh
python3 -m pip install -r requirements.txt
```

After installing the required dependencies, run the Python script via:

```sh
python3 EDM2022\ CLO.py
python3 Multi-Label.py
```

You can look through the terminal output and compare the numbers within the paper.

Additionally, you can run the notebook versions instead.

[cuda]: https://developer.nvidia.com/cuda-toolkit
[cudnn]: https://developer.nvidia.com/cudnn
[cuda_docs]: https://docs.nvidia.com/cuda/
[docker]: https://www.docker.com/
[nvidia_docker]: https://github.com/NVIDIA/nvidia-docker
[jammies]: https://github.com/ahaim5357/jammies
[python]: https://www.python.org/
