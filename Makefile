ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.PHONY: all
all: update dotfiles

.PHONY: update
	@git checkout master
	@git pull

.PHONY: dotfiles
dotfiles: # Create directories and symlinks for dotfiles
	cd links && \
	  find . -type d -exec mkdir -p $(HOME)/{} \; && \
	  find . -type f -exec ln -fsv $(ROOT_DIR)/links/{} $(HOME)/{} \;
