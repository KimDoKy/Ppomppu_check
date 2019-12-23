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

COPY    .conf/uwsgi-app.ini /etc/uwsgi/sites/app.ini
COPY    .conf/uwsgi.service /etc/systemd/system/uwsgi.service
COPY    .conf/nginx-app.conf /etc/nginx/sites-available/app
COPY    .conf/nginx.conf /etc/nginx/nginx.conf
COPY    .conf/supervisor-app.conf /etc/supervisor/conf.d/
COPY    .conf/celery_ppomppu_beat.conf /etc/supervisor/conf.d/
COPY    .conf/celery_ppomppu_worker.conf /etc/supervisor/conf.d/
COPY    ./ppomppu/.secret /srv/app/ppomppu/.secret
RUN     ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app

EXPOSE  4567 5432 6379 80
CMD     supervisord -n

