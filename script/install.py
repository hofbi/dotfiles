#!/usr/bin/env python3

"""Installer for all dotfiles and the tools using it"""

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


def get_ubuntu_version() -> str:
    lines = Path("/etc/os-release").read_text().splitlines()  # pylint: disable=W1514
    version = next(line for line in lines if "VERSION_ID" in line)
    return version.split("=")[1].strip('"')


def install_apt_packages() -> None:
    call("sudo apt update")
    call("sudo apt install -y vim zsh terminator tmux powerline fonts-powerline mmv ripgrep")
    if get_ubuntu_version().split(".")[0] >= "24":
        call("sudo apt install -y git-delta")


def install_fonts() -> None:
    wget_fonts_base_call = "wget -P ~/.local/share/fonts https://github.com/romkatv/powerlevel10k-media/raw/master"
    call(f"{wget_fonts_base_call}/MesloLGS%20NF%20Regular.ttf")
    call(f"{wget_fonts_base_call}/MesloLGS%20NF%20Bold.ttf")
    call(f"{wget_fonts_base_call}/MesloLGS%20NF%20Italic.ttf")
    call(f"{wget_fonts_base_call}/MesloLGS%20NF%20Bold%20Italic.ttf")


def install_oh_my_zsh() -> None:
    def install_plugins() -> None:
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
            'sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -) --keep-zshrc"'  # noqa: E501
        )
    install_plugins()


def install_vim_config() -> None:
    clone_or_update_git_repo("https://github.com/VundleVim/Vundle.vim.git", "~/.vim/bundle/Vundle.vim")
    call("vim +PluginInstall +PluginClean! +qall")


def install_tmux_config() -> None:
    tmp_path = "~/.tmux/plugins/tpm"
    clone_or_update_git_repo("https://github.com/tmux-plugins/tpm", tmp_path)
    call(
        f"tmux start-server && tmux new-session -d && sleep 1 && {tmp_path}/scripts/install_plugins.sh && tmux kill-server"  # noqa: E501
    )


def install_fzf() -> None:
    clone_or_update_git_repo("https://github.com/junegunn/fzf.git", "~/.fzf")
    call("~/.fzf/install --all")


def install_local_config() -> None:
    Path.home().joinpath(".gitconfig.local").touch(exist_ok=True)
    Path.home().joinpath(".zshrc.local").touch(exist_ok=True)


def install_i3() -> None:
    call("sudo add-apt-repository ppa:agornostal/ulauncher")
    call("sudo apt update && sudo apt install -y i3 feh arandr ulauncher")
    call("pip3 install i3ipc")


def main() -> None:
    install_apt_packages()
    install_fonts()
    install_oh_my_zsh()
    install_vim_config()
    install_tmux_config()
    install_fzf()
    install_local_config()


if __name__ == "__main__":
    main()
