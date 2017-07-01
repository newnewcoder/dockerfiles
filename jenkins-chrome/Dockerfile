FROM jenkins
################################################################################
# jenkins with chrome
# Author: Newnewcoder <pinkycho1221@gmail.com>
################################################################################

USER root
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d//google-chrome.list
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN apt-get update \
 && apt-get -y install libxpm4 libxrender1 libgtk2.0-0 libnss3 libgconf-2-4 \
 && apt-get -y install google-chrome-stable \
 && apt-get -y install xvfb gtk2-engines-pixbuf \
 && apt-get -y install xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable
 
ENV DISPLAY :99

ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

USER jenkins