ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.PHONY: all
all: update dotfiles

.PHONY: setup
setup:
	@script/install.py

.PHONY: dotfiles
dotfiles: # Create directories and symlinks for dotfiles
	cd links && \
	  find . -type d -exec mkdir -p $(HOME)/{} \; && \
	  find . -type f -exec ln -fsv $(ROOT_DIR)/links/{} $(HOME)/{} \;
