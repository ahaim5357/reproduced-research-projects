# Set global arguments
ARG PROJECT_PATCHER_VER=0.3.0

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

## Add git to alpine to pull necessary repositories
RUN apk update
RUN apk add git

## Install project_patcher and run
RUN python3 -m pip install "project-patcher[git]==${PROJECT_PATCHER_VER}"
RUN project_patcher src

## Setup project specific info
FROM python:3.7.3-slim-stretch

## Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

## Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

## Install required dependencies to run code
RUN apt update
RUN apt -y install gcc g++
RUN apt -y install texlive texlive-latex-extra
RUN apt -y install imagemagick

## Copy project files from previous stage here
RUN mkdir /src
COPY --from=projects /_src /src

## Setup python
RUN python3 -m pip install -r /src/requirements.txt

## Allow execution of the script file
RUN chmod 744 /src/run_demos_and_synthetics.sh

## Setup script run
WORKDIR /src
CMD [ "sh", "run_demos_and_synthetics.sh" ]
