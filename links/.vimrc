" General
set number                              " Show line numbers
set linebreak                           " Break lines at word (requires Wrap lines)
set showbreak=+++                       " Wrap-broken line prefix
set textwidth=100                       " Line wrap (number of cols)
set showmatch                           " Highlight matching brace
set spell                               " Enable spell-checking

set hlsearch                            " Highlight all search results
set smartcase                           " Enable smart-case search
set ignorecase                          " Always case-insensitive
set incsearch                           " Searches for strings incrementally

set autoindent                          " Auto-indent new lines
set expandtab                           " Use spaces instead of tabs
set shiftwidth=4                        " Number of auto-indent spaces
set smartindent                         " Enable smart-indent
set smarttab                            " Enable smart-tabs
set softtabstop=4                       " Number of spaces per Tab

set list                                " Show invisible chars but whitespace
set listchars=eol:$,tab:>-,trail:~,extends:>,precedes:<

" Advanced
set ruler                               " Show row and column ruler information

set undolevels=1000                     " Number of undo levels
set backspace=indent,eol,start          " Backspace behaviour

"Plugin runtime
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

"Plugins
Plugin 'VundleVim/Vundle.vim'
Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}

call vundle#end()

"Powerline
set laststatus=2
