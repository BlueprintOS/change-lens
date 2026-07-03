# Change Manifest Schema

Default path: `.change-lens/change-manifest.json`.

```json
{
  "manifest_version": "1.1",
  "task": "Fix order partial processing bug",
  "created_at": "2026-06-30T15:30:00+08:00",
  "baseline": {
    "git_head": "abc1234",
    "created_at": "2026-06-30T15:30:00+08:00",
    "preexisting_changed_files": [
      "docs/notes.md"
    ]
  },
  "allowed_files": [
    "src/orders/service.py",
    "tests/orders/test_partial_process.py"
  ],
  "allowed_symbols": [
    "OrderProcessService::process_partial"
  ],
  "forbidden_files": [
    "src/auth/**",
    "src/common/**",
    "migrations/**"
  ],
  "expected_diff": {
    "max_files_changed": 3,
    "max_added_lines": 120,
    "max_deleted_lines": 80
  },
  "required_checks": [
    "run targeted tests",
    "rerun refs for changed public symbols",
    "audit diff within allowed_files"
  ],
  "stop_conditions": [
    "need to edit a file outside allowed_files",
    "need schema or migration changes",
    "impact expands beyond listed callers",
    "tests require broad unrelated rewrites"
  ]
}
```

`baseline` records the repository state at lock time. During audit, files listed in `preexisting_changed_files` are reported separately and are not counted as new scope escapes unless their diff changed after lock time can be proven.

Use neutral examples only. Replace sample names with project-specific names only when they come from the user's actual locate results.
