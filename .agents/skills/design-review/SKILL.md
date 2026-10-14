---
name: design-review
description: Run a blind, scored design-critic round on the latest renders of a feature
---

Read [Codex runtime guidance](../../CODEX_RUNTIME.md) before this workflow.



Run one critique round for: the feature/path and options in the user's request

Load the `design-critique` skill and follow it. In short:

1. Find the feature folder and its newest `shots/rN/`. If the HTML changed after that render, run `$render` first. If `report.md` has any FAIL, stop and list them: the critic does not see work with open FAILs.
2. Read `critique/config.md`, `critique/anchors.md`, and `critique/lessons.md` if they exist. Mention the top carry-forward items before starting. If there is no config, say that defaults apply and offer to create one after this round.
3. If this job already has a critic, continue the same agent. Otherwise spawn one `design-critic` with the first brief from the skill (§4). The track is `wireframe` when the HTML has `data-mode="wireframe"`, otherwise `ui`. Never include your own scores or opinion of the work.
4. When the report comes back, write the round into the feature's `CRITIQUE.md` and compute the official score with the config's weights (skill §7).
5. Reply with: the official score and the change since the last round, the lowest lines, the five asks, the critic's blind spot, and its verdict. Ask which asks to take and which to decline before editing anything.
