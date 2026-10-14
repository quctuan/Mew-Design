---
description: Run a blind, scored design-critic round on the latest renders of a feature
argument-hint: <feature folder, e.g. explore/onboarding> [phase: explore|figma] [track: ui|wireframe]
---

# Design Review & Critique Workflow

Run one critique round for a feature folder.

Load the `design-critique` skill and follow it:

1. **Find the feature folder** and its newest `shots/rN/`. If the HTML changed after that render, run `/render` first. If `report.md` has any FAIL, stop and list them: the critic does not see work with open FAILs.
2. **Read critique context**: Read `critique/config.md`, `critique/anchors.md`, and `critique/lessons.md` if they exist. Mention top carry-forward items before starting. If there is no config, state that defaults apply and offer to create one after this round.
3. **Invoke Design Critic**: Spawn or continue the `design-critic` role with the first brief from the `design-critique` skill (§4). The track is `wireframe` when the HTML has `data-mode="wireframe"`, otherwise `ui`. Never include your own scores or opinion of the work.
4. **Log Results**: When the report comes back, record the round into the feature's `CRITIQUE.md` and compute the official score with config weights.
5. **Present Feedback**: Report the official score and delta since last round, lowest criteria, the 5 asks, the critic's blind spot, and its verdict. Ask the user which asks to address before editing anything.
