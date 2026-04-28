---
name: marp-presentation
description: Use when the user wants to create, edit, or export a MARP markdown presentation. Triggers on "build a deck", "create slides", "MARP", "presentation", "export to PDF", "slide pattern", or any markdown deck authoring task.
---

# marp-presentation

You help the user produce polished slide decks from markdown using
MARP. Two themes ship with the plugin — the user picks one per deck
via the `theme:` frontmatter. The same markdown contract (chrome via
`.brand` / `.source` / frontmatter `footer:` + `paginate: true`,
patterns via `_class:`) works for both, so swapping themes is a
one-line change.

## Bundled themes

| Theme | `theme:` value | Aesthetic |
|---|---|---|
| Editorial (default) | `editorial` | Magazine/editorial — Fraunces display serif + Inter, terracotta accent, warm off-white paper, paper-2 surfaces on cards |
| Soft Tech | `soft-tech` | Linear/Vercel/Stripe-doc — Inter sans + JetBrains Mono micro labels, indigo accent, near-white canvas, line-bordered surfaces |

Both themes support the **same pattern set**, so a deck written for
one renders cleanly under the other. Pick by the user's brief — when
unsure, ask once.

## Workflow

1. **Resolve the active design.** Before generating or exporting any
   deck, determine which theme to use using this precedence:
   1. The deck's own frontmatter `theme:` if present — author's intent
      always wins.
   2. Otherwise, read `.marp-design` from the current working directory
      if it exists. The file is a single line containing either a
      bundled design name (`editorial`, `soft-tech`) or a path to a
      custom CSS file. The user manages this via `/define-design`.
   3. Otherwise, fall back to `editorial`.
   When generating new deck markdown, write the resolved design into
   the deck's frontmatter `theme:` line so the deck is portable.
2. **Confirm format**: HTML by default. Render PDF only when the user
   explicitly asks (PDF needs Chromium and is slower). Never render
   PDF speculatively or "as a bonus".
3. **Check the source**: existing `.md`, or start from
   `templates/starter-deck.md`.
4. **Choose layout per slide**: the bundled patterns are starting
   points, not a closed set — see "Patterns are examples, not a cage"
   below.
5. **Export**: invoke `marp-cli` via `npx` — see
   `references/export-workflow.md`. Default output filename is
   `<deck>.html`; only add a `-<theme>` suffix if a render from a
   different theme already exists for the same deck.

## Switching designs

The user can pin a design for the current project via the
`/define-design` command:

- `/define-design` (no args) — lists bundled designs with their use
  cases and offers to switch, re-skin, or fork.
- `/define-design <name|path>` — writes the choice to `.marp-design`
  in the cwd. From that point on, follow the precedence chain in
  step 1 above.

## Patterns are examples, not a cage

`references/slide-patterns.md` and `examples/reference-deck.md` document
**seven canned patterns** (title, agenda, section-divider, default
content, two-col, cards, statement). They are the most common shapes
and a good fall-back — but they are **examples of what the design
language can do, not the only allowed layouts**.

When the content benefits from something different, build it. Common
reasons to step outside the canned patterns:

- A 2×2 matrix, quadrant chart, or 4-up grid
- A timeline / horizontal stages with arrows or rule
- A single big number / KPI tile with supporting context
- A stacked-column layout with a sidebar
- A hero image / chart with annotation callouts
- An "vs." compare slide with a center divider
- Asymmetric splits (e.g., 1/3 lead column + 2/3 detail)
- Anything else the content actually wants

How to do it well:

- **Stay inside the design language.** Use the existing CSS variables
  (`var(--c-accent)`, `var(--c-paper-2)`, `var(--font-display)`, etc.),
  the existing typography scale (h1/h2/h3/h4 sizes), and the same
  vertical rhythm (top-chrome / bottom-chrome zones).
- **Compose with HTML + inline `style="..."` or scoped style blocks.**
  MARP markdown happily accepts custom HTML structures inside a slide.
- **Add a new `_class`** when a layout will recur across slides — drop
  the matching CSS into a per-deck `<style>` block at the top of the
  markdown, or extend `editorial.css` if it's broadly useful.
- **Reuse the chrome.** Brand marker top-left, footer / page number
  bottom-right, source line bottom-left — these stay even on custom
  layouts.

Reach for a canned pattern when it fits. When it doesn't, design the
slide for the content.

## Density check — pick the layout BEFORE you author

The slide canvas is fixed (1280×720) and the bottom-chrome zone (64px)
is sacred. Default content with too many bullets silently overflows
the bottom — `overflow: hidden` hides what doesn't fit. Always size
the content against these budgets before committing to a layout:

| Layout | Budget |
|---|---|
| Default content (h1 + h2 + lead + bullets) | ≤ 5 bullets, each ≤ 2 wrapped lines |
| Default content without lead | ≤ 6–7 bullets |
| `two-col` | per column: paragraph + ~3 bullets |
| `three-col` | per column: short paragraph + ~3 short bullets |
| `four-col` | per column: short paragraph + 2–3 short bullets |
| `cards` (3-up) | per card: ~25 words description |
| `cards-4` | per card: ~15 words description |
| `process` | 3–7 phases, each with ≤ 1 sentence description |
| `options` | per option: 1 short lead + 3 short bullets + 4 KPIs |

When the content exceeds the budget, **switch layout** before authoring:

- 6+ short, parallel bullets → `cards` (3-up or 4-up) or `two-col`
- 6+ longer bullets → split across two slides, or use `three-col` / `four-col`
- A sequential plan with descriptions → `process` pattern
- Several stats with context → `kpi-strip` or `kpi-hero`

After rendering, **visually verify** every content-dense slide. If
anything is cut off at the bottom, restructure — never shrink type
below the theme defaults.

## Authoring rules

- Every content slide has an **action title** as `h1` — full sentence
  that states the takeaway, not a topic label
- Optional **subtitle** as `h2` (italic display serif) for context
- Optional **lead paragraph** (`<p class="lead">`) right after the
  subtitle — one sentence to frame the body
- Body supports the title with evidence: bullets, columns, cards
- **Brand marker** at the top of every non-title slide:
  `<span class="brand">SECTION · NN</span>`
- **Source line** at the bottom-left when claims are externally backed:
  `<p class="source">Source: ...</p>`
- Footer + page number are automatic via frontmatter

## Default frontmatter

```yaml
---
marp: true
theme: editorial   # or `soft-tech`
paginate: true
size: 16:9
header: ""
footer: "Project name 2026 · Subtitle · Confidential"
---
```

Pick `theme:` based on the brief — `editorial` (default, magazine) or
`soft-tech` (Linear-style). If the project has a `.marp-design` file
set via `/define-design`, prefer that value unless the user has asked
for a different design for this specific deck. Override only if the
user has supplied a custom CSS.

## When to read which reference

- Picking a layout → `references/slide-patterns.md`
- MARP directives / frontmatter → `references/frontmatter.md`
- Images, backgrounds, sizing → `references/images-and-media.md`
- Customizing theme colors / fonts → `references/theme-customization.md`
- Exporting → `references/export-workflow.md`
- Things that commonly break → `references/pitfalls.md`
- Full pattern showcase → `examples/reference-deck.md`

## Bundled patterns at a glance

These are the patterns the theme has CSS for out of the box. Pick one
when it fits the content; otherwise build a custom layout (see above).

**Core**

| Pattern | `_class` | Wrappers expected in body |
|---|---|---|
| Title | `title` | `.t-top`, `.t-hero`, `.t-sub`, `.t-meta` |
| Agenda | `agenda` | `<span class="brand">`, ordered list with inline `*em*` descriptions |
| Section divider | `section-divider` | `<span class="brand">`, h3, h1, `<ol>` with `class="current"` on active item |
| Content (default) | none | `<span class="brand">`, optional `.lead`, ul, optional `.source` |
| Two-column | `two-col` | `.columns` with two child `<div>`s |
| Three-column | `three-col` | `.columns` with three child `<div>`s (denser type) |
| Four-column | `four-col` | `.columns` with four child `<div>`s (denser still) |
| Cards 3-up | `cards` | `.grid` with three `.card` children |
| Cards 2-up | `cards-2` | `.grid` with two larger `.card` children |
| Cards 4-up | `cards-4` | `.grid` with four denser `.card` children |
| Statement | `statement` | h1 with optional `*em*` for terracotta accent |

**Scalable** — children get `flex: 1`, so the number of items can vary
(typically 3–7) without touching CSS.

| Pattern | `_class` | Body |
|---|---|---|
| Process | `process` | `.steps` + N× `.step` (each with `.step-head` containing `.step-num` + `.step-title`, plus `.step-desc` outside the head) |
| KPI strip | `kpi-strip` | `.strip` + N× `.stat` (each with `.num`, `.label`, optional `.delta`) |
| Timeline | `timeline` | `.events` + N× `.event` (each with `.when` + `.what` group) |

**Specialty**

| Pattern | `_class` | Body |
|---|---|---|
| 2×2 matrix | `matrix` | `.quadrants` with `.axis-y`, `.axis-x`, four `.q.q1..q4` cells |
| KPI hero | `kpi-hero` | `.hero-stat` grid: big number on left, `.ctx` (with `.sub` stats) on right |
| Compare | `compare` | `.vs` with two `.side` divs flanking a `.divider` |
| Options | `options` | `.opts` with two `.opt` columns (each: `.opt-head` + `.lead` + `ul` + `.stats` 2×2 grid) flanking a `.divider`; one column may carry the `recommended` badge |
| Quote | `quote` | `.quote-body` (the quote) + `.attribution` (name, role) |
| Closing | `closing` | `.close-block` with h1 and optional `.contact` row |
