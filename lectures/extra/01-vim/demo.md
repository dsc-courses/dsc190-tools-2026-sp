# Vim Demo

## Modal Editing
- Normal, Insert, Visual, Command-line
- `i`, `Esc`, `v`, `:`

## Movement
- `h j k l`
- Word motions: `w`, `b`, `e`
- Line: `0`, `^`, `$`
- File: `gg`, `G`, `Ctrl-d`, `Ctrl-u`
- Search: `/pattern`, `n`, `N`

## The Verb-Modifier-Noun Grammar
- `d2w` — delete 2 words
- `ci"` — change inside quotes
- `da)` — delete around parens
- `.` — repeat last edit

## Editing Essentials
- `o` / `O` — open line below/above
- `x`, `dd`, `yy`, `p`
- `u`, `Ctrl-r` — undo/redo

## Visual Mode
- Character `v`, line `V`, block `Ctrl-v`
- Block editing: prepend/append to multiple lines

## Command-Line Mode
- `:w`, `:q`, `:wq`, `:q!`
- `:s/old/new/g` — substitution
- `:%s/old/new/g` — whole-file substitution
- `:!command` — run shell command

## Registers and Macros
- Named registers: `"ayy`, `"ap`
- Record macro: `qa ... q`, replay: `@a`, `10@a`
