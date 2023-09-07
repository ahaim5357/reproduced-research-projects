# [Faster Confidence Intervals for Item Response Theory via an Approximate Likelihood Profile](https://doi.org/10.5281/zenodo.6852950)

![Essentially Reproducible](https://img.shields.io/badge/Status-Essentially%20Reproducible-green)

This is a project constructor for the paper [*Faster Confidence Intervals for Item Response Theory via an Approximate Likelihood Profile*](https://doi.org/10.5281/zenodo.6852950) by [Benjamin Paassen](https://orcid.org/0000-0002-3899-2450), [Christina Göpfert](https://orcid.org/0000-0003-2517-4907), [Niels Pinkwart](https://orcid.org/0000-0001-7076-9737).

### Associated Metadata

#### Tested Systems

![Debian: bullseye (11) | bookworm (12)](https://img.shields.io/badge/Debian-bullseye%20%2811%29%20%7C%20bookworm%20%2812%29-informational)  
![Docker NVIDIA: 20.10 | 23.0](https://img.shields.io/badge/Docker%20NVIDIA-20.10%20%7C%2023.0-informational)  

#### Languages
![Python: 3.11](https://img.shields.io/badge/Python-3.11-informational)  

#### Resources

* [Faster Confidence Intervals for Item Response Theory via an Approximate Likelihood Profile](https://doi.org/10.5281/zenodo.6852950) (Public)
    * Contains paper under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
* [GitHub](https://github.com/bpaassen/ability_bounds) (Public)
    * Contains data under [GPL-3.0-or-later](https://spdx.org/licenses/GPL-3.0-or-later.html)
    * Contains materials under [GPL-3.0-or-later](https://spdx.org/licenses/GPL-3.0-or-later.html)

## Project Files

The constructor downloads the following files: 
* [Cloned GitHub](https://github.com/ahaim5357/ability_bounds) under [GPL-3.0-or-later](https://spdx.org/licenses/GPL-3.0-or-later.html)

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
python3 synthetic_experiments.py
```

You can look through the terminal output and compare the numbers within the paper.

## Method 2: Local Setup

This project uses the Python package `jammies[all]` to setup and fix any issues in the codebase. For instructions on how to download and generate the project from this directory, see the [`jammies`][jammies] repository.

The following instructions have been reproduced using [Python][python] 3.11.4. This project does not make any guarantees that this will work outside of the specified version. Make sure you have Python, along with gcc for Cython, before attempting anything below.

First, you will need to navigate to the generated `src` directory. You will need to install the required dependencies into the global Python instance or a virtual environment via:

```sh
python3 -m pip install -r requirements.txt
```

> `python3` is replaced with `py` on Windows machines. Additionally, the `python3 -m` prefix is unnecessary if `pip` is properly added to the path.

After installing the required dependencies, run the Python script via:

```sh
python3 synthetic_experiments.py
```

You can look through the CSVs or the terminal output and compare the numbers within the paper.

[docker]: https://www.docker.com/
[jammies]: https://github.com/ahaim5357/jammies
[java]: https://adoptium.net/temurin/releases/?version=17
[hadoop]: http://apache.github.io/hadoop/
[python]: https://www.python.org/

## Issues

### Table 1

The results tend to be within the confidence intervals provided when running the experiment multiple times. Three results, however, seem to be extremes which do not fit into the confidence interval. After 10 runs, the best measures and bounds have been provided below:

* Wald (m = 30, n = 20): 1.000 +- 0.000 -> 0.996 +- 0.010
* Barrier (m = 100, n = 20): 0.059 +- 0.012 -> 0.077 +- 0.030
* Barrier (m = 500, n = 20): 0.097 +- 0.016 -> 0.080 +- 0.021

### Figure 3

The runtime graphs will differ depending on the machine used, so the results are inconsistent. However, the reported line plots are similar in relation to the other experimental conditions.

*[CC-BY-4.0]: Creative Commons Attribution 4.0 International
*[GPL-3.0-or-later]: GNU General Public License v3.0 or later
*[Cloned GitHub]: Cloned GitHub Repository
*[GitHub]: GitHub Repository
