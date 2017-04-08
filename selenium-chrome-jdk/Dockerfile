################################################################################
# Selenium/standalone-chrome with jdk8
# Author: Newnewcoder <pinkycho1221@gmail.com>
################################################################################

# Pull base image.
FROM selenium/standalone-chrome:3.0.1-germanium
MAINTAINER Newnewcoder <pinkycho1221@gmail.com>

# Supervisord
USER root

# Install open-jdk8.
RUN apt-get update && apt-get install -y software-properties-common && \
add-apt-repository ppa:openjdk-r/ppa -y && \
apt-get update && \
apt-get install -y openjdk-8-jdk && \
update-alternatives --config javac

USER seluser