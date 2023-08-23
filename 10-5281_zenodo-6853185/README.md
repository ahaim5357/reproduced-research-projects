# [Can Population-based Engagement Improve Personalisation? A Novel Dataset and Experiment](https://doi.org/10.5281/zenodo.6853185)

![Not at All Reproducible](https://img.shields.io/badge/Status-Not%20at%20All%20Reproducible-red)

This is a project constructor for the paper [*Can Population-based Engagement Improve Personalisation? A Novel Dataset and Experiment*](https://doi.org/10.5281/zenodo.6853185) by Sahan Bulathwela, Meghana Verma, [María Pérez-Ortiz](https://orcid.org/0000-0003-1302-6093), [Emine Yilmaz](https://orcid.org/0000-0003-4734-4532), [John Shawe-Taylor](https://orcid.org/0000-0002-2030-0073).

### Associated Metadata

#### Tested Systems

![Debian: bullseye (11) | bookworm (12)](https://img.shields.io/badge/Debian-bullseye%20%2811%29%20%7C%20bookworm%20%2812%29-informational)  
![Docker NVIDIA: 20.10 | 23.0](https://img.shields.io/badge/Docker%20NVIDIA-20.10%20%7C%2023.0-informational)  

#### Languages
![Java: 17.0.8](https://img.shields.io/badge/Java-17.0.8-informational)  
![Python: 3.11.2 | 3.11.4](https://img.shields.io/badge/Python-3.11.2%20%7C%203.11.4-informational)  

#### Resources

* [Can Population-based Engagement Improve Personalisation? A Novel Dataset and Experiment](https://doi.org/10.5281/zenodo.6853185) (Public)
    * Contains paper under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
* [GitHub](https://github.com/sahanbull/VLE-Dataset) (Public)
    * Contains data under ARR
    * Contains materials under ARR

## Project Files

The constructor downloads the following files: 
* [Cloned GitHub](https://github.com/ahaim5357/VLE-Dataset) under ARR

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
docker run --rm -itv <local_directory>:/volume <image_name> sh
```

A `volume` directory will be created within the image which will link to the `local_directory` specified. You can specify the current directory of execution via `${PWD}`.

> We are loading into the terminal instead of into Python to copy any generated figures onto the local machine as they cannot otherwise be easily viewed.

Once in the docker terminal, you can run the Python script via:

```sh
python3 ./helper_code/models/regression/train_rf_regression_full_cv.py --training-data-filepath VLE_datasets/v1/VLE_12k_dataset_v1.csv --output-dir ./results
```

You can look through the terminal output and compare the numbers within the paper. To view the figures on the local machine, you can copy them to the volume via:

```sh
cp -R ./results /volume
```

## Method 2: Local Setup

This project uses the Python package `jammies[all]` to setup and fix any issues in the codebase. For instructions on how to download and generate the project from this directory, see the [`jammies`][jammies] repository.

You will also need a version of [Java][java] to run Spark, as consumed by the codebase. Any version of Java 8+ will work, though this setup guide recommends using the latest LTS, which is 17 as of the writing of this guide.

Spark also takes advantage of [Apache Hadoop][hadoop], but this is not necessary to run the codebase, nor does it affect the outcomes, so it will not be used in this guide.

The following instructions have been reproduced using [Python][python] 3.11.4. This project does not make any guarantees that this will work outside of the specified version. Make sure you have Python, along with gcc for Cython, before attempting anything below.

First, you will need to navigate to the generated `src` directory. You will need to install the required dependencies into the global Python instance or a virtual environment via:

```sh
python3 -m pip install .
```

> `python3` is replaced with `py` on Windows machines. Additionally, the `python3 -m` prefix is unnecessary if `pip` is properly added to the path.

After installing the required dependencies, run the Python script via:

```sh
python3 ./helper_code/models/regression/train_rf_regression_full_cv.py --training-data-filepath VLE_datasets/v1/VLE_12k_dataset_v1.csv --output-dir ./results
```

You can look through the `results` directory and compare the numbers within the paper.

[docker]: https://www.docker.com/
[jammies]: https://github.com/ahaim5357/jammies
[java]: https://adoptium.net/temurin/releases/?version=17
[hadoop]: http://apache.github.io/hadoop/
[python]: https://www.python.org/

## Issues

None of the results generated match anything reported in the papers. The `results.csv` generated reports the RMSE, but not for the 12k results, so while the code may work, no direct correlation can be interpreted from the results in the paper.

As such, no consistent results are reported in the paper.

*[CC-BY-4.0]: Creative Commons Attribution 4.0 International
*[GitHub]: GitHub Repository
*[ARR]: All Rights Reserved
*[Cloned GitHub]: Cloned GitHub Repository
