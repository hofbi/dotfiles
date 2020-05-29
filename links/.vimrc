"Plugin runtime
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

"Plugins
Plugin 'VundleVim/Vundle.vim'
Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
Plugin 'michaeljsmith/vim-indent-object'
Plugin 'tpope/vim-surround.git'
Plugin 'wincent/command-t' " cd ~/.vim/bundle/command-t/ruby/command-t/ext/command-t && ruby extconf.rb && make and probably sudo apt install ruby2.5-dev
Plugin 'scrooloose/nerdtree'
Plugin 'tpope/vim-fugitive'
Plugin 'preservim/nerdcommenter'

call vundle#end()
filetype plugin indent on    " required

" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

" Leader
let mapleader = ","

" Powerline
set laststatus=2

" Command-t
map <Leader>t <Plug>(CommandT)

" NERDTree
map <C-n> :NERDTreeToggle<CR>
let NERDTreeShowHidden=1
" If more than one window and previous buffer was NERDTree, go back to it.
autocmd BufEnter * if bufname('#') =~# "^NERD_tree_" && winnr('$') > 1 | b# | endif

" FZF
set rtp+=~/.fzf
map <C-t> :FZF<CR>

" General
set number                              " Show line numbers
set linebreak                           " Break lines at word (requires Wrap lines)
set showbreak=+++                       " Wrap-broken line prefix
set textwidth=100                       " Line wrap (number of cols)
set showmatch                           " Highlight matching brace

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

set ruler                               " Show row and column ruler information

set undolevels=1000                     " Number of undo levels
set backspace=indent,eol,start          " Backspace behaviour
