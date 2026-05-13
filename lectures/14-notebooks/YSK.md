# Data pipelines

- What is a data pipeline in a data science project?
    - **Answer**: A sequence of processing steps (e.g., clean, transform, extract features) applied to raw data.

- What problem do DVC data pipelines solve?
    - **Answer**: They keep processed data in sync with the code that produced it.

- What command defines a new stage of a DVC pipeline?
    - **Answer**: `dvc stage add`.

- In `dvc stage add -n clean -d data/raw.csv -o data/clean.csv python src/clean.py`, what does the `-n` flag specify?
    - **Answer**: The name of the stage (`clean`).

- In `dvc stage add -n clean -d data/raw.csv -o data/clean.csv python src/clean.py`, what does the `-d` flag specify?
    - **Answer**: A dependency of the stage (the input file `data/raw.csv`).

- In `dvc stage add -n clean -d data/raw.csv -o data/clean.csv python src/clean.py`, what does the `-o` flag specify?
    - **Answer**: An output of the stage (the file `data/clean.csv`).

- What file does `dvc stage add` create or update with the pipeline's stage definitions?
    - **Answer**: `dvc.yaml`.

- What command runs the pipeline defined in `dvc.yaml`?
    - **Answer**: `dvc repro`.

- If you change the code for an early stage of a DVC pipeline and run `dvc repro`, what happens?
    - **Answer**: That stage and all subsequent stages that depend on it are re-run.
