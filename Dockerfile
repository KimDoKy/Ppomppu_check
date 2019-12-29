FROM        ubuntu:18.04
MAINTAINER  makingfunk0@gmain.com

COPY        ./ppomppu /srv/app/ppomppu

RUN         apt-get -y update
RUN         apt-get -y install python3.6
RUN         apt-get -y install python3-pip
RUN         apt-get -y install nginx
RUN         apt-get -y install supervisor
RUN         apt-get -y install systemd

WORKDIR     /srv/app/ppomppu/

COPY        ./requirements.txt /srv/app/ppomppu
RUN         pip3 install -r requirements.txt
RUN         pip3 install uwsgi
RUN         pip3 install --upgrade 'sentry-sdk==0.13.5'
RUN         pip3 install raven --upgrade
RUN         apt-get install -y redis-server
