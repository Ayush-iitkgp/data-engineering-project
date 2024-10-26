FROM python:3.10.11-buster

WORKDIR /opt/data-engineering-project

COPY poetry.lock pyproject.toml ./

RUN pip install --upgrade pip && \
    pip install "poetry==1.6.1" && \
    poetry config virtualenvs.create false && \
    poetry install

COPY src src
COPY tests tests

ENV PYTHONPATH /opt/data-engineering-project
