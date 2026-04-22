# Git branches

- What is the name of the single branch that every new Git repo starts with?
    - **Answer**: `main`

- What command creates a new branch called `alpha` and switches to it?
    - **Answer**: `git switch -c alpha`

- What command switches to an existing branch named `alpha`?
    - **Answer**: `git switch alpha`

- When you run `git switch alpha`, which of the three trees are updated?
    - **Answer**: All three: HEAD, the staging area, and the working tree.

- What command lists all branches in the current repo?
    - **Answer**: `git branch`

- What command deletes a branch named `alpha`?
    - **Answer**: `git branch -d alpha`

# Merging

- What command merges the branch `alpha` into the current branch?
    - **Answer**: `git merge alpha`

- What sequence of commands merges branch `alpha` into `main`?
    - **Answer**: `git switch main` followed by `git merge alpha`.

- What command aborts an in-progress merge and returns to the pre-merge state?
    - **Answer**: `git merge --abort`

- What command merges `alpha` into the current branch, but if there are conflicts, it automatically resolves them in favor of the current branch's changes?
    - **Answer**: `git merge -X ours alpha`

- What command merges `alpha` into the current branch, but if there are conflicts, it automatically resolves them in favor of `alpha`'s changes?
    - **Answer**: `git merge -X theirs alpha`

# Branch theory and detached HEAD

- What command moves HEAD to a specific commit `a1b2c3` that is not associated with any branch?
    - **Answer**: `git switch --detach a1b2c3`

- What is a detached HEAD?
    - **Answer**: A state where HEAD points to a commit that is not pointed to by any branch.

- Why is committing while in a detached HEAD state dangerous?
    - **Answer**: The new commits are not reachable from any branch, so they will eventually be garbage collected.

- What does git do with commits that are not reachable from any branch?
    - **Answer**: They are eventually garbage collected.
