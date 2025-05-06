# Git Commit Guidelines

These conventions ensure clarity and consistency in commit history for this project.

## Commit Title Format

Use the following format:

```
<type>: <imperative, lowercase summary>
```

* **Use lowercase** for both `<type>` and the summary.
* **Imperative mood**: Describe what the commit *does*, not what it *did* (e.g., "add support" not "added support").
* Limit to **50 characters** or less when possible.

### Examples

```
feat: add --genre filter to CLI
fix: handle missing metadata gracefully
docs: update README with usage instructions
chore: configure ruff and black
```

## Common Commit Types

| Type       | Use for                                          |
| ---------- | ------------------------------------------------ |
| `feat`     | New features                                     |
| `fix`      | Bug fixes                                        |
| `docs`     | Documentation only changes                       |
| `style`    | Code style/formatting changes (no logic changes) |
| `refactor` | Code changes that don’t fix bugs or add features |
| `test`     | Adding or updating tests                         |
| `chore`    | Routine tasks, tooling, dependencies, setup      |
| `build`    | Build system or dependency changes               |
| `ci`       | CI/CD pipeline changes                           |

## Closing Issues

Include this in the **commit body** to automatically close an issue when merged:

```
Closes #<issue-number>
```

### Example Full Commit Message

```
chore: configure ruff and black

- Added to requirements.txt
- Added .vscode/settings.json for integration

Closes #4
```

---

This file is part of the project's standards and procedures documentation.
