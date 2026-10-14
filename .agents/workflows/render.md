---
description: Render web-explore screens to PNG, run the checks, and compare with the previous round
argument-hint: <path/to/mockup.html> [extra wx-render flags]
---

# Web Explore Render Workflow

Render the web exploration screens to PNG and run visual checks.

1. **Find the HTML file** (first argument). If none was given, look for `explore/*/mockup.html`, then `explore/*/explore.html`, and ask which one if there are several.
2. **Pick the output folder** next to that file: `shots/rN`, where N is one more than the highest existing `shots/r*` folder. If a previous round exists, add `--compare <previous folder>`.
3. **Run render command**, from the project root:
   ```bash
   ./.agents/bin/wx-render <file> --out <folder> [--compare <previous>] <any extra flags>
   ```
4. **Read `<folder>/report.md`** and report:
   - The FAIL and warn counts, then each FAIL in one line.
   - Which screens are unchanged since the previous round, and whether any of them was meant to change.
   - The path to `sheet.png`.
5. **Handoff:** Do not fix anything and do not call the critic automatically. Ask the user whether to fix the FAILs first or run `/design-review`.
