# change-lens for OpenCode

Use this file as an OpenCode project/global instruction companion for the change-lens skill folders installed under `skills/`.

## Available Commands

- `/change-lens-locate find|where|refs|impact|draft-concept`: read-only code location.
- `/change-lens-guard plan|lock|audit|explain-escape`: scoped production-change guardrails.
- `/change-lens-report generate|update|crosscheck|diff`: optional `.change-lens/` reports.
- `/change-lens-memory --add|--list|--remove|--prune`: optional pitfall memory.

## Operating Rules

1. Treat `skills/change-lens-*/SKILL.md` as the source of truth.
2. Load only the relevant `references/` file for the requested command.
3. Do not modify production code after locate; lock scope with `change-lens-guard` first.
4. Ask for document paths when crosschecking; do not guess document context.
5. Keep outputs concrete with `file:line` locations and visible degradation warnings.
