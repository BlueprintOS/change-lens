#!/usr/bin/env python3
"""Install or uninstall change-lens skills for supported agent CLIs."""

from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path

SKILL_NAMES = [
    "change-lens-locate",
    "change-lens-guard",
    "change-lens-report",
    "change-lens-memory",
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def default_target(agent: str) -> Path:
    home = Path.home()
    if agent == "codex":
        return Path(os.environ.get("CODEX_HOME", home / ".codex")) / "skills"
    if agent == "claude":
        return Path(os.environ.get("CLAUDE_HOME", home / ".claude")) / "skills"
    if agent == "opencode":
        return Path(os.environ.get("OPENCODE_HOME", home / ".opencode")) / "skills"
    raise ValueError(f"unsupported agent: {agent}")


def copy_skill(src: Path, dst: Path, *, force: bool) -> None:
    if dst.exists():
        if not force:
            raise SystemExit(f"Refusing to overwrite existing skill: {dst}. Re-run with --force.")
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def install_agent(agent: str, target: Path, *, force: bool) -> None:
    root = repo_root()
    skills_dir = root / "skills"
    target.mkdir(parents=True, exist_ok=True)

    for name in SKILL_NAMES:
        copy_skill(skills_dir / name, target / name, force=force)

    if agent == "opencode":
        template = root / "templates" / "opencode" / "AGENTS.md"
        agent_file = target.parent / "AGENTS.change-lens.md"
        if agent_file.exists() and not force:
            raise SystemExit(f"Refusing to overwrite existing file: {agent_file}. Re-run with --force.")
        shutil.copyfile(template, agent_file)

    print(f"Installed change-lens skills for {agent} at {target}")


def uninstall_agent(agent: str, target: Path, *, force: bool) -> None:
    removed = []
    for name in SKILL_NAMES:
        dst = target / name
        if dst.exists():
            shutil.rmtree(dst)
            removed.append(str(dst))

    if agent == "opencode":
        agent_file = target.parent / "AGENTS.change-lens.md"
        if agent_file.exists():
            agent_file.unlink()
            removed.append(str(agent_file))

    if not removed and not force:
        print(f"No change-lens files found for {agent} at {target}")
        return

    print(f"Uninstalled change-lens files for {agent}:")
    for path in removed:
        print(f"- {path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install or uninstall change-lens skills.")
    parser.add_argument("action", choices=["install", "uninstall"], help="operation to perform")
    parser.add_argument("--agent", choices=["codex", "claude", "opencode", "all"], default="all")
    parser.add_argument("--target", type=Path, help="override target skills directory; valid only with one agent")
    parser.add_argument("--force", action="store_true", help="overwrite on install; ignore empty uninstall")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    agents = ["codex", "claude", "opencode"] if args.agent == "all" else [args.agent]
    if args.target and len(agents) != 1:
        raise SystemExit("--target can only be used when --agent is codex, claude, or opencode")

    for agent in agents:
        target = args.target or default_target(agent)
        if args.action == "install":
            install_agent(agent, target, force=args.force)
        else:
            uninstall_agent(agent, target, force=args.force)


if __name__ == "__main__":
    main()
