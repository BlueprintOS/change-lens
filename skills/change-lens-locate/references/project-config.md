# Project Configuration

Optional config path: `.change-lens.yaml` in the project root.

```yaml
sources:
  - src/
  - lib/
exclude:
  - "**/node_modules/**"
  - "**/build/**"
  - "**/.git/**"
  - "**/dist/**"
  - "**/__pycache__/**"
  - "**/vendor/**"
language: python
entry_points:
  - src/main.py
```

Priority order:

1. Explicit command flags such as `--in` or `--lang`.
2. `.change-lens.yaml`.
3. Built-in defaults.

Built-in source candidates: `src/`, `lib/`, `pkg/`, `cmd/`, `app/`, `internal/`.

Built-in excludes: `.git/`, `node_modules/`, `build/`, `target/`, `dist/`, `__pycache__/`, `venv/`, `.venv/`, `vendor/`.
