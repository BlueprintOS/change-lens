# change-lens skills

中文 | [English](#english)

`change-lens` 是一组通用 Agent CLI skills，用来把“我要找/改哪段代码”变成可定位、可约束、可审计的工作流。

- `change-lens-locate`：只读定位，支持 `find`、`where`、`refs`、`impact`、`draft-concept`。
- `change-lens-guard`：生产修改护栏，生成/锁定 `change-manifest.json`，审计 `git diff` 是否越界。
- `change-lens-report`：可选报告，生成/更新 `.change-lens/`，做文档交叉审核和快照 diff。
- `change-lens-memory`：可选踩坑记忆，记录通用经验并在下次类似命令前提醒。

## 支持的 Agent CLI

| Agent CLI | 支持方式 | 默认安装目录 |
|---|---|---|
| Codex | 原生 skill 目录，含 `SKILL.md` + `agents/codex.yaml` | `${CODEX_HOME:-~/.codex}/skills/` |
| Claude | 兼容 skill 目录，含 `SKILL.md` + `agents/claude.yaml` | `${CLAUDE_HOME:-~/.claude}/skills/` |
| OpenCode | skill 目录 + `AGENTS.change-lens.md` companion 文件 | `${OPENCODE_HOME:-~/.opencode}/skills/` |

> 说明：Codex 和 Claude 使用每个 skill 目录中的 `SKILL.md` 作为主要入口。OpenCode 通过同一套 skill 文件加 `templates/opencode/AGENTS.md` 生成的 companion 指令使用。

## 调用方式

`change-lens` 不绑定某一个 Agent CLI。使用时按当前工具支持的形式调用同一个 skill：

| Agent CLI | 推荐调用形式 |
|---|---|
| Codex | `$change-lens-locate`、`$change-lens-guard`、`$change-lens-report`、`$change-lens-memory`，或当前 Codex surface 支持的 `/change-lens-*` |
| Claude | `$change-lens-locate`、`$change-lens-guard`、`$change-lens-report`、`$change-lens-memory` |
| OpenCode | `/change-lens-locate`、`/change-lens-guard`、`/change-lens-report`、`/change-lens-memory` |

## 安装

### 从 GitHub 一键安装到全部 Agent CLI

```bash
git clone https://github.com/BlueprintOS/change-lens.git
cd change-lens
./install.sh
```

`install.sh` 默认执行 `install --agent all`。如果需要覆盖已有安装：

```bash
./install.sh --force
```

### 从 GitHub 只安装到某一个 Agent CLI

```bash
git clone https://github.com/BlueprintOS/change-lens.git
cd change-lens
./install.sh --agent codex
./install.sh --agent claude
./install.sh --agent opencode
```

如果已经 clone 过仓库，直接进入目录执行安装脚本即可：

```bash
cd change-lens
./install.sh
```

### 指定安装目录

`--target` 只能和单个 `--agent` 一起使用：

```bash
python3 scripts/manage-agent-install.py install --agent codex --target "$HOME/.codex/skills"
python3 scripts/manage-agent-install.py install --agent claude --target "$HOME/.claude/skills"
python3 scripts/manage-agent-install.py install --agent opencode --target "$HOME/.opencode/skills"
```

### 覆盖已有安装

```bash
./install.sh --force
```

### 更新到最新版并重新安装

```bash
cd change-lens
git pull
./install.sh --force
```

### 手动安装

如果不想运行安装脚本，也可以 clone 后手动复制：

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

## 卸载

### 从全部 Agent CLI 卸载

```bash
./install.sh uninstall --agent all
```

### 只从某一个 Agent CLI 卸载

```bash
python3 scripts/manage-agent-install.py uninstall --agent codex
python3 scripts/manage-agent-install.py uninstall --agent claude
python3 scripts/manage-agent-install.py uninstall --agent opencode
```

### 从指定目录卸载

```bash
python3 scripts/manage-agent-install.py uninstall --agent codex --target "$HOME/.codex/skills"
```

卸载会删除这些由本仓库安装的目录/文件：

- `change-lens-locate/`
- `change-lens-guard/`
- `change-lens-report/`
- `change-lens-memory/`
- OpenCode 额外文件：`AGENTS.change-lens.md`

## 使用手册

### 1. 定位代码：`/change-lens-locate`

适合“我知道要找什么，但不知道在哪”的场景。

```text
/change-lens-locate find Process
/change-lens-locate where src/orders/service.py:142
/change-lens-locate refs ORDER_ITEM_ID
/change-lens-locate impact src/orders/service.py::OrderService::process
/change-lens-locate draft-concept order-partial-process
```

行为约束：

- 默认只读，不写盘。
- 输出必须包含具体 `file:line`。
- 缺少 `ctags` 或 `tree-sitter` 时会降级，并明确提示精度下降。
- `impact` 是静态估算，必须输出 `Confidence` 和 `Blind spots`。
- 找不到时不会自动进入自由探索，只给下一步建议。

### 2. 锁定修改范围：`/change-lens-guard`

适合生产代码修改前后使用。

```text
/change-lens-guard plan "Fix order partial processing bug"
/change-lens-guard plan --ephemeral "Fix a one-file display bug"
/change-lens-guard lock --from .change-lens/change-manifest.json
/change-lens-guard audit
/change-lens-guard explain-escape src/common/date_utils.py
```

推荐流程：

1. 先用 `/change-lens-locate` 找入口、引用和影响面。
2. 用 `/change-lens-guard plan` 生成授权范围。
3. 用户确认后 `lock` 到 `.change-lens/change-manifest.json`。
4. 编码时只改 `allowed_files`。
5. 完成后运行 `/change-lens-guard audit`，按 `file_scope`、`symbol_scope`、`checks` 审计 diff。

小改路径：低风险、通常不超过 2 个生产文件且不涉及 schema、migration、auth、common utility 时，可以用 `plan --ephemeral` 在聊天中锁定临时范围；最终只能输出 audit-lite，不能声称已完成锁定 manifest 审计。

### 3. 生成代码视图报告：`/change-lens-report`

适合新接手项目、重构前留基线、PR 前审计结构变化。

```text
/change-lens-report generate
/change-lens-report update --code-only
/change-lens-report update --snapshot --tag before-chg-001
/change-lens-report diff --before before-chg-001 --after after-chg-001
/change-lens-report crosscheck --doc-path docs/prd/v1.2.md
```

生成的主文件：

- `.change-lens/README.md`
- `.change-lens/structure.md`
- `.change-lens/symbols.md`
- `.change-lens/entry-points.md`
- `.change-lens/.last-scan.json`

上下文原则：

- `generate` 遇到已有 `.change-lens/` 时默认不覆盖。
- `update` 默认必须询问“仅代码”还是“代码 + 文档”。
- 涉及文档时必须由用户提供 `--doc-path`，不能替用户猜测版本。

### 4. 记录踩坑：`/change-lens-memory`

适合沉淀通用经验，避免重复踩坑。

```text
/change-lens-memory --add "crosscheck --auto picked a stale draft document"
/change-lens-memory --list
/change-lens-memory --remove P-001
/change-lens-memory --prune
```

存储位置：

- 全局：当前 Agent CLI 的安装目录，例如 `${CODEX_HOME:-~/.codex}/skills/change-lens-memory/.memories.md`、`${CLAUDE_HOME:-~/.claude}/skills/change-lens-memory/.memories.md` 或 `${OPENCODE_HOME:-~/.opencode}/skills/change-lens-memory/.memories.md`
- 项目：`.change-lens/.memories.md`

写入原则：默认只读提醒；新增记录或更新触发次数必须先得到用户确认。

## 推荐端到端工作流

```text
/change-lens-locate find <known-symbol-or-concept>
/change-lens-locate impact <file::symbol>
/change-lens-guard plan "<task>"
/change-lens-guard lock --from .change-lens/change-manifest.json
# code within allowed files only
/change-lens-guard audit
# optional: /change-lens-report update --code-only
```

小改可用轻量路径：

```text
/change-lens-locate find <known-symbol-or-concept>
/change-lens-guard plan --ephemeral "<small task>"
# code within the chat-only scope only
/change-lens-guard audit
```

## 仓库结构

```text
skills/
  change-lens-locate/
  change-lens-guard/
  change-lens-report/
  change-lens-memory/
scripts/
  manage-agent-install.py
templates/
  opencode/AGENTS.md
```

## 设计边界

- 通用：不包含真实公司、行业、客户、业务域、表名、接口路径或合规知识。
- 显式触发：默认只响应当前 Agent CLI 支持的 change-lens 调用形式，例如 `/change-lens-*`、`$change-lens-*` 或命名 skill 调用。
- 小步受控：生产修改必须先定位，再锁范围，再编码，最后审计。
- 可降级：缺少外部工具时继续工作，但必须说明精度下降。

---

# English

`change-lens` is a general-purpose Agent CLI skill collection for turning “where is this code?” and “how do I change it safely?” into a locatable, scoped, and auditable workflow.

- `change-lens-locate`: read-only location commands: `find`, `where`, `refs`, `impact`, and `draft-concept`.
- `change-lens-guard`: production-change guardrails with `change-manifest.json` and `git diff` audits.
- `change-lens-report`: optional `.change-lens/` reports, updates, document crosschecks, and snapshot diffs.
- `change-lens-memory`: optional pitfall memory with pre-flight reminders.

## Supported Agent CLIs

| Agent CLI | Support mode | Default install directory |
|---|---|---|
| Codex | Native skill folder with `SKILL.md` + `agents/codex.yaml` | `${CODEX_HOME:-~/.codex}/skills/` |
| Claude | Compatible skill folder with `SKILL.md` + `agents/claude.yaml` | `${CLAUDE_HOME:-~/.claude}/skills/` |
| OpenCode | Skill folder plus `AGENTS.change-lens.md` companion instructions | `${OPENCODE_HOME:-~/.opencode}/skills/` |

## Invocation

`change-lens` is not bound to a single Agent CLI. Invoke the same skill through the form supported by the active tool:

| Agent CLI | Recommended invocation form |
|---|---|
| Codex | `$change-lens-locate`, `$change-lens-guard`, `$change-lens-report`, `$change-lens-memory`, or `/change-lens-*` when supported by the active Codex surface |
| Claude | `$change-lens-locate`, `$change-lens-guard`, `$change-lens-report`, `$change-lens-memory` |
| OpenCode | `/change-lens-locate`, `/change-lens-guard`, `/change-lens-report`, `/change-lens-memory` |

## Install

### Install from GitHub for all supported Agent CLIs

```bash
git clone https://github.com/BlueprintOS/change-lens.git
cd change-lens
./install.sh
```

`install.sh` runs `install --agent all` by default. To overwrite an existing install:

```bash
./install.sh --force
```

### Install from GitHub for one Agent CLI

```bash
git clone https://github.com/BlueprintOS/change-lens.git
cd change-lens
./install.sh --agent codex
./install.sh --agent claude
./install.sh --agent opencode
```

If you already cloned the repository, enter it and run the installer directly:

```bash
cd change-lens
./install.sh
```

### Install into a custom directory

`--target` is valid only with a single `--agent`:

```bash
python3 scripts/manage-agent-install.py install --agent codex --target "$HOME/.codex/skills"
python3 scripts/manage-agent-install.py install --agent claude --target "$HOME/.claude/skills"
python3 scripts/manage-agent-install.py install --agent opencode --target "$HOME/.opencode/skills"
```

### Overwrite an existing install

```bash
./install.sh --force
```

### Update to the latest version and reinstall

```bash
cd change-lens
git pull
./install.sh --force
```

### Manual install

If you prefer not to run the installer, clone the repository and copy the files manually:

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

## Uninstall

### Uninstall from all supported Agent CLIs

```bash
./install.sh uninstall --agent all
```

### Uninstall from one Agent CLI

```bash
python3 scripts/manage-agent-install.py uninstall --agent codex
python3 scripts/manage-agent-install.py uninstall --agent claude
python3 scripts/manage-agent-install.py uninstall --agent opencode
```

### Uninstall from a custom directory

```bash
python3 scripts/manage-agent-install.py uninstall --agent codex --target "$HOME/.codex/skills"
```

Uninstall removes the four installed `change-lens-*` skill folders. For OpenCode it also removes `AGENTS.change-lens.md`.

## User Manual

### 1. Locate Code: `/change-lens-locate`

Use it when you know what you are looking for, but not where it lives.

```text
/change-lens-locate find Process
/change-lens-locate where src/orders/service.py:142
/change-lens-locate refs ORDER_ITEM_ID
/change-lens-locate impact src/orders/service.py::OrderService::process
/change-lens-locate draft-concept order-partial-process
```

Rules:

- Read-only by default.
- Output concrete `file:line` locations.
- If `ctags` or `tree-sitter` is missing, degrade visibly.
- `impact` is a static estimate and must include `Confidence` and `Blind spots`.
- On no hits, suggest next steps instead of starting broad exploration automatically.

### 2. Guard the Change Scope: `/change-lens-guard`

Use it before and after production-code changes.

```text
/change-lens-guard plan "Fix order partial processing bug"
/change-lens-guard plan --ephemeral "Fix a one-file display bug"
/change-lens-guard lock --from .change-lens/change-manifest.json
/change-lens-guard audit
/change-lens-guard explain-escape src/common/date_utils.py
```

Recommended flow:

1. Use `/change-lens-locate` to find entry points, references, and impact.
2. Use `/change-lens-guard plan` to draft the authorized scope.
3. Lock the scope into `.change-lens/change-manifest.json` after user confirmation.
4. Code only inside `allowed_files`.
5. Run `/change-lens-guard audit` before delivery, reporting `file_scope`, `symbol_scope`, and `checks`.

Small-change path: for low-risk edits that usually touch no more than two production files and do not involve schema, migrations, auth, or common utilities, use `plan --ephemeral` to state a chat-only scope. The final result is audit-lite only; do not claim a locked manifest audit.

### 3. Generate Code-View Reports: `/change-lens-report`

Use it for onboarding, pre-refactor baselines, and reviewable code-view diffs.

```text
/change-lens-report generate
/change-lens-report update --code-only
/change-lens-report update --snapshot --tag before-chg-001
/change-lens-report diff --before before-chg-001 --after after-chg-001
/change-lens-report crosscheck --doc-path docs/prd/v1.2.md
```

Main generated files:

- `.change-lens/README.md`
- `.change-lens/structure.md`
- `.change-lens/symbols.md`
- `.change-lens/entry-points.md`
- `.change-lens/.last-scan.json`

Context rules:

- `generate` does not overwrite existing `.change-lens/` by default.
- `update` must ask whether to use code-only or code-plus-docs mode when no mode flag is present.
- Document crosschecks require user-provided `--doc-path`; do not guess document versions.

### 4. Record Pitfalls: `/change-lens-memory`

Use it to preserve reusable lessons and avoid repeated mistakes.

```text
/change-lens-memory --add "crosscheck --auto picked a stale draft document"
/change-lens-memory --list
/change-lens-memory --remove P-001
/change-lens-memory --prune
```

Storage:

- Global: the active Agent CLI install directory, for example `${CODEX_HOME:-~/.codex}/skills/change-lens-memory/.memories.md`, `${CLAUDE_HOME:-~/.claude}/skills/change-lens-memory/.memories.md`, or `${OPENCODE_HOME:-~/.opencode}/skills/change-lens-memory/.memories.md`
- Project: `.change-lens/.memories.md`

Write rule: reminders are read-only by default; adding records or updating trigger counts requires user confirmation.

## Recommended End-to-End Flow

```text
/change-lens-locate find <known-symbol-or-concept>
/change-lens-locate impact <file::symbol>
/change-lens-guard plan "<task>"
/change-lens-guard lock --from .change-lens/change-manifest.json
# code within allowed files only
/change-lens-guard audit
# optional: /change-lens-report update --code-only
```

Small edits may use the lightweight path:

```text
/change-lens-locate find <known-symbol-or-concept>
/change-lens-guard plan --ephemeral "<small task>"
# code within the chat-only scope only
/change-lens-guard audit
```

## Repository Layout

```text
skills/
  change-lens-locate/
  change-lens-guard/
  change-lens-report/
  change-lens-memory/
scripts/
  manage-agent-install.py
templates/
  opencode/AGENTS.md
```

## Boundaries

- Domain-neutral: no real company, industry, customer, private system, table, endpoint, or compliance knowledge.
- Explicit trigger: defaults to the active Agent CLI's supported change-lens invocation form, such as `/change-lens-*`, `$change-lens-*`, or named skill calls.
- Scoped changes: locate first, lock scope second, code third, audit last.
- Graceful degradation: continue when external tools are missing, but state precision loss.
