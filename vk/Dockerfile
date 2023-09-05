FROM python:3.10
LABEL authors="igor"

COPY ./requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY . /src
WORKDIR src