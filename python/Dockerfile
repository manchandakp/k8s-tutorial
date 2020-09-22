FROM python:3.6.12-slim-buster

WORKDIR /usr/src/app

RUN pip install --trusted-host pypi.org --upgrade pip
COPY ./requirements.txt ./
RUN pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org -r requirements.txt

COPY ./ ./
