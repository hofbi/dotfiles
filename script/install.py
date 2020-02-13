#!/usr/bin/env python3

import os
from pathlib import Path
from subprocess import check_call


def call(command):
    print(f"calling: \"{command}\"")
    return check_call(command, shell=True)


def clone_or_update_git_repo(url, path):
    if not Path(path).expanduser().is_dir():
        call(f"git clone {url} {path}")
    else:
        call(f"git -C {path} pull")


def install_apt_packages():
    call("sudo apt install -y vim zsh terminator tmux powerline fonts-powerline mmv")


def install_oh_my_zsh():
    def install_plugins():
        oh_path = "~/.oh-my-zsh/custom"
        clone_or_update_git_repo(
            "https://github.com/romkatv/powerlevel10k.git", f"{oh_path}/themes/powerlevel10k")
        clone_or_update_git_repo("https://github.com/zsh-users/zsh-autosuggestions.git",
                                 f"{oh_path}/plugins/zsh-autosuggestions")
        clone_or_update_git_repo("https://github.com/zsh-users/zsh-syntax-highlighting.git",
                                 f"{oh_path}/plugins/zsh-syntax-highlighting")

    if "ZSH" not in os.environ:
        call("sh -c \"$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)\"")
    install_plugins()


def install_vim_config():
    clone_or_update_git_repo(
        "https://github.com/VundleVim/Vundle.vim.git", "~/.vim/bundle/Vundle.vim")
    call("vim +PluginInstall +qall")


def install_tmux_config():
    clone_or_update_git_repo(
        "https://github.com/tmux-plugins/tpm", "~/.tmux/plugins/tpm")
    call(
        "tmux start-server && tmux new-session -d && ~/.tmux/plugins/tpm/bin/install_plugins && tmux kill-server")


def install_fzf():
    clone_or_update_git_repo("https://github.com/junegunn/fzf.git", "~/.fzf")
    call("~/.fzf/install")


def main():
    install_apt_packages()
    install_oh_my_zsh()
    install_vim_config()
    install_tmux_config()
    install_fzf()


if __name__ == "__main__":
    main()
