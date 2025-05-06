import argparse
from pathlib import Path
from typing import Dict

from mutagen import File as MutagenFile


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


def extract_metadata(file_path: Path, verbose: bool = False) -> Dict[str, str] | None:
    try:
        audio = MutagenFile(file_path)
        if audio is None or not audio.tags:
            if verbose:
                print(f"[INFO] No readable metadata in {file_path.name}")
            return None

        # Normalize tags to lowercase keys for consistent access
        raw_tags = {k.lower(): v for k, v in audio.tags.items()}

        def get(tag_keys: list[str]) -> str:
            for key in tag_keys:
                value = raw_tags.get(key.lower())
                if value:
                    return str(value[0]).strip()
            return ""

        metadata = {
            "genre": get(["genre", "TCON", "©gen"]),
            "artist": get(["artist", "TPE1", "©ART"]),
            "albumartist": get(["albumartist", "TPE2", "aART"]),
            "composer": get(["composer", "TCOM", "©wrt", "©com"]),
            "title": get(["title", "TIT2", "©nam"]),
            "tracknumber": get(["tracknumber", "TRCK", "trkn"]),
            "date": get(["date", "TDRC", "TYER", "©day"]),
        }

        if verbose:
            print(f"[INFO] Parsed: {file_path.name}")
            for k, v in metadata.items():
                print(f"  {k}: {v or '[empty]'}")

        return metadata

    except Exception as e:
        print(f"[WARN] Failed to read tags from {file_path.name}: {e}")
        return None
                        

def extract_all_metadata(file_paths: list[Path], verbose: bool = False) -> dict[Path, dict[str, str]]:
    metadata_map = {}
    for file in file_paths:
        data = extract_metadata(file, verbose=verbose)
        if data is not None:
            metadata_map[file] = data
    return metadata_map


def main():
    parser = argparse.ArgumentParser(description="Scan for audio files and metadata")
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
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Print metadata for each matched file",
    )
    args = parser.parse_args()

    source_dir = Path(args.source).resolve()
    if not source_dir.is_dir():
        print(f"Error: {source_dir} is not a valid directory")
        return

    files = find_audio_files(source_dir, recursive=args.recursive)
    metadata_by_file = extract_all_metadata(files)

    for file, metadata in metadata_by_file.items():
        print(f"\n{file}")
        if args.verbose:
            for key, value in metadata.items():
                print(f"  {key}: {value}")


if __name__ == "__main__":
    main()