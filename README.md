# Bool plugin

The official plugin for [Bool](https://bool.com), which builds and publishes web apps from a description. Bool is operated by CodeHS, Inc.

The plugin connects an AI assistant to Bool's hosted MCP server at `https://bool.com/api/mcp` and adds a skill that tells the assistant how to use Bool's tools. It runs no server of its own and holds no secrets. Users sign in with their Bool account through OAuth. The license is MIT.

## Install

| Client | How |
|---|---|
| ChatGPT and Codex | Search **Bool** in the plugin directory once it's listed. |
| Cursor | Customize, then Marketplace, then search **Bool**. |
| Grok Build | Settings, then Plugins, then search **Bool**. |
| Any other MCP client | Add `https://bool.com/api/mcp` as a remote MCP server and sign in with Bool. |

## Layout

One repo serves every client. The shared parts follow the [Agent Plugins](https://agent-plugins.org) format, which ChatGPT, Codex, Cursor, VS Code and GitHub Copilot read directly. Each client that needs more gets a small file of its own.

| Path | Read by | Holds |
|---|---|---|
| `plugin.json` | Agent Plugins clients | Name, version, publisher. The OpenAI listing, review cases and release notes live under `extensions.com.openai`. |
| `mcp.json` | Agent Plugins clients | The `bool` server, over Streamable HTTP. |
| `skills/bool/SKILL.md` | Every client | When and how to use Bool's tools. |
| `assets/` | Every client | Icon, logo and wordmark. |
| `.cursor-plugin/plugin.json` | Cursor | Display name and logo. |
| `.claude-plugin/plugin.json`, `.mcp.json` | Claude Code, Grok Build | The same plugin in their manifest format. |

Keep the version the same in all three manifests. CI checks it.

## Release to the OpenAI plugin directory

```bash
scripts/build-openai-zip.sh
```

The script writes `dist/bool-<version>.zip` with only what OpenAI reads: `plugin.json`, `mcp.json`, `skills/`, `assets/`, `README.md` and `LICENSE`. Upload it from the Bool plugin's page in the OpenAI Platform with **Upload plugin to make changes**. The **Upload new or existing plugin** button on the Plugins list creates a separate plugin.

## Support

- [Terms](https://bool.com/terms)
- [Privacy](https://bool.com/privacy)
- [MCP docs](https://bool.com/docs/mcp)
- [hello@bool.com](mailto:hello@bool.com)
