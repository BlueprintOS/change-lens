# Audit Rules

Inputs:

- `.change-lens/change-manifest.json`
- `git diff --name-status`
- `git diff --numstat`

Checks:

1. Every changed file must match `allowed_files` and must not match `forbidden_files`.
2. Changed file count must be less than or equal to `expected_diff.max_files_changed` when set.
3. Added/deleted line counts must be within `expected_diff` when set.
4. If public symbols changed, require a refs rerun or list it as unchecked.
5. If no manifest exists, audit is inconclusive and coding should not proceed.

Passed template:

```markdown
## Change Scope Audit

**Result**: Passed

| File | Status | Authorized |
|---|---|---|
| src/orders/service.py | modified | yes |
```

Failed template:

```markdown
## Change Scope Audit

**Result**: Failed - scope escape detected

| File | Reason | Recommendation |
|---|---|---|
| src/common/date_utils.py | not in allowed_files | revert or request manifest expansion |
```
