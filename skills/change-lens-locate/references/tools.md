# Tool Strategy

Prefer these tools in order:

- `rg`: baseline text search. Use fixed strings for literal symbols and globs for scope.
- `ctags`: symbol index for `find`, `where`, and `impact` precision.
- `tree-sitter`: syntax filtering for `refs` and call extraction for `impact`.
- direct file reads: context lines for `where` and summaries.

Degradation rules:

| Missing tool | Behavior |
|---|---|
| `rg` | Use `grep` only as a slow fallback and say so. |
| `ctags` | Fall back to file/text-level results and warn about lost symbol precision. |
| `tree-sitter` | Do not filter comments/strings; mark refs/impact as text-level. |

Large result rules:

- More than 50 hits: show first 20 grouped results and suggest `--in`.
- More than 30 seconds: stop, return partial data, and suggest `.change-lens.yaml`.
- Depth 2 explosion: cap recursive callers at 100 and ask the user to narrow scope.
