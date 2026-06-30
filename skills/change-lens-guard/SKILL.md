---
name: change-lens-guard
description: |
  Use when the user explicitly enters `/change-lens-guard plus a subcommand`, names `$change-lens-guard`, or asks for small, controlled, auditable production-code modifications. Converts locate results into a change manifest, locks allowed files/symbols, detects scope escape, and audits git diff after coding. Do not implement the code change directly as part of this skill; enforce boundaries and stop on unauthorized expansion.
---

# change-lens-guard

Turn code location findings into an auditable edit boundary. This skill constrains coding; it does not replace implementation or testing.

## Commands

- `plan <request>`: create a proposed change manifest from the request and locate results.
- `lock --from <manifest>`: write/confirm `.change-lens/change-manifest.json`.
- `audit`: compare actual git diff against the manifest.
- `explain-escape <file>`: explain why an out-of-scope file is needed and ask the user to expand scope.

Read `references/manifest-schema.md` for the manifest contract, `references/audit-rules.md` for diff checks, and `references/workflows.md` for the end-to-end safe edit flow.

## Hard Rules

1. Require location evidence before allowing production edits.
2. No file outside `allowed_files` may be modified without user confirmation.
3. No schema, migration, auth, common utility, or broad refactor work may be smuggled into a narrow manifest.
4. If implementation needs an out-of-scope file, stop and produce `explain-escape`.
5. After coding, run `audit` before final delivery.
6. If audit fails, mark delivery blocked until the user either reverts out-of-scope changes or approves a manifest expansion.

## Audit Output

Always classify the result as one of:

- Passed: all changed files and diff size are within the manifest.
- Failed: unauthorized files, symbols, or size limits detected.
- Inconclusive: no Git diff, missing manifest, or unavailable baseline.
