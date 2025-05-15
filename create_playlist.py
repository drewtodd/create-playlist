import argparse
from pathlib import Path
from typing import Dict
import re
import sys
from typing import Optional

from mutagen import File as MutagenFile

# Default file formats to include if --format is not specified
DEFAULT_FORMATS = {".mp3", ".m4a", ".wav", ".aiff", ".flac", ".ogg"}


def normalize_extensions(exts: list[str] | None) -> set[str]:
    if not exts:
        return DEFAULT_FORMATS
    return {e.lower() if e.startswith(".") else f".{e.lower()}" for e in exts}


def find_audio_files(
    source_dir: Path,
    recursive: bool = False,
    allowed_extensions: set[str] = DEFAULT_FORMATS,
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


def extract_metadata(file_path: Path) -> Dict[str, str] | None:
    try:
        audio = MutagenFile(file_path)
        if audio is None or not audio.tags:
            return None

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

        return metadata

    except Exception as e:
        print(f"[WARN] Failed to read tags from {file_path.name}: {e}")
        return None


def extract_all_metadata(file_paths: list[Path]) -> dict[Path, dict[str, str]]:
    metadata_map = {}
    for file in file_paths:
        data = extract_metadata(file)
        if data is not None:
            metadata_map[file] = data
    return metadata_map


def filter_by_string_field(
    metadata_map: dict[Path, dict[str, str]],
    field_name: str,
    filter_values: list[str],
    partial: bool = False,
    verbose: bool = False,
) -> dict[Path, dict[str, str]]:
    filtered = {}
    normalized_values = [v.lower().strip() for v in filter_values]
    for path, tags in metadata_map.items():
        field_value = tags.get(field_name, "").lower().strip()
        if not field_value:
            if verbose:
                print(f"[SKIP] {path.name} — {field_name} tag missing or empty")
            continue
        match = any(val in field_value if partial else val == field_value for val in normalized_values)
        if match:
            filtered[path] = tags
            if verbose:
                print(f"[MATCH] {path} — {field_name}: {field_value}")
        else:
            if verbose:
                print(f"[SKIP] {path.name} — {field_name} '{field_value}' did not match any of {normalized_values}")
    return filtered


def filter_by_genre(
    metadata_map: dict[Path, dict[str, str]],
    genre_filter: list[str],
    partial: bool = False,
    verbose: bool = False,
) -> dict[Path, dict[str, str]]:
    return filter_by_string_field(metadata_map, "genre", genre_filter, partial, verbose)


def filter_by_year(
    metadata_map: dict[Path, dict[str, str]],
    start_year: int,
    end_year: int,
    verbose: bool = False,
) -> dict[Path, dict[str, str]]:
    filtered = {}
    for path, tags in metadata_map.items():
        raw_date = tags.get("date", "").strip()
        match = re.match(r"^(\d{4})", raw_date)
        if match:
            year = int(match.group(1))
            if start_year <= year <= end_year:
                filtered[path] = tags
                if verbose:
                    print(f"[MATCH] {path} — year: {year}")
            else:
                if verbose:
                    print(f"[SKIP] {path.name} — year {year} not in range {start_year}-{end_year}")
        else:
            if verbose:
                print(f"[SKIP] {path.name} — no valid 4-digit year in tag")
    return filtered


def write_playlist(
    file_paths: list[Path],
    output_path: Path,
    dry_run: bool = False,
    verbose: bool = False,
    relative_paths: bool = False,
    base_path: Path | None = None,
    append: bool = False,
) -> None:
    if dry_run:
        print("\n[INFO] Dry run enabled. Skipping playlist write.\n")
        return

    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        mode = "a" if append else "w"

        if verbose:
            path_mode = "appending to" if append else "writing to"
            print(f"[INFO] {path_mode} playlist with {'relative' if relative_paths else 'absolute'} paths")
            if relative_paths and base_path:
                print(f"[INFO] Relative base: {base_path}")

        with output_path.open(mode, encoding="utf-8", newline="\n") as f:
            for path in file_paths:
                if relative_paths and base_path:
                    try:
                        line = str(path.relative_to(base_path))
                    except ValueError:
                        line = str(path.resolve())
                else:
                    line = str(path.resolve())
                f.write(line + "\n")

        print(f"\n[INFO] Playlist written to: {output_path.resolve()}\n")

    except Exception as e:
        print(f"\n[ERROR] Failed to write playlist: {e}\n")


def parse_year_range(raw_input: str) -> Optional[tuple[int, int]]:
    raw_input = raw_input.strip()
    if re.fullmatch(r"\d{4}", raw_input):
        return int(raw_input), int(raw_input)
    if re.fullmatch(r"\d{4}-\d{4}", raw_input):
        start, end = map(int, raw_input.split("-"))
        if start > end:
            raise ValueError(f"Invalid year range: {start} > {end}")
        return start, end
    raise ValueError(f"Invalid --year format: '{raw_input}'")


def main():
    parser = argparse.ArgumentParser(description="Scan for audio files and metadata")
    parser.add_argument("--source", type=str, default=".", help="Source directory to scan")
    parser.add_argument("-r", "--recursive", action="store_true", help="Recurse into subdirectories")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print metadata for each matched file")
    parser.add_argument("--output", type=str, default="playlist.m3u", help="Path and filename for output playlist")
    parser.add_argument("-d", "--dry-run", action="store_true", help="Simulate playlist creation without writing output")
    parser.add_argument("--genre", nargs="+", help="Filter by one or more genres")
    parser.add_argument("-p", "--partial-match", action="store_true", help="Enable substring matching for text-based filters")
    parser.add_argument("-l", "--relative-paths", action="store_true", help="Write paths as relative to the output directory")
    parser.add_argument("--format", nargs="+", help="Audio file extensions to include (e.g., flac mp3). Defaults to common formats.")
    parser.add_argument("--year", type=str, help="Filter by year or year range (e.g., 1970 or 1970-1979)")
    parser.add_argument("--artist", nargs="+", help="Filter by one or more artists")
    parser.add_argument("--composer", nargs="+", help="Filter by one or more composers")
    parser.add_argument("--albumartist", nargs="+", help="Filter by one or more album artists")
    parser.add_argument("-a", "--append", action="store_true", help="Append to the playlist if it already exists")
    parser.add_argument("--base-dir", type=str, help="Optional root directory to use for relative paths")

    args = parser.parse_args()

    source_dir = Path(args.source).resolve()
    if not source_dir.is_dir():
        print(f"Error: {source_dir} is not a valid directory")
        return

    output_path = Path(args.output).resolve()
    if args.relative_paths:
        if args.base_dir:
            base_path = Path(args.base_dir).resolve()
            if not base_path.is_dir():
                print(f"[ERROR] base-dir '{base_path}' is not a valid directory")
                sys.exit(1)
        else:
            base_path = output_path.parent
    else:
        base_path = Path.cwd()

    allowed_exts = normalize_extensions(args.format)

    files = find_audio_files(source_dir, recursive=args.recursive, allowed_extensions=allowed_exts)
    if args.verbose:
        print(f"[INFO] Found {len(files)} audio file(s) to examine")
    metadata_by_file = extract_all_metadata(files)

    if args.genre:
        metadata_by_file = filter_by_genre(
            metadata_by_file,
            genre_filter=args.genre,
            partial=args.partial_match,
            verbose=args.verbose,
        )

    if args.year:
        try:
            year_start, year_end = parse_year_range(args.year)
        except ValueError as e:
            print(f"[ERROR] {e}")
            sys.exit(1)
    else:
        year_start, year_end = None, None

    if year_start and year_end:
        metadata_by_file = filter_by_year(
            metadata_by_file,
            start_year=year_start,
            end_year=year_end,
            verbose=args.verbose,
        )

    if args.artist:
        metadata_by_file = filter_by_string_field(metadata_by_file, "artist", args.artist, partial=args.partial_match, verbose=args.verbose)
    if args.composer:
        metadata_by_file = filter_by_string_field(metadata_by_file, "composer", args.composer, partial=args.partial_match, verbose=args.verbose)
    if args.albumartist:
        metadata_by_file = filter_by_string_field(metadata_by_file, "albumartist", args.albumartist, partial=args.partial_match, verbose=args.verbose)

    playlist_files = list(metadata_by_file.keys())
    if args.verbose:
        print(f"[INFO] {len(playlist_files)} file(s) matched and will be added to the playlist")

    write_playlist(
        playlist_files,
        output_path=output_path,
        dry_run=args.dry_run,
        verbose=args.verbose,
        relative_paths=args.relative_paths,
        base_path=base_path,
        append=args.append,
    )


if __name__ == "__main__":
    main()