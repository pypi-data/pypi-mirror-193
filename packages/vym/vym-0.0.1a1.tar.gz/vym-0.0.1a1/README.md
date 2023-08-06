# f2dv.vimrc

## broot

- `enter` | `right` | `]`: browse down / edit file
- `left` | `h` | `[`: browse up
- `w`: set working dir to selection
- `:cd <path>` | `:z <path>`: set working dir to `<path>`
- `:$ <command>`: run shell command
- `:v <path>`: open vym at `<path>`
- `e`: edit file/dir distraction-free
- `n`: new empty file
- `y`: open vym at pwd
- `v`: open vym at selection
- `t`: new terminal at selection
- `g`: only show files with a git status
- `=`: show diff/status of selected file/dir
- `-`: stage/unstage selected file
- `` ` ``: show terminal
- `/`: start search
- `s`: sort by type
- `r`: sort by date
- `F5`: refresh
- `q`: quit

### staging

- `i`: add/remove selection to/from staging area
- `u`: clear staging area
- `o`: toggle staging area visibility
- `p`: focus on right panel
- `q` | `<ESC>`: close focused panel
- `:$ echo $1`: run command for each staged path

> search options: https://dystroy.org/broot/input/#the-filtering-pattern

## amix.vimrc

- `,`: leader key
- `:W`: force save as sudo
- `/` | `<space>`: start search
- `*` | `#`: (visual-mode) search for selected text
- `,<enter>`: clear search highlight
- `gt` / `gT`: jump to next/prev tab
- `gt#`: jump to tab `#`
- `,tn`: new tab
- `,tc`: close tab
- `,to`: close other tabs
- `,tm`: move tab
- `,tl`: jump to last-accessed tab
- `,te`: open a new tab with current path
- `,cd`: chdir to parent of current file
- `,pp`: toggle paste-mode
- `,ss`: toggle spell check
- `,sn`: jump to next spelling issue
- `,sp`: jump to prev spelling issue
- `,sa`: add word to dictionary
- `,s?`: show spelling suggestions
- `,dss`: toggle repeated word highlight (Ditto)

## FZF

- `C+P`: map search (fzf)
- `C+Y`: snippet search (fzf + ultisnips)
- `,bb`: buffer search (fzf)
- `,hh`: help search (fzf)
- `,ff`: file search (fzf)
- `,ft`: show file tree (nerdtree)
- `,fs`: content search (ripgrep)
- `,rg`: content search (ripgrep)

> Use `<Tab>` to add search results to vim's quickfix.

- `C+Y`: view snippets
- `,x`: edit snippets

To pass visual selection to snippet:
1. make selection
2. press `<Tab>`
3. expand desired snippet

### Within FZF

- `Alt+a`: select all
- `Alt+a`: deselect all

- `<enter>` | `C+t`: open selection(s) in new tab(s)
- `C+x`: open selection(s) split below
- `C+v`: open selection(s) split right
- `C+q`: add selection(s) to vim's quickfix

- `C+jk`: navigate results
- `C+<Up><Down>`: navigate preview

## vim-visual-multi (multi-cursor)

- `C+Down`: Add cursor below
- `C+Up`: Add cursor above
- `C+n`: Add cursor at next match
- `C+m`: Add cursor to all matches
- `C+\`: Add cursor to all regex search matches

Press `<Tab>` to cycle between cursor- and multi-visual mode.

## cs-surround

- `S"`: (visual-mode) surround selected text with `"`
- `cs'"`: change enclosing `"` to `'`
- `ds"`: delete enclosing `"`
- `ysiw"`: surround text object with `"` (`iw` is text object)
- `yss"`: surround line with `"`

## vim-markdown

- `gx`: open link under cursor in web browser
- `]]`: jump to next header
- `[[`: jump to prev header
- `]h`: jump to current header
- `]u`: jump to parent header
- `:Toc`: show table of contents
- `:InsertToc #`: insert ToC with depth `#`
- `:InsertNToc #`: insert ToC (numbered) with depth `#`
- `:TableFormat`: format markdown table

### Custom Mappings

- `,itc`: insert table of contents
- `,itc#`: insert table of contents with depth `#`
- `,ntc`: insert table of contents (numbered)
- `,ntc#`: insert table of contents (numbered) with depth `#`
- `,tbf`: table format

| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

- `,mdp`: open markdown preview

## goyo + limelight

- `,ee`: toggle goyo
- `,ll`: toggle limelight

## git-gutter / fugitive

- `,ggg`: git log
- `,ggs`: git status
- `,ggb`: git blame
- `,ggt`: toggle git-gutter
- `,ggh`: toggle diff highlights
- `,ggr`: refresh all signs
- `,ggz`: fold unchanged lines
- `,ggd`: show diffs in vimdiff
- `,gg]`: show next hunk
- `,gg[`: show prev hunk
- `,gga`: add current hunk to stage (`:w` changes in new buffer)
- `,ggx`: undo current hunk
- `,ggq`: file hunk's to quickfix
- `yid`, `yad`: yank changed hunk (i.e., yank diff)


## Other

- `,nn`: toggle line numbers
- `,mm`: toggle minimap (minimap.vim)
- `C+/`: toggle comments (nerdcommenter)
- `U`: toggle undo-tree (UndoTree)

## floaterm

- `,tt`: toggle floating terminal (floaterm)
- `,tr`: toggle floating broot (floaterm)
- `,tv`: show terminal on right
- `,tb`: show terminal on bottom

## ale

> TODO

- `,pds`: create python docstring
- `,pdt`: create python docstring, with types


## quickfix

> TODO
