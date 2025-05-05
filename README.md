# create-playlist

A Python CLI tool to generate `.m3u` playlists from a local music library using metadata filters (genre, year, artist, etc.).

## Features
- Filter by genre, year range, artist, composer, album artist
- Optional partial string matching
- Generates Rockbox-friendly `.m3u` playlists
- Works with FLAC, ALAC, and other taggable formats
- Designed for large music collections

## Usage
```sh
python create_playlist.py \
  --source ~/Music/flac \
  --output ~/Playlists \
  --artist muddy waters \
  --album-artist mose allison \
  --composer muddy waters \
  --genre blues jazz \
  --year-range 1960 1979 \
  --recursive \
  --name blues_and_jazz
```

## Installation
```sh
pip install -r requirements.txt
```

## Contributing & Project Standards

This project includes a growing internal documentation library located in the `[docs/](docs/)` directory. These documents outline development practices, naming conventions, and project workflows to ensure consistency and long-term maintainability.

### Key Docs

- [Git Commit Guidelines](docs/git-commit-guidelines.md)
- [File Naming Conventions](docs/file-naming-conventions.md)

**@FutureDrew**: If you’re returning to this project after a break, please refer to these documents first. They provide quick guidance on things like commit message formats, file naming, and other working agreements.

