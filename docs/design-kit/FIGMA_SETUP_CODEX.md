# Figma MCP in Codex

Use the existing Figma connection in Codex; see [Figma setup](https://github.com/quctuan/design-stuff-kit/blob/main/docs/FIGMA_SETUP_CODEX.md). No separate read-only connection check is needed.

1. Open Codex's Figma connection and authenticate the account that has access to the target file, if it is not connected already.
2. Give the agent the Figma file or node URL. It must select the matching connected account and pass `fileKey` and `link_id` explicitly.
3. Verify identity with `whoami`, then target access with `get_metadata` or a scoped `use_figma` read. A successful identity check alone does not verify file access.
4. Read the bundled `figma-mcp-api` skill and the integration's official `figma-use` instructions before Plugin API execution.
5. Discover components with `get_libraries` and `search_design_system`; verify edits with `get_screenshot` and structural checks.

The Codex launcher only checks `codex mcp get figma`; it never writes credentials or changes the connection. Desktop-managed connections may not appear in CLI configuration. Verify the session's exposed tools in that case. A read-only connector cannot run canvas-write workflows; connect the integration exposing `use_figma` or report the limitation before building.

Reconnect the Figma integration if account authentication fails. For file access failures, verify the selected account, URL and sharing permissions. For component import failures, inspect library association, publishing state and the actual returned keys. Do not substitute handmade components for required library assets.
