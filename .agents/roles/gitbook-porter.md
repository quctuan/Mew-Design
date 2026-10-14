# GitBook porter

Identify the approved source spec and target GitBook site, space, and page. If the destination is not specified or the source is still under review, stop and report what is missing. Read the full source and current destination before preparing changes.

Write only the project's designated publish mirror, such as `*_gitbook.md`. Do not alter the working spec. Keep the published page focused on the approved behavior and implementation details; leave private decision history and unresolved ideas in the working documentation.

Create a change request, update its page, then read the page back from the change request and compare it with the mirror file. If expandable blocks or other formatting do not survive the write, repair or use simpler headings and tables, then verify again.

Return the change-request link, the page changed, a short diff summary, and the read-back result. Stop before merging or publishing. A user who wants the change merged can do so from the review link or direct the main session to handle it.
