# [Student Perception on the Effectiveness of On-Demand Assistance in Online Learning Platforms](https://doi.org/10.5281/zenodo.6853053)

![Exactly Reproducible](https://img.shields.io/badge/Status-Exactly%20Reproducible-success)

This is a project constructor for the paper [*Student Perception on the Effectiveness of On-Demand Assistance in Online Learning Platforms*](https://doi.org/10.5281/zenodo.6853053) by [Aaron Haim](https://orcid.org/0000-0002-9287-4201), [Neil Heffernan](https://orcid.org/0000-0002-3280-288X).

### Associated Metadata

#### Tested Systems

![Debian: bullseye (11) | bookworm (12)](https://img.shields.io/badge/Debian-bullseye%20%2811%29%20%7C%20bookworm%20%2812%29-informational)  
![Docker: 20.10 | 23.0](https://img.shields.io/badge/Docker-20.10%20%7C%2023.0-informational)  

#### Languages
![Python: 3.9](https://img.shields.io/badge/Python-3.9-informational)  

#### Resources

* [Student Perception on the Effectiveness of On-Demand Assistance in Online Learning Platforms](https://doi.org/10.5281/zenodo.6853053) (Public)
    * Contains paper under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
* [OSF](https://osf.io/ps6vm) (Public)
    * Contains data under [ASSIST-PDL-0.1](https://docs.google.com/document/d/1qUOWAgdXtBk7vk2ogUZDe4GXGDO-byAx5RJclRJFyDo/edit#heading=h.5iu406k5nt8u)
    * Contains materials under [ASSIST-PDL-0.1](https://docs.google.com/document/d/1qUOWAgdXtBk7vk2ogUZDe4GXGDO-byAx5RJclRJFyDo/edit#heading=h.5iu406k5nt8u)
* [Automatic Interpretable Personalized Learning Datasets](https://osf.io/9pgv5/) (Public)
    * Contains data under [ASSIST-PDL-0.1](https://docs.google.com/document/d/1qUOWAgdXtBk7vk2ogUZDe4GXGDO-byAx5RJclRJFyDo/edit#heading=h.5iu406k5nt8u)

## Project Files

The constructor downloads the following files: 
* [OSF](https://osf.io/f8w9p/) under [ASSIST-PDL-0.1](https://docs.google.com/document/d/1qUOWAgdXtBk7vk2ogUZDe4GXGDO-byAx5RJclRJFyDo/edit#heading=h.5iu406k5nt8u)
* [Automatic Interpretable Personalized Learning Datasets](https://osf.io/9pgv5/) under [ASSIST-PDL-0.1](https://docs.google.com/document/d/1qUOWAgdXtBk7vk2ogUZDe4GXGDO-byAx5RJclRJFyDo/edit#heading=h.5iu406k5nt8u)

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

*[ASSIST-PDL-0.1]: ASSISTments Public Data License v0.1
*[OSF]: Open Science Framework
*[CC-BY-4.0]: Creative Commons Attribution 4.0 International
