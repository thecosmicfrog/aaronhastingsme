FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN apt update && apt dist-upgrade -y && pip install -r requirements.txt
COPY . /app/

