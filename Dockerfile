FROM ubuntu:18.04
MAINTAINER Inhyuk Choi <dlsgur9710@naver.com>

RUN apt-get -y update
RUN apt-get install -y python3.8
RUN apt-get install python3-pip
RUN apt-get install python3.8-dev
RUN apt-get install libmysqlclient-dev

RUN update-alternatives --install /usr/bin/python3 python /usr/bin/python3.8 1

RUN mkdir /code
WORKDIR /code

ADD requirement.txt /code/
RUN pip install -r requirements.txt
ADD . /code/



