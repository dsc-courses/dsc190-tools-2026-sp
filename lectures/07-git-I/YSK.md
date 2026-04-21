# Git basics

- What command creates a new Git repository in the current directory?
    - **Answer**: `git init`

Which command stages `README.md` for the next commit?
    - **Answer**: `git add README.md`

- What does `git commit -m "foo"` do?
    - **Answer**: Creates a new commit from the staged files with the given message.

- What command shows the current state of files in the working tree and staging area?
    - **Answer**: `git status`

- What command shows the commit history of the repository?
    - **Answer**: `git log`

# Undoing changes

- What command unstages `README.md`, leaving the working tree unchanged?
    - **Answer**: `git restore --staged README.md`

- What command discards working-tree changes to `README.md` by restoring it from the staging area?
    - **Answer**: `git restore README.md`

- What command restores `README.md` in the working tree to its contents at commit `a1b2c3`?
    - **Answer**: `git restore --source a1b2c3 README.md`

# The three trees

- What are the three "trees" that Git uses to track your files?
    - **Answer**: The working tree, the staging area, and HEAD.

- What does the working tree contain?
    - **Answer**: The actual files in your project directory.

- What does the staging area contain?
    - **Answer**: The files as they were when you last staged them.

- What does HEAD refer to?
    - **Answer**: The files as they were in the last commit.

# How commands affect the trees

- Which tree does `git add <file>` modify?
    - **Answer**: The staging area.

- Which tree does `git commit` modify?
    - **Answer**: `HEAD`.

- Which command copies `<file>` from HEAD into the staging area?
    - **Answer**: `git restore --staged <file>`

- Which command copies `<file>` from the staging area into the working tree?
    - **Answer**: `git restore <file>`
