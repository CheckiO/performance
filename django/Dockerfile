FROM python:3.9.0

RUN \
    groupadd -r site && \
    useradd -r -s /bin/bash -g site site

RUN \
    chown -R site:site /opt

RUN \
    apt-get update && \
    apt-get install -y \
        nginx && \
    rm -rf /var/lib/apt/lists/*

RUN \
    ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

ENV SUPERVISOR_VERSION=4.2.1
ENV GUNICORN_VERSION=20.0.4
ENV DJANGO_VERSION==2.2.17
ENV DJANGORESTFRAMEWORK_VERSION==3.12.2

RUN \
    pip install --upgrade \
        pip \
        setuptools \
        wheel \
        supervisor==$SUPERVISOR_VERSION \
        gunicorn==$GUNICORN_VERSION \
        django==$DJANGO_VERSION \
        djangorestframework==$DJANGORESTFRAMEWORK_VERSION


COPY deploy/nginx.conf /etc/nginx/conf.d/default.conf

COPY deploy/supervisord.conf /opt/supervisord.conf

COPY project /opt/project

WORKDIR /opt/project

EXPOSE 8001
