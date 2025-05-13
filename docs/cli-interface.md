# CLI Interface

This document defines the command-line interface for `create_playlist.py`, including available arguments, flags, usage examples, and behavior expectations.

## Basic Usage

```bash
python create_playlist.py [options]
```

## Arguments and Flags

| Flag / Argument        | Description                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------- |
| `--source`             | Root directory to scan (defaults to current directory)                                 |
| `--recursive, -r`      | Recurse through subdirectories                                                         |
| `--format`             | Accepts one or more file extensions (e.g., `flac mp3`). Defaults to common formats     |
| `--genre`              | Filter by one or more genres (e.g., `--genre blues jazz`)                              |
| `--artist`             | Filter by one or more artist names                                                     |
| `--albumartist`        | Filter by one or more album artist names                                               |
| `--composer`           | Filter by one or more composers                                                        |
| `--year`               | Filter by year or year range (e.g., `--year 1990` or `--year 1990-1999`)               |
| `--partial-match, -p`  | Enables partial substring matches for text filters                                     |
| `--output`             | Name and path for the generated `.m3u` playlist file                                   |
| `--relative-paths, -l` | Write file paths relative to the playlist's location (or current directory if omitted) |
| `--append, -a`         | Append to the playlist if it already exists                                            |
| `--verbose, -v`        | Print matched files and actions to console                                             |

## Planned Behavior

* All filters are **case-insensitive**
* Filters accept **multiple values** and apply a logical OR
* Files with missing or invalid metadata are **skipped**
* Playlist is a plain text `.m3u` file with **absolute or relative paths**
* By default, the playlist file is **overwritten** unless `--append` is specified
* `--dry-run` prevents any file writing and prints planned actions only

## Example

```bash
python create_playlist.py \
  --source ./Music \
  --format flac mp3 \
  --genre blues jazz \
  --artist "B.B. King" "Etta James" \
  --year 1960-1979 \
  --recursive \
  --output blues_playlist.m3u \
  --relative-paths \
  --append \
  --verbose
```
