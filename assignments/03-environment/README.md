# Assignment 03: Your Shell Environment

## Part 1) Python Environments

In this part, we're going to dive deeper into how Python environments work by
intentionally breaking one and then attempting to fix it.

Intentionally breaking anything on your computer is not a good idea in general
-- that's why we're going to break the Docker container instead. One nice (and
initially confusing and/or surprising) thing about Docker containers is that
any changes you make to them do not *persist* after you shut down the container
(with the exception of the home directory, which we've configured to persist).
This means that you can delete files, install software, and totally break your
Python environment within the Docker container and get back to a clean, working
state by simply exiting the container and starting a new one with `bash
start-linux.sh`.

In this part, you will record your answers in a text file, one answer per line,
in a file named `part01.txt` that you'll submit to the Gradescope autograder.

### 1) Installing `httpie` with `apt`

In this class, we've been using a Docker container to provide everything with
the same Linux environment. There are different "flavors" (called
*distributions*) of Linux, and the one we're using is named Debian. Debian
versions are not numbered (there is no Debian 6.0). Instead, Debian versions
are named after characters from the movie Toy Story. Our Debian version is
"Bookworm".

Most Linux distributions allow you to install software quickly and easily using
a command line *package manager*. Different distributions use different package
managers, and Debian uses one called `apt`.

Suppose you are working on a project that requires a tool called `httpie`, but
you don't have it installed. Luckily, some gracious volunteer has (for free!)
"packaged" this piece of software for Debian, so that you can easily install it
with `apt`. First, we need to update `apt`'s list of available packages. Go ahead
and run:

```bash
apt update
```

You should see an error ("permission denied"). This is because Linux is
designed to let many users share the same computer, and it doesn't let just any
user install software -- that would be an easy way to break the system.

Instead, you need to have *superuser* permissions (sometimes called "root"
permissions) to install software. If you're using a Linux server that you
didn't set up, you probably don't have these permissions, but we've set up the
Docker container so that you do. To run a command with superuser permissions,
you simply prefix it with `sudo`. Go ahead and run:

```bash
sudo apt update
```

This will download the most recent "package lists" from the Debian servers.

Next, we search for the exact name of the package we want to install (if we
already know this, we can skip this step). To do this, we can use `apt search`
(it doesn't require `sudo`, and it's generally a good practice to *only* use
`sudo` when you *need* it):

```bash
apt search
```

You should see something like `httpie/oldstable 3.2.1-1 all`, which is telling
you that the package is named `httpie` from the "oldstable" Debian release, and
that the version is 3.2.1-1.

To install the package, go ahead and run:

```bash
sudo apt install httpie
```

You will be shown a list of *additional* packages that will be installed along
with httpie. These are called *dependencies* -- they are other pieces of
software that httpie depends upon. Notice that many of the dependencies are in
fact Python packages, including one called `python3-urllib3`. Each of these
packages is a specific version of a Python package that the Debian maintainers
have tested and verified works with `httpie`.

You'll also be asked if you want to continue. Type `y` and hit enter to proceed
with the installation. Try running `httpie` in the shell: you should see a
usage message -- if you do, the program is installed and working.

Before you move on, answer the following questions on lines 1, 2, and 3 of `part01.txt`:

**Question 1**: what is the full path to the `httpie` executable?
**Question 2**: what is the absolute path to the directory where the `python3-urllib3` package is installed?
**Question 3**: what version of `urllib3` is packaged with Debian Bookworm?

### 2) Upgrading `urllib3`

It's one week later, and now you're working on a Python project that requires
`urllib3`. In fact, you've already installed `urllib3` "system-wide" as a
side-effect of installing `httpie` with `apt`. However, the version that Debian
Bookworm packages is quite old, and you want to use a newer version. To do so,
you can use the `pip` package manager to install a newer version of `urllib3`
(version 2.6.3).

Go ahead and run:

```bash
sudo pip install urllib3==2.6.3
```

Make sure to include the `sudo`!

You should see an error about the environment being "externally managed" by a
package manager. This is `pip`'s way of saving you from yourself, because what
we're trying to do is actually a bad idea for reasons that will become
apparent.

Let's do it anyway. The error message actually give us a hint on how: use the
`--break-system-packages`. So go ahead and run:

```bash
sudo pip install --break-system-packages urllib3==2.6.3
```

You'll probably see some warnings along the lines of "can't uninstall urllib3",
but that's OK -- the package should still have been installed.

Before moving to the next part, answer the following questions in `part01.txt`:

**Question 4**: what is the full path to the `urllib3` package that Python finds when you `import urllib3`?
**Question 5**: (yes or no) is the old version of `urllib3` that came with Debian still present on the system?

### 3) Everything is broken

After updating `urllib3` with `pip`, you might not notice that anything is
wrong -- that is, until you try to run `httpie` again (go ahead). When you do,
you'll see an ugly error:

```
...
ImportError: cannot import name 'DEFAULT_CIPHERS' from 'urllib3.util.ssl_' (/usr/local/lib/python3.11/dist-packages/urllib3/util/ssl_.py)
```

The path printed here is a smoking gun: it tells us which version of `urllib3` is being used by `httpie`.

**Question 6**: which version of `urllib3` is `httpie` using, the old one installed via `apt` or the new one installed via `pip`? Respond with `apt` for the former, and `pip` for the latter.

### 4) Fixing the environment

The problem, of course, is that newer versions of `urllib3` made
backwards-incompatible changes. `httpie`, on the other hand, was built using
features from the old version of `urllib3` which were apparently removed in the
newer version. When we run `httpie`, it tries to use these features and fails
when it can't find them.

In this case, the fix is easy: uninstall the new version that we installed with
`pip`, and instead use a virtual environment. But this is only simple because
it was one package! If you make a habit of `sudo pip install`ing packages,
you'll end up with a mess of a Python installation that will be difficult to
fix.

To uninstall, run:

```bash
sudo pip uninstall urllib3 --break-system-packages
```

This will print the paths to the files and directories that will be removed.
Verify that these are indeed the paths to the *new* version of `urllib3`, and
approve.

Now try running `httpie` again -- it should work!

The correct way to have installed `urllib3` version 2.6.3 would have been to
create a virtual environment for our project and install it there. That will
allow us to have both versions of `urllib3` installed at the same time without
conflicts.

There is nothing to turn in for this step.

## Part 2) Setting up your UNIX environment

So far, you've been doing your work inside the Docker container, which gives
everyone a consistent Linux environment. But to use your computer for data
science and software development beyond this class, you'll want a proper UNIX
environment set up directly on your own machine. You'll also want a coding
agent (AI) available to help you with your work.

In this part, you'll follow two guides to set up your environment and pick an
AI, and then answer a short survey about the choices you made. There are no
right or wrong answers.

### 1) Set up your UNIX environment

Follow the guide that matches your operating system:

- **macOS**: <https://github.com/dsc-courses/dsc190-tools-2026-sp/tree/main/resources/01-unix_on_mac>
- **Windows**: <https://github.com/dsc-courses/dsc190-tools-2026-sp/tree/main/resources/01-unix_on_windows>

At a minimum, complete Steps 1 and 2 (installing a package manager and `git`).
Step 3 (the "make it nice" section) is optional but recommended.

### 2) Pick an AI

Next, follow this guide to pick and set up a coding agent:

- **Picking an AI**: <https://github.com/dsc-courses/dsc190-tools-2026-sp/tree/main/resources/02-picking_an_ai>

### 3) Survey

Record your answers in a text file named `part02.txt`, one answer per line, and
submit it to the Gradescope autograder. There are no right or wrong answers --
this is just a survey.

**Question 1**: What operating system are you using? (`macOS`, `Windows`, or `Linux`)

**Question 2**: What terminal app are you using? (e.g., `Terminal`, `Ghostty`, `iTerm2`, `Windows Terminal`, etc.)

**Question 3**: What shell are you using within your UNIX environment? (e.g., `bash`, `zsh`, `fish`)

**Question 4**: What is the full path to your `git` executable? (the top line of `type -a git`, or the output of `which git`)

**Question 5**: Which coding agent will you use for this class? (e.g., `OpenCode free`, `OpenCode Go`, `OpenCode Zen`, `Codex`, `Claude Code`, etc.)
