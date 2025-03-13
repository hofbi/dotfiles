[[ -e ~/.profile ]] && emulate sh -c 'source ~/.profile'

if [[ $(uname) == "Darwin" ]]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi
