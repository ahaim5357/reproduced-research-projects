# [Sparse Factor Autoencoders for Item Response Theory](https://doi.org/10.5281/zenodo.6853067)

![Essentially Reproducible](https://img.shields.io/badge/Status-Essentially%20Reproducible-green)

This is a project constructor for the paper [*Sparse Factor Autoencoders for Item Response Theory*](https://doi.org/10.5281/zenodo.6853067) by [Benjamin Paassen](https://orcid.org/0000-0002-3899-2450), Malwina Dywel, Melanie Fleckenstein, [Niels Pinkwart](https://orcid.org/0000-0001-7076-9737).

### Associated Metadata

#### Tested Systems

![Debian (GPU): bullseye (11) | bookworm (12)](https://img.shields.io/badge/Debian%20%28GPU%29-bullseye%20%2811%29%20%7C%20bookworm%20%2812%29-informational)  
![Docker NVIDIA (GPU): 20.10 | 23.0](https://img.shields.io/badge/Docker%20NVIDIA%20%28GPU%29-20.10%20%7C%2023.0-informational)  

#### Languages
![Python: 3.11.2 | 3.11.4](https://img.shields.io/badge/Python-3.11.2%20%7C%203.11.4-informational)  

#### Resources

* [Sparse Factor Autoencoders for Item Response Theory](https://doi.org/10.5281/zenodo.6853067) (Public)
    * Contains paper under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
* [GitHub](https://github.com/bpaassen/sparfae) (Public)
    * Contains data under [GPL-3.0-or-later](https://spdx.org/licenses/GPL-3.0-or-later.html)
    * Contains materials under [GPL-3.0-or-later](https://spdx.org/licenses/GPL-3.0-or-later.html)
* [NeurIPS 2020 Education Challenge Dataset](https://eedi.com/projects/neurips-education-challenge) (Public)
    * Contains data under [CC-BY-NC-ND-4.0](https://creativecommons.org/licenses/by-nc-nd/4.0//)

## Project Files

The constructor downloads the following files: 
* [Cloned GitHub](https://github.com/ahaim5357/sparfae) under [GPL-3.0-or-later](https://spdx.org/licenses/GPL-3.0-or-later.html)
* [NeurIPS 2020 Education Challenge Dataset](https://eedi.com/projects/neurips-education-challenge) under [CC-BY-NC-ND-4.0](https://creativecommons.org/licenses/by-nc-nd/4.0//)

## Setup Instructions

A NVIDIA Graphics Card is necessary to make full use of the models provided in this codebase. Additionally, this makes use of the [CUDA Toolkit][cuda] 11.8 and [cuDNN][cudnn] 8.8.0. You can follow the instructions on how to setup on [their website][cuda_docs]. It is highly recommended, and sometimes required, to use a Linux distribution for use with any implementations of the CUDA Toolkit in other software.

### Method 1: Docker

This project contains the necessary files needed to setup a [docker container][docker] with the [NVIDIA Container Toolkit runtime][nvidia_docker]. Make sure you have both Docker and the NVIDIA runtime installed before attempting anything below. 

To build the docker container, navigate to this directory and run the following command:

```sh
docker build -t <image_name> .
```

`image_name` should be replaced with whatever name you would like to refer to the docker container as. It will take around 30 minutes to an hour to build the image.

From there, you can load into the terminal via:

```sh
docker run --rm --runtime=nvidia --gpus all -itv <local_directory>:/volume <image_name> sh
```

A `volume` directory will be created within the image which will link to the `local_directory` specified. You can specify the current directory of execution via `${PWD}`.

> We are loading into the terminal instead of into Python to copy any generated figures onto the local machine as they cannot otherwise be easily viewed.

Once in the docker terminal, you can run the Python script via:

```sh
python3 synthetic_experiment_Qlearning.py
python3 eedi_experiment-fixedQ.py
python3 eedi_experiment-Qlearning.py
```

You can look through the terminal output and compare the numbers within the paper. To view the figures on the local machine, you can copy them to the volume via:

```sh
cp -R ./images /volume
```

### Method 2: Local Setup

This project uses the Python package `jammies[all]` to setup and fix any issues in the codebase. For instructions on how to download and generate the project from this directory, see the [`jammies`][jammies] repository.

The following instructions have been reproduced using [Python][python] 3.11.4. This project does not make any guarantees that this will work outside of the specified version. Make sure you have Python, along with gcc for Cython, before attempting anything below.

First, you will need to navigate to the generated `src` directory. You will need to install the required dependencies into the global Python instance or a virtual environment via:

```sh
python3 -m pip install -r requirements.txt
```

> `python3` is replaced with `py` on Windows machines. Additionally, the `python3 -m` prefix is unnecessary if `pip` is properly added to the path.

After installing the required dependencies, run the Python script via:

```sh
python3 synthetic_experiment_Qlearning.py
python3 eedi_experiment-fixedQ.py
python3 eedi_experiment-Qlearning.py
```

You can look through the terminal output and compare the numbers within the paper. Additionally, the figures are generated within the `images` directory within `src`.

Additionally, you can run the notebook versions instead. The images will be generated as part of its output.

[cuda]: https://developer.nvidia.com/cuda-toolkit
[cudnn]: https://developer.nvidia.com/cudnn
[cuda_docs]: https://docs.nvidia.com/cuda/
[docker]: https://www.docker.com/
[nvidia_docker]: https://github.com/NVIDIA/nvidia-docker
[jammies]: https://github.com/ahaim5357/jammies
[python]: https://www.python.org/

## Issues

### Figures 2-5

Based on some analysis of the graphs, this assumes that condition A is condition 1 and condition B is condition 3.

* The graphs reported for Figure 2 roughly follow similar trends after running multiple attempts of the codebase; however, the individaul shape differs quite a bit, likely due to randomness.
* Aside from AUC, the graphs reported for Figure 3 can widely greatly, having different trends across multiple attempts.
* Aside from AUC and rθ, the graphs reported for Figure 4 can widely greatly, having different trends across multiple attempts.
* The train time for hyperparameters in Figure 5 is similar except for the SPARFA model, which had an odd training time on the reproduced machine.

### Reported Results in Table 2

* After running the fixed methods multiple times, there are likely a few typos in the result:
    * SparFAE_f (AUC)
        * 0.88 +- 0.04 -> 0.88 +- 0.05
* The following are likely due to differences in the machines used:
    * VIBO_f (Training Time)
        * 8.01 +- 5.59 -> 10.62 +- 6.97
    * SparFAE_f (Training Time)
        * 0.05 +- 0.03 -> 0.05 +- 0.02
    * VIBO_f (Prediction Time)
        * 1.31 +- 2.76 -> 2.01 +- 2.56
    * SparFAE_f (Prediction Time)
        * 0.15 +- 0.13 -> 0.18 +- 0.00

* After running the experiment methods multiple times, there are likely a few typos in the result:
    * SPARFA (Sparsity)
        * 0.16 +- 0.06 -> 0.16 +- 0.07
    * VIBO (Sparsity)
        * 0.00 +- 0.00 -> 0.00 +- 0.01
    * SparFAE2 (Sparsity)
        * 0.33 +- 0.10 -> 0.33 +- 0.11
* The following are likely due to differences in the machines used; however, the results are quite similar to those reported, so it could also be interpreted as a potential typo:
    * Training Time
        * SPARFA: 31.0 +- 20.9 -> 31.0 +- 21.2
        * VIBO: 7.83 +- 5.12 -> 7.83 +- 5.21
        * SparFAE1: 1.94 +- 1.78 -> 1.94 +- 1.95
        * SparFAE2: 15.7 +- 15.9 -> 15.7 +- 18.8
    * Prediction Time
        * SPARFA: 633 +- 444 -> 634 +- 458
        * VIBO: 0.31 +- 0.18 -> 0.31 +- 0.50
        * SparFAE1: 0.19 +- 0.12 -> 0.19 +- 0.35
        * SparFAE2: 0.20 +- 0.13 -> 0.20 +- 0.36

* The Wilcoxon Signed-Rank Test is reported backwards, meaning that the sentence should read, "Method 1 has lower AUC than Method 2".

### Figures 6-8

* Figures 7 and 8 are not generated in the codebase.
* Only the number of skills in Figure 6 is generated, but without the lines of best fit. However, the points are essentially accurate to those in the paper.

*[GPL-3.0-or-later]: GNU General Public License v3.0 or later
*[Cloned GitHub]: Cloned GitHub Repository
*[CC-BY-4.0]: Creative Commons Attribution 4.0 International
*[GitHub]: GitHub Repository
*[CC-BY-NC-ND-4.0]: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
