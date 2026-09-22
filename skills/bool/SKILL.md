---
name: bool
description: >
  Use when creating, listing, building, publishing, remixing, or managing Bool
  apps and projects. Also use when the user mentions Bool, bool.com, a live Bool
  URL, or deploying a generated app through Bool. Prefer Bool MCP tools over
  guessing the dashboard.
---

# Bool

Connect your client to Bool through this plugin's MCP server at `https://bool.com/api/mcp`, then drive workspaces and projects with the official tools.

Docs: [bool.com/docs/mcp](https://bool.com/docs/mcp)

## Connect

1. Enable this plugin's `bool` MCP server in your client (Grok Build, Cursor, or any MCP client).
2. Complete Bool OAuth. The connector URL is `https://bool.com/api/mcp`. Protected-resource metadata lives at `https://bool.com/.well-known/oauth-protected-resource`.
3. Do not add a second Bool MCP server. Do not paste a personal MCP URL. Do not put API keys or tokens in this plugin.

## First calls

Call `list_workspaces`, then `list_projects`. Pass `workspace_id` when the user wants one workspace. Do not invent workspace or project ids.

## Build and iterate

- New app: `create_project` with a `prompt`, then poll `get_project_status` until the turn finishes and `live_url` is set.
- Blank project: `create_project` without a `prompt`, then `prompt_project` or `publish_project`.
- Iterate: `prompt_project`, then poll `get_project_status`.
- Templates: `list_templates` before passing `template` to `create_project`.
- Remix: `fork_project` (user-facing word is remix). Then `prompt_project` if they want changes.
- Rename, description, or visibility: `update_project`. Visibility on an existing project can also go through `get_project`.
- Move across workspaces: `move_project` (owner only).
- Local backend link: `get_project_connection`. If `include_api_key` is true, the admin data key is owner-only. Never commit it.

## Safety

Confirm with the user before `delete_project` or `delete_record`. Both are permanent.

Record tools (`list_records`, `create_records`, `update_record`, `delete_record`) run as the project admin. They see and change every row, including every end-user's rows on a private entity. Treat them as admin-level. On a private entity, `create_records` needs `owner_id` on each row.

`define_entity` is additive. It creates a table or adds missing columns. It does not drop columns or change types.

## Live tools

Use only these names. Do not invent tools.

- `create_project`
- `create_records`
- `define_entity`
- `delete_project`
- `delete_record`
- `fork_project`
- `get_project`
- `get_project_connection`
- `get_project_status`
- `list_entities`
- `list_projects`
- `list_records`
- `list_templates`
- `list_workspaces`
- `move_project`
- `prompt_project`
- `publish_project`
- `update_project`
- `update_record`
