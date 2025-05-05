# File Naming Conventions

To maintain consistency and improve readability across the project, follow these file naming conventions for source code, configuration files, and documentation.

## 🔤 General Rules

* Use **lowercase** letters for all file names.
* Avoid spaces; use hyphens or underscores depending on context.
* Be descriptive, but concise.
* File names should reflect their contents or purpose.

## 🐍 Python Files

* Use **snake\_case** for all Python module names:

  * ✅ `create_playlist.py`
  * ✅ `metadata_utils.py`

## 📝 Markdown / Documentation Files

* Use **kebab-case** for documentation files:

  * ✅ `git-commit-guidelines.md`
  * ✅ `file-naming-conventions.md`
  * ✅ `project-structure.md`

### Why kebab-case?

* Common in markdown documentation
* Better for URLs and cross-platform tools
* Consistent with conventions used in static site generators (e.g., Hugo, Jekyll)

## 📁 Directory Names

* Use **kebab-case** or **snake\_case** depending on the context:

  * For Python packages: `playlist_utils/`
  * For documentation or public assets: `docs/`, `audio-samples/`

---

These conventions are part of the project's standards and are intended to keep collaboration, tooling, and long-term maintenance smooth and error-free.
