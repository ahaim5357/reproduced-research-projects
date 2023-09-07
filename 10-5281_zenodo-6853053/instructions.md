## Setup Instructions

### Method 1: Docker

This project contains the necessary files needed to setup a [docker container][docker]. Make sure you have Docker installed before attempting anything below. 

To build the docker container, navigate to this directory and run the following command:

```sh
docker build -t <image_name> .
```

`image_name` should be replaced with whatever name you would like to refer to the docker container as. It will take around 30 minutes to an hour to build the image.

From there, you can load into the terminal via:

```sh
docker run --rm -it <image_name> sh
```

Once in the docker terminal, you can run the Python script via:

```sh
python3 analysis.py
```

You can look through the terminal output and compare the numbers within the paper.

## Method 2: Local Setup

This project uses the Python package `jammies[all]` to setup and fix any issues in the codebase. For instructions on how to download and generate the project from this directory, see the [`jammies`][jammies] repository.

The following instructions have been reproduced using [Python][python] 3.9.18. This project does not make any guarantees that this will work outside of the specified version. Make sure you have Python, along with gcc for Cython, before attempting anything below.

First, you will need to navigate to the generated `src` directory. You will need to install the required dependencies into the global Python instance or a virtual environment via:

```sh
python3 -m pip install -r requirements.txt
```

> `python3` is replaced with `py` on Windows machines. Additionally, the `python3 -m` prefix is unnecessary if `pip` is properly added to the path.

After installing the required dependencies, run the Python script via:

```sh
python3 analysis.py
```

You can look through the terminal output and compare the numbers within the paper. Additionally, you can view the notebook instead.

[docker]: https://www.docker.com/
[jammies]: https://github.com/ahaim5357/jammies
[java]: https://adoptium.net/temurin/releases/?version=17
[hadoop]: http://apache.github.io/hadoop/
[python]: https://www.python.org/
