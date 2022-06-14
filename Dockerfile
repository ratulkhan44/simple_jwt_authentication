FROM python:3.8-slim-buster

RUN mkdir /home/drf_authentication

WORKDIR /home/drf_authentication

COPY ./ /home/drf_authentication/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip
RUN pip3 install -r /home/drf_authentication/requirements.txt

EXPOSE 9000

