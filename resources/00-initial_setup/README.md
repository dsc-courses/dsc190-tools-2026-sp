# Initial Course Setup

## 1) Install a terminal

To get started in this course, you'll need to set up a Unix-like environment on
your machine, complete with a terminal. We'll use that terminal in the first
lecture, so you should try to get it installed and running before then.

Here are some instructions and recommendations for setting up your terminal
environment, depending on your operating system.

### macOS

macOS is a Unix-based operating system, so it already has everything you need
to get started. That said, you might want to install a more modern terminal app
(the default Terminal is pretty basic). We give two recommendations below, but
feel free to use whatever terminal you like (Justin uses Ghostty).

#### Option 1: Ghostty

[Ghostty](https://ghostty.org/) is a relatively new terminal that has quickly
become popular. It's fast, looks great out of the box, and has sensible
defaults so you can get started without much configuration.

To install, download the `.dmg` from the [Ghostty
website](https://ghostty.org/download), open it, and drag the app to your
Applications folder. Then launch it from Applications or Spotlight.

#### Option 2: Kitty

[Kitty](https://sw.kovidgoyal.net/kitty/) has been around longer than Ghostty
and is very configurable.

To install, follow the instructions for macOS on the [Kitty
website](https://sw.kovidgoyal.net/kitty/binary/).

### Windows

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

### Linux

If you're running Linux on your machine, then you're all set (but you knew that
already).

## 2) Set up SSH access to the course server

So that you can follow along with the lectures and work on the assignments, I
have set up an account for your on our course server. You should have received
an email with your username and password. First, try connecting use these.
Open your terminal and run:

    ssh <your-username>@172.235.41.44

(172.235.41.44 is the server's IP address. Replace `<your-username>` with your
actual username that was sent to you via email.)

You should be asked for your password. After you enter it, you should be logged in to the server.

To connect without typing a password every time, you'll set up SSH key
authentication. This is a more secure and convenient way to log in. Plus, after
the first week, we'll disable password authentication for security reasons, so
you'll *need* to set up SSH keys to continue accessing the server.

Whether you are on macOS or Windows, the below instructions should work (on
Windows, make sure to run them within your WSL terminal).

### Generate an SSH key (if you don't have one)

If you've never created an SSH key before, run:

    ssh-keygen -t ed25519

The `-t ed25519` flag specifies the type of encryption to use. Ed25519 is a
modern, secure choice that is widely supported.

Press Enter to accept the default file location and set a passphrase if you'd
like (or press Enter again for none).

### Copy your key to the server

Now run the following command to copy your public key to the server:

    ssh-copy-id <your-username>@172.235.41.44

Here, `172.235.41.44` is the server's IP address. Replace `<your-username>` with your actual username that was sent to you via email.

You'll be prompted for your password one last time. After this, you should be
able to log in without a password. To test it, close your terminal, open it again,
and type:

    ssh <your-username>@172.235.41.44

This time, you should be logged in without being asked for a password.

### Add the server to your SSH config

To avoid typing the full address every time, add an entry to your SSH config
file (`/Users/<your username>/.ssh/config` on a mac, or `/home/<your
username>/.ssh/config` in WSL2). Open it in a text editor and add:

    Host dsc190
        HostName 172.235.41.44
        User <your-username>

Replace `<your-username>` with your actual username on the server. Now you can
connect with just:

    ssh dsc190

Easy!
