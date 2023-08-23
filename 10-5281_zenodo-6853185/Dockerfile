# Set global arguments
ARG JAMMIES_VER=0.4.5

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
RUN jammies patch src -y

# Setup Java runtime via jlink
FROM eclipse-temurin:17.0.8_7-jdk-jammy as java

# Create custom runtime
RUN $JAVA_HOME/bin/jlink \
    --add-modules ALL-MODULE-PATH \
    --strip-debug \
    --no-man-pages \
    --no-header-files \
    --compress=2 \
    --output /javaruntime

# Setup project specific info
FROM python:3.11.4-bookworm

## Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

## Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

## Copy Java runtime over
ENV JAVA_HOME=/opt/java/openjdk
ENV PATH $JAVA_HOME/bin:$PATH
COPY --from=java /javaruntime $JAVA_HOME

## Copy project files from previous stage here
RUN mkdir /src
COPY --from=projects /src /src
WORKDIR /src

## Setup python
RUN python3 -m pip install .

## Setup script run
CMD [ "python3", "./helper_code/models/regression/train_rf_regression_full_cv.py", "--training-data-filepath", "./VLE_datasets/v1/VLE_12k_dataset_v1.csv", "--output-dir", "./results" ]
