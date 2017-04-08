################################################################################
# Jenkins DooD with Dapper
# Author: Newnewcoder <pinkycho1221@gmail.com>
################################################################################

FROM axltxl/jenkins-dood
MAINTAINER Newnewcoder <pinkycho1221@gmail.com>

# Supervisord
USER root

# Install Dapper
RUN curl -sL https://releases.rancher.com/dapper/latest/dapper-`uname -s`-`uname -m` > /usr/local/bin/dapper && \
chmod +x /usr/local/bin/dapper && \
usermod -aG staff jenkins

# Jenkins user
USER jenkins

# Start supervisord when running the container
CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf