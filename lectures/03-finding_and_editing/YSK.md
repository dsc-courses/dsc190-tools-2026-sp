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
