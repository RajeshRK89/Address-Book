FROM python:3.9.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /address_book
WORKDIR /address_book
COPY ./requirements.txt /address_book/requirements.txt


# RUN apt-get update &&\
#     apt-get install -y binutils libproj-dev gdal-bin

RUN pip install -r /address_book/requirements.txt

RUN python manage.py migrate