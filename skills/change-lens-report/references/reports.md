# Reports

## Generated Files

- `.change-lens/README.md`: overview, project name, language hints, scan stats, entry summary.
- `.change-lens/structure.md`: directory tree and inferred directory purposes.
- `.change-lens/symbols.md`: symbol index grouped by file with kind, name, location, and summary.
- `.change-lens/entry-points.md`: HTTP routes, CLI commands, scheduled jobs, main functions, exported public entry points.
- `.change-lens/.last-scan.json`: metadata for version, timestamps, file mtimes, tool versions, and counts.

## Generate Behavior

1. Read `.change-lens.yaml` when present.
2. Exclude common generated/dependency directories.
3. Use ctags/tree-sitter when available and degrade visibly when missing.
4. Refuse to overwrite existing `.change-lens/` unless explicit confirmation or flag exists.
5. Print generated file list and scan statistics.

## Crosscheck Behavior

Extract from documents:

- Markdown headings as feature anchors.
- Backticked function/field names.
- HTTP paths.
- Table rows for entities and fields.

Compare both directions:

- Document to code: requirements with implementation locations or gaps.
- Code to document: public entry points with or without document coverage.

When coverage is low, warn rather than fail; documents may be stale or abstract.
