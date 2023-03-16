# Set global arguments
ARG PROJECT_PATCHER_VER=0.3.0
ARG RENV_VER=0.16.0

# Get and patch project for working directory
FROM python:3.11.2-alpine3.17 as projects

## Set local arguments
ARG PROJECT_PATCHER_VER

## Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

## Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

## Copy files to directory
COPY . ./

## Install project_patcher and run
RUN python3 -m pip install project-patcher==${PROJECT_PATCHER_VER}
RUN project_patcher src

## Setup project specific info
FROM r-base:4.2.2

## Set local arguments
ARG RENV_VER

## Add necessary libraries to debian
RUN apt update
RUN apt -y install cmake
RUN apt -y install libcurl4-openssl-dev
RUN apt -y install libssl-dev
RUN apt -y install libfontconfig1-dev
RUN apt -y install libxml2-dev

## Setup renv
ENV RENV_VERSION ${RENV_VER}
RUN R -e "install.packages('remotes', repos = c(CRAN = 'https://cloud.r-project.org'))"
RUN R -e "remotes::install_github('rstudio/renv@${RENV_VERSION}')"

## Copy project files from previous stage here
RUN mkdir /src
WORKDIR /src
COPY --from=projects /_src ./

## Restore renv environment
RUN R -e "renv::restore()" 
CMD [ "R" ]
