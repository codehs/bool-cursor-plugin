"""Checks the manifests agree with each other and the skill is well formed."""
import json
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parent.parent
errors = []

manifests = ["plugin.json", ".cursor-plugin/plugin.json", ".claude-plugin/plugin.json"]
versions = {m: json.loads((root / m).read_text())["version"] for m in manifests}
if len(set(versions.values())) != 1:
    errors.append(f"versions differ: {versions}")

names = {m: json.loads((root / m).read_text())["name"] for m in manifests}
if len(set(names.values())) != 1:
    errors.append(f"names differ: {names}")

for mcp in ["mcp.json", ".mcp.json"]:
    servers = json.loads((root / mcp).read_text())["mcpServers"]
    if list(servers) != ["bool"] or servers["bool"]["url"] != "https://bool.com/api/mcp":
        errors.append(f"{mcp} must declare exactly the bool server at https://bool.com/api/mcp")

skill = (root / "skills/bool/SKILL.md").read_text()
front = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
if not front or "name: bool" not in front.group(1) or "description:" not in front.group(1):
    errors.append("skills/bool/SKILL.md needs name and description front matter")

interface = json.loads((root / "plugin.json").read_text())["extensions"]["com.openai"]["interface"]
for key in ["composerIcon", "logo"]:
    if not (root / interface[key]).is_file():
        errors.append(f"plugin.json {key} points at a missing file: {interface[key]}")

for e in errors:
    print(f"error: {e}", file=sys.stderr)
sys.exit(1 if errors else 0)
