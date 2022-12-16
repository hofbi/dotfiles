FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Berlin

RUN apt-get update && apt-get install -y \
    tzdata \
    keyboard-configuration \
    git \
    make \
    python3 \
    sudo \
    wget

RUN useradd -ms /bin/bash foo && echo "foo:a" | chpasswd && adduser foo sudo
USER foo
