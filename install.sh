#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

usage() {
  cat <<'USAGE'
Usage:
  ./install.sh [install|uninstall] [options]

Defaults:
  ./install.sh
    installs change-lens for all supported Agent CLIs.

Examples:
  ./install.sh
  ./install.sh --force
  ./install.sh --agent codex
  ./install.sh install --agent claude --force
  ./install.sh uninstall --agent all

Options are passed through to scripts/manage-agent-install.py:
  --agent codex|claude|opencode|all
  --target <skills-dir>   valid only with one agent
  --force                 overwrite existing install
USAGE
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

ACTION="install"
if [[ "${1:-}" == "install" || "${1:-}" == "uninstall" ]]; then
  ACTION="$1"
  shift
fi

exec python3 "$ROOT_DIR/scripts/manage-agent-install.py" "$ACTION" --agent all "$@"
