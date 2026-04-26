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
3. **Apply patterns**: pick the right `_class` per slide — see
   `references/slide-patterns.md`
4. **Use the bundled theme**: `assets/themes/editorial.css` unless the
   user specifies another
5. **Export**: invoke `marp-cli` via `npx` — see
   `references/export-workflow.md`

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

## Patterns at a glance

| Pattern | `_class` | Wrappers expected in body |
|---|---|---|
| Title | `title` | `.t-top`, `.t-hero`, `.t-sub`, `.t-meta` |
| Agenda | `agenda` | `<span class="brand">`, ordered list with inline `*em*` descriptions |
| Content (default) | none | `<span class="brand">`, optional `.lead`, ul, optional `.source` |
| Two-column | `two-col` | `.columns` with two child `<div>`s |
| Card grid | `cards` | `.grid` with three `.card` children |
| Section divider | `section-divider` | `<span class="brand">`, h3, h1 |
| Statement | `statement` | h1 with optional `*em*` for terracotta accent |
