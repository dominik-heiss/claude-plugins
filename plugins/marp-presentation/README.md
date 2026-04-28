# marp-presentation

Standalone Claude Code plugin for authoring and exporting **MARP** markdown
presentations. Bundles **two themes** — `editorial` (magazine, terracotta
on warm paper) and `soft-tech` (Linear-style, indigo on near-white) —
plus a shared layout-pattern catalog, example decks for both themes, and
a `/marp-export` command that wraps `marp-cli`.

## What you get

- **Skill** `marp-presentation` — Claude knows how to write good decks
  with both design languages and where every asset lives.
- **Command** `/marp-export` — render a deck to HTML (default) or PDF
  using the selected theme.
- **Command** `/define-design` — list bundled designs and pin one
  (writes `.marp-design` at the cwd root). Without arguments it lists
  the available designs and offers to switch, re-skin, or fork.
- **Themes** in `assets/themes/`:
  - `editorial.css` — 16:9, Fraunces + Inter, terracotta accent, paper-2
    surfaces. Magazine feel.
  - `soft-tech.css` — 16:9, Inter + JetBrains Mono micro labels, indigo
    accent on near-white, line-bordered surfaces. Linear/Vercel feel.
  - Both implement the same pattern set and the same markdown contract,
    so swapping themes is a one-line `theme:` change.
- **Templates** — copy `templates/starter-deck.md`, edit, export.
- **Examples** — `examples/reference-deck.md` (editorial) and
  `examples/reference-deck-soft-tech.md` show every layout pattern
  with abstract content so the patterns travel to any domain.

## Install

### Prerequisites

| Tool | Why | Install |
|---|---|---|
| Node.js 18+ | runs `marp-cli` via `npx` | https://nodejs.org/ |
| Chrome / Chromium | required for PDF export | https://www.google.com/chrome/ |
| VS Code + "Marp for VS Code" | live preview while editing (recommended) | VS Code Marketplace |

No global `marp` install required — `npx @marp-team/marp-cli` is invoked
on demand.

### Plugin install

This plugin ships through the `dh-claude-plugins` marketplace:

```shell
/plugin marketplace add dominik-heiss/claude-plugins
/plugin install marp-presentation@dh-claude-plugins
```

## Quickstart

1. Copy `templates/starter-deck.md` to your work area
2. Edit the markdown
3. Run `/marp-export <your-deck.md>` (or invoke `marp-cli` manually — see
   below)
4. Open the resulting PDF / HTML

## Layout patterns

Apply via `<!-- _class: NAME -->` at the top of a slide. Default (no class)
is a single-column content slide.

| Class | Use |
|---|---|
| `title` | Cover slide (hero, eyebrow, subtitle, meta) |
| `agenda` | Numbered agenda with inline italic descriptions |
| (none) | Single-column content (action title + lead + bullets) |
| `two-col` | Two-column body (`.columns` wrapper) |
| `cards` | Three-card grid (`.grid` + `.card` children) |
| `options` | Two-option matrix with KPI grid per side and recommended badge |
| `section-divider` | Section transition with the upcoming item highlighted |
| `statement` | Single large pull-quote slide |

See `examples/reference-deck.md` (editorial) for each pattern in use —
rendered previews are committed alongside the markdown:
[`reference-deck.html`](examples/reference-deck.html) (open in browser)
and [`reference-deck.pdf`](examples/reference-deck.pdf) (GitHub-viewable).
The same content rendered with the soft-tech theme:
[`reference-deck-soft-tech.html`](examples/reference-deck-soft-tech.html)
and
[`reference-deck-soft-tech.pdf`](examples/reference-deck-soft-tech.pdf).
For the full catalog with content guidance, see
`skills/marp-presentation/references/slide-patterns.md`.

## Per-slide chrome

Every non-title slide needs a brand marker at the top:

```markdown
<span class="brand">01 · Section name</span>
```

Renders as a small uppercase sans marker top-left. Footer and page
number are pulled from frontmatter automatically.

For source / footnote text, use:

```markdown
<p class="source">Source: ...</p>
```

It anchors to the bottom-left, separately from the footer.

## Export

**HTML is the default** — PDF only when explicitly requested.

HTML (default):

```bash
npx @marp-team/marp-cli your-deck.md \
  --theme assets/themes/editorial.css \
  --html \
  -o exports/your-deck.html
```

PDF (only on explicit request — needs Chromium, slower):

```bash
npx @marp-team/marp-cli your-deck.md \
  --theme assets/themes/editorial.css \
  --pdf --allow-local-files \
  -o exports/your-deck.pdf
```

Or use `/marp-export` and let Claude assemble the command. Pin a
design with `/define-design <name>` to skip per-deck `theme:`
frontmatter.

## Design decisions (settled)

- **Format:** 16:9 (1280×720)
- **Aesthetic:** magazine / editorial — display serif + sans, asymmetric,
  generous whitespace
- **Palette:**
  - Ink `#111111` (primary)
  - Paper `#F4EFE6` (warm off-white background)
  - Card surface `#E8E1D3`
  - Terracotta `#C2410C` (accent — bullets, page nr, eyebrow)
  - Muted `#6B645A` (meta, source, footer)
- **Typography:** Fraunces (display serif) + Inter (sans)
- **Action titles:** 46pt display serif, full-sentence takeaways
- **Subtitles:** 25pt italic display serif
- **Brand marker:** 10pt uppercase sans, top-left
- **Bottom chrome:** source line bottom-left, footer + page number
  bottom-right (page nr in italic terracotta)

Re-skin via the CSS variables at the top of `editorial.css` — see
`skills/marp-presentation/references/theme-customization.md`.

## Out of scope

- **Editable PPTX.** MARP's native `--pptx` produces bitmap-per-slide
  (each slide = one image), not editable in PowerPoint. Real editable
  PPTX needs a different toolchain (Pandoc + reference template) — that
  belongs in a separate plugin, not here.
- **PNG / image export per slide** — supported by `marp-cli --images png`
  if you need it, but not the focus.

## Folder layout

```
marp-presentation/
  README.md                          this file
  CLAUDE.md                          dev brief for Claude in this repo
  .claude-plugin/plugin.json         Claude Code plugin manifest
  skills/marp-presentation/
    SKILL.md                         skill trigger + workflow
    references/                      Claude-facing reference docs
  commands/
    marp-export.md                   /marp-export command
    define-design.md                 /define-design command
  assets/themes/
    editorial.css                    bundled default theme
    soft-tech.css                    second bundled theme (Linear-style)
  templates/
    starter-deck.md                  minimal new-deck template
  examples/
    reference-deck.md                full pattern showcase (editorial)
    reference-deck-soft-tech.md      same content, soft-tech theme
  exports/                           generated output (gitignored)
```
