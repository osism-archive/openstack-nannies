FROM python:3.7-alpine

COPY requirements.txt /requirements.txt
COPY files/crontab /etc/crontabs/root

COPY src/neutron-* /usr/local/bin
COPY src/nova-* /usr/local/bin

RUN apk add --no-cache --virtual .build-deps \
      build-base \
      libffi-dev \
      openssl-dev \
      python3-dev \
    && apk add --no-cache tini \
    && pip install --no-cache-dir -r requirements.txt \
    && rm /requirements.txt \
    && apk del .build-deps

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["/usr/sbin/crond", "-f", "-d", "8"]
