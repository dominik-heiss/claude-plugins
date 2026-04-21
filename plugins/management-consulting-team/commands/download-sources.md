---
description: Download the most relevant sources registered in the source registry to local storage. PDFs are saved as-is; HTML pages are saved as HTML files. Run at the end of a research phase or on demand.
allowed-tools: Read, Write, Glob, WebFetch, Bash
argument-hint: "[optional: 'all' to download all sources, or leave empty to download only high-reliability sources]"
---

You are the Engagement Manager. The Principal has requested a source download.

## Instructions

**Step 1 — Read the source registry.**
Load `project-data/sources/source-registry.json`. List all sources with a URL.

**Step 2 — Determine which sources to download.**

If `$ARGUMENTS` = "all": download every source with a URL that has not yet been downloaded (local_path is null).

Otherwise (default): download sources meeting ALL of the following criteria:
- `reliability` is "high" or "medium"
- `local_path` is null (not yet downloaded)
- The source was actually cited in at least one research or analysis document (grep for the SRC ID in `project-data/research/` and `project-data/analysis/`)

Present the list to be downloaded and confirm with the Principal before proceeding if more than 10 sources are in scope.

**Step 3 — Download each source.**
For each source to download:

1. Determine file type from the URL:
   - URL ends in `.pdf` → save as PDF
   - Otherwise → save as HTML

2. Use WebFetch to retrieve the content.

3. Save to the appropriate location:
   - PDF: `project-data/sources/documents/[SRCID]-[slug].pdf`
   - HTML: `project-data/sources/web/[SRCID]-[slug].html`

4. Update the source registry entry: set `local_path` to the saved file path.

5. If a download fails (URL unreachable, paywall, etc.): log the failure in the registry with `"local_path": "FAILED: [reason]"` and continue with the next source.

**Step 4 — Report.**
Summarize: how many sources downloaded successfully, how many failed, and where the files are stored.
