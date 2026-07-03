# Changelog

All notable changes to **change-lens** are documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/) and the project adheres to [Semantic Versioning](https://semver.org/).

---

## [1.1.0] — 2026-07-03

> **Small-change guardrail release.**
> Tightens the `change-lens-guard` workflow without adding a full CLI engine.

### Changed

- **Manifest baseline** — `change-manifest.json` examples now use `manifest_version: "1.1"` and record `baseline.git_head`, `baseline.created_at`, and `baseline.preexisting_changed_files` to avoid misclassifying dirty-worktree changes as new scope escapes.
- **Audit output** — guard audits now separate `file_scope`, `symbol_scope`, and `checks`, making symbol-level uncertainty explicit instead of implying full precision.
- **Lightweight edits** — `plan --ephemeral` documents a chat-only scope for low-risk small edits and reports the final result as audit-lite, not as a locked manifest audit.
- **Impact honesty** — `change-lens-locate impact` now requires `Confidence` and `Blind spots` so static impact estimates are not mistaken for complete call graphs.
- **Docs sync** — README and OpenCode companion instructions now describe the v1.1.0 workflow and audit wording.

### Notes

- This release remains documentation-contract only; it does not introduce a standalone executable `change-lens` CLI.
- The workflow remains domain-neutral and Agent CLI agnostic.

## [1.0.0] — 2026-06-30

> **Initial public release.**
> Four-skill Agent CLI skill collection for locating, scoping, auditing, and remembering code changes — domain-neutral, agent-CLI agnostic.

### Highlight

A single repo that installs four cooperating skills for any supported Agent CLI:

| Skill | Purpose |
|---|---|
| `change-lens-locate` | Read-only code location (`find`, `where`, `refs`, `impact`, `draft-concept`). |
| `change-lens-guard` | Production-change guardrails (`plan`, `lock`, `audit`, `explain-escape`) backed by `change-manifest.json`. |
| `change-lens-report` | Optional `.change-lens/` code-view reports, snapshot diffs, and document crosschecks. |
| `change-lens-memory` | Optional pitfall memory with pre-flight reminders. |

### Added

- **`change-lens-locate`** — read-only symbol/regex/concept lookup with concrete `file:line` output; degrades visibly when `ctags` / `tree-sitter` are missing.
- **`change-lens-guard`** — generates and locks a `change-manifest.json` of authorized files, then audits `git diff` against it; supports `explain-escape` to justify out-of-scope edits.
- **`change-lens-report`** — produces `.change-lens/{README,structure,symbols,entry-points}.md` and supports `--snapshot`/`--before`/`--after`/`--doc-path` for diff and crosscheck.
- **`change-lens-memory`** — global + project-level pitfall log with `--add` / `--list` / `--remove` / `--prune`; reminders are read-only by default.
- **Agent-CLI agnostic installer** (`install.sh` + `scripts/manage-agent-install.py`) supporting Codex, Claude, and OpenCode out of the box.
- **OpenCode companion template** at `templates/opencode/AGENTS.md` to bridge the four skills onto OpenCode's `AGENTS.md` entrypoint.
- **Bilingual README** (中文 + English) with install, uninstall, manual, and end-to-end workflow sections.
- **Repo hygiene**: `.gitignore`, `.gitattributes` (LF normalization), and an empty `.github/` folder for future community files.

### Design boundaries

- Domain-neutral: no real company, industry, customer, internal system, table, endpoint, or compliance knowledge.
- Explicit invocation: only responds when the active Agent CLI routes a `change-lens-*` skill.
- Scoped edits: locate → lock → code → audit.
- Graceful degradation: missing external tools do not block the workflow; precision is stated honestly.

### Notes

- No tags created in this commit. The `v1.0.0` cut is documented here for parity with future Git Releases.
- See `README.md` for end-to-end install and usage. The `.github/RELEASE_NOTES_v1.0.0.md` file carries the same narrative as a single, shareable artifact.

[1.1.0]: https://github.com/BlueprintOS/change-lens/releases/tag/v1.1.0
[1.0.0]: https://github.com/BlueprintOS/change-lens/releases/tag/v1.0.0
