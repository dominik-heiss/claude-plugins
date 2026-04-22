---
description: Generate the project dashboard. Builds a self-contained HTML file from all project data (JSONs, deliverables, reviews, findings, sources). Open the resulting file in any browser — no server needed.
allowed-tools: Read, Bash
argument-hint: "[optional: 'open' to open in browser after building]"
---

**Use when:** You want to rebuild the HTML dashboard from current project data.
**Standalone:** no — requires an active engagement (`project-data/engagement.json`).

You are the Engagement Manager. The Principal has requested a dashboard update.

## Instructions

**Step 1 — Build the dashboard.**
Run the build script:

```bash
bash ${CLAUDE_PLUGIN_ROOT}/assets/dashboard/build-dashboard.sh project-data
```

This reads all JSON files and markdown documents from `project-data/`, injects them into the dashboard template, and writes `project-data/dashboard.html`.

**Step 2 — Report.**
Confirm the dashboard was built successfully. Tell the Principal:
- Where the file is: `project-data/dashboard.html`
- How to open it: double-click or `open project-data/dashboard.html`
- What's included: list the sections with content (Overview, Engagement, Team, etc.)

**Step 3 — If `$ARGUMENTS` includes "open":**
Attempt to open the dashboard in the default browser:
```bash
# macOS
open project-data/dashboard.html
# Linux
xdg-open project-data/dashboard.html 2>/dev/null || echo "Open project-data/dashboard.html in your browser"
```

## Notes
- The dashboard is regenerated from scratch each time — it's a snapshot, not a live view
- All data is embedded in the HTML file (no external dependencies, no server needed)
- Binary files (Excel, PowerPoint) are listed with their file paths but cannot be rendered inline
- Markdown files are rendered as formatted HTML with an accordion UI
