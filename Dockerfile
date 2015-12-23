FROM alpine:latest
MAINTAINER jesse.miller@adops.com

# install deps
RUN apk update && \
    apk add --update \
      build-base \
      git \
      postgresql \
      postgresql-dev \
      python3 \
      python3-dev
RUN pip3 install --upgrade pip && \
    pip3 install bottle \
                 git+https://github.com/OAODEV/config-finder.git@master \
                 nose \
                 psycopg2


# clean up from instalation
RUN rm -rf ~/.pip/cache/*
RUN apk del postgresql-dev \
            python3-dev \
            git \
    && rm -rf /var/cache/apk/* \
    && rm -rf /var/lib/postgresql/data
