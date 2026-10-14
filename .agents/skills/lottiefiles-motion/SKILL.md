---
name: lottiefiles-motion
description: Build, edit, and verify motion in LottieFiles Creator using Creator MCP. Use for loading, onboarding, success feedback, animated illustrations, loops, themes, and supported dotLottie state-machine interactions; export .lottie or Lottie JSON for developers. Use figma-prototype-motion for Figma reactions and interactive-prototype for coded app prototypes.
metadata:
  author: quctuan
  version: 1.0.0
  mcp-server: lottiefiles-creator
---

Read [Codex runtime guidance](../../CODEX_RUNTIME.md) before this workflow.


# LottieFiles motion

Use Lottie Creator as the editable motion canvas. The Creator MCP edits scenes, layers and keyframes. The separate hosted LottieFiles MCP manages account/workspace data; its GraphQL tools are not a substitute for Creator editing tools.

## 1. Preflight and scope

Read `references/connection.md` when setting up or reconnecting. Discover the current Creator tool schemas rather than guessing method names. Confirm the connected Creator tab, file, scene and selected layers through a read-only query before editing. Keep that tab open and local MCP enabled. If multiple tabs are connected, select the intended target explicitly.

Installation alone does not establish a live editor connection. Report separately: configuration registered, server initialized, tools discovered, browser bridge connected, scene read verified. Stop editor writes when scene identity or connection is uncertain.

Inspect the existing artwork and timing; use approved SVGs or assets whenever supplied. Capture a supported snapshot or duplicate before substantial changes, preserving existing node/layer identifiers when a reviewed file is being corrected. Do not publish, change sharing or delete unrelated files as part of an animation request.

## 2. Define the motion

For a new animation, turn the brief into a short spec: purpose, scene size, frame rate, duration, loop behavior, named layers, event/keyframe table, easing, brand colors, transparent background and reduced-motion alternative. Reuse decisions already approved; clarify only missing decisions that materially affect the result.

For interactive assets, list segments, states, inputs, transitions and event actions actually supported by the current Creator workspace and target runtime. State machines and themes belong in dotLottie when supported. A plain Lottie JSON export does not carry the same interactive package. Do not translate another editor's view models, scripts or artboard APIs into invented Creator calls.

Use `references/motion-craft.md` for timing and choreography. If the official LottieFiles `motion-design` skill is installed, load the relevant sections for the task. For music, also use `beat-synced-motion`.

## 3. Build in small batches

Inspect scene → import/reuse artwork → organize named layers → set keyframes and easing → verify a batch → add loops/segments/themes/interactivity where required. Discover tool names, parameter units and frame/time conventions from actual schemas; never assume opacity, scale or time uses a particular unit.

Read fresh layer IDs immediately before mutations. If an ID is missing, re-query the scene and locate the real target; do not keep retrying stale IDs or replace the approved artwork. After a timeout inspect the actual state before rerunning a write to prevent duplicate layers or keyframes.

Use the smallest scoped edit that implements the request. For loops, match the first and last visual states and their motion continuity. For state transitions, verify both the outgoing and return paths. Feature access depends on the current workspace and plan; report any unavailable effect or export rather than claiming it succeeded.

## 4. Verify and hand off

Read the scene and keyframes back against the spec. Preview the animation in Creator at start, accents, settle and loop seam; screenshots alone cannot prove temporal behavior. Verify state inputs and transitions in playback where applicable. If visual playback cannot be inspected, report that limitation and request the designer's review.

Export through the actual supported export tools or Creator controls. Verify the saved file exists and matches the requested format. For JSON, inspect canvas dimensions, frame rate, in/out points and asset dependencies. For .lottie, inspect ZIP integrity, manifest and embedded animation entries. Include runtime compatibility and state-machine/theme support requirements; do not promise identical support across platforms.

Deliver: Creator URL, validated .lottie or JSON asset, dimensions/FPS/duration/loop, segment/state/input names, reduced-motion behavior, runtime target and any unverified items. A successful MCP connection, an in-progress export or a copied sharing URL is not proof that the asset was saved and handed off.
