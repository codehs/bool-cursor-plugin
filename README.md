# Bool for Cursor

Official [Cursor](https://cursor.com) and Grok Bot plugin for [Bool](https://bool.com).

This is a thin connector. It points at Bool's hosted Streamable HTTP MCP at `https://bool.com/api/mcp` and ships a skill for when to use those tools. It does not run an MCP server, wrap REST, or store API keys.

The plugin is free. The source is public. The license is MIT.

Listing on the Cursor Marketplace is free. The plugin collects no extra data beyond what Bool's official MCP and OAuth already handle. Users authenticate with Bool. This repo has no secrets. Bool does not use user content from this connector to train models.

## Terms and support

- [Bool Terms](https://bool.com/terms/)
- [Bool Privacy](https://bool.com/privacy/)
- [MCP docs](https://bool.com/docs/mcp)
- Support: [hello@bool.com](mailto:hello@bool.com)
- [Cursor Marketplace Publisher Terms](https://cursor.com/marketplace-publisher-terms)
- [Marketplace security](https://cursor.com/help/security-and-privacy/marketplace-security)

## Install

1. In Cursor: Customize / Marketplace → search **Bool** → Add.
2. In Grok Bot: Settings → Plugins → search **Bool** → Add.
3. Connect the `bool` MCP server and finish Bool OAuth.

Do not add headers, a `type` field, or a `BOOL_API_KEY` plugin variable. Cursor discovers OAuth from Bool's protected-resource metadata.

## Local test

Copy this folder to `~/.cursor/plugins/local/bool` and reload the window (Developer: Reload Window). Then connect `bool` and sign in with Bool.

```bash
cp -R . ~/.cursor/plugins/local/bool
```

On Teams and Enterprise, local plugin imports may be off until an admin allows them.

## Submit

Submit this public GitHub repo at [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish):

`https://github.com/codehs/bool-cursor-plugin`

Cursor reviews listings by hand. Open source is required. Updates are reviewed the same way. Pushes to this repo do not publish on their own.

## Layout

- `.cursor-plugin/plugin.json` — marketplace manifest
- `mcp.json` — url-only Bool MCP (`https://bool.com/api/mcp`)
- `skills/bool/SKILL.md` — when to use Bool tools
- `assets/logo.svg` — Bool mark
- `LICENSE` — MIT

## License

MIT. See [LICENSE](LICENSE).
