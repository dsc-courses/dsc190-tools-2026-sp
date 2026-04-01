# The `rm` command

- What does `rm foo/` do if foo is a directory?
    - **Answer**: prints an error because `rm` by default only removes files, not directories

- What does `rm -r` do?
    - **Answer**: removes a directory and everything inside it recursively

- What does `rm -rf` do?
    - **Answer**: removes recursively and forcefully, without prompting for confirmation

# The `mkdir` command

- What does `mkdir` do?
    - **Answer**: creates a new directory

# The `mv` command

- What does `mv` do?
    - **Answer**: moves a file or directory to a new location

- What command is used to rename a single file?
    - **Answer**: `mv <old-name> <new-name>`

# The `cp` command

- What does `cp` do?
    - **Answer**: copies a file to a new location

- What does the `-r` flag do in the `cp` command?
    - **Answer**: copies directories and their contents recursively

- What does `cp -r foo/ ~` do?
    - **Answer**: copies the `foo/` directory and everything inside it to your home directory

# The `less` command

- What does `less` do?
    - **Answer**: opens a file for viewing one screen at a time

- How do you scroll down in `less`?
    - **Answer**: arrow keys, `j`, or `Ctrl-d` (half page)

- How do you jump to the end of a file in `less`?
    - **Answer**: press `G`

- How do you search for text in `less`?
    - **Answer**: press `/` then type your search term

- How do you quit `less`?
    - **Answer**: press `q`

# Other commands

- What does the `man` command do?
    - **Answer**: displays the manual page for a command

- What does the `pwd` command do?
    - **Answer**: prints the current working directory

# The `cd` command

- What does `cd` do if we don't give it any arguments?
    - **Answer**: changes to your home directory

- What does `cd -` do?
    - **Answer**: changes to the previous directory you were in

- What does `cd ..` do?
    - **Answer**: moves up one directory level

- What does `cd ~` do?
    - **Answer**: changes to your home directory

# Keyboard shortcuts

- What does pressing the up arrow key do at the command line?
    - **Answer**: cycles through previous commands in your history

- What does `<Alt-w>` do at the command line? (Option-w on Mac)
    - **Answer**: deletes the word before the cursor

- What does `<Alt-left arrow>` do at the command line? (Option-left arrow on Mac)
    - **Answer**: moves the cursor one word to the left

- What does `<Alt-right arrow>` do at the command line? (Option-right arrow on Mac)
    - **Answer**: moves the cursor one word to the right

- What does `<Ctrl-u>` do at the command line?
    - **Answer**: deletes everything from the cursor to the beginning of the line

- What does `<Ctrl-a>` do at the command line?
    - **Answer**: moves the cursor to the beginning of the line

- What does `<Ctrl-e>` do at the command line?
    - **Answer**: moves the cursor to the end of the line

- What does `<Ctrl-w>` do at the command line?
    - **Answer**: deletes the word before the cursor

# The `find` command

- How do you use `find` to find all CSV files under the current directory?
    - **Answer**: `find . -name '*.csv'`

- What does `find foo/ -name bar` do?
    - **Answer**: searches for files named "bar" (exactly) under the directory "foo"

- Your current directory contains a file named "test_backend.py". Will `find . -name 'test'` match it?
    - **Answer**: No, it only matches files named exactly "test"

- What is the difference between `-name` and `-iname` in `find`?
    - **Answer**: `-iname` is case-insensitive, so `-iname 'data*'` matches `Data_Dictionary` and `data.csv`

- How do you find only directories (not files) named "data"?
    - **Answer**: `find . -type d -name 'data'`

- What argument do you add to `find` to prevent it from searching subdirectories?
    - **Answer**: `-maxdepth 1`, e.g., `find . -maxdepth 1 -name '*.csv'`

- What does `find . -name '*.csv' -exec rm {} \;` do?
    - **Answer**: deletes all CSV files under the current directory and its subdirectories

- In the `-exec` syntax, what does `{}` represent?
    - **Answer**: a placeholder that gets replaced with the path of each found file

# The `grep` command

- What does `grep foo bar` do?
    - **Answer**: searches for the string "foo" in the file "bar" and prints matching lines

- What does `grep -r foo bar` do?
    - **Answer**: searches for the string "foo" in all files under the directory "bar" recursively

- What does `grep -ri foo bar` do?
    - **Answer**: searches for the string "foo" in all files under the directory "bar" recursively, ignoring case

- The file `file.txt` contains the line "One foo bar two". Will `grep 'foo' file.txt` return (match) that line?
    - **Answer**: Yes, it matches because "foo" is a substring of "One foo bar two"

# Vim

- How do you exit Vim?
    - **Answer**: Press `<Esc>` and then `:q`, followed by the enter key.
