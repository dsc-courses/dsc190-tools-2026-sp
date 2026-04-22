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


Git Branching and Remotes
=========================

To follow along...

1. Download and run [Fork](https://git-fork.com), a Git GUI.
2. Open a terminal, `cd` to a place where you want to work.
    - E.g., your desktop on macOS, or your home directory in WSL.

You should not use the Docker container.

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Git Branches</span>**

Git
===

- Git is a **version control system** (VCS).
- It gives you two new, important capabilities:
    - **Time machine**: You can go back to any previous version of your project files (code, data, etc.)
    - **Parallel universes**: you can work on multiple versions of your project and merge them together when you're done.
        - This allows *collaboration*.

Git Branches
============

- Git implements "parallel universes" using <span class="term">**branches**</span>.
- All repos start with a single branch, called `main`.

Creating Branches
=================


- To create a new branch and switch to it (splitting the history):

```bash
git switch --create <branch-name>
# or
git switch -c <branch-name>
```

Switching Branches
==================

- To switch to an existing branch:

```bash
git switch <branch-name>
```

- This updates all three trees:
    - Work tree, staging area, and HEAD.

<span class="exercise">**Demo**</span>
===

Create a new repo, make a few commits, then:
- Create a new branch and switch to it.
- Make a commit on the new branch.
- Switch back to the main branch and make a commit there.

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Merging</span>**

Git Merging
===========

- Branches allow working on multiple versions of a project in parallel.
- When you're done on a branch, you'll <span class="term">**merge**</span> it back into the main branch:

```bash
git switch main
git merge <other-branch-name>
```

<span class="exercise">**Demo**</span>
===

- Merge the branch you created in the previous demo back into `main`.

Merge Conflicts
===============

- Two branches can make changes to the same file.
- Git's merge algorithms are "smart".
    - Can figure out how to "weave" together changes using context.
- But sometimes it's unclear which branch's changes should be kept.
- When this happens, there is a <span class="term">**merge conflict**</span>.

<span class="exercise">**Demo**</span>
===

1. Create a new repo with `README.md` containing "Hello, world!".
2. On a new branch, modify it to say "Hello, Git!" and commit.
3. Back on `main`, modify it to say "Hello, everyone!" and commit.
4. Try to merge the new branch into `main`.

Merge Conflicts
===============

- When there is a merge conflict, Git will stop the merge and insert <span class="term">**conflict markers**</span> into the affected files.


```text
<<<<<<< HEAD
Hello, everyone!
=======
Hello, Git!
>>>>>>> alpha
```

Aborting a Merge
================

- We can <span class="term">**abort**</span> a merge to return to the pre-merge state:

```bash
git merge --abort
```

- Usually, though, we want to <span class="term">**resolve**</span> the merge conflict instead of aborting.


Resolving Merge Conflicts
=========================

We'll discuss three common ways to resolve merge conflicts:

1. Manually (most common)
2. Abort and take all of "their" changes
3. Abort and take all of "our" changes

Approach 1: Manual Resolution
=============================

1. Edit each file with conflict markers to resolve the conflict.
    - Remove the conflict markers and keep the changes you want.
2. Stage the affected files with `git add`.
3. Commit the merge with `git commit`.

<span class="exercise">**Demo**</span>
===

Try resolving the merge conflict from the previous demo manually.

Approach 2: Abort and Take All of "Their" Changes
=================================================

Sometimes, we want to decide every conflict in favor of the other branch. To do this:

```bash
git merge --abort
git merge -X theirs <other-branch-name>
```

<span class="exercise">**Demo**</span>
===

Try resolving the merge conflict by taking all of the other branch's changes.

Approach 3: Abort and Take All of "Our" Changes
===============================================

Other times, we want to decide every conflict in favor of our branch. To do this:

```bash
git merge --abort
git merge -X ours <other-branch-name>
```

<span class="exercise">**Demo**</span>
===

Try resolving the merge conflict by taking all of the current branch's changes.

---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">More Branch Commands</span>**

Listing Branches
================

- To list all branches in the repo:

```bash
git branch
```

Deleting Branches
=================

To delete a branch:

```bash
git branch --delete <branch-name>
# or
git branch -d <branch-name>
```

Garbage Collection
==================

- When you delete a branch, the commits are **not** deleted.
- However, if a commit is no longer reachable from any branch, it will eventually be <span class="term">**garbage collected**</span> by Git.
- For this reason, you must "force delete" a branch if it has not been fully merged into another branch.
- <span class="bad">**Warning**</span>: force deleting a branch can lead to data loss!


Old Commands
============

- The old way to create a branch and switch to it was:

```bash
git checkout -b <branch-name>
```

- The old way to switch branches was:

```bash
git checkout <branch-name>
```

- You should prefer `git switch`.


---

<!-- new_lines: 4 -->
<!-- alignment: center -->

![image:w:70%](../COMMON/logo.png)

**<span class="term">Branch Theory</span>**

Branch Theory
=============

- Branches are just "pointers" to specific commits.

Recall
======

- HEAD is a pointer to the *current* commit.
- Consider:
```bash
git switch alpha
```
- This:
    - Moves HEAD to point to the commit that `alpha` points to.
    - Updates the staging area and work tree to match that commit.

Detached HEAD
=============

- In normal operation, HEAD points to a commit that is also pointed to by a branch.
- But you can move the HEAD to *any* commit:
```bash
git switch --detach <commit-hash>
```
- This is called a <span class="term">**detached HEAD**</span>.

<span class="exercise">**Demo**</span>
===

Go back to the first commit in your repo using

```bash
git switch --detach <commit-hash>
```

Detached HEAD
=============

- Detaching the HEAD is useful for going back in time *temporarily*.
<!-- pause -->
- However, it can be <span class="bad">**dangerous**</span>.
    - Commits made in a detached HEAD state are not reachable from any branch.
    - These commits will eventually be garbage collected by Git, leading to data loss.
    - **Solution**: detach HEAD, then create a new branch.

This Week's Assignment
======================

- Git branches allow *collaboration*.
- This week's assignment introduces you to <span class="term">**remote branches**</span>, as well as git fetch, git push, and git pull.

