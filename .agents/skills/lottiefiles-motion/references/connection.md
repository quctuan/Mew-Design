# LottieFiles connections

Checked against official documentation on 2026-10-11.

## Creator MCP: edit motion

Requires Node.js 18+ and an open Lottie Creator browser tab.

```sh
codex mcp add lottiefiles-creator -- npx -y @lottiefiles/creator-mcp@latest
```

In Creator: Settings → MCP Settings → Enable local MCP. Wait for the local bridge-connected indicator. Start a fresh Codex session after registering the server, discover its tools, then query the current scene without changing it. Keep the tab open throughout editing. Inspect schemas for actual tool names and parameter units. Do not register a second bridge when a working connection already exists.

Source: https://docs.lottiefiles.com/en/creator/13_ai-tools/lottie-creator-mcp

## Hosted account MCP: organize files (optional)

Remote endpoint: https://mcp.lottiefiles.com/mcp

```sh
codex mcp add lottiefiles --url https://mcp.lottiefiles.com/mcp
codex mcp login lottiefiles
```

OAuth sign-in is required. Verify the tools operations_list, schema_search, schema_details and graphql_execute, discover the schema, then run a scoped read before mutations. This connection manages workspace/account data; use Creator MCP for animation editing.

Source: https://docs.lottiefiles.com/en/platform/mcp/connect

## Browser WebMCP

A compatible browser/assistant can use Creator's WebMCP tools without the local bridge. Browser WebMCP support and ordinary MCP support are separate; verify the actual tools before choosing this path. Do not assume availability from a UI badge alone.

Source: https://docs.lottiefiles.com/en/creator/13_ai-tools/lottie-creator-webmcp

## Verified Creator tool contract (package 0.2.2)

`read_scene` takes an empty argument object and returns the active scene, layers and selection. It has no fileKey or account selector. Confirm the intended browser tab before calling it; do not copy Figma arguments into this tool. The inspected server also exposes `read_keyframes`, `apply_keyframes`, `retime_keyframes`, `create_shape`, `create_text`, `list_scenes` and `set_current_frame`. Re-read each schema before using it. Tool discovery is not proof that the browser bridge is connected; a no-tab error means the editor is still disconnected.
