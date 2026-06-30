# Change Manifest Schema

Default path: `.change-lens/change-manifest.json`.

```json
{
  "manifest_version": "1.0",
  "task": "Fix order partial processing bug",
  "created_at": "2026-06-30T15:30:00+08:00",
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

Use neutral examples only. Replace sample names with project-specific names only when they come from the user's actual locate results.
