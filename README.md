# create-playlist

A Python CLI tool to generate `.m3u` playlists from a local music library using metadata filters (genre, year, artist, composer, album artist, etc.).

## Features
- Filter by genre, year (or year range), artist, composer, album artist
- Supports multiple values and optional partial string matching
- Case-insensitive filters
- Generates Rockbox-friendly `.m3u` playlists
- Absolute or relative path output
- Appends to or overwrites playlist files
- Works with FLAC, ALAC, MP3, and other taggable formats
- Designed for large music collections

## Usage
```sh
python create_playlist.py \
  --source ~/Music/flac \
  --output ~/Playlists/blues_and_jazz.m3u \
  --genre blues jazz \
  --artist "Muddy Waters" "Howlin' Wolf" \
  --albumartist "Mose Allison" \
  --composer "Muddy Waters" \
  --year 1960-1979 \
  --recursive \
  --partial-match \
  --relative-paths \
  --append \
  --verbose
```

## Installation
```sh
pip install -r requirements.txt
```

## Contributing & Project Standards

This project includes a growing internal documentation library located in the `[docs/](docs/)` directory. These documents outline development practices, naming conventions, and project workflows to ensure consistency and long-term maintainability.

### Key Docs

- [CLI Interface](docs/cli-interface.md): Full command-line interface specification
- [Audio File Formats](docs/audio-file-formats.md): Supported file extensions and encoding notes
- [M3U Reference](docs/m3u-reference.md): Overview of the `.m3u` format and path rules
- [Project Structure](docs/project-structure.md): Directory layout and source organization
- [File Naming Conventions](docs/file-naming-conventions.md): Naming rules for scripts, assets, and data
- [Git Commit Guidelines](docs/git-commit-guidelines.md): Commit message format and conventions
- [GitHub Issue Authoring Guidelines](docs/github-issue-authoring-guidelines.md): How to write clear, testable issues

**@FutureDrew**: If you’re returning to this project after a break, please refer to these documents first. They provide quick guidance on things like commit message formats, file naming, and other working agreements.
