# MARP frontmatter and directives

## Global frontmatter

At the top of every deck file:

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

| Key | Effect |
|---|---|
| `marp: true` | Required — enables MARP processing |
| `theme: NAME` | Theme to use; matches the `@theme NAME` declaration in the CSS — `editorial` for the bundled theme |
| `paginate: true` | Show page numbers (rendered bottom-right in italic terracotta) |
| `footer: '...'` | Running footer text (rendered bottom-right, italic muted) |
| `header: '...'` | Running header text — leave empty (`""`) in the editorial theme; chrome lives in the `.brand` span instead |
| `size: 16:9` | Aspect ratio — `16:9` (default in this theme) or `4:3` |
| `class: foo` | Default class applied to every slide |

## Per-slide directives

Place HTML comments at the top of a slide, before content. Underscore
prefix = local to that slide only.

```markdown
<!-- _class: title -->
<!-- _paginate: false -->
<!-- _footer: '' -->
<!-- _header: '' -->
<!-- _backgroundColor: '#0a1f3d' -->
<!-- _color: '#ffffff' -->
```

| Directive | Use |
|---|---|
| `_class` | Apply a layout pattern (`title`, `section`, `matrix-2x2`, …) |
| `_paginate: false` | Hide page number on this slide |
| `_footer: ''` | Hide footer on this slide |
| `_header: '...'` | Override header for this slide |
| `_backgroundColor` / `_color` | Per-slide override (theme normally handles this) |

## Slide separator

Three dashes on their own line:

```markdown
---
```

The first `---` block at the top of the file is YAML frontmatter; every
subsequent `---` starts a new slide.

## Speaker notes

HTML comments inside a slide that **don't** start with an underscore are
treated as speaker notes — visible in presenter mode, hidden in print.

```markdown
# Slide title

Visible content

<!-- These are speaker notes, not directives. -->
```

The convention: directives use `_name`; everything else is a note.

## Local vs global

Drop the underscore to make a directive apply from that slide *onward*:

```markdown
<!-- class: takeaway -->
```

Keep the underscore to scope it to the current slide only:

```markdown
<!-- _class: takeaway -->
```

Use the underscore form by default — it's less surprising.
