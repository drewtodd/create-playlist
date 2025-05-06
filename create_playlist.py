import argparse
from pathlib import Path


def find_audio_files(
    source_dir: Path,
    recursive: bool = False,
    allowed_extensions: set[str] = {".flac"},
) -> list[Path]:
    matched_files = []
    if recursive:
        for path in source_dir.rglob("*"):
            if (
                path.is_file()
                and path.suffix.lower() in allowed_extensions
                and not path.name.startswith(".")
            ):
                matched_files.append(path.resolve())
    else:
        for path in source_dir.glob("*"):
            if (
                path.is_file()
                and path.suffix.lower() in allowed_extensions
                and not path.name.startswith(".")
            ):
                matched_files.append(path.resolve())
    return matched_files


def main():
    parser = argparse.ArgumentParser(description="Scan for audio files")
    parser.add_argument(
        "--source",
        type=str,
        default=".",
        help="Source directory to scan",
    )
    parser.add_argument(
        "--recursive",
        "-r",
        action="store_true",
        help="Recurse into subdirectories",
    )
    args = parser.parse_args()

    source_dir = Path(args.source).resolve()
    if not source_dir.is_dir():
        print(f"Error: {source_dir} is not a valid directory")
        return

    files = find_audio_files(source_dir, recursive=args.recursive)
    for f in files:
        print(f)


if __name__ == "__main__":
    main()