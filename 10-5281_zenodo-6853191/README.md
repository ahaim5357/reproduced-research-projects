# [Automatic Classification of Learning Objectives Based on Bloom's Taxonomy](https://doi.org/10.5281/zenodo.6853191)

![Essentially Reproducible](https://img.shields.io/badge/Status-Essentially%20Reproducible-green)

This is a project constructor for the paper [*Automatic Classification of Learning Objectives Based on Bloom's Taxonomy*](https://doi.org/10.5281/zenodo.6853191) by [Yuheng Li](https://orcid.org/0000-0002-5971-8469), Mladen Raković, Boon Xin Poh, [Dragan Gasevic](https://orcid.org/0000-0001-9265-1908), [Guanliang Chen](https://orcid.org/0000-0002-8236-3133).

### Associated Metadata

#### Tested Systems

![Docker NVIDIA (GPU): 20.10 | 23.0](https://img.shields.io/badge/Docker%20NVIDIA%20%28GPU%29-20.10%20%7C%2023.0-informational)  
![Ubuntu (GPU): Focal Fossa (20.04)](https://img.shields.io/badge/Ubuntu%20%28GPU%29-Focal%20Fossa%20%2820.04%29-informational)  

#### Languages
![Python: 3.9](https://img.shields.io/badge/Python-3.9-informational)  

#### Resources

* [Automatic Classification of Learning Objectives Based on Bloom's Taxonomy](https://doi.org/10.5281/zenodo.6853191) (Public)
    * Contains paper under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
* [GitHub](https://github.com/SteveLEEEEE/EDM2022CLO) (Public)
    * Contains data under ARR
    * Contains materials under ARR

## Project Files

The constructor downloads the following files: 
* [Cloned GitHub](https://github.com/ahaim5357/EDM2022CLO) under ARR

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

## Issues

There are numerous differences within Table 3 from the reproduced run, but all of the values seems within a reasonable bound of the reported results.

The BERT model with a Binary classifier, the Random Forest (RF) model with a Multi-class Multi-label (MCML) classifier, and the BERT model with a MCML classifier have differing results on each run. The best results for each column switches between the Binary and MCML classifier with the BERT model.

There are also some results for the Naive Baves (NB), Random Forest (RF), and Logistic Regression (LR) models with a Binary classifier which could either be considered typos or a more significant difference. Though, the results would still be within a reasonable bound:

* Apply
    * NB
        * F1 0.668 -> 0.669
* Analyze
    * RF
        * Acc 0.961 -> 0.959
        * Cohen's K 0.851 -> 0.843
        * AUC 0.902 -> 0.897
        * F1 0.874 -> 0.866
* Evaluate
    * RF
        * Cohen's K 0.887 -> 0.888
        * F1 0.907 -> 0.908
* Create
    * LR
        * Cohen's K 0.604 -> 0.605
    * RF
        * Acc 0.943 -> 0.944
        * Cohen's K 0.792 -> 0.794
        * AUC 0.877 -> 0.875
        * F1 0.826 -> 0.827

*[ARR]: All Rights Reserved
*[CC-BY-4.0]: Creative Commons Attribution 4.0 International
*[GitHub]: GitHub Repository
*[Cloned GitHub]: Cloned GitHub Repository
