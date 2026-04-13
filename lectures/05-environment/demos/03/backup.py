import argparse
import shutil
from pathlib import Path


def backup_path(path: Path) -> Path:
    if path.suffix:
        return path.with_suffix(f".bak{path.suffix}")
    return path.with_name(f"{path.name}.bak")


def main():
    parser = argparse.ArgumentParser(
        description="Back up files by copying them to .bak variants."
    )
    parser.add_argument("paths", nargs="+", type=Path, help="Files to back up.")
    args = parser.parse_args()

    for src in args.paths:
        dst = backup_path(src)
        shutil.copy2(src, dst)
        print(f"{src} -> {dst}")


if __name__ == "__main__":
    main()
