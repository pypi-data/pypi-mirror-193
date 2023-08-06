" quick write
nmap <leader>w :w<cr>
nmap <leader>W :wa<cr>
" quick quit
nmap <leader>q :q<cr>
nmap <leader>Q :qa<cr>

" Smart way to move windows
map <C-x> <C-W>J
map <C-v> <C-W>L

" "line" text-objects
" https://vi.stackexchange.com/a/6102
xnoremap il g_o^
onoremap il :normal vil<cr>
xnoremap al $o^
onoremap al :normal val<cr>

" paste and retain original value
" https://stackoverflow.com/a/7164121
xnoremap p pgvy

" squash newlines
" https://unix.stackexchange.com/a/12813
nmap <leader>nl :%!cat -s<cr>

nmap <leader>ls :ls<cr>

" show whitespace
:set listchars+=eol:¬,tab:>·,trail:◦,extends:>,precedes:<
" ,space:
:set list

" change default split direction
set splitright
set splitbelow

" launch terminal
nmap <leader>ts :botright terminal ++kill=term<cr>
nmap <leader>tv :vertical terminal ++kill=term<cr>

" open file at position in new split
nmap <leader>gf :wincmd F<CR>

nmap <leader>gv :vertical wincmd F<CR>
" quick splits
nmap <leader>vs :vs<CR>
nmap <leader>sp :split<CR>

" diff this, diff off
nmap <leader>dft :windo diffthis<CR>
nmap <leader>dfo :diffoff!<CR>

" toggle line number
set number
nnoremap ,nn :set nonumber!<cr>

" case-sensitive by default
set ignorecase
set smartcase

" marker at column 88
set colorcolumn=88

" faster updates
set updatetime=666

" share vim with system clipboard
" https://stackoverflow.com/a/30691754
set clipboard^=unnamed,unnamedplus

" duration to respect key combinations
set timeout timeoutlen=1000 ttimeoutlen=200

" force black background on all themes
function! s:force_black_bg()
    " force black bg
    hi Normal ctermbg=16 guibg=#000000
    hi LineNr ctermbg=16 guibg=#000000
endfunction

set background=dark
autocmd! ColorScheme * call s:force_black_bg()
