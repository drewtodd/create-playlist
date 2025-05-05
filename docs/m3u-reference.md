# M3U Playlist Format

This document outlines the structure of the `.m3u` playlist format for reference when generating playlists programmatically.

## Basic M3U Format

* An `.m3u` file is a plain text file.
* Each line represents a **path to an audio file**.
* No headers or metadata are strictly required (except for the extended format).

### Example (Simple Format)

```m3u
/Users/drew/Music/Artist1/Album1/01 - Track One.flac
/Users/drew/Music/Artist2/Album2/02 - Track Two.flac
```

## Extended M3U Format (Optional)

* Begins with `#EXTM3U` on the first line.
* Each track is preceded by an `#EXTINF` line that includes duration and display name:

```m3u
#EXTM3U
#EXTINF:210,Artist1 - Track One
/Users/drew/Music/Artist1/Album1/01 - Track One.flac
#EXTINF:185,Artist2 - Track Two
/Users/drew/Music/Artist2/Album2/02 - Track Two.flac
```

### Notes

* Duration is in **seconds** (can be `-1` if unknown)
* Display name typically follows the format: `Artist - Title`

## Implementation Notes

* This project will start with **basic M3U** output (no `#EXTM3U` or `#EXTINF`) unless specified by a future feature.
* All paths written will be **absolute** to ensure compatibility with external players.
* Line endings should be `\n` (Unix-style), even on Windows.

## External Reference

* [Wikipedia: M3U](https://en.wikipedia.org/wiki/M3U) — Describes basic and extended formats with examples.