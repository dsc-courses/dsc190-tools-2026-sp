---
theme:
  path: ../../../.presenterm/theme.yaml
options:
  list_item_newlines: 2
---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../../COMMON/logo.png)

**<span class="term">Extra: Managing Your Config</span>**

Dotfiles
========

- Over time, you'll accumulate a lot of configuration settings for the tools you use.
- These settings are typically stored in <span class="term">**dotfiles**</span> under your home directory.
    - E.g., fish's config is in `~/.config/fish/config.fish`.


Versioning Your Dotfiles
========================

- It's a good idea to keep your dotfiles in version control.
    - Allows you to revert if a change breaks something.
    - With GitHub, makes it easy to sync your dotfiles across multiple machines.

<span class="bad">**Problem**</span>
====================================

- Your dotfiles are scattered across your home directory.
- For example:
    - Fish is in `~/.config/fish/config.fish`
    - Git is in `~/.gitconfig`
- You don't want to store your entire home directory in version control.
    - Not even all of `~/.config`.

<span class="good">**Solution: stow**</span>
============================================

- Instead, store all of your config files in a separate directory (e.g., `~/.dotfiles`).
- Then *symlink* them into your home directory with **stow**.

Tangents: Symlinks
==================

- Symbolic links ("symlinks") are *pointers* to files or directories.
- They allow the same file to be accessed from multiple places.

```bash
> cat foo.txt
Hello world!
> ln -s foo.txt bar.txt
> cat bar.txt
Hello world!
```

stow
====

- Stow is a tool that creates and manages whole trees of symlinks for you.
- Useful for keeping all of your dotfiles in one location.

Example
=======

With stow, you put your dotfiles in a single directory.


```bash
 ~/.dotfiles
├──  fish
│   └──  .config
│       └──  fish
│           └──  config.fish
├──  git
│   ├──  .gitconfig
│   └──  .gitignore_global
└──  README.md
```

Example
=======

```bash
 ~/.dotfiles
├──  fish
│   └──  .config
│       └──  fish
│           └──  config.fish
```

```bash
stow fish --target ~
```

Creates a symlink from `~/.config/fish/config.fish` to `~/.dotfiles/fish/.config/fish/config.fish`.


stow
====

- Stow is smart: it won't overwrite existing files, and it "merges" directories.


Starter Dotfiles
================

I've created a starter dotfile repo for you, here:

> https://github.com/dsc-courses/dsc190-dotfiles

Tangent: task runners
=====================

- In that repo, there is a *justfile* with frequent tasks and the commands used to carry them out.

```justfile
packages := "fish git starship"
target := "~"

default: install

install:
    stow {{packages}} --target {{target}}

uninstall:
    stow -D {{packages}} --target {{target}}
```

Tangent: task runners
=====================

- To run a task, use `just <task-name>`. For example:

```bash
just install
```

What these dotfiles contain...
==============================

- Basic fish configuration with some aliases and functions.
    - ls, gr, go, etc.
- Starship prompt configuration.
- Git configuration
    - User name and email.
    - `autoSetupRemote = true`















