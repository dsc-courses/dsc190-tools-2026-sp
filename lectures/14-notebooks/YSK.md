# Data pipelines

- What command defines a new stage of a DVC pipeline?
    - **Answer**: `dvc stage add`.

- In `dvc stage add -n clean -d data/raw.csv -o data/clean.csv python src/clean.py`, what does the `-n` flag specify?
    - **Answer**: The name of the stage (`clean`).

- In `dvc stage add -n clean -d data/raw.csv -o data/clean.csv python src/clean.py`, what does the `-d` flag specify?
    - **Answer**: A dependency of the stage (the input file `data/raw.csv`).

- In `dvc stage add -n clean -d data/raw.csv -o data/clean.csv python src/clean.py`, what does the `-o` flag specify?
    - **Answer**: An output of the stage (the file `data/clean.csv`).

- What command runs the pipeline defined in `dvc.yaml`?
    - **Answer**: `dvc repro`.

# Jupyter notebook pitfalls

- What kind of file is a Jupyter notebook on disk?
    - **Answer**: A JSON file containing both the code and its outputs.

- How are images embedded in a Jupyter notebook file stored on disk?
    - **Answer**: As a binary blob inside the JSON notebook file.

- Why can a Jupyter notebook produce inconsistent or non-reproducible results?
    - **Answer**: Its output depends on the order in which cells were executed and on hidden state.

- Why is version-controlling Jupyter notebooks with git problematic?
    - **Answer**: Because diffs are hard to read and merge conflicts are difficult to resolve.

# Marimo notebooks

- What command opens a Marimo notebook for editing?
    - **Answer**: `marimo edit <notebook>`.

- In what file format are Marimo notebooks stored on disk?
    - **Answer**: As plain Python (`.py`) files.

- By default, does a Marimo notebook store the output of each cell on disk?
    - **Answer**: No.

- What does Marimo do when you execute a cell that other cells depend on?
    - **Answer**: It automatically executes the dependent cells to ensure that the results are up to date.

- Why are Marimo notebooks easier to version control with git than Jupyter notebooks?
    - **Answer**: They are plain Python files with no embedded outputs, so diffs are readable and merges are straightforward.

- How can a Marimo notebook be shared so that the recipient can run it without installing Python?
    - **Answer**: By publishing it as a WebAssembly app that runs entirely in the browser.
