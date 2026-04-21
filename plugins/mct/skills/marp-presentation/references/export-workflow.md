# MARP Export Workflow

How to turn a `.md` MARP source into a distributable file (PDF, HTML,
PPTX, editable PPTX). The `/mct:marp-export` command wraps this — this
reference explains what happens under the hood and covers the cases
the command doesn't.

## Tooling

- **marp-cli** — invoked via `npx @marp-team/marp-cli …` (no global
  install needed)
- **Chrome / Chromium** — required for PDF and PPTX export. HTML
  export does not need it.
- **Pandoc** — optional, only for the editable-PPTX path

Node.js 18+ must be installed. On WSL/Ubuntu:

```bash
sudo apt install -y nodejs npm chromium-browser
```

## Standard exports

### HTML (fast preview)

No browser required. Outputs a single self-contained HTML file.

```bash
npx @marp-team/marp-cli \
  --theme ${CLAUDE_PLUGIN_ROOT}/assets/marp-themes/consulting.css \
  deck.md \
  --html -o exports/deck.html
```

Use for: rapid iteration, internal review, preview in a browser.

### PDF (client-ready, primary delivery format)

Needs Chrome/Chromium on PATH. Output is print-quality, layout-faithful.

```bash
npx @marp-team/marp-cli \
  --theme ${CLAUDE_PLUGIN_ROOT}/assets/marp-themes/consulting.css \
  deck.md \
  --pdf -o exports/deck.pdf
```

Optional flags:

- `--allow-local-files` — required if you embed images from outside
  the deck's folder (e.g., absolute paths). Normally `assets/` is
  relative to the `.md` and this flag is not needed.
- `--pdf-notes` — include presenter notes as PDF text notes
  (annotations), useful for rehearsal prints

### PPTX (bitmap-per-slide, NOT editable)

Produces a `.pptx` where each slide is a full-slide image. Readable on
any PowerPoint install but text cannot be edited.

```bash
npx @marp-team/marp-cli \
  --theme ${CLAUDE_PLUGIN_ROOT}/assets/marp-themes/consulting.css \
  deck.md \
  --pptx -o exports/deck.pptx
```

Use only when:
- The recipient explicitly wants PowerPoint format
- The deck will not be edited by the recipient, only presented or shared
- The deck's layout fidelity is more important than editability

Do **not** use when the client expects to edit text, adjust numbers, or
rework slides — for that, see the editable-PPTX path below.

## Editable PPTX path (advanced)

MARP's own PPTX export is bitmap-only. For editable PowerPoint with
real text boxes, the path goes via Pandoc + a reference template.
Quality is lower than MARP/PDF (Pandoc can't reproduce custom CSS
layouts like `matrix-2x2` or `kpi-row`) — but the text is editable.

Strategy:
1. **Keep MARP as source of truth.** All content lives in the `.md`.
2. **Produce the MARP PDF first.** This is the layout-faithful,
   client-ready output.
3. **On explicit request, produce an editable PPTX alongside.**
   Pandoc converts a simpler, MARP-free Markdown into PPTX against a
   branded reference template.

Command shape (requires `pandoc` and a `reference.pptx` template):

```bash
pandoc deck.md -o exports/deck-editable.pptx \
  --reference-doc=${CLAUDE_PLUGIN_ROOT}/assets/marp-themes/reference.pptx
```

**Caveats (important to communicate to the Principal):**
- MARP directives (`<!-- _class: ... -->`, YAML front matter, custom
  `<div>` blocks) will not render — strip them for the Pandoc pass, or
  maintain a Pandoc-friendly duplicate
- Matrix and KPI layouts become plain bullets or tables
- The reference template controls colors, fonts and layouts — so the
  editable PPTX **inherits the template's branding**, not the MARP
  theme's

A reference template is **not shipped with the plugin today**. When the
Principal first requests an editable PPTX, the Slide Architect produces
a minimal `reference.pptx` in the engagement's `client-data/` folder
and uses it for all editable exports in that engagement.

## Command summary (`/mct:marp-export`)

The command handles the standard workflow:

```
/mct:marp-export [path-to-deck.md] [--format pdf|html|pptx|all]
```

- Defaults to `--format pdf` when no format flag is given
- `all` produces pdf + html + pptx in one run
- Resolves `--theme` automatically to the plugin's
  `consulting.css`
- Writes outputs into `exports/` next to the deck
- Reports the output file paths and opens the PDF if `xdg-open` /
  `wslview` / `open` is available

## Troubleshooting

### PDF export fails with "Failed to launch chrome"
Chrome/Chromium is not installed or not on PATH.

```bash
sudo apt install -y chromium-browser
which chromium-browser    # confirm it's on PATH
```

Under WSL, if `chromium-browser` is problematic, install
`google-chrome-stable` from the `.deb` package instead.

### Fonts look wrong in PDF
Inter is not installed on the system. The theme falls back to Helvetica
Neue / Arial — so output is still readable, just not the intended
face. To install Inter:

```bash
sudo apt install -y fonts-inter
```

### Images don't appear in PDF
marp-cli blocks local file access by default. Either:
- Use relative paths inside the deck's folder (`![](assets/chart.png)`)
  — recommended
- Add `--allow-local-files` to the export command (only if you must
  use absolute paths)

### "Theme not found" when using `theme: consulting`
The `consulting.css` file is passed via `--theme`, not installed
globally. Either keep the explicit `--theme` flag in the export
command, or use the theme file's path as the `theme:` value in the
front matter:

```yaml
theme: /absolute/path/to/consulting.css
```

### Slide content overflows the frame
The theme is fixed at 1280×720. If content runs off, the solution is
**split the slide**, not shrink the font. Hard minimums: 13pt body,
24pt title.

### PPTX output has weird artifacts
The bitmap-per-slide PPTX is produced by rendering each slide in a
headless browser and packaging the PNGs. Artifacts usually mean the
Chrome rendering is slightly off — try the PDF export to verify the
source is correct, then regenerate the PPTX.
