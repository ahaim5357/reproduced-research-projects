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

> We are loading into the terminal instead of into the shell script to copy any generated figures onto the local machine as they cannot otherwise be easily viewed.

Once in the docker terminal, you can run the shell script via:

```sh
sh run_demos_and_synthetics.sh
```

You can look through the terminal output and compare the numbers within the paper. To view the figures on the local machine, you can copy them to the volume via:

```sh
cp -R ../data /volume
```

### Method 2: Local Setup

This project uses the Python package `project_patcher[git]` to setup and fix any issues in the codebase. For instructions on how to download and generate the project from this directory, see the [`project_patcher`][project_patcher] repository.

The following instructions have been reproduced using [Python][python] 3.7.3. This project does not make any guarantees that this will work outside of the specified version. Make sure you have Python, along with gcc for Cython, before attempting anything below.

> You will be unable to execute the code on Windows Native. It expects libraries which are only easily installable through Cygwin or Mingw. Additionally, any non-computationally powerful machine won't be able to run the code. One of the substructures in the intervention takes approximately 2-3 days to execute.

First, you will need to download the following libraries using your associated package manager or through the binaries:

* [gcc](https://gcc.gnu.org/)
* g++
* [TeX Live](https://www.tug.org/texlive/)
* texlive-latex-extra
* [ImageMagick](https://imagemagick.org/)

> On the subject of ImageMagick, the conversion to the PDF may fail on newer versions. This is likely due to a preventative measure ImageMagick took when a security vulnerability was discovered in GhostScript, one of its dependencies. If you are using GhostScript 9.24 or above (check via `gs --version`), then you can comment out the line in question within `/etc/ImageMagick-<ver>/policy.xml` to allow the conversion to occur. `<ver>` in this case is the version of ImageMagick downloaded (currently 6 as of March 2023).
> ```xml
> <policymap>
>   <!-- ... -->
>   <!-- disable ghostscript format types -->
>   <policy domain="coder" rights="none" pattern="PS" />
>   <policy domain="coder" rights="none" pattern="PS2" />
>   <policy domain="coder" rights="none" pattern="PS3" />
>   <policy domain="coder" rights="none" pattern="EPS" />
> <!--  <policy domain="coder" rights="none" pattern="PDF" /> -->
>   <policy domain="coder" rights="none" pattern="XPS" />
> </policymap>
> ```

Then, you will need to navigate to the generated `_src` directory. You will need to install the required dependencies into the global Python instance or a virtual environment via:

```sh
python3 -m pip install -r requirements.txt
```

After installing the required dependencies, navigate to the project directory and run the `run_demos_and_synthetics.sh` script via:

```sh
sh run_demos_and_synthetics.sh
```

> As Windows Native is not supported, a bash script can be typically run across any machine or unix subsystem. If not, you can run the methods inside the script manually.

You can look through the terminal output and compare the numbers within the paper. Additionally, the figures are generated within the `data` directory within `_src`.

[docker]: https://www.docker.com/
[project_patcher]: https://github.com/ahaim5357/project-patcher
[python]: https://www.python.org/
