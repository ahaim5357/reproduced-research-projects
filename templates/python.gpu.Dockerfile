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

# Setup project specific info
FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04

## Disable interactions with package configurations
ARG DEBIAN_FRONTEND=noninteractive

## Setup necessary libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    make \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    ca-certificates \
    curl \
    llvm \
    libncurses5-dev \
    xz-utils \
    tk-dev \
    libxml2-dev \
    libxmlsec1-dev \
    libffi-dev \
    liblzma-dev \
    mecab-ipadic-utf8 \
    git

## Install pyenv and chosen Python version
ENV PYENV_ROOT /.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN curl https://pyenv.run | bash \
    && pyenv install 3.11.4 \
    && pyenv global 3.11.4 \
    && pyenv rehash

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
WORKDIR /src
CMD [ "python3", "<file_name>" ]
