# Using Stageshow with existing UI workflows

Stageshow is bundled with its MIT license and notices. `ui-craft-stageshow` is the integration entrypoint for every visible UI task. It adds craft and motion guidance; the existing workflow still owns product behavior, Figma edits, design-system bindings and deployment.

## Examples

- “Build this dashboard using the project library. Apply ui-craft-stageshow in production mode; verify desktop and mobile.”
- “Create a 12-second hero walkthrough. Use ui-craft-stageshow in illustration mode and the full stageshow rehearsal workflow.”
- “Update these Figma screens. Reuse the existing components and apply Stageshow craft without inventing business states.”

After pulling updates, refresh/reinstall the skill package using the repository’s normal installation instructions and start a fresh Codex session. For project-scoped Mew-Design use, open the repository root so AGENTS.md is loaded. For kit projects, use start-design and merge the updated project instruction template. Existing projects need the UI routing paragraph added to their AGENTS.md once. A GitHub update alone does not update already-installed plugin caches or unrelated projects.

If both packages are installed, select one canonical stageshow/ui-craft-stageshow pair. Do not load two vendored copies or run two review pipelines. Explicit invocation is a fallback: `$ui-craft-stageshow` plus the implementation skill. Automatic routing requires the package to be installed/discoverable and project instructions to be loaded; it is not a global guarantee for every chat.
