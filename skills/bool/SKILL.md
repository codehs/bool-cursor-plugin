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

1. Enable this plugin's `bool` MCP server in your client.
2. Complete Bool OAuth. The connector URL is `https://bool.com/api/mcp`. Protected-resource metadata lives at `https://bool.com/.well-known/oauth-protected-resource`.
3. Do not add a second Bool MCP server. Do not paste a personal MCP URL. Do not put API keys or tokens in this plugin.

## First calls

Call `list_workspaces`, then `list_projects`. Pass `workspace_id` when the user wants one workspace. Do not invent workspace or project ids.

## Build and iterate

You build the app yourself. Bool's own AI runs only when the user asks for it.

- New app: `create_project` makes a blank project from a starter template. It takes only `name`, `template`, `workspace_id`, and `visibility`, and defaults to the workspace chosen in Bool's settings. A created project is an empty starter until `build_app` passes.
- Build: `get_build_guide` for that `project_id`, and follow it. Read and edit with `list_files`, `read_file`, `create_file`, and `edit_file`. Use `delete_file`, `run_command`, `define_entity`, and `run_db_migration` when the guide calls for them. Run `build_app` until it passes, then `save_version`.
- Iterate: the same loop on the existing project. Read its files first. Do not create a new project.
- Publish: `publish_project` only when the user wants the app live.
- Bool's AI: when the user asks for it, `prompt_project` on an existing project, then poll `get_project_status` until the turn finishes. `cancel_project_turn` stops it.
- Images: `add_image` saves an image the user shared, or one you generated, into the project's files. `set_project_icon` makes an image the app's icon.
- Templates: `list_templates` before passing `template` to `create_project`.
- Remix: `fork_project` (user-facing word is remix). Then the build loop if they want changes.
- Show projects: `open_bool_editor`. In clients that can't show the Bool editor, `render_project_widget` shows a status card.
- Rename, description, or visibility: `update_project`.
- Move across workspaces: `move_project` (owner only).
- Local backend link: `get_project_connection`. It returns only the public connection details. Admin data keys are created in Bool's project settings, never through the conversation.

## Safety

Confirm with the user before `delete_project` or `delete_record`. Both are permanent.

Record tools (`list_records`, `create_records`, `update_record`, `delete_record`) run as the project admin. They see and change every row, including every end-user's rows on a private entity. Treat them as admin-level. On a private entity, `create_records` needs `owner_id` on each row.

`define_entity` is additive. It creates a table or adds missing columns. It does not drop columns or change types.

`run_db_migration` runs SQL on the project's database. Confirm with the user before SQL that drops or rewrites data.

## Live tools

Use only these names. Do not invent tools.

- `add_image`
- `build_app`
- `cancel_project_turn`
- `create_file`
- `create_project`
- `create_records`
- `define_entity`
- `delete_file`
- `delete_project`
- `delete_record`
- `edit_file`
- `fork_project`
- `get_build_guide`
- `get_project`
- `get_project_connection`
- `get_project_status`
- `list_entities`
- `list_files`
- `list_projects`
- `list_records`
- `list_templates`
- `list_workspaces`
- `move_project`
- `open_bool_editor`
- `prompt_project`
- `publish_project`
- `read_file`
- `render_project_widget`
- `run_command`
- `run_db_migration`
- `save_version`
- `set_project_icon`
- `update_project`
- `update_record`
