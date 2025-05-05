# Supported Audio File Formats

This document outlines commonly used audio file formats and their typical use cases, extensions, and compatibility considerations for playlist generation.

## 🎵 Lossless Formats

| Format | Extension | Description                                                                                                                 |
| ------ | --------- | --------------------------------------------------------------------------------------------------------------------------- |
| FLAC   | `.flac`   | Free Lossless Audio Codec. Open source, widely supported by high-res players and Rockbox. Not natively supported in iTunes. |
| ALAC   | `.m4a`    | Apple Lossless Audio Codec. Ideal for Apple ecosystem; same container as AAC but lossless.                                  |
| WAV    | `.wav`    | Raw audio. Large file size, no compression. Great for archival/mastering, but limited metadata support.                     |
| AIFF   | `.aiff`   | Apple’s uncompressed format (like WAV but with better metadata support).                                                    |

## 🎧 Lossy Formats

| Format     | Extension | Description                                                                                                             |
| ---------- | --------- | ----------------------------------------------------------------------------------------------------------------------- |
| MP3        | `.mp3`    | The most universally supported format. Good metadata and compression balance.                                           |
| AAC        | `.m4a`    | Advanced Audio Coding. Preferred in the Apple ecosystem; better quality than MP3 at same bitrate.                       |
| Ogg Vorbis | `.ogg`    | Open-source alternative to MP3/AAC. Smaller file size with similar or better quality, but less support on some players. |

---

## 📂 Default Supported Formats in This Project

By default, the playlist generator supports the following extensions:

```
.flac, .mp3, .m4a, .ogg, .wav, .aiff
```

You can use the `--format` flag to include or limit to specific extensions.

---

## ℹ️ Notes

- Playlist entries are based on file extension and path, not content sniffing.
- All matching is **case-insensitive**.
- Future enhancements may add format validation or embedded metadata checks.


## 🏷️ Metadata Support by Format

| Format     | Tag Standard    | Common Tags Supported                                                                            | Notes                                                    |
| ---------- | --------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| FLAC       | Vorbis Comments | title, artist, album, albumartist, composer, genre, date, year, tracknumber, discnumber, comment | Flexible and widely supported                            |
| ALAC / M4A | iTunes Metadata | title, artist, album, albumartist, composer, genre, date, tracknumber, discnumber, comments      | Uses proprietary Apple tagging; tools like AtomicParsley |
| MP3        | ID3v1 / ID3v2   | title, artist, album, albumartist, composer, genre, date, year, tracknumber, discnumber, comment | ID3v2 is more capable and common today                   |
| WAV        | RIFF INFO List  | title, artist, album, genre, date, tracknumber, comment                                          | Limited and inconsistent metadata support                |
| AIFF       | ID3v2 or iXML   | title, artist, album, albumartist, composer, genre, date, tracknumber, discnumber, comment       | Depends on authoring tool; ID3 support varies            |
| Ogg Vorbis | Vorbis Comments | title, artist, album, albumartist, composer, genre, date, year, tracknumber, discnumber, comment | Same format as FLAC                                      |

---

- For reliable playlist filtering, the following metadata fields are prioritized:

  - `title`
  - `artist`
  - `album`
  - `albumartist`
  - `composer`
  - `genre`
  - `date` / `year`
  - `tracknumber`
  - `discnumber`
  - `comment`