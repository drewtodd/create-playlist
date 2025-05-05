# Project Structure

This document outlines the current directory structure and intended use of each top-level folder and file in the project.

## Root Directory Layout

```
create-playlist/
├── create_playlist.py        # Main CLI entry point
├── requirements.txt          # Python dependencies
├── .gitignore                # Files and folders excluded from git
├── .vscode/                  # Editor configuration (VS Code/VSCodium)
│   └── settings.json         # Formatting, linting, interpreter setup
├── docs/                     # Project standards and internal documentation
│   ├── file-naming-conventions.md
│   ├── git-commit-guidelines.md
│   ├── project-structure.md
│   └── cli-interface.md
```

## Folder Details

### `docs/`

Houses markdown files documenting project standards, conventions, and procedures. Intended as an internal knowledge base.

### `.vscode/`

Local IDE/editor configuration for consistent tooling (e.g., Python interpreter, Black, Ruff). This folder is optional but tracked for reproducibility.
