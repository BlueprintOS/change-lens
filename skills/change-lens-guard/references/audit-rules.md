# Audit Rules

Inputs:

- `.change-lens/change-manifest.json`
- manifest `baseline.git_head`
- manifest `baseline.preexisting_changed_files`
- `git diff --name-status`
- `git diff --numstat`
- evidence for required checks, usually command output summarized by the agent

Checks:

1. Split changed files into preexisting files from `baseline.preexisting_changed_files` and new changed files.
2. Every new changed file must match `allowed_files` and must not match `forbidden_files`.
3. New changed file count must be less than or equal to `expected_diff.max_files_changed` when set.
4. Added/deleted line counts for new changed files must be within `expected_diff` when set.
5. If public symbols changed, require a refs rerun or mark `symbol_scope` as `unchecked`.
6. Every `required_checks` item must be listed as run, skipped with reason, or unchecked.
7. If no manifest exists, audit is inconclusive unless the agent is performing an explicitly ephemeral audit-lite.

Result sections:

- `file_scope`: `passed`, `failed`, or `inconclusive`.
- `symbol_scope`: `checked`, `unchecked`, or `failed`.
- `checks`: `passed`, `skipped`, or `unchecked`.

Do not report an overall `Passed` when `file_scope` fails. Do not imply symbol-level safety when `symbol_scope` is `unchecked`.

Passed template:

```markdown
## Change Scope Audit

**Result**: Passed

### file_scope: passed

| File | Status | Authorized | Baseline |
|---|---|---|---|
| src/orders/service.py | modified | yes | new change |

### symbol_scope: unchecked

Public symbol refs were not rerun; list this as residual risk.

### checks: passed

| Check | Status | Evidence |
|---|---|---|
| run targeted tests | run | `pytest tests/orders/test_partial_process.py` passed |
```

Failed template:

```markdown
## Change Scope Audit

**Result**: Failed - scope escape detected

### file_scope: failed

| File | Reason | Recommendation |
|---|---|---|
| src/common/date_utils.py | not in allowed_files | revert or request manifest expansion |

### symbol_scope: unchecked

Skipped because file scope failed.

### checks: unchecked

Required checks were not trusted because the diff is out of scope.
```

Audit-lite template:

```markdown
## Change Scope Audit

**Result**: Audit-lite - no locked manifest

### file_scope: inconclusive

| File | Status | Ephemeral scope |
|---|---|---|
| src/orders/service.py | modified | listed in chat-only scope |

### symbol_scope: unchecked

No locked `allowed_symbols` list exists.

### checks: passed

| Check | Status | Evidence |
|---|---|---|
| run targeted tests | run | targeted test passed |
```
