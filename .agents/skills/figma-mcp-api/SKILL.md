---
name: figma-mcp-api
description: Use the directly connected Figma MCP in Codex to inspect libraries, reuse components, bind variables, and safely edit Figma files with use_figma. Load before Figma Plugin API queries or writes in Design Stuff Kit workflows.
metadata:
  author: quctuan
  version: 1.0.0
  mcp-server: figma
---

Read [Codex runtime guidance](../../CODEX_RUNTIME.md) before this workflow.


# Direct Figma MCP API

Discover the tools actually exposed by the connected Figma integration. Prefixes vary by host. In Codex, load the integration's official `figma-use` skill before every `use_figma` call, and the relevant generate-design, generate-library or motion skill for those tasks. This guide complements those instructions; it does not replace their tool contract.

## Connection and target

Use the existing Figma connection in Codex. No separate bridge, token entry or background server is installed by this kit. Select the connected account (`link_id`) that can access the user's URL; extract `fileKey` and concrete `nodeId` from that URL. Never hardcode account identifiers. `whoami` checks account identity, not target-file access. Verify access using `get_metadata` or a scoped read through `use_figma`. Pass the target file explicitly to every call. Query `figma.root.name` if a file-name check is needed; there is no implicit `fileContext` response.

## Read and discover

- `get_libraries`: discover libraries associated with the destination file.
- `search_design_system`: search components, variables and styles within the actual destination and returned library keys. Use names found in the file; retain the returned keys and IDs.
- `get_variable_defs`: inspect definitions for a concrete node where supported. For local variable collections or details not exposed by a dedicated tool, use a narrowly scoped read through `use_figma` and supported Plugin API methods.
- `get_metadata` and `get_screenshot`: inspect hierarchy and visual output. Preserve returned evidence; do not treat an import or script result as visual verification.

A missing import can reflect access, publishing, key validity or library availability. Inspect these causes and report the real gap. Do not invent lookalike components when the task requires approved library assets.

## Execute and verify

Use `use_figma` with its real arguments: `fileKey`, selected `link_id`, `description`, and `code`. Run code directly in the provided execution context, using top-level await and returning small structured results. Do not wrap it in an async IIFE, log results with console.log, or call closePlugin. Follow the integration's limits on page switching, image loading and supported methods.

Read the target node before editing. Load fonts before changing text; use returned component keys for imports; bind actual variables rather than hardcoding token values. Build approved substantial work in a new labeled section. Preserve the shared library and unrelated approved frames.

For bulk changes, capture a scoped structural snapshot and screenshot before work. Use a genuine version checkpoint only if the exposed API supports it; report exactly which backup exists. A screenshot is not a full restorable version. Do not assert that a version-history method is available. After a tool failure inspect the target before retrying; retry a write only when its completion state is known and duplication is prevented. Honor the tool's retry guidance.

Verify IDs, instance/variant properties, text, variable bindings, interactions and screenshots after writing. Record the Figma URL and remaining gaps. Never claim completion based only on a successful connection.

## Tokens and motion

Export tokens by querying supported variable APIs and serializing the actual names, collection modes, types and alias relationships. Resolve aliases deliberately; preserve mode semantics. Import tokens through supported `use_figma` variable APIs after mapping existing collections and IDs, with explicit user authorization for library changes. Do not claim an export/import helper or universal plan entitlement exists.

For prototype reactions and animation, load the connected Figma motion skill and inspect supported APIs first. Use an external prototype or documented timing specification if the connection cannot express the requested behavior; report that limitation.
