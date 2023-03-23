# [Examining Student Effort on Help through Response Time Decomposition](https://doi.org/10.1145/3448139.3448167)

![Exactly Reproducible](https://img.shields.io/badge/Status-Exactly%20Reproducible-success)

This is a project constructor for the paper [*Examining Student Effort on Help through Response Time Decomposition*](https://doi.org/10.1145/3448139.3448167) by [Ashish Gurung](https://orcid.org/0000-0001-7003-1476), [Anthony Botelho](https://orcid.org/0000-0002-7373-4959), [Neil Heffernan](https://orcid.org/0000-0002-3280-288X).

### Associated Metadata

#### Tested Systems

![Debian: bullseye (11)](https://img.shields.io/badge/Debian-bullseye%20%2811%29-informational)  
![Docker: 20.10 | 23.0](https://img.shields.io/badge/Docker-20.10%20%7C%2023.0-informational)  
![macOS: High Sierra (10.13)](https://img.shields.io/badge/macOS-High%20Sierra%20%2810.13%29-informational)  
![Windows Native: 10](https://img.shields.io/badge/Windows%20Native-10-informational)  

#### Languages
![Python: 3.9 | 3.10 | 3.11](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11-informational)  

#### Resources

* [Examining Student Effort on Help through Response Time Decomposition](https://doi.org/10.1145/3448139.3448167) (Public)
    * Contains paper under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
* [Google Drive](https://drive.google.com/drive/folders/1fRhyVEetIsgRdp-B8J5seH64FCHC2HMI) (Public)
    * Contains data under [ASSIST-PDL-0.1](https://docs.google.com/document/d/1qUOWAgdXtBk7vk2ogUZDe4GXGDO-byAx5RJclRJFyDo/edit#heading=h.5iu406k5nt8u)
* [GitHub](https://github.com/AshishJumbo/ResponseTimeDecomposition) (Public)
    * Contains materials under [MIT](https://opensource.org/license/mit/)

## Project Files

The constructor downloads the following files: 
* [GitHub](https://github.com/AshishJumbo/ResponseTimeDecomposition) under [MIT](https://opensource.org/license/mit/)
* [RTD_data_randomsample_20K_new.csv](https://drive.google.com/file/d/1XYqsty-FpvQ6gSaJ3LKvOr3_HBFpO9Cn/view?usp=sharing) under [ASSIST-PDL-0.1](https://docs.google.com/document/d/1qUOWAgdXtBk7vk2ogUZDe4GXGDO-byAx5RJclRJFyDo/edit#heading=h.5iu406k5nt8u)
* [hint_infos.csv](https://drive.google.com/file/d/1mkxPq2XfvngxHnRP9SBC0TJs5Tu38ECk/view?usp=sharing) under [ASSIST-PDL-0.1](https://docs.google.com/document/d/1qUOWAgdXtBk7vk2ogUZDe4GXGDO-byAx5RJclRJFyDo/edit#heading=h.5iu406k5nt8u)
* [assignment_problem_npc_infos_with_priors.csv](https://drive.google.com/file/d/1T4ADTdvS97wMwaB8oiI9zI5cZ3T3x6UQ/view?usp=sharing) under [ASSIST-PDL-0.1](https://docs.google.com/document/d/1qUOWAgdXtBk7vk2ogUZDe4GXGDO-byAx5RJclRJFyDo/edit#heading=h.5iu406k5nt8u)

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

*[ASSIST-PDL-0.1]: ASSISTments Public Data License v0.1
*[GitHub]: GitHub Repository
*[CC-BY-4.0]: Creative Commons Attribution 4.0 International
*[MIT]: MIT License
