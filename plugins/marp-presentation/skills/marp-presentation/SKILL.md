---
name: marp-presentation
description: Use when the user wants to create, edit, or export a MARP markdown presentation. Triggers on "build a deck", "create slides", "MARP", "presentation", "export to PDF", "slide pattern", or any markdown deck authoring task.
---

# marp-presentation

You help the user produce polished slide decks from markdown using MARP
and the bundled `editorial` theme — magazine/editorial aesthetic with
display-serif headings, terracotta accent, warm off-white paper.

## Workflow

1. **Confirm format**: 16:9 PDF (default), or HTML for fast preview
2. **Check the source**: existing `.md`, or start from
   `templates/starter-deck.md`
3. **Choose layout per slide**: the bundled patterns are starting points,
   not a closed set — see "Patterns are examples, not a cage" below
4. **Use the bundled theme**: `assets/themes/editorial.css` unless the
   user specifies another
5. **Export**: invoke `marp-cli` via `npx` — see
   `references/export-workflow.md`

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
theme: editorial
paginate: true
size: 16:9
header: ""
footer: "Project name 2026 · Subtitle · Confidential"
---
```

Override `theme:` only if the user has supplied a custom CSS.

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

| Pattern | `_class` | Wrappers expected in body |
|---|---|---|
| Title | `title` | `.t-top`, `.t-hero`, `.t-sub`, `.t-meta` |
| Agenda | `agenda` | `<span class="brand">`, ordered list with inline `*em*` descriptions |
| Content (default) | none | `<span class="brand">`, optional `.lead`, ul, optional `.source` |
| Two-column | `two-col` | `.columns` with two child `<div>`s |
| Card grid | `cards` | `.grid` with three `.card` children |
| Section divider | `section-divider` | `<span class="brand">`, h3, h1 |
| Statement | `statement` | h1 with optional `*em*` for terracotta accent |
