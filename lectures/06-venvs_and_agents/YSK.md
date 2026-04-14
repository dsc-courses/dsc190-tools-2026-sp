# Python virtual environments

- Why is running `sudo pip install numpy` (without a virtual environment) generally a bad idea?
    - **Answer**: It installs numpy globally, so all projects share the same version.

- Where does `pip install numpy` install the package by default (without a virtual environment)?
    - **Answer**: Into the system's global Python directory

- What problem do Python virtual environments solve?
    - **Answer**: They let each project have its own independent set of package versions.

- What command creates a virtual environment named `myenv` in the current directory?
    - **Answer**: `python3 -m venv myenv`

- What command activates a virtual environment located at `env/`?
    - **Answer**: `source env/bin/activate` while in `env`'s parent directory.

- What command deactivates the currently-active virtual environment?
    - **Answer**: `deactivate`

- When you activate a virtual environment, which path-related variables are modified?
    - **Answer**: The shell's `$PATH` and Python's `sys.path`

- What happens to `$PATH` and `sys.path` when you run `deactivate`?
    - **Answer**: They are restored to their values from before activation.

- With a virtual environment activated, what does `pip install numpy` do?
    - **Answer**: Installs numpy into the active virtual environment, not globally.

- What command installs numpy version 1.23 specifically into the active virtual environment?
    - **Answer**: `pip install numpy==1.23`

# AI agents and safety

- What is a "prompt injection" attack?
    - **Answer**: Malicious instructions hidden inside otherwise innocuous data that the AI consumes and obeys.

- What command creates a Docker sandbox, installs opencode, and shares only the current directory with it?
    - **Answer**: `sbx run opencode`
