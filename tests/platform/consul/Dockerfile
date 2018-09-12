FROM alpine:latest
ARG consul_version=3
ARG url="https://releases.hashicorp.com/consul/${consul_version}/consul_${consul_version}_linux_amd64.zip"

COPY config.json /tmp/consul/config.json
COPY acl.json /tmp/consul/acl.json

RUN apk add --update unzip wget && \
    wget  $url -O /tmp/consul.zip && \
    unzip /tmp/consul.zip -d /usr/bin/
#    consul agent -config-dir=/tmp/consul
