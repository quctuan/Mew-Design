---
name: theboxexplore
description: Run an explicitly requested satirical product-idea exercise that starts with a real frustration, pushes an absurd feature to its limit, then extracts a usable concept. Invoke only when the user says theboxexplore; do not use for ordinary brainstorming or specs.
metadata:
  author: quctuan
  version: 1.0.0
  trigger: manual only
  inspiration: https://sorens.beehiiv.com/
---

Read [Codex runtime guidance](../../CODEX_RUNTIME.md) before this workflow.


# The Box Explore

An idea exercise inspired by [Soren's Newsletter](https://sorens.beehiiv.com/). The satirical format helps expose a real user frustration without judging the first idea too early. The final extraction table is the product-design step added here.

## When to run

Only run when the designer explicitly says `theboxexplore` or invokes `/theboxexplore`. Other requests to brainstorm or explore use a normal design process. The deadpan voice would be wrong for an ordinary product decision.

Input: `/theboxexplore [topic or real frustration]`. If the frustration is missing, ask for one concrete incident. Do not invent a personal anecdote for the user. Default to five ideas unless the user specifies a count.

## One idea

Write about 150–220 words and follow this arc:

1. **Headline:** product plus an absurd but plausible feature, in a few words.
2. **Subtitle:** one dry line that sharpens the premise.
3. **Real annoyance:** the concrete moment that makes the idea understandable.
4. **What if:** overbuild a solution to that small problem.
5. **Mockup:** describe one screen and its interaction as if the feature shipped.
6. **Self-critique:** let the idea fail on its own terms. Keep a straight face.
7. **Close:** a short line that lands the joke without pretending the feature is approved.

For example, a calendar could require a “meeting weather forecast” before accepting an invitation. The serious need beneath the joke might be showing a person's focus load before scheduling another call. Use original examples for each run; do not reproduce another creator's newsletter examples.

## Tone

- Write like a product manager explaining an actual feature. Avoid emoji and a narrator who laughs at the joke.
- Keep the problem believable. The comic gap is between a small, real pain and an oversized solution.
- Push the idea far enough to reveal its boundary, then step back. Do not turn the satirical section into a polished roadmap.
- One idea needs one screen. If the interaction cannot be pictured, the concept is still too abstract.

## After the ideas

Add a separate table:

| Idea | Real frustration | Serious version worth testing |
|---|---|---|

This table is analysis, not part of the satirical piece. State which ideas have a screen worth prototyping and which should be dropped. Do not write a production spec or edit Figma unless the designer separately asks for that work.
