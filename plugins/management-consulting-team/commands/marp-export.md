---
description: Export a MARP presentation (.md) to PDF / HTML / PPTX using the consulting.css theme. Wraps marp-cli and resolves the theme path automatically.
allowed-tools: Read, Bash, Glob
argument-hint: "[path-to-deck.md] [--format pdf|html|pptx|all]  (e.g. 'project-data/deliverables/presentations/P001-market-entry/P001-market-entry-V01.md --format pdf')"
---

You are the Engagement Manager. The Principal wants to export a MARP
deck to a distributable format.

## Instructions

**Step 1 — Parse the arguments.**
`$ARGUMENTS` contains the deck path and optionally a `--format` flag.

- If `$ARGUMENTS` is empty:
  - List all MARP decks in `project-data/deliverables/presentations/`:
    ```bash
    find project-data/deliverables/presentations -name '*.md' -not -path '*/exports/*' 2>/dev/null | sort
    ```
  - Ask the Principal: "Which deck do you want to export? Available: [list]. Default format is PDF — say 'all' for pdf+html+pptx."
- If a path is given but no `--format`, default to `pdf`.
- If `--format all`, produce pdf + html + pptx.

**Step 2 — Verify the deck exists and is a MARP source.**

- Check the file exists. If not: "Deck not found at [path]. Presentations live under `project-data/deliverables/presentations/`."
- Read the first 10 lines and verify the YAML front matter has `marp: true`. If not: "This file doesn't look like a MARP deck (no `marp: true` in front matter). Want me to convert a plain Markdown wireframe into MARP format first? That's a Slide-Architect task, not a simple export."

**Step 3 — Verify tooling.**

- `node -v` — must be 18+
- For PDF or PPTX format, check a browser is available:
  ```bash
  which google-chrome-stable chromium-browser chromium 2>/dev/null
  ```
  If none found: "PDF and PPTX export need Chrome or Chromium installed. On WSL/Ubuntu: `sudo apt install chromium-browser`. HTML export works without it — want me to do HTML only for now?"

**Step 4 — Resolve the output folder.**

The deck lives at `project-data/deliverables/presentations/PXXX-[topic]/PXXX-[topic]-V[NN].md`.
The exports go into the sibling `exports/` folder:

```bash
DECK="[deck-path]"
DECK_DIR=$(dirname "$DECK")
DECK_STEM=$(basename "$DECK" .md)
EXPORT_DIR="$DECK_DIR/exports"
mkdir -p "$EXPORT_DIR"
```

**Step 5 — Run the export(s).**

Theme path resolves to the plugin asset:
```
${CLAUDE_PLUGIN_ROOT}/assets/marp-themes/consulting.css
```

Run the appropriate `npx @marp-team/marp-cli` command(s):

```bash
THEME="${CLAUDE_PLUGIN_ROOT}/assets/marp-themes/consulting.css"

# HTML
npx @marp-team/marp-cli --theme "$THEME" "$DECK" --html \
  -o "$EXPORT_DIR/${DECK_STEM}.html"

# PDF
npx @marp-team/marp-cli --theme "$THEME" "$DECK" --pdf \
  -o "$EXPORT_DIR/${DECK_STEM}.pdf"

# PPTX (bitmap-per-slide, NOT editable — warn Principal before using)
npx @marp-team/marp-cli --theme "$THEME" "$DECK" --pptx \
  -o "$EXPORT_DIR/${DECK_STEM}.pptx"
```

If `--format all`, run all three sequentially. Capture stderr to surface
errors cleanly.

**Step 6 — Offer to open the PDF.**

If the export succeeded and a PDF was produced, try to open it:

```bash
# Linux / WSL
xdg-open "$EXPORT_DIR/${DECK_STEM}.pdf" 2>/dev/null || \
wslview "$EXPORT_DIR/${DECK_STEM}.pdf" 2>/dev/null || \
echo "Open manually: $EXPORT_DIR/${DECK_STEM}.pdf"
```

**Step 7 — Report.**

```
## Export complete

**Deck:** [relative path]
**Outputs:**
- [path/to/deck.pdf]   (X pages)
- [path/to/deck.html]  (fast preview)
- [path/to/deck.pptx]  (bitmap PPTX — NOT editable)

[If PPTX was produced:]
⚠ The PPTX is a bitmap export — each slide is a full-slide image,
text is not editable. If the recipient needs to edit text, let me
know and I'll run the editable-PPTX path via Pandoc.
```

## Notes

- **Editable PPTX is not this command.** This command only wraps
  `marp-cli`. Editable PPTX uses Pandoc + reference template and is
  handled by the Slide Architect on explicit request.
- **PPTX warning is mandatory.** Every time a PPTX is produced,
  remind the Principal that it's bitmap-only before sharing with a
  client who might try to edit it.
- **No in-repo preview window.** `marp-cli` can run a dev-server mode
  for live preview, but that requires a long-running process. For
  iterative work, use the Marp VS Code extension instead.
- **Theme not found errors** mean `${CLAUDE_PLUGIN_ROOT}` didn't
  resolve — confirm the plugin is loaded. As a fallback, absolute path
  to `assets/marp-themes/consulting.css` works too.
