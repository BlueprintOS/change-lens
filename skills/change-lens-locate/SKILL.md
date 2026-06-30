---
name: change-lens-locate
description: |
  Use only when the user explicitly enters `/change-lens-locate plus a subcommand` or names `$change-lens-locate`. Provides read-only, stateless code location commands: find symbols, identify context for file:line, list references, estimate 1-2 layer impact, and draft a concept card. Do not use for vague exploration, task planning, design review, or project/domain-specific knowledge.
---

# change-lens-locate

Provide read-only, real-time code location. Do not write files unless the user explicitly requests a `--json` output path for machine-readable locate results.

## Command Router

- `find <pattern>`: locate definitions for classes, functions, variables, or files.
- `where <file:line>`: identify the containing symbol and nearby context.
- `refs <symbol>`: find references, preferably filtering comments and strings when syntax tooling is available.
- `impact <file::func>`: show direct callers and callees; default to depth 1.
- `draft-concept <name>`: output a draft concept card to chat, not to disk.

Read `references/subcommands.md` for command-specific steps and output templates. Read `references/tools.md` before running tool-dependent searches. Read `references/project-config.md` when `.change-lens.yaml` exists or the project is large.

## Operating Rules

1. Require an explicit slash command. If the user only says "find code" or gives an unknown concept, suggest general exploration instead of invoking this skill.
2. Always output concrete `file:line` locations when hits exist.
3. Report three states clearly: hits, partial hits with caveats, or no hits with next-step suggestions.
4. Prefer `rg`; use ctags for symbol precision when available; use tree-sitter filtering when available.
5. If ctags or tree-sitter is missing, continue with a visible precision warning.
6. Do not assume any language, framework, company, industry, database, or domain model.
7. Keep examples domain-neutral (`orders`, `items`, `users`).
8. For production edits, stop after locating and recommend `/change-lens-guard` to lock scope.

## Minimal Workflow

1. Parse subcommand, required argument, and flags.
2. Load `.change-lens.yaml` if present; otherwise infer sources and excludes.
3. Run the narrowest search first.
4. Group, dedupe, truncate noisy results, and include caveats.
5. Finish with an actionable next command when useful.
