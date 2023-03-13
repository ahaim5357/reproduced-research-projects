# [Examining Student Effort on Help through Response Time Decomposition][paper]

This is a project constructor for the paper [*Examining Student Effort on Help through Response Time Decomposition*][paper] by Ashish Gurung, Anthony F. Botelho, and Neil T. Heffernan.

![](https://img.shields.io/badge/Status-Exactly%20Reproducible-success)
![](https://img.shields.io/badge/Systems-Windows%2C%20Mac%20OSX%2C%20Linux%2C%20Docker-informational)
![](https://img.shields.io/badge/Language-Python%203.9.5-informational)

## Project Files

The constructor downloads the following files:

* [GitHub Repository][github] under the [MIT License][mit]
* [RTD_data_randomsample_20K_new.csv][rtd] under the [ASSISTments Public Data License v0.1][apdl]
* [hint_infos.csv][hi] under the [ASSISTments Public Data License v0.1][apdl]
* [assignment_problem_npc_infos_with_priors.csv][apniwp] under the [ASSISTments Public Data License v0.1][apdl]

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

[paper]: https://doi.org/10.1145/3448139.3448167
[github]: https://github.com/AshishJumbo/ResponseTimeDecomposition
[mit]: https://github.com/AshishJumbo/ResponseTimeDecomposition/blob/2165e7e913daa9eab38b9655a472dbe4bae320f6/LICENSE
[rtd]: https://drive.google.com/file/d/1XYqsty-FpvQ6gSaJ3LKvOr3_HBFpO9Cn/view?usp=sharing
[hi]: https://drive.google.com/file/d/1mkxPq2XfvngxHnRP9SBC0TJs5Tu38ECk/view?usp=sharing
[apniwp]: https://drive.google.com/file/d/1T4ADTdvS97wMwaB8oiI9zI5cZ3T3x6UQ/view?usp=sharing
[apdl]: https://github.com/AshishJumbo/ResponseTimeDecomposition/2165e7e913daa9eab38b9655a472dbe4bae320f6/master/DATA-LICENSE

[docker]: https://www.docker.com/
[python]: https://www.python.org/
