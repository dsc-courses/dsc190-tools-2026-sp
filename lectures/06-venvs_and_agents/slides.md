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


Virtual Environments and Agents
================================

To follow along:

1. Run `bash start-linux.sh`.
2. `cd` into the course repository directory.
3. Run `git pull`.
4. Go to the first demo for Lecture 06:

```bash
demo 6 1
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

<span class="exercise">**Exercise: demo 6 1**</span>
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


<span class="exercise">**Exercise: demo 6 1**</span>
===

Install numpy version 1.23 into old-project's virtual environment.

Run python, import numpy, and check the numpy's `__version__` and `__path__` attributes.

<span class="exercise">**Exercise: demo 6 1**</span>
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
