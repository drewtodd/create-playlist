# CLI Interface

This document defines the command-line interface for `create_playlist.py`, including available arguments, flags, usage examples, and behavior expectations.

## Basic Usage

```bash
python create_playlist.py [options]
```

## Arguments and Flags (Planned)

| Flag / Argument       | Description                                                   |
| --------------------- | ------------------------------------------------------------- |
| `--source`            | Root directory to scan (defaults to current directory)        |
| `--recursive, -r`     | Recurse through subdirectories                                |
| `--format`            | Accepts one or more file extensions (e.g., `.flac .mp3`)      |
| `--genre`             | Filter by genre (e.g., `--genre blues`)                       |
| `--artist`            | Filter by artist name                                         |
| `--albumartist`       | Filter by album artist                                        |
| `--composer`          | Filter by composer                                            |
| `--year-range`        | Filter by year or year range (e.g., `--year-range 1990-1999`) |
| `--partial-match, -p` | Enables partial substring matches for filters                 |
| `--output`            | Name and path for the generated `.m3u` playlist file          |
| `--verbose, -v`       | Print matched files and actions to console                    |

## Planned Behavior

* Filters are **case-insensitive**
* Files with missing or invalid metadata are **skipped**
* Output playlist is a plain text `.m3u` file with **absolute paths**

## Example

```bash
python create_playlist.py \
  --source ./Music \
  --format .flac .mp3 \
  --genre blues \
  --year-range 1960-1979 \
  --recursive \
  --output blues_playlist.m3u
```
