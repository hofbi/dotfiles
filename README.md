# Dotfiles

[![Actions Status](https://github.com/hofbi/dotfiles/workflows/CI/badge.svg)](https://github.com/hofbi/dotfiles)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](/LICENSE.md)

Collection of config and dotfiles.

## Setup

Clone the repository and run

```shell
./install.sh
```

This will change the default shell to zsh.

## Test Environment

Setup the docker test environment

```shell
cd docker
docker compose build --build-arg user_id=$UID
docker compose run dotfiles
```
