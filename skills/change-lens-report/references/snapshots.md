# Versioning, Updates, and Snapshots

## `.last-scan.json`

```json
{
  "version": "v1.3",
  "created_at": "2026-06-30T11:42:08+08:00",
  "previous_version": "v1.2",
  "files_scanned": 487,
  "symbols_total": 1243,
  "entry_points": 12,
  "file_mtimes": {},
  "tool_versions": {}
}
```

Version rules:

- `generate`: initialize `v1.0`.
- `update`: increment minor version.
- `generate --force`: increment major version and reset minor.
- `update --snapshot`: copy current `.change-lens/` to `.change-lens/archive/<tag-or-version>/` before updating.

## Update Modes

- Code-only: rescan code and update core report files.
- Code plus docs: code-only plus crosscheck for user-provided `--doc-path` values.
- Dry run: print planned changes and write nothing.

Never infer document paths for code-plus-docs mode unless the user explicitly supplied `--auto` for `crosscheck`.

## Diff

`diff --before <tag> --after <tag>` compares archived report files and groups changes into:

- added symbols
- removed symbols
- changed entry points
- impact-summary changes when available

If either tag is missing, fail visibly and list available archive tags.
