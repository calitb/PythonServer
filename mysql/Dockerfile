FROM jsurf/rpi-mariadb

LABEL maintainer="Carlos Thurber B."

COPY ./config/my.cnf /etc/mysql/conf.d
COPY ./scripts/dump.sql docker-entrypoint-initdb.d/init.sql
