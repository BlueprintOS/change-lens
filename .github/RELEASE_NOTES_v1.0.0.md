# Release Notes — v1.0.0 (2026-06-30)

> First public release of **change-lens** — a four-skill collection for Agent CLIs that turns *"where is this code?"* and *"how do I change it safely?"* into a locatable, scoped, and auditable workflow.

---

## TL;DR

`change-lens` ships four cooperating skills plus a one-shot installer for **Codex**, **Claude**, and **OpenCode**. It is **domain-neutral** — it contains no company, industry, customer, internal system, table, endpoint, or compliance knowledge — and it is **agent-CLI agnostic**: the same skill files are dispatched through whichever surface the active CLI exposes (`/change-lens-*`, `$change-lens-*`, or named skill calls).

```bash
git clone https://github.com/BlueprintOS/change-lens.git
cd change-lens
./install.sh
```

By default the installer registers `change-lens-*` with every supported Agent CLI. Use `--agent codex|claude|opencode|all` to scope it, and `--force` to overwrite an existing install. Use `uninstall` to remove the four installed skill folders (and `AGENTS.change-lens.md` for OpenCode).

---

## What's in the box

| Skill | Job to be done | Main commands |
|---|---|---|
| `change-lens-locate` | Read-only code location. | `find`, `where`, `refs`, `impact`, `draft-concept` |
| `change-lens-guard` | Production-change guardrails. | `plan`, `lock`, `audit`, `explain-escape` |
| `change-lens-report` | Code-view reports, snapshot diffs, document crosschecks. | `generate`, `update`, `diff`, `crosscheck` |
| `change-lens-memory` | Reusable pitfall memory with pre-flight reminders. | `--add`, `--list`, `--remove`, `--prune` |

### Recommended end-to-end flow

```text
/change-lens-locate find <known-symbol-or-concept>
/change-lens-locate impact <file::symbol>
/change-lens-guard plan "<task>"
/change-lens-guard lock --from .change-lens/change-manifest.json
# Code strictly inside allowed_files
/change-lens-guard audit
/change-lens-report update --code-only
```

---

## Highlights

- **One installer, three CLIs.** `./install.sh` handles Codex, Claude, and OpenCode from a single entrypoint; the Python helper behind it (`scripts/manage-agent-install.py`) is also exposed for direct use.
- **OpenCode bridge.** `templates/opencode/AGENTS.md` materializes a `AGENTS.change-lens.md` companion file under the OpenCode install directory so the four skills become first-class capabilities on OpenCode as well.
- **Honest degradation.** Skills keep working when `ctags` or `tree-sitter` are missing — they just call out the precision loss.
- **Scoping before edits.** `change-lens-guard` requires a `change-manifest.json` of `allowed_files` before coding, and an `audit` step after — guarding production edits against silent scope creep.
- **Memory by confirmation.** `change-lens-memory` writes only after user confirmation; otherwise it only surfaces existing pitfalls as pre-flight reminders.

---

## Installation

### All Agent CLIs at once

```bash
git clone https://github.com/BlueprintOS/change-lens.git
cd change-lens
./install.sh
```

### One Agent CLI at a time

```bash
./install.sh --agent codex
./install.sh --agent claude
./install.sh --agent opencode
```

### Overwrite, custom target, uninstall

```bash
./install.sh --force                                                  # overwrite existing install
python3 scripts/manage-agent-install.py install --agent codex \
    --target "$HOME/.codex/skills"                                    # custom install dir
./install.sh uninstall --agent all                                   # remove every install
```

### Manual install (no script)

```bash
git clone https://github.com/BlueprintOS/change-lens.git
cd change-lens

mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/change-lens-* "${CODEX_HOME:-$HOME/.codex}/skills/"

mkdir -p "${CLAUDE_HOME:-$HOME/.claude}/skills"
cp -R skills/change-lens-* "${CLAUDE_HOME:-$HOME/.claude}/skills/"

mkdir -p "${OPENCODE_HOME:-$HOME/.opencode}/skills"
cp -R skills/change-lens-* "${OPENCODE_HOME:-$HOME/.opencode}/skills/"
cp templates/opencode/AGENTS.md "${OPENCODE_HOME:-$HOME/.opencode}/AGENTS.change-lens.md"
```

See the full README for env-var conventions (`CODEX_HOME` / `CLAUDE_HOME` / `OPENCODE_HOME`) and uninstall paths.

---

## Compatibility

- **Codex** — relies on the native skill directory (`${CODEX_HOME:-$HOME/.codex}/skills/`). Each skill ships `SKILL.md` plus `agents/codex.yaml`.
- **Claude** — compatible skill directory (`${CLAUDE_HOME:-$HOME/.claude}/skills/`). Each skill ships `SKILL.md` plus `agents/claude.yaml`.
- **OpenCode** — `${OPENCODE_HOME:-$HOME/.opencode}/skills/` plus the generated `AGENTS.change-lens.md` companion.
- No external services, network calls, or binaries are required. `ctags` / `tree-sitter` are optional and only improve precision.

---

## Known limitations

- Skill content is bilingual in the README only; the skill files themselves are English-first.
- Snapshot diff and document crosscheck require the user to supply the snapshot tag or `--doc-path`; they are deliberately not guessed.
- `change-manifest.json` files are local to each repo; there is no cross-repo lock coordination.

---

## Upgrade notes

There is no prior version. Upgrading only applies on re-installation:

```bash
cd change-lens
git pull
./install.sh --force
```

---

## Acknowledgements

Built and curated by **Jason SUN** under MIT for the community to use, fork, and adapt without domain-specific assumptions.
