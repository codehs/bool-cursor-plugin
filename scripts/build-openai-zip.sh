#!/usr/bin/env bash
# Builds the ZIP for the OpenAI plugin directory from the committed files.
# OpenAI reads the Agent Plugins package only, so the Cursor and Claude Code
# overlays stay out of it.
set -euo pipefail
cd "$(dirname "$0")/.."

version=$(python3 -c 'import json; print(json.load(open("plugin.json"))["version"])')
out="dist/bool-${version}.zip"

if [ -n "$(git status --porcelain -- plugin.json mcp.json skills assets README.md LICENSE)" ]; then
  echo "Commit your changes first: the ZIP is built from HEAD." >&2
  exit 1
fi

mkdir -p dist
rm -f "$out"
git archive --format=zip -o "$out" HEAD plugin.json mcp.json skills assets README.md LICENSE
echo "$out"
