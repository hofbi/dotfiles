file_finder = find . -type f $(1) -not -path './venv/*'

ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.PHONY: default
default:
	@script/install.py

.PHONY: setup
setup: dotfiles default

.PHONY: dotfiles
dotfiles: # Create directories and symlinks for dotfiles
	cd links && \
	  find . -type d -exec mkdir -p $(HOME)/{} \; && \
	  find . -type f -exec ln -fsv $(ROOT_DIR)/links/{} $(HOME)/{} \;
