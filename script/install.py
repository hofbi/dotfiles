#!/usr/bin/env python3

# flake8: noqa: E501

import os
from pathlib import Path
from subprocess import check_call


def call(command: str) -> int:
    print(f'calling: "{command}"')
    return check_call(command, shell=True)


def clone_or_update_git_repo(url: str, path: str) -> None:
    if not Path(path).expanduser().is_dir():
        call(f"git clone {url} {path}")
    else:
        call(f"git -C {path} pull")


def install_apt_packages():
    sudo_command = "sudo"
    if "PASS" in os.environ:
        # Set pass for CI job
        sudo_command = f"echo {os.environ.get('PASS')} | sudo -S"

    call(
        f"{sudo_command} apt update && {sudo_command} apt install -y vim zsh terminator tmux powerline fonts-powerline mmv"
    )


def install_fonts():
    call(
        "wget -P ~/.local/share/fonts https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf"
    )
    call(
        "wget -P ~/.local/share/fonts https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf"
    )
    call(
        "wget -P ~/.local/share/fonts https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf"
    )
    call(
        "wget -P ~/.local/share/fonts https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf"
    )


def install_oh_my_zsh():
    def install_plugins():
        oh_path = "~/.oh-my-zsh/custom"
        clone_or_update_git_repo(
            "https://github.com/romkatv/powerlevel10k.git",
            f"{oh_path}/themes/powerlevel10k",
        )
        clone_or_update_git_repo(
            "https://github.com/zsh-users/zsh-autosuggestions.git",
            f"{oh_path}/plugins/zsh-autosuggestions",
        )
        clone_or_update_git_repo(
            "https://github.com/zsh-users/zsh-syntax-highlighting.git",
            f"{oh_path}/plugins/zsh-syntax-highlighting",
        )

    if "ZSH" not in os.environ:
        call(
            'sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -) --keep-zshrc"'
        )
    install_plugins()


def install_vim_config():
    clone_or_update_git_repo(
        "https://github.com/VundleVim/Vundle.vim.git", "~/.vim/bundle/Vundle.vim"
    )
    call("vim +PluginInstall +PluginClean! +qall")


def install_tmux_config():
    clone_or_update_git_repo(
        "https://github.com/tmux-plugins/tpm", "~/.tmux/plugins/tpm"
    )
    call(
        "tmux start-server && tmux new-session -d && sleep 1 && ~/.tmux/plugins/tpm/scripts/install_plugins.sh && tmux kill-server"
    )


def install_fzf():
    clone_or_update_git_repo("https://github.com/junegunn/fzf.git", "~/.fzf")
    call("~/.fzf/install --all")


def install_local_config():
    Path.home().joinpath(".zshrc.local").touch(exist_ok=True)


def main():
    install_apt_packages()
    install_fonts()
    install_oh_my_zsh()
    install_vim_config()
    install_tmux_config()
    install_fzf()
    install_local_config()


if __name__ == "__main__":
    main()
