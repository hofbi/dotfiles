#!/usr/bin/env python3

"""Installer for all dotfiles and the tools using it."""

import os
import platform
from pathlib import Path
from subprocess import check_call


def call(command: str) -> int:
    print(f'calling: "{command}"')
    return check_call(command, shell=True)


def clone_or_update_git_repo(url: str, path: Path) -> None:
    if not path.is_dir():
        call(f"git clone {url} {path}")
    else:
        call(f"git -C {path} pull")


def get_major_ubuntu_version() -> int:
    lines = Path("/etc/os-release").read_text().splitlines()  # pylint: disable=W1514
    version = next(line for line in lines if "VERSION_ID" in line)
    ubuntu_version = version.split("=")[1].strip('"')
    return int(ubuntu_version.split(".")[0])


def install_apt_packages() -> None:
    call("sudo apt update")
    call("sudo apt install -y wget vim zsh terminator tmux powerline fonts-powerline mmv ripgrep")
    min_version_required_for_git_delta = 24
    if get_major_ubuntu_version() >= min_version_required_for_git_delta:
        call("sudo apt install -y git-delta")


def install_brew_packages() -> None:
    call("brew update")
    call("brew install wget vim zsh tmux mmv ripgrep git-delta pipx")
    call("pipx install powerline-status --force")


def install_fonts() -> None:
    fonts_dir = Path.home() / ("Library/Fonts" if platform.system() == "Darwin" else ".local/share/fonts")
    fonts_dir.mkdir(parents=True, exist_ok=True)

    wget_fonts_base_call = f"wget -P {fonts_dir} https://github.com/romkatv/powerlevel10k-media/raw/master"
    call(f"{wget_fonts_base_call}/MesloLGS%20NF%20Regular.ttf")
    call(f"{wget_fonts_base_call}/MesloLGS%20NF%20Bold.ttf")
    call(f"{wget_fonts_base_call}/MesloLGS%20NF%20Italic.ttf")
    call(f"{wget_fonts_base_call}/MesloLGS%20NF%20Bold%20Italic.ttf")


def install_oh_my_zsh() -> None:
    def install_plugins() -> None:
        oh_path = Path.home() / ".oh-my-zsh" / "custom"
        clone_or_update_git_repo("https://github.com/romkatv/powerlevel10k.git", oh_path / "themes" / "powerlevel10k")
        clone_or_update_git_repo(
            "https://github.com/zsh-users/zsh-autosuggestions.git", oh_path / "plugins" / "zsh-autosuggestions"
        )
        clone_or_update_git_repo(
            "https://github.com/zsh-users/zsh-syntax-highlighting.git", oh_path / "plugins" / "zsh-syntax-highlighting"
        )

    if "ZSH" not in os.environ:
        call(
            'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended --keep-zshrc'  # noqa: E501
        )
        call("sudo chsh -s $(which zsh)")
    install_plugins()


def install_vim_config() -> None:
    clone_or_update_git_repo(
        "https://github.com/VundleVim/Vundle.vim.git", Path.home() / ".vim" / "bundle" / "Vundle.vim"
    )
    call("vim +PluginInstall +PluginClean! +qall")


def install_tmux_config() -> None:
    tpm_path = Path.home() / ".tmux" / "plugins" / "tpm"
    clone_or_update_git_repo("https://github.com/tmux-plugins/tpm", tpm_path)
    call(
        f"tmux start-server && tmux new-session -d && sleep 1 && {tpm_path}/scripts/install_plugins.sh && tmux kill-server"  # noqa: E501
    )


def install_fzf() -> None:
    fzf_path = Path.home() / ".fzf"
    clone_or_update_git_repo("https://github.com/junegunn/fzf.git", fzf_path)
    call(f"{fzf_path / 'install'} --all")


def install_local_config() -> None:
    Path.home().joinpath(".gitconfig.local").touch(exist_ok=True)
    Path.home().joinpath(".zshrc.local").touch(exist_ok=True)


def install_i3() -> None:
    call("sudo add-apt-repository ppa:agornostal/ulauncher")
    call("sudo apt update && sudo apt install -y i3 feh arandr ulauncher")
    call("pip3 install i3ipc")


def main() -> None:
    if platform.system() == "Linux":
        install_apt_packages()
    elif platform.system() == "Darwin":
        install_brew_packages()

    install_fonts()
    install_oh_my_zsh()
    install_vim_config()
    install_tmux_config()
    install_fzf()
    install_local_config()


if __name__ == "__main__":
    main()
