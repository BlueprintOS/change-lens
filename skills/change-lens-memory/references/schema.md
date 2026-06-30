# Memory Schema

## IDs

- Project memory: `P-NNN`, for example `P-001`.
- Global memory: `P-G-NNN`, for example `P-G-001`.

## Entry Format

```markdown
### P-001 [2026-07-01 14:30]
- **Trigger scenario**: `/change-lens-report crosscheck --auto`
- **Failure**: Used a stale draft document.
- **Fix**: Provide the exact `--doc-path`.
- **Scope**: project
- **Trigger count**: 1
- **Last triggered**: 2026-07-01 14:30
```

## Add Flow

1. Parse the user's description.
2. Ask for any missing structured fields.
3. Recommend `global` or `project` scope.
4. Write only after confirmation.
5. Print the new id and path.

## Match Flow

Match exact command names first, then flag subsets, then keywords. Show concise reminders before execution:

```markdown
Warning: similar pitfall found [P-001]
- Scenario: `/change-lens-report crosscheck --auto`
- Fix: provide exact `--doc-path`.
```

Do not update `Trigger count` or `Last triggered` unless the user confirms recording this trigger.

## Prune Flow

Delete entries whose `Last triggered` is older than 90 days. If no timestamp exists, ask before deleting.
