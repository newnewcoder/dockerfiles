################################################################################
# simple Mysql auto backup
# Author: Newnewcoder <pinkycho1221@gmail.com>
################################################################################

FROM python:3.6.7-jessie

ENV TZ=Asia/Taipei

COPY . /

RUN apt-get update && apt-get install mysql-client -y
RUN pip install -r requirements.txt
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]