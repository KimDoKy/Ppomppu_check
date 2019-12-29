FROM        leafunk/ppomppu-checker
MAINTAINER  python.dev@kakao.com

COPY    .conf/nginx-app.conf /etc/nginx/sites-available/app
COPY    .conf/nginx.conf /etc/nginx/nginx.conf
RUN     ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app

EXPOSE  4567 5432 6379 80
CMD     supervisord -n

