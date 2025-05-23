# Project Structure

This document outlines the current directory structure and intended use of each top-level folder and file in the project.

## Root Directory Layout

```
create-playlist/
├── create_playlist.py        # Main CLI entry point
├── requirements.txt          # Python dependencies
├── .gitignore                # Files and folders excluded from git
├── LICENSE
├── pyproject.toml
├── README.md
├── .vscode/                  # Editor configuration (VS Code/VSCodium)
│   └── settings.json         # Formatting, linting, interpreter setup
├── docs/                     # Project standards and internal documentation
│   ├── file-naming-conventions.md
│   ├── git-commit-guidelines.md
│   ├── project-structure.md
│   └── cli-interface.md
├── test                      # Files (mp3, flac, etc.) and directories for testing
│   ├── Bryan Ferry - Frantic.flac
│   ├── Bryan Ferry - Frantic.mp4
│   ├── Marvin Gaye
│   │   └── Let's Get It On
│   │       ├── 01 Let's Get It On.mp3
│   │       ├── 02 Please Stay (Once You Go Away).mp3
│   │       ├── 03 If I Should Die Tonight.mp3
...
```

## Folder Details

### `docs/`

Houses markdown files documenting project standards, conventions, and procedures. Intended as an internal knowledge base.

### `.vscode/`

Local IDE/editor configuration for consistent tooling (e.g., Python interpreter, Black, Ruff). This folder is optional but tracked for reproducibility.

### `test/`

Houses test data (mp3, flac, other music files). To be excluded from Git repo (`.gitignore`)