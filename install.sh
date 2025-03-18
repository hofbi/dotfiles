#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

setup_dotfiles() {
    cd "$SCRIPT_DIR/links" || exit 1
    find . -type d -exec mkdir -p "$HOME/{}" \;
    find . -type f -exec ln -fsv "$SCRIPT_DIR/links/{}" "$HOME/{}" \;
}

main() {
    "$SCRIPT_DIR/script/install.py"
}

setup_dotfiles
main
