---
theme:
  path: ../../.presenterm/theme.yaml
  override:
    footer:
      style: template
      right: "{current_slide} / {total_slides}"
options:
  list_item_newlines: 2
---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Lecture 04 — Shell Features</span>**

Shell Features
==============

To follow along:

1. Run `bash start-linux.sh`.
2. `cd` into the course repository directory.
3. Run `git pull`.
4. Go to the first demo for Lecture 04:

```bash
demo 4 1
```

Shell Features
==============

- The shell is an interface to the operating system.
- It's main job: help you run programs and work with files.
- Today, several convenience features:
    - Globbing and brace expansion
    - Variables
    - Command substitution
    - Pipes and redirection

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Globbing, Expansion, and Quoting</span>**

<span class="term">**Globbing**</span>
===

- Globbing: a way to specify multiple files using patterns.
- *: matches any sequence of characters.
- ?: matches any single character.

```bash
# copy all CSV files to the backup directory
cp *.csv backup/

# copy all files of the form data_01.txt, data_02.txt,
# etc. to the backup directory
cp data_??.txt backup/

```

<span class="exercise">Exercise: demo 4 1</span>
===

This directory has some CSV files and some Python files.

1. Copy all of the CSVs to a `data/` directory.
2. Copy all of the Python files to a `scripts/` directory.
3. There are no text files, but try the following and see what happens:

```bash
cp *.txt data/
```

How does this work?
===================

- When you type a command, the shell:
    1. Parses the command into a program and its arguments.
    2. Finds that program on the system.
    3. Executes the program, passing it the arguments.
- Globbing happens during the parsing step.

Let's try it
============

- In the demo directory, run:
```bash
source count_args.sh
```
- This "installs" a "count_args" helper command that counts the number of args it receives and prints each on a new line.
- Try: count_args foo bar baz

<span class="exercise">Exercise: demo 4 1</span>
===

- Try each of:

```bash
count_args *.csv
count_args *
count_args *.txt
```

What's happening?
=================

- The shell is replacing the glob pattern with the list of files that match it **before** sending args to the program.
- This is called <span class="term">**expansion**</span>.
- Notes:
    - Not recursive. Only matches files in the current directory.
    - If no files match the pattern, the pattern is left unchanged.

Quoting
=======

- Quotes prevent expansion. Try:

```bash
count_args "*.csv"
```
- The program is passed the literal string "*.csv" instead of the list of CSV files.


<span class="exercise">Exercise: demo 4 1</span>
===

Compare these. Why does the first one succeed and the second one fail?
```bash
find . -name "*.csv"
```
```bash
find . -name *.csv
```

Answer
======

```bash
find . -name *.csv
```
Here, the shell expands "*.csv" before running "find". This is equivalent
to running:

```bash
find . -name revenue.csv sales_q1.csv sales_q2.csv ...
```

Answer
======

```bash
find . -name "*.csv"
```

Here, the shell is prevented from expanding "*.csv" because of the quotes.

Brace Expansion
===============

- Braces allow you to specify multiple options for a part of a command.
```bash
# make three directories
mkdir data_{1,2,3}

# this "expands" to
mkdir data_1 data_2 data_3
```

<span class="exercise">Exercise: demo 4 1</span>
===

Try:
```bash
count_args data_{1,2,3}
count_args data_{a,b}{1,2,3}
```

Quoting
=======

- Just like with globbing, quotes prevent brace expansion.

```bash
# three args
count_args data_{1,2,3}

# just one argument, the literal string "data_{1,2,3}"
count_args "data_{1,2,3}"
```

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Variables</span>**

Variables
=========

- The shell supports variables.
- To set a variable, use `=` with no spaces:
```bash
name=Justin
number=42
greeting="Hello, world!" # quotes are important here
```

Referencing Variables
=====================

- To use the value of a variable, prefix it with `$`:
```bash
# echo is a program that prints its arguments
echo $number
echo $greeting
echo my name is $name
```

Variables and Quoting
=====================

- Variable references are also expanded by the shell.
- But quoting is a little more nuanced. Try:
```bash
x='This is a test'
count_args $x
count_args "$x"
count_args '$x'
```

What we found...
================

- **Unquoted**: substitute and split on whitespace.
- **Double quotes**: substitute, but don't split.
- **Single quotes**: don't substitute, don't split.

- Typically, you want double quotes.

Variables are just strings
==========================

- The shell doesn't have types. Variables are always strings.

```bash
x=42

# prints "42 + 1", not "43"
echo $x + 1
```

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Command Substitution</span>**

Command Substitution
====================

- The shell also allows you to use the output of one command as an argument to another.

```bash
# prints the current date in YYYY-MM-DD format
date +%Y-%m-%d

# make a directory with the current date in its name
mkdir data_$(date +%Y-%m-%d)
```

Command Substitution and Variables
==================================

- Command substitution can be used to set variables too:

```bash
today=$(date +%Y-%m-%d)
echo "Today's date is $today"
```

Command Substitution and Quoting
================================

- Same rules as with variables.
- Usually, you want double quotes to prevent word splitting.

```bash
mkdir "data_$(date)"
```

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">I/O Streams, Pipes and Redirection</span>**

It's all text...
================

- Command line programs take *text* as input and produce *text* as output.


The `wc` Command
================

- `wc` (word count) is a command that counts lines, words, and characters.

```bash
# count lines, words, and characters in count_args.sh
wc count_args.sh
```

The `wc` Command, Without Arguments
===================================

- If you run `wc` without any arguments, it looks like it's not doing anything.
- But actually, it's waiting for you to type some text.
- Type a line or two.
- To signal that you're done, enter a new line and press Ctrl-D.

I/O Streams
===========

- When you run a program, the shell connects three text "streams" to it:
    - **Standard input** (stdin). Default: keyboard (or unused).
    - **Standard output** (stdout). Default: terminal output.
    - **Standard error** (stderr) Default: terminal output.
- It also provides arguments.

Example
=======

```bash
wc count_args.sh
```

![image:w:100%](fig/wc-io.png)

Example
=======

```bash
wc
```

![image:w:100%](fig/wc-noargs-io.png)

Pipe
====

- We can attach the **output** of one program to the **input** of another using a pipe (`|`):

```bash
# pipe the output of "ls" to "wc"
# counts number of files in directory
ls | wc -l
```

Example
=======

```bash
ls | wc -l
```


Grep in a Pipe
==============

- grep is especially useful in a pipe.

```bash
# print all running processes
ps aux

# is python running?
ps aux | grep python
```

Example
=======

```bash
# sort the results of find and look at them in less
find . -name "*.csv" | sort | less
```

Output Redirection
==================

- The `>` operator redirects the STDOUT to a file instead of the terminal.
- If the file already exists, it will be overwritten.

```bash
# save the list of CSV files to a text file
find . -name '*.csv' > csv_files.txt
```

Example
=======

```bash
# save the list of CSV files to a text file
find . -name '*.csv' > csv_files.txt
```


Output Redirection, Append Mode
===============================

- The `>>` operator also redirects STDOUT to a file, but it appends to the file instead of overwriting it.

```bash
# append the list of Python files to the same text file
find . -name '*.py' >> csv_files.txt
```

Redirecting Standard Error
==========================

- The `2>` operator redirects STDERR to a file.


Redirecting Both
================

- To redirect both STDOUT and STDERR to the same file, you can use `&>`:


The UNIX Philosophy
===================

- "Do one thing and do it well."
- "Write programs that work together."
- "Write programs to handle text streams, because that is a universal interface."

The Result
==========

- If each program can "speak" to the others, it's easy to combine them in powerful ways.
