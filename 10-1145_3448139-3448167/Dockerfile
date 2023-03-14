# Set global arguments
ARG PROJECT_PATCHER_VER=0.2.0

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
FROM python:3.9.5-slim-buster

## Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

## Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

## Copy project files from previous stage here
RUN mkdir /src
COPY --from=projects /_src /src

## Setup python
RUN python3 -m pip install -r /src/requirements.txt

## Setup script run
WORKDIR /src/analysis
CMD [ "python3", "paper_results_replication_file.py" ]
