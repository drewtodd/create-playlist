# create-playlist

A Python CLI tool to generate `.m3u` playlists from a local music library using metadata filters (genre, year, artist, etc.).

## Features
- Filter by genre, year range, artist, composer, albumartist
- Optional partial string matching
- Generates Rockbox-friendly `.m3u` playlists
- Works with FLAC, ALAC, and other taggable formats
- Designed for large music collections

## Usage
```
python create_playlist.py \
  --source ~/Music/flac \
  --output ~/Playlists \
  --genre blues jazz \
  --year-range 1960 1979 \
  --recursive \
  --name blues_and_jazz
```

## Installation
`pip install -r requirements.txt`
