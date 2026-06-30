---
name: change-lens-report
description: |
  Use when the user explicitly enters `/change-lens-report plus a subcommand` or names `$change-lens-report`. Generates or updates optional `.change-lens/` code-view reports, crosschecks user-provided documents against code, and diffs report snapshots. Writes files only for generate, update, snapshot, or explicit crosscheck --output. Must ask for ambiguous document context instead of auto-guessing.
---

# change-lens-report

Generate persistent, reviewable reports. This skill is optional and separate from read-only locating.

## Commands

- `generate [path]`: create `.change-lens/README.md`, `structure.md`, `symbols.md`, `entry-points.md`, and `.last-scan.json`.
- `update`: incrementally refresh an existing `.change-lens/` view.
- `crosscheck`: compare explicitly provided documents with code.
- `diff --before <tag> --after <tag>`: compare two `.change-lens/archive/<tag>/` snapshots without relying on Git.

Read `references/reports.md` for generated file expectations. Read `references/snapshots.md` for update, versioning, and diff behavior.

## Context Confirmation Rules

1. If `generate` would overwrite `.change-lens/`, ask for explicit confirmation or require `--force`/`--merge`.
2. If `update` has no mode flag, ask the user to choose code-only or code-plus-docs.
3. If docs are required and no `--doc-path` is provided, ask the user for paths. Do not silently scan `docs/`.
4. `crosscheck --auto` is allowed only when the user explicitly passed `--auto`.
5. If the user cancels a prompt, exit without writing files.

## Persistence Rules

- `generate` and `update` write only under `.change-lens/` by default.
- `crosscheck` writes only with explicit `--output <file>`.
- `.change-lens/archive/` should usually be ignored by Git unless the user wants to keep snapshots.
