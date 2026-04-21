---
name: marp-presentation
description: >
  This skill activates when the user asks to "build a MARP deck",
  "create a MARP presentation", "export slides to PDF", "produce a
  visual deck", "make a client-ready presentation", or when the EM
  chooses MARP as the output format for a steerco, final presentation,
  pitch, or interim report. Covers the `consulting.css` theme, the full
  layout-pattern catalog, the folder convention, and the marp-cli export
  workflow.
---

# MARP Presentation — Consulting Deck Format

MARP is the plugin's visual-presentation format. It is markdown-driven,
diff-friendly, and exports to PDF / HTML via `marp-cli`. Use it when
the deliverable needs to look like a client-ready deck — not when a
plain Markdown wireframe is sufficient.

## When to use MARP (vs. plain Markdown)

| Use plain Markdown (slide wireframe) | Use MARP |
|---|---|
| Internal working doc, storyline draft | Steerco, final presentation, pitch |
| Fast turnaround, no visual polish needed | Client-ready or board-ready output |
| Principal will copy/paste into their own slides | Principal wants a finished PDF to share |
| Storyline review with EM only | Review cascade output that goes outside the EM |

**Default is plain Markdown.** MARP is opt-in and requested by the
Principal or triggered by commands like `/mct:present-final --marp` or
`/mct:steerco --marp`.

## The theme

The consulting theme lives at:

```
${CLAUDE_PLUGIN_ROOT}/assets/marp-themes/consulting.css
```

Design language (do not alter without Principal approval):

- 16:9, 1280×720, white background
- Deep Navy `#0a1f3d` primary, Warm Red `#c9302c` accent (sparse)
- Greyscale `#f5f5f5`, `#d0d0d0`, `#6b6b6b`
- Inter with Helvetica Neue fallback
- Action title 28pt bold, subtitle 15pt muted
- Footer right-aligned, pagination right-most, both 10pt grey
- Source convention: `<p class="src">Source: ...</p>` pinned above footer

## Layout patterns

Set via `<!-- _class: xxx -->` at the top of a slide. Detailed catalog
with realistic consulting examples: `references/slide-patterns.md`.

| Class | Purpose |
|---|---|
| `title` | Title slide (project name, date, author) |
| `agenda` | Agenda / table of contents |
| `section` | Section divider (Navy background) |
| `content` | Default — action title + supporting evidence |
| `two-col` | 2-column comparison |
| `matrix-2x2` | 2×2 strategic matrix (with optional `.q-hl` highlight) |
| `kpi-row` | 3-4 KPIs displayed prominently |
| `quote` | Stakeholder / expert quote |
| `takeaway` | Recommendation / call-to-action (accent background) |
| `back` | Back cover (Navy, centered) |

## Folder convention

Presentations live in their own folder under `deliverables/` so source,
assets and exports stay together:

```
project-data/deliverables/presentations/
  PXXX-[topic]/
    PXXX-[topic]-V[NN].md       ← MARP source (single source of truth)
    assets/                     ← charts, images, logos used inline
    exports/                    ← generated PDF / HTML (gitignored)
      PXXX-[topic]-V[NN].pdf
      PXXX-[topic]-V[NN].html
```

- **P-prefix** — presentations are numbered `P001`, `P002`, … in
  `document-registry.json`, sequential no-gaps per the plugin convention
- **Versioning** on the `.md` only — exports are rebuilt, not versioned
- **Assets** — use relative paths from the `.md`: `![](assets/chart.png)`

## Authoring rules

Action titles drive the deck — the pyramid principle and the storyline
rules from the `executive-storylining` skill apply in full. What's
specific to MARP:

1. **Start with a front matter block** that sets the theme and footer:
   ```yaml
   ---
   marp: true
   theme: consulting
   paginate: true
   footer: '[Client] · [Engagement] · Confidential'
   ---
   ```
2. **Title, section and back slides disable pagination + footer** with
   per-slide directives:
   ```
   <!-- _paginate: false -->
   <!-- _footer: '' -->
   ```
3. **Source citations** use the `.src` class, not the SCR footer from
   plain Markdown:
   ```html
   <p class="src">Source: Internal analysis, Market Report 2024 (SRC001)</p>
   ```
4. **One message per slide** — the same hard rule as in
   `executive-storylining`: if a slide has two messages, split it.
5. **Max 5 bullets** — hard ceiling for senior readers.

## Exporting

The export workflow is wrapped by `/mct:marp-export [path]`. Manually:

```bash
# HTML (fast preview, no browser required for export itself)
npx @marp-team/marp-cli \
  --theme ${CLAUDE_PLUGIN_ROOT}/assets/marp-themes/consulting.css \
  deck.md --html -o exports/deck.html

# PDF (client-ready, needs Chrome/Chromium installed)
npx @marp-team/marp-cli \
  --theme ${CLAUDE_PLUGIN_ROOT}/assets/marp-themes/consulting.css \
  deck.md --pdf -o exports/deck.pdf
```

Detailed export guidance (PPTX limitations, browser setup, troubleshooting,
the editable-PPTX path via Pandoc): `references/export-workflow.md`.

## What this skill does NOT cover

- **Editable PowerPoint output** — `marp-cli --pptx` produces a
  bitmap-per-slide file (not editable). The editable-PPTX path goes
  via Pandoc + reference template — documented in
  `references/export-workflow.md` as an advanced option.
- **Storyline or pyramid principle** — those live in
  `executive-storylining`. Load that skill first; MARP is the
  presentation format, not the argument.
- **Chart generation** — MARP embeds images. Build the chart
  separately (openpyxl for Excel charts, matplotlib for PNG) and save
  the export into `assets/`.

## Reference files

- `references/slide-patterns.md` — full pattern catalog with realistic
  consulting examples, complete markup for each class
- `references/export-workflow.md` — marp-cli commands, browser setup,
  PPTX options, editable-PPTX path, troubleshooting
- `references/example-deck.md` — an end-to-end reference deck that
  demonstrates every pattern in sequence
