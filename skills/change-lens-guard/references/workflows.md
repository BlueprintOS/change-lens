# Safe Change Workflow

## Locked Workflow

1. Locate: use `change-lens-locate find`, `refs`, or `impact` to identify exact files and symbols.
2. Plan: use `change-lens-guard plan <request>` to draft allowed files, symbols, risks, and stop conditions.
3. Lock: write `.change-lens/change-manifest.json` only after the user confirms scope; include the current `git_head` and preexisting changed files in `baseline`.
4. Code: make the smallest change that satisfies one manifest item.
5. Escape: if a needed file is outside scope, stop and run `explain-escape <file>`.
6. Verify: run targeted tests or checks from the manifest.
7. Audit: run `change-lens-guard audit` and report `file_scope`, `symbol_scope`, and `checks` before final delivery.

## Ephemeral Workflow

Use `plan --ephemeral <request>` only for low-risk edits that are usually limited to two production files and do not touch schema, migrations, auth, shared utilities, or broad refactors.

1. Locate the target files and symbols.
2. State the chat-only allowed files, allowed symbols, checks, and stop conditions.
3. Code only within that chat-only scope.
4. Run targeted checks.
5. Run audit-lite against the stated scope and report that the result is not a locked manifest audit.

Escape explanation must include:

- requested file
- why existing allowed files are insufficient
- risk of expanding scope
- proposed manifest addition
- user confirmation request
