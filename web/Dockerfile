FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean && pip install telebot && pip install pyTelegramBotAPI

RUN mkdir /PR
COPY . /PR/
WORKDIR /PR

RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /PR/
