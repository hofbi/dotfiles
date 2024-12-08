FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Berlin

RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    git \
    make \
    python3 \
    sudo \
    wget && \
    rm -rf /var/lib/apt/lists/*

ARG user_id=1000
ARG group_id="${user_id}"
ARG username="foo"

RUN groupadd --gid "${group_id}" "${username}" \
    && useradd --create-home --shell /bin/bash --no-log-init --uid "${user_id}" --gid "${group_id}" "${username}" \
    && usermod -aG sudo "${username}" \
    && echo "${username} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER "${user_id}"

ENV USER="${username}" USERNAME="${username}"
ENV HOME /home/"${username}"
WORKDIR "${HOME}"
