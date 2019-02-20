ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.PHONY: all
all: update dotfiles

.PHONY: update
	@git checkout master
	@git pull

.PHONY: dotfiles
dotfiles: # Create symlinks for dotfiles
	@cd links; find . -type f -exec ln -fsv $(ROOT_DIR)/links/{} $(HOME)/{} \;    # create links
