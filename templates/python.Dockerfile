# Set global arguments
ARG JAMMIES_VER=0.4.3

# Get and patch project for working directory
FROM python:3.11.2-alpine3.17 as projects

## Set local arguments
ARG JAMMIES_VER

## Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

## Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

## Copy files to directory
COPY . ./

## Add git to alpine to pull necessary repositories
RUN apk update
RUN apk add git

## Install jammies and run
RUN python3 -m pip install "jammies[all]==${JAMMIES_VER}"
RUN jammies patch src

## Setup project specific info
FROM python:3.11.4-bookworm

## Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

## Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

## Copy project files from previous stage here
RUN mkdir /src
COPY --from=projects /src /src

## Setup python
RUN python3 -m pip install -r /src/requirements.txt

## Setup script run
CMD [ "python3", "<file_name>" ]