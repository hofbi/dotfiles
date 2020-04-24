file_finder = find . -type f $(1) -not -path './venv/*'

ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PY_FILES = $(call file_finder,-name "*.py")

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

format:
	$(PY_FILES) | xargs black

check_format:
	$(PY_FILES) | xargs  black --diff --check
