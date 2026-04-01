---
theme:
  path: ../../.presenterm/theme.yaml
options:
  list_item_newlines: 2
---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Lecture 02 — The Shell</span>**

The Shell
=========

- Welcome back.
- Open a terminal and run: `bash start-linux.sh`.

Updating the Repo
=================

- We need to pull the latest version of the course repo.
- Run:
    - `cd dsc190-tools-2026-sp`
    - `git pull`

Demo 01
=======

We left off with Demo 01...

Tips
====

Use the keyboard shortcuts!

<!-- list_item_newlines: 1 -->
- Up/down arrows: cycle through command history
- Ctrl-a / Ctrl-e: move to beginning/end of line
- Ctrl-u: delete from cursor to beginning of line
- Ctrl-w: delete previous word
- Alt-left/right: move cursor one word left/right

Example: `mdkir foo bar baz`

Again, With AI
==============

- Your docker container has *opencode* pre-installed.
- opencode is a coding agent that works in the terminal.
- Let's try it out.

Getting Help
============

- 1976: `man <command>` or `<command> --help`
- 2016: `tldr <command>`
- 2026: AI

Try:
```bash
opencode run "How do I use the ls command?"
# or (only in this class's docker container):
ask "How do I use the ls command?"
```
---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Finding Things</span>**

The `find` Command
==================

- We can use the *find* command to search for files or directories.

```bash
find <root-of-search> -name '<pattern>'
```

Finding by Name
===============

- Use '*' as a wildcard to match any characters.
- The quotes are important!

```bash
# find all CSV files under the current directory
find . -name '*.csv'

# find all python files in the "scripts" directory
find scripts/ -name '*.py'

# find all files starting with "test"
find . -name 'test*'

# find all files starting with "test" (case insensitive)
find . -iname 'test*'
```

Finding by Type
===============

- Use `-type d` to search only for directories.
- Use `-type f` to search only for files.

```bash
# find all directories named "data", case-insensitive
find . -type d -iname 'data'

# find all files named "data", case-insensitive
find . -type f -iname 'data'
```

Finding by Other Criteria
=========================

<!-- list_item_newlines: 1 -->
Can find files by:

- Size
    - example: `-size +1M` for files larger than 1 megabyte
- Modification time
    - example: `-mtime -7` for files modified in the last 7 days
- Regex
    - example: `-regex '.*\.\(csv\|tsv\)'` for files ending in csv or tsv
- More!

Maximum Depth
=============

- By default, `find` searches all subdirectories recursively.
- Use `-maxdepth <N>` to limit how deep it searches.

```bash
# find all CSV files in the current directory, but not subdirectories
find . -maxdepth 1 -name '*.csv'

# find all CSV files in the current directory and its immediate subdirectories, but not deeper
find . -maxdepth 2 -name '*.csv'
```

Executing Commands on Found Files
=================================

<!-- list_item_newlines: 1 -->
- Use `-exec` to run a command on each found file.
- Kind of a clunky syntax, but very powerful.
    - The `{}` is replaced with the file path.
    - Do *not* use quotes!
    - The `\;` is required to terminate the command.

```bash
# copy all CSV files to a new directory
find . -name '*.csv' -exec cp {} /path/to/destination/ \;

# delete all CSV files
find . -name '*.csv' -exec rm {} \;
```

Demo
====

- Let's do a quick demo.
- It's in `lectures/02-shell/demos/02/`.
- You can use the "demo" command to get there quickly:

```bash
# usage: demo <lecture-number> <demo-number>
demo 2 2
```

Remember, use "tldr" or "ask" for help!


Finding by Content
==================

- *find* can only search by file name or metadata, not by file content.
- For that, we use *grep*.

```bash
# search this file for the pattern
grep '<pattern>' <file>

# search this file for the pattern, case-insensitive
grep -i '<pattern>' <file>

# search all files in this directory (recursively) for the pattern
grep -r '<pattern>' <directory>

```

Note
====

- If you don't provide a file, `grep` reads from "standard input"

```bash
grep 'foo'
```

- It will look like it's stuck.
- Press `<Ctrl-c>` to stop it.


Demo
====

Let's try out grep.

```bash
demo 2 2
```

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Editing Files</span>**

Editing in the Terminal
=======================

- Editing files in the terminal *can* be a pain.
- Usually, you'll use your editor (e.g., VSCode).
- But sometimes, it's quickest and easiest to just edit the file right in the terminal.

nano
====

- nano is a simple terminal text editor.
- Use it for quick edits to files.
```bash
nano <file>
```
- Bottom toolbar shows important keyboard shortcuts.
    - e.g., "^X" means "Ctrl-X"

VIM
===

- VIM is a much more powerful (and complex) terminal text editor that is pre-installed almost everywhere.
- But it has a (very?) steep learning curve.

```bash
vim <file>
```

- For this class, you only need to know one thing about VIM: how to quit it.
    - Press `Esc` to make sure you're in "normal mode", then type `:q` and press Enter to quit.

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Quiz 01</span>**

Quiz 01
=======

- This Friday.
- 10 questions, 10 minutes.
- Prepare using the `YSK.md` files.
- Afterwards, I'll talk about some topic for fun.

Quiz Me
=======

Try opening *opencode* in the DSC 190 course repo and asking "Quiz Me".
