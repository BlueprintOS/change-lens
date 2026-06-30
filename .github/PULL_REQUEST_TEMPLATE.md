<!--
Thanks for contributing to change-lens!
Please fill in the sections below. Sections marked *optional* may be deleted.
-->

## Summary

<!-- One short paragraph: what this PR does and why. -->

## Type of change

- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds a skill, subcommand, or option)
- [ ] Breaking change (existing behavior changes — explain in "Migration")
- [ ] Documentation / wording only
- [ ] Refactor without behavior change
- [ ] CI / tooling change

## Skills touched

- [ ] `change-lens-locate`
- [ ] `change-lens-guard`
- [ ] `change-lens-report`
- [ ] `change-lens-memory`
- [ ] Installer (`install.sh` / `scripts/manage-agent-install.py`)
- [ ] OpenCode companion (`templates/opencode/AGENTS.md`)
- [ ] None of the above

## Agent CLIs affected

- [ ] Codex
- [ ] Claude
- [ ] OpenCode
- [ ] None

## How I verified this

<!-- Required. Replace with the actual commands you ran and their outcomes. -->

```bash
# Replace with the commands you actually executed, e.g.:
./install.sh --agent codex
./install.sh --agent claude
./install.sh --agent opencode
./install.sh uninstall --agent all
python3 -m py_compile scripts/manage-agent-install.py
bash -n install.sh
```

## Boundary check

`change-lens` is domain-neutral. Confirm:

- [ ] No real company, industry, customer, internal system, table, endpoint, or compliance knowledge was added.
- [ ] No proprietary data, real credentials, or PII are committed.
- [ ] Output still names concrete `file:line` locations when applicable.
- [ ] Skills still degrade visibly when optional tools (`ctags`, `tree-sitter`) are absent.

## Migration notes

<!-- Only for breaking changes. Otherwise delete this section. -->

## Linked issues

<!-- `Closes #NNN`, `Fixes #NNN`, or `Refs #NNN`. Delete if not applicable. -->
