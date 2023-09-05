FROM python:3.11
LABEL authors="igor"

COPY ./requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY . /src
WORKDIR src