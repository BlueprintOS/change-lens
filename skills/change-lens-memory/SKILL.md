---
name: change-lens-memory
description: |
  Use when the user explicitly enters `/change-lens-memory plus flags`, names `$change-lens-memory`, or asks to record/list/remove/prune reusable lessons from change-lens usage. Maintains optional global and project pitfall memories, reminds before matching commands, and writes only after explicit user confirmation.
---

# change-lens-memory

Record reusable pitfalls so future change-lens commands can warn before repeating them.

## Commands

- `--add <description>`: structure and record a pitfall after user confirmation.
- `--list`: show merged global and project memories.
- `--remove <id>`: delete a memory by id.
- `--prune`: remove records not triggered for more than 90 days.

Read `references/schema.md` before adding, updating, removing, or pruning memories.

## Storage

- Global: `${CODEX_HOME:-~/.codex}/skills/change-lens-memory/.memories.md`
- Project: `.change-lens/.memories.md`

Global memories are private and should not be committed. Project memories may be committed if the team wants shared reminders.

## Rules

1. Before any change-lens command, matching memories may be read and shown as reminders.
2. Updating trigger counts or timestamps requires user confirmation.
3. Adding a record requires structured fields: trigger scenario, failure, fix, and scope.
4. Default to project scope for project-specific paths or conventions; default to global for generic tool behavior.
5. Never store private company, customer, credential, or regulated data unless the user explicitly includes it and confirms scope.
