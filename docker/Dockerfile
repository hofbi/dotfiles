FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    git \
    make \
    python3 \
    sudo \
    wget

RUN useradd -ms /bin/bash foo && echo "foo:a" | chpasswd && adduser foo sudo
USER foo
