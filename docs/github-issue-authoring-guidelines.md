# GitHub Issue Authoring Guidelines

This document outlines the conventions, best practices, and templates used when writing and maintaining GitHub issues for the `create_playlist.py` project.

Our goal is to keep issues clear, consistent, and actionable—ensuring they're useful for both current and future contributors (including future-you).

---

## Issue Structure Template

All issues should follow this structure:

```markdown
### Summary

A clear, one-paragraph overview of what the feature, bugfix, or enhancement does. Include the “why” if not obvious from context.

### Requirements

- [ ] Specific, testable expectations (bulleted checkbox list)
- [ ] Describe input behavior, edge cases, defaults, and failure states
- [ ] Describe user-visible behavior and CLI interactions (if any)

### Success Criteria

- [ ] Outcome-based checks that confirm completion
- [ ] Match CLI output or behavior to functional goals
- [ ] Include at least one behavioral example or test scenario

### Notes

- Optional section for design rationale, UX decisions, limitations, or future enhancements
- Include sample CLI output where appropriate
- Include tips for users or contributors (e.g., quoting multi-word values)
```

## Labels & Their Purpose

| Label           | Description                                             |
| --------------- | ------------------------------------------------------- |
| `feature`       | A new capability or CLI flag                            |
| `bug`           | A defect, crash, or incorrect behavior                  |
| `enhancement`   | A minor improvement to an existing feature              |
| `documentation` | Work related to usage docs, README, or CLI descriptions |
| `chore`         | Maintenance, cleanup, refactors, or CI/CD changes       |
| `question`      | Exploratory or clarification-focused tickets            |
| `help wanted`   | Flagged for possible outside contribution               |

## Best Practices

- Scope narrowly: One issue = one feature, fix, or concern
- Use checkboxes to clarify distinct implementation steps
- Use consistent terminology (`--format`, not `--extension`)
- Reference related issues when helpful (e.g., "Requires #2")
- Always assume CLI usage as the interface unless otherwise noted
- Include CLI output samples when the change impacts stdout

## Tone & Style

- Use direct, unambiguous language
- Write for clarity: Prefer explicit examples over abstract ideas
- Treat issue docs as an extension of the product—good UX applies here too

## Reuse & Refactor

- If you find yourself duplicating logic across filters, include a note to consolidate in a shared utility function
- Reuse applies not just to code, but to issue writing as well—copy and adapt templates where applicable