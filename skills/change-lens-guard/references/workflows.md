# Safe Change Workflow

1. Locate: use `change-lens-locate find`, `refs`, or `impact` to identify exact files and symbols.
2. Plan: use `change-lens-guard plan <request>` to draft allowed files, symbols, risks, and stop conditions.
3. Lock: write `.change-lens/change-manifest.json` only after the user confirms scope.
4. Code: make the smallest change that satisfies one manifest item.
5. Escape: if a needed file is outside scope, stop and run `explain-escape <file>`.
6. Verify: run targeted tests or checks from the manifest.
7. Audit: run `change-lens-guard audit` and report pass/fail before final delivery.

Escape explanation must include:

- requested file
- why existing allowed files are insufficient
- risk of expanding scope
- proposed manifest addition
- user confirmation request
