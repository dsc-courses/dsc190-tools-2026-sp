# Initial Course Setup

To get started in this course, you'll need to set up a Unix-like environment on
your machine, complete with a terminal. We'll use that terminal in the first
lecture, so you should try to get it installed and running before then.

Here are some instructions and recommendations for setting up your terminal environment, depending on your operating system.

## macOS

macOS is a Unix-based operating system, so it already has everything you need
to get started. That said, you might want to install a more modern terminal app
(the default Terminal is pretty basic). We give two recommendations below, but
feel free to use whatever terminal you like (Justin uses Ghostty).

### Option 1: Ghostty

[Ghostty](https://ghostty.org/) is a relatively new terminal that has quickly
become popular. It's fast, looks great out of the box, and has sensible
defaults so you can get started without much configuration.

To install, download the `.dmg` from the [Ghostty
website](https://ghostty.org/download), open it, and drag the app to your
Applications folder. Then launch it from Applications or Spotlight.

### Option 2: Kitty

[Kitty](https://sw.kovidgoyal.net/kitty/) has been around longer than Ghostty
and is very configurable.

To install, follow the instructions for macOS on the [Kitty
website](https://sw.kovidgoyal.net/kitty/binary/).

## Windows

Windows is not a Unix-based operating system, but can still run a Unix-like
environment within Windows by installing **WSL2** (Windows Subsystem for
Linux). WSL2 runs a real Linux environment inside of Windows, giving you a
proper bash shell and access to the full suite of Linux command-line tools.
This is what we recommend for this course.

To install WSL2, follow the instructions on the official Microsoft documentation:

    https://learn.microsoft.com/en-us/windows/wsl/setup/environment

You can stop before the "Add additional distributions" step. However, if you'd
like to have a nicer terminal experience, you can continue to "Set up Windows
Terminal".

## Linux

If you're running Linux on your machine, then you're all set (but you knew that
already).
