################################################################################
# python3.6 with ffmpeg
# Author: Newnewcoder <pinkycho1221@gmail.com>
################################################################################

# Pull base image.
FROM ubuntu:trusty
MAINTAINER Newnewcoder <pinkycho1221@gmail.com>

# Add ppa.
RUN apt-get update && apt-get install -y software-properties-common && \
    add-apt-repository ppa:jonathonf/python-3.6 -y && \
    add-apt-repository ppa:mc3man/trusty-media -y

# Install python3.6.
RUN apt-get update -y && \
    apt-get install python3.6 -y && \
    apt-get -y install python3.6-dev 

# Setting python3.6 default
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1

# Install pip
RUN apt-get -y install curl
RUN curl https://bootstrap.pypa.io/get-pip.py | python

# Install ffmpeg.
RUN apt-get update -y && \
    apt-get dist-upgrade -y && \
    apt-get install ffmpeg -y

# Setting Timezone
ENV TZ 'Asia/Taipei'
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Setting locale
RUN locale-gen zh_TW zh_TW.UTF-8 en_US.UTF-8
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8 

RUN apt-get autoremove
RUN apt-get clean

WORKDIR /work