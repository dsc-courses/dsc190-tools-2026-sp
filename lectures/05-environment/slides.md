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


Environments
============

To follow along:

1. Run `bash start-linux.sh`.
2. `cd` into the course repository directory.
3. Run `git pull`.
4. Go to the first demo for Lecture 05:

```bash
demo 5 1
```

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Environment Variables</span>**

Variables
=========

Last time, we saw how to set and use shell variables:

```bash
name="Justin"
x=42

# prints: Hello Justin, your number is 42
echo "Hello $name, your number is $x."
```

Useful for *shell scripting*.

Variable Scope
==============

- Shell variables are only available in the **current** shell.
- They do **not** survive when you exit the shell.
- They are **not** "inherited".

```bash
name="Justin"
echo $name
# starts a new shell, *within* the old shell
bash
echo $name
# type <c-d> to exit the new shell
echo $name
```

Environment Variables
=====================

- <span class="term">**Environment variables**</span> are special: they **are** inherited.
- To define an environment variable, use the `export` command:

```bash
export name="Justin"
echo $name
bash
echo $name
```

Convention
==========

- By convention, environment variable names should be in all caps.

```bash
export NAME="Justin"
echo $NAME
bash
echo $NAME
```

Alternative: Inline Definition
==============================

- You can also define an environment variable inline when running a command:
- It will be local to that command's process.

```bash
NAME=Justin bash
echo $NAME
# press <c-d> to exit the new shell
# not defined
echo $NAME
```

<span class="exercise">**Exercise**</span>
===

Exported variables are inherited by child processes.

Are they also inherited by grandchild, great-grandchild, etc. processes? I.e.,
are they inherited recursively?

<!-- pause -->
**Yes!**

Environment Variables and Python
================================

- Any program run in a shell inherits its environment variables.
- In Python, you can access them via the `os` module:

```python
# in your python script...
import os
print(os.environ['NAME'])
```

Permanent Environment Variables
===============================

- Variables do not survive when you exit the shell.
- To make them permanent, you need to redefine them *every time* your shell starts.
- In `bash`, do this by editing the shell's startup file: `~/.bash_profile` (or `~/.profile` if that doesn't exist.)

```bash
# ~/.profile
...
export NAME="Justin"
```

<span class="exercise">**Exercise**</span>
===

Add an environment variable to your `~/.profile` that contains your name.

Then, exit your linux container and start it. Is `$NAME` still defined?

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">The PATH</span>**

Running Programs
================

- The shell's main job is to run programs.
- On Unix/Linux, a program is just a file marked as "executable".
- When you type a command, how does the shell know where to find it?

```bash
ls
```

The PATH
========

- The <span class="term">**$PATH**</span> environment variable contains a list of directories to search for programs.
```bash
echo $PATH

# prints:
# /usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games
```

Note, $PATH is a single string, with directories separated by colons (`:`).

The PATH
========

- When you run a command, the shell looks through these directories to find an executable file with the same name.
- The *first* one it finds is the one it runs.


type
====

- The `type` command shows the program that is found by searching the $PATH.
- `type -a` shows all matches in the $PATH.

```bash
type grep
type python3
type cd
type ls
type -a ls
```

Permanently Modifying the PATH
==============================

- You'll often want to add directories to your $PATH, e.g., to run programs you installed yourself.
- To do so, edit `~/.profile`.
- Example: add `~/bin` to the $PATH:

```bash
# ~/.profile
...
export PATH="~/bin:$PATH"
```

Order Matters!
==============

- The first entries in the $PATH are searched first.
- To give a directory **high priority**, put it at the beginning:
```bash
export PATH="~/bin:$PATH"
```
- To give a directory **low priority**, put it at the end:
```bash
export PATH="$PATH:~/bin"
```

---


<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Python Environments</span>**

Python Environments
===================

- Suppose we write a Python program that uses a package (like `numpy` or `pandas`).
- Python packages are also just files (and directories).
- How does Python find the package?

```python
import numpy
import pandas
```

Python's Search Path
====================

- Python looks for packages in the directories listed in the `sys.path` variable.

```python
# in your python script...
import sys
print(sys.path)
```

<span class="exercise">**Exercise: demo 5 1**</span>
===

`print_path.py` prints the directories in `sys.path`. What are they?

`sys.path`
==========

- The first entry: directory of the script being run.
    - This is what enables importing "helper" files.
- `/usr/lib/python3.11`: python standard library.
- `/usr/lib/python3/dist-packages`: "system" packages

Checking a Package's Location
=============================

- To check where a package is being imported from, look at its `__path__` attribute:

```python
import numpy
print(numpy.__path__)
```

Modifying the Search Path
=========================

To modify the package search path, set the `sys.path` variable in your script:

```python
# in my_script.py
import sys
sys.path.append('/path/to/my/packages')
```

Alternative: PYTHONPATH
=======================

You can also set the `PYTHONPATH` environment variable:

```bash
# in the shell
export PYTHONPATH="/path/to/my/packages:$PYTHONPATH"
python3 my_script.py
```

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Python Virtual Environments</span>**

Python Dependencies
===================

- Suppose we need a package (numpy) that is not installed.
- How should we install it?

One answer: pip
===============

- `pip` is the standard Python package manager.
- To install a package, run:
```bash
# in the shell
pip install numpy
```
<!-- pause -->
- This is generally a <span class="bad">**bad idea**</span>.

Why?
====

- By default, pip installs packages *globally*.
    - i.e., into the system's Python directory (e.g., `/usr/lib/python3/dist-packages`).
- Result: all of your Python projects will share this same version of numpy.

The Version Problem
===================

- Over time, packages make backwards-incompatible changes.
- Example: older versions of `numpy` had a `np.in1d` function, but it was removed in numpy v2.0.
- Result: older projects need a different version of numpy than newer projects.
    - They can't share the same version.

Solution
========

- Give each project its own Python <span class="term">**virtual environment**</span>.
- This allows each to have its own packages.

Creating a Virtual Environment
==============================

- To create a virtual environment, run (in your project's directory):

```bash
python3 -m venv <env-name>
```

Activating a Virtual Environment
================================

- To use the virtual environment, you need to "activate" it:

```bash
source <env-name>/bin/activate
```

- To deactivate the virtual environment, run:

```bash
deactivate
```

<span class="exercise">**Exercise: demo 5 2**</span>
===

In the demo is a directory named "old-project".

In this directory, create a virtual environment named "env", then activate it.

How did $PATH and Python's `sys.path` change?

How it works...
===============

- Virtual environments work by modifying the $PATH and Python's `sys.path` variables when activated.
- When you deactivate, it restores them to their original values.

Installing into a Virtual Environment
=====================================

- To install a package into a virtual environment, first activate the environment, then run pip as normal:

```bash
source env/bin/activate
pip install numpy
```

Versions
========

- To install a specific version:
```bash
pip install numpy==1.23
```


<span class="exercise">**Exercise: demo 5 2**</span>
===

Install numpy version 1.23 into old-project's virtual environment.

Run python, import numpy, and check the numpy's `__version__` and `__path__` attributes.

<span class="exercise">**Exercise: demo 5 2**</span>
===

Create a separate virtual environment for the "new-project" directory, and
install the latest version of numpy into it.

My Take
=======

- Always, *always* use virtual environments.
- However, we typically will not use `python -m venv` directly.
- We will see a better way (uv) in a coming lecture.

Why?
====

Creating virtualenvs this way has some deficiencies:

- It is hard to share the environment with others.
- It is slow.

uv fixes these problems, and is the recommended way to manage Python environments in 2026.

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Custom Tools</span>**

Custom Tools
============

- Over time, you will custom develop scripts and command line programs that will make your job easier.
- You can "install" these so that they are just as easy to run as ls, grep, find, etc:
    1. Add a "shebang" line.
    2. Mark as executable.
    3. Move (or link it from) a directory in your $PATH.


<span class="exercise">**Exercise: demo 5 3**</span>
===

In the demo directory, there is a script called `backup.py`.

We can run it like any other Python script:

```bash
# copies foo.csv to foo.bak.csv
python3 backup.py foo.csv
```

Goal: be able to run it like...

```bash
backup foo.csv
```

Step 1: Add a "shebang" line
============================

- First, we add a "shebang" line to the top of the script to tell the shell how to run it.
- Should be the path to the python interpreter
    - See: type python3

```python
#! /usr/bin/python3
import argparse
```

Step 2: Mark as Executable
==========================

- Next, tell the shell that this file is a program by marking it as executable:

```bash
chmod +x backup.py
```

- To unmark as executable:

```bash
chmod -x backup.py
```

Running the Script
==================

With these two, we can now run the script without explicitly calling `python3`:

```bash
./backup.py foo.csv
```

But if we're in another directory, we would need to specify the full path:

```bash
# in the root of the course repository
./lectures/05-environment/demos/03/backup.py foo.csv
```

Step 3: Move to a Directory in $PATH
=======================================

- To run it from anywhere, we need to move it to a directory in our $PATH.

```bash
cp backup.py ~/bin
```
- Now we can run it from anywhere:
```bash
backup.py foo.csv
```

Tip: Remove the Extension
=========================

- The .py extension is an "implementation detail".
    - Users don't need to know it's implemented in Python.
- Moreover, extensions are not special on Unix/Linux.
- It's better to rename it to just `backup`:

```bash
mv ~/bin/backup.py ~/bin/backup

# now we can write...
backup foo.csv
```

Tip: Use Links
==============

- You don't need to copy/move the whole file to a directory in your $PATH (and sometimes you can't).
- Instead, create a <span class="term">**symbolic link**</span>.
    - I.e., a "shortcut" that points to the original file.

```bash
cd ~/bin

# creates a link from "backup" to the original file
# at "/path/to/backup.py"
ln -s /path/to/backup.py backup

# now we can run it from anywhere:
backup foo.csv
```

Tip: Combine Programs
=====================

- You can use your custom programs with other standard tools, like find:

```bash
# find all .csv files and back them up
find . -name '*.csv' -exec backup {} \;
```
