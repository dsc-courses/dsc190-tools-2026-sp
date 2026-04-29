# Assignment 04: Collaborating with Git

In lecture, we saw the basics of git branches. Branches allow you to have
multiple versions of a repository in parallel, each with their own history.
Because of this, branches are especially useful for *collaboration*: a fact
that we'll explore in this assignment.

**What to turn in**: this assignment is more of a guided tour of git remotes
than a traditional assignment. However, as you go through the steps below,
you'll be asked to manipulate several git repositories. At the end of the
assignment, you will be asked to turn in one of the git repos to Gradescope.
The autograder will check that the repository contains the expected files and
commits, and that the commit history matches what is expected. All of the
autograder's tests are public. See the last step for more details on what to
turn in.

## Step 1: Create a "bare" repository

You've just joined a research lab, and the professor has asked you to work with
another lab member, Justin, on a new project. The first step: set up a git
repository to track your code and your results.

In practice, you'd typically do this by creating a new repository on GitHub or
one of the other git hosting services. You would then "clone" this repo to your
machine, and Justin would clone it to his, so that the repo exists on three
separate machines all at once.

In this assignment, however, we're not going to use GitHub or any other repo
hosting service. Instead, we'll simulate this situation by having all three of
these repositories -- the central one, yours, and Justin's -- on *one* machine:
yours. This way, you can run commands in your repo, but also in your
collaborator's repo, and see how they interact.

To begin, we need to create the central repository. The central repository is a
special kind of git repo called a "bare" repository. A bare repository is a git
repository that doesn't have a working tree. To do this, run the following
commands in your terminal:

```bash
git init --bare central.git
```

This will create a new directory called `central.git` in your current working
directory. Take a look inside this directory. You should see that it contains a
bunch of files and directories, similar to what is typically inside `.git/`
within a normal git repository. It is conventional to name a bare repository
with the `.git` suffix, but this is not strictly necessary.

## Step 2: Clone your copy

Now we need to create your copy of the repository. To copy a repository (often
from another machine), we use the `git clone` command. For instance, if we were
cloning the GitHub repository for this course, we would run:

```bash
git clone https://github.com/dsc-courses/dsc190-tools-2026-sp.git
```

For this assignment, though, we just want to clone the `central.git` repository
that we created in Step 1. While in the directory containing `central.git`, go
ahead and run:

```bash
git clone central.git mine
```

This will "copy" the `central.git` repository into a new directory called
`mine` (named "mine" because this repository represents your copy of the central repository).

**Before moving on**

- Create and commit a `README.md` file in your `mine` repository. The file should be empty.
- Create and commit a new file called `results.txt` in your `mine` repository. The file should be empty.

## Step 3: Making and pushing changes

At the end of the last step, you should have created two commits in your `mine`
repository. However, these commits only exist in your local copy of the
repository. To "push" your changes to the central repository, you need to run
`git push`.

**Before moving on**

- Run `git push` in your copy of the repo.

## Step 4: Clone Justin's copy

Now let's clone a copy of the central repository for Justin. Back in the
directory containing `central.git`, run:

```bash
git clone central.git justin
```

Now `cd` into Justin's repository and take a look around. You should notice
that all of the files that you made in your copy of the repository are also
present in Justin's repo. In fact, all of the *history* of the repository is
present in Justin's repo, too. This is one of the key features of git: when you
clone a repository, you get the entire history of that repository.

To test this, run `git log` in Justin's repo. You should see the same commit history that you saw in your repo.

## Step 5: Making and pushing changes in Justin's copy

Now let's try making some changes in Justin's copy of the repository.

**Before moving on**:

- While in, Justin's repo, edit `README.md` to contain a single line "Justin was here.". Commit and push this change.

## Step 6: Pulling changes into your copy

Justin let you know that he made some changes. If you go back to your copy of
the repository. And take a look inside of the `README.md` file, you'll see that
it doesn't contain the changes Justin made. This is because your copy of the
repository is not automatically updated when Justin makes changes. To get the
latest changes from the central repository, you need to *pull* the changes from
the central repo. To do this, we use the `git pull`.

Go ahead and run `git pull` in your copy of the repository. After running this
command, you should see that the changes Justin made to `README.md` are now
present.

This is the basic workflow for collaborating with git: you make changes in your
local copy of the repository, push those changes to the central repository, and
then pull changes from the central repository to get the latest updates from
your collaborators.

As it turns out, this workflow is making heavy use of *branches* under the
hood, as we'll see in the next steps.

## Step 7: Tracking branches

Let's take a deeper look at the branches that exist in your repo. If you just
run `git branch`, you'll see that there is only one branch: `main`. However,
this command is hiding some things from you by default. To see what's hidden, run:

```bash
git branch -avv
```

The `-a` flag tells git to show all branches, including remote tracking
branches. The `-vv` flag tells git to be "very verbose". You should see
something like the following:

```text
* main                611e03f [origin/main] Updated readme.
  remotes/origin/HEAD -> origin/main
  remotes/origin/main 611e03f Updated readme.
```

This is telling you that there are actually *three* branches in your
repository: `main`, `origin/HEAD`, and `origin/main`. The two additional
branches are called "remote tracking branches". They are created automatically
when you clone a repository (or, in our case, push a new branch to a
repository). They are intended to be read-only branches that track the
last-known state of the central repo.

Let's break it down even more. Take the first line:

```text
* main                611e03f [origin/main] Updated readme.
```

This is telling us that there's a branch called `main`, and it's the current
branch (the `*` indicates this). The `611e03f` is the short hash of the commit
that `main` is currently pointing to, and "Updated readme." is the commit
message of that commit. The `[origin/main]` is the new bit: it is telling us
that `origin/main` is the remote tracking branch that corresponds to `main`.

When we pushed our `main` branch to the central repository, it created a `main`
branch within that repo. At the same time, it created a `origin/dev` branch on
our local copy of the repository that "tracks" the `main` branch in the central
repository.

**Before moving on**:

- Create a new branch called `dev` in your copy of the repo. Add a new file called `dev.txt` to this branch, and commit the change. However, do not push this branch to the central repository yet!

## Step 8: Pushing and pulling a new branch

At the end of the last step, you created a new branch called `dev`, but you
didn't push it. We'll do so in just a moment, but before we do, run `git branch -a. vv` again. You should see that there is now a new branch called `dev`, but there is no corresponding remote tracking branch for it yet.

Now run `git push`. This time, you'll likely see an error like:

```text
fatal: The current branch dev has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin dev
```

This is because `dev` is a brand new branch that you created locally, and git
doesn't yet know which remote branch (if any) it should be associated with. To
fix this, run the command git suggests:

```bash
git push --set-upstream origin dev
```

The `--set-upstream` flag (which can be shortened to `-u`) tells git to create
a `dev` branch on the remote and to set up your local `dev` branch to track
it. After this first push, future `git push` and `git pull` commands on this
branch will work without needing the flag.

Now re-run `git branch -avv`. You should see that there is now a new remote
tracking branch called `origin/dev` that corresponds to your `dev` branch.

Now let's switch to Justin's copy of the repository and run `git branch -avv`
there. You should see that there is no trace of the `dev` branch in Justin's
repo yet. Now try running a new command: `git fetch`. This command is used to
fetch *information* about the latest changes from the central repository, but
that's it -- it doesn't actually modify the local branches. To see what
changed, run `git branch -avv` again: you should now see a new remote tracking
branch called `origin/dev` in Justin's repo, but there is still no `dev`
branch.

Now let's say Justin wants to work on the `dev` branch. To do this, he just
needs to run `git switch dev` to switch to the `dev` branch. You might think
that this would fail, since there is no `dev` branch in Justin's repo yet. But
go ahead and try it -- you'll see that git is smart enough to create a new
`dev` branch in Justin's repo that tracks the `origin/dev` branch. 

**Before moving on**:

- On Justin's copy of the repo, edit `dev.txt` to contain a single line "Justin was here, too.". Commit and push this change.

## Step 9: Back in your repo

Now let's go back to your copy of the repository, where we should still be on
the `dev` branch. Run `git branch -avv` to see the status of the branches. Then
run `git fetch` to get the latest information from the central repository. Now
run `git branch -avv` again to see what changed. You should see that the
`origin/dev` branch has been updated to point to the latest commit that Justin
made, but your own `dev` branch is still pointing to the old commit. If you run
`git status`, it will tell you that your `dev` branch is behind `origin/dev` by
1 commit.

Now let's update your `dev` branch to match the latest changes from Justin. To
do this, remember: `dev` and `origin/dev` are two separate *branches*. If we 
want the changes from `origin/dev` to be reflected in `dev`, we need to *merge* the two. To do so, simply run:

```bash
git merge origin/dev
```

The merge should succeed without any conflicts, and now your `dev` branch
should be up to date with the latest changes from Justin.

In short, this is how `git pull` works under the hood: it is essentially a `git
fetch` followed by a `git merge` of the remote tracking branch into the current
branch.

## Step 10: What to turn in

Once you're done with all of the steps above, you should turn in your three repositories to Gradescope. To do this, use the `git bundle` command to create a single file that contains the entire history of each repository. To create
a bundle for your repo, run (inside `mine/`):

```
git bundle create mine.bundle --all
```

Run the equivalent command in Justin's repo and the central repo to create `justin.bundle` and `central.bundle`. Then, submit all three bundle files to Gradescope. The autograder will check that the bundles contain the expected commits and files, and that the commit history matches what is expected.

