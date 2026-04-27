# Practical Git

- `.gitignore`: what it is, how it works, common patterns.

- What not to commit, and why:
    - Temporary files.
    - Generated/build artifacts.
    - Large data files.
    - Secrets and credentials.

- Git remembers everything.
    - Removing a committed file from history is not trivial.
    - Anything pushed to GitHub should be considered public, even if later "deleted".

- Secrets handling.
    - What to do if you accidentally commit a secret: rotate it, don't just `rm` it.
    - Tools/techniques for scrubbing history (mention, but emphasize prevention).

- GitHub.
    - Creating a new repository on GitHub.
    - Public vs. private repositories.
    - Branch protections on `main`.

- Git workflows.
    - Working alone: a simple linear flow.
    - Working with a team: GitHub flow (branch, PR, review, merge).

- Commit hygiene.
    - How often to commit (small, focused commits).
    - Squash merging vs. rebasing vs. plain merge — when to use each.

- Writing good commit messages.
    - Subject line conventions.
    - Why the "why" matters more than the "what".
