# [Mathematical Creativity in Elementary School Children: General Patterns and Effects of an Incubation Break][paper]

This is a project constructor and patcher for the paper [*Mathematical Creativity in Elementary School Children: General Patterns and Effects of an Incubation Break*][paper] by Stacy T. Shaw, Michelle L. Luna, Briana Rodriguez, Jan Yeh, Nancy Villalta, and Gerardo Ramirez.

## Project Files

The constructor downloads the following files:

* [Open Science Framework Project][osf]

## Setup Instructions

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

After making sure you have `renv` installed, open an R terminal in the generated `_src` directory. This should bootstrap `renv` to the specified version. From there, you can initialize the environment via `renv::restore()`, or by using `renv::init()` followed by `1` in the selection menu.

Afterwards, run `child_R_code.R`. You can do this directly in the R terminal via:

```r
source('child_R_code.R', echo = TRUE)
```

## Issues

* Typo in Paper: (r(209) = 0.48, p < 0.001, 95% CI [0.37, −0.58])
    * Correction: (r(209) = 0.48, p < 0.001, 95% CI [0.37, 0.58])
* Incorrect Rounding in Paper: (γ = 0.12, SE = 0.03, p = 0.013, R2 = 0.12)
    * Correction: (γ = 0.12, SE = 0.03, p = 0.014, R2 = 0.12)
* η^2 is not calculated in the codebase

[paper]: https://doi.org/10.3389/feduc.2022.835911
[osf]: https://osf.io/fwh6g/

[project_patcher]: https://github.com/ahaim5357/project-patcher
[rlang]: https://www.r-project.org/
[renv]: https://rstudio.github.io/renv/
[devtools]: https://www.r-project.org/nosvn/pandoc/devtools.html
