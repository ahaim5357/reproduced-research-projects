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

> We are loading into the terminal instead of into R to copy any generated figures onto the local machine as they cannot otherwise be easily viewed.

Once in the docker terminal, you can run the R script via:

```sh
R -e "source('child_R_code.R', echo = TRUE)"
```

You can look through the terminal output and compare the numbers within the paper. To view the figures on the local machine, you can copy them to the volume via:

```sh
cp -R ./figures /volume
```

### Method 2: Local Setup

This project uses the Python package `project_patcher` to setup and fix any issues in the codebase. For instructions on how to download and generate the project from this directory, see the [`project_patcher`][project_patcher] repository.

The following instructions have been reproduced using [R][rlang] 4.2.2. This project does not make any guarantees that this will work outside of the specified version. Make sure you have R, along with RTools for Windows, before attempting anything below.

This project uses [`renv`][renv] 0.16.0 to manage its dependencies. You can install `renv` from CRAN through an R terminal via:

```r
install.packages("renv")
```

If you would like to use the exact version of `renv` in this instruction, you can use [`devtools`][devtools] to download a specific version of the library:

```r
install.packages("devtools")
devtools::install_version("renv", version = "0.16.0")
```

After making sure you have `renv` installed, open an R terminal in the generated `_src` directory. This should bootstrap `renv` to the specified version. If `renv` isn't activated, it will prompt you to activate renv by either answering `Y` to a prompt or by typing `renv::activate()`. From there, you can initialize the environment via `renv::restore()`, or by using `renv::init()` followed by `1` in the selection menu if needed. The process should take anywhere from 30 minutes to an hour.

> If the restoration ends up crashing, you may be missing some necessary Operating System specific dependencies. As such, you will need to download or setup the dependencies on your machine. R will mention the necessary dependencies needed every time it crashes; however, for the sake of convenience, the ones encountered for Unix-like operating systems are listed below:
> * CMake - cmake (All)
> * libcurl - libcurl4-openssl-dev (Debian, Ubuntu, etc.), libcurl-devel (Fedora, CentOS, RHEL)
> * openssl - libssl-dev (Debian, Ubuntu, etc.), openssl-devel (Fedora, CentOS, RHEL), libssl_dev (Solaris), openssl (Mac OSX)
> * fontconfig freetype2 - libfontconfig1-dev (Debian, Ubuntu, etc.),fontconfig-devel (Fedora, EPEL), fontconfig_dev (Solaris), freetype (OSX)
> * libxml-2.0 - libxml2-dev (Debian, Ubuntu, etc.), libxml2-devel (Fedora, CentOS, RHEL), libxml2_dev (Solaris)
> * GCC - gcc (All)
> * XCode Command Line Tools - xcode-select (Mac OSX only)
> * XQuartz - xquartz (Mac OSX only)
> * Independent JPEG Group's JPEG - jpeg (Mac OSX only)

Afterwards, run `child_R_code.R`. You can do this directly in the R terminal via:

```r
source('child_R_code.R', echo = TRUE)
```

You can look through the terminal output and compare the numbers within the paper. Additionally, figures are generated within the `figures` directory within `_src`.

[docker]: https://www.docker.com/
[project_patcher]: https://github.com/ahaim5357/project-patcher
[rlang]: https://www.r-project.org/
[renv]: https://rstudio.github.io/renv/
[devtools]: https://www.r-project.org/nosvn/pandoc/devtools.html
