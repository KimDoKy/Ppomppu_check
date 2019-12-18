FROM        ppomppu-base
MAINTAINER  makingfunk0@gmain.com


COPY    .conf/uwsgi-app.ini /etc/uwsgi/sites/app.ini
COPY    .conf/uwsgi.service /etc/systemd/system/uwsgi.service
COPY    .conf/nginx-app.conf /etc/nginx/sites-available/app
COPY    .conf/nginx.conf /etc/nginx/nginx.conf
COPY    .conf/supervisor-app.conf /etc/supervisor/conf.d/
COPY    .conf/celery_ppomppu_beat.conf /etc/supervisor/conf.d/
COPY    .conf/celery_ppomppu_worker.conf /etc/supervisor/conf.d/
COPY    ./ppomppu/.secret /srv/app/ppomppu/.secret
RUN     ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app

EXPOSE  4567 5432 6379 8000
CMD     supervisord -n

