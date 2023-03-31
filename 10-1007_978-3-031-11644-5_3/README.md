# [Adaptive Scaffolding in Block-Based Programming via Synthesizing New Tasks as Pop Quizzes](https://doi.org/10.1007/978-3-031-11644-5_3)

![Partially Reproducible](https://img.shields.io/badge/Status-Partially%20Reproducible-yellow)

This is a project constructor for the paper [*Adaptive Scaffolding in Block-Based Programming via Synthesizing New Tasks as Pop Quizzes*](https://doi.org/10.1007/978-3-031-11644-5_3) by Ahana Ghosh, [Sebastian Tschiatschek](https://orcid.org/0000-0002-2592-0108), [Sam Devlin](https://orcid.org/0000-0002-7769-3090), [Adish Singla](https://orcid.org/0000-0001-9922-0668).

### Associated Metadata

#### Tested Systems

![Debian: bullseye (11)](https://img.shields.io/badge/Debian-bullseye%20%2811%29-informational)  

#### Languages
![Python: 3.7](https://img.shields.io/badge/Python-3.7-informational)  

#### Resources

* [Adaptive Scaffolding in Block-Based Programming via Synthesizing New Tasks as Pop Quizzes](https://doi.org/10.1007/978-3-031-11644-5_3) (Public)
    * Contains paper under ARR
* [GitHub](https://github.com/machine-teaching-group/aied2022_pquizsyn) (Public)
    * Contains data under ARR
    * Contains materials under ARR

## Project Files

The constructor downloads the following files: 
* [Cloned GitHub](https://github.com/ahaim5357/aied2022_pquizsyn) under ARR

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
docker run -itv <local_directory>:/volume <image_name> sh
```

A `volume` directory will be created within the image which will link to the `local_directory` specified. You can specify the current directory of execution via `${PWD}`.

> We are loading into the terminal instead of into Python to copy any generated figures onto the local machine as they cannot otherwise be easily viewed.

Once in the docker terminal, you can run the Python script via:

```sh
python3 paper_results_replication_file.py
```

You can look through the terminal output and compare the numbers within the paper. To view the figures on the local machine, you can copy them to the volume via:

```sh
cp -R ../images /volume
```

### Method 2: Local Setup

This project uses the Python package `project_patcher[git]` to setup and fix any issues in the codebase. For instructions on how to download and generate the project from this directory, see the [`project_patcher`][project_patcher] repository.

The following instructions have been reproduced using [Python][python] 3.9.5. This project does not make any guarantees that this will work outside of the specified version. Make sure you have Python, along with gcc for Cython, before attempting anything below.

First, you will need to navigate to the generated `_src` directory. You will need to install the required dependencies into the global Python instance or a virtual environment via:

```sh
python3 -m pip install -r requirements.txt
```

> python3 is replaced with `py` on Windows machines. Additionally, the `python3 -m` prefix is unnecessary if `pip` is properly added to the path.

After installing the required dependencies, navigate to the `analysis` folder and run the `paper_results_replication_file.py` script via:

```sh
python3 paper_results_replication_file.py
```

> Your terminal should be within the `analysis` folder, or the code will fail to execute.

You can look through the terminal output and compare the numbers within the paper. Additionally, the figures are generated within the `images/plots` directory within `_src`.

[docker]: https://www.docker.com/
[project_patcher]: https://github.com/ahaim5357/project-patcher
[python]: https://www.python.org/

## Issues

* Typo in Paper: (r(209) = 0.48, p < 0.001, 95% CI [0.37, −0.58])
    * Correction: (r(209) = 0.48, p < 0.001, 95% CI [0.37, 0.58])
* Incorrect Rounding in Paper: (γ = 0.12, SE = 0.03, p = 0.013, R2 = 0.12)
    * Correction: (γ = 0.12, SE = 0.03, p = 0.014, R2 = 0.12)

*[GitHub]: GitHub Repository
*[Cloned GitHub]: Cloned GitHub Repository
*[ARR]: All Rights Reserved
