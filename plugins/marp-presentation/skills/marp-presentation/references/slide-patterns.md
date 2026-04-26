# Slide patterns

The editorial theme ships six layout patterns. Apply via `<!-- _class: NAME -->`
at the top of a slide. Default (no `_class`) is a single-column content slide.

## Per-slide chrome conventions

Every non-title slide includes a brand marker that names the **current
agenda section**:

```markdown
<span class="brand">01 · Context</span>
```

Convention:
- The brand text matches the agenda item the slide belongs to
- Format is up to you — `01 · Context`, `Context`, `Section 01`, `Findings`
- On the agenda slide itself, use `<span class="brand">Agenda</span>`
- On a section-divider, use the upcoming section's name
- Update this string whenever you cross a section boundary

The theme renders these automatically from frontmatter / pagination:
- **Footer** (right side, italic grey) — from `footer:` directive
- **Page number** (right corner, italic terracotta) — from `paginate: true`

A slide can override the footer with `<!-- _footer: "..." -->` or hide it
with `<!-- _footer: "" -->`.

For a source / footnote line, use a dedicated paragraph:

```markdown
<p class="source">Source: ...</p>
```

It anchors to the bottom-left, separately from the footer.

---

## title

Cover slide. Suppress pagination and footer. The body uses four wrappers
that the theme expects:

```markdown
<!-- _class: title -->
<!-- _paginate: false -->
<!-- _footer: "" -->

<div class="t-top">

### Optional eyebrow

</div>

<div class="t-hero">

# Project title with *italic accent*

</div>

<div class="t-sub">

## Subtitle — one or two sentences of context.

</div>

<div class="t-meta">

<div><span>Date</span><strong>25 April 2026</strong></div>
<div><span>Author</span><strong>Author / organization</strong></div>

</div>
```

Notes:
- Hero (`h1`) renders at 108pt display serif **in terracotta accent
  color**, max 14ch. Use `*italics*` for emphasis — they render in the
  same display serif at the same weight.
- Eyebrow (`h3`) is optional. Leave the `<div class="t-top">` empty (or
  omit it) if you don't want one — the slot stays reserved.
- Meta uses two columns: `Date` and `Author`. Add more columns by adding
  more `<div>` children inside `.t-meta`.

## agenda

Numbered list, each item with an inline-italic description that the
theme breaks onto its own line as a small grey caption. Title is just
"Agenda" — no subtitle.

```markdown
<!-- _class: agenda -->

<span class="brand">Agenda</span>

# Agenda

1. Section one*Short description of what this section covers.*
2. Section two*Short description.*
3. Section three*Short description.*
4. Section four*Short description.*
```

The `*…*` directly after the item title becomes `<em>…</em>`; the theme
displays it as a block-level grey caption underneath. Don't put a space
before the `*` — keep it touching the title text.

## section-divider

Place between sections. Restates the agenda with the upcoming section
highlighted in terracotta and its description visible; the other items
are dimmed.

```markdown
<!-- _class: section-divider -->

<span class="brand">01 · Section one</span>

# Agenda

<ol>
<li class="current">Section one<em>Short description.</em></li>
<li>Section two<em>Short description.</em></li>
<li>Section three<em>Short description.</em></li>
<li>Section four<em>Short description.</em></li>
</ol>
```

Notes:
- Mark the upcoming item with `class="current"`. The CSS dims the other
  items and hides their descriptions, so the focus is on what's coming
  next.
- **Include the `<em>...</em>` description on every item**, even the
  inactive ones. The CSS uses `visibility: hidden` (not `display: none`)
  so the inactive items keep the same vertical positions they have on
  the agenda — without the placeholder text, items 2-4 would shift up
  and the layout would jump between agenda and divider.
- Markdown's `1. item` syntax can't carry a class — use raw `<ol><li>`
  HTML for this slide.
- Place a section-divider **before each major section transition** — it
  helps the audience track where the deck is.

## content (default)

The most common slide. No `_class` needed.

```markdown
<span class="brand">01 · Context</span>

# Action title states the takeaway in one sentence

## Optional subtitle for context.

<p class="lead">Lead paragraph — one sentence that frames the slide before the bullets.</p>

- **Evidence point one** — supporting sentence.
- **Evidence point two** — supporting sentence.
- **Evidence point three** — supporting sentence.

<p class="source">Source: ...</p>
```

Rule of thumb: **action title first, evidence second**. Drop the lead if
the slide is short. Bullets render with em-dash markers in terracotta.

## two-col

Two side-by-side columns under a shared title. Wrap the columns in
`<div class="columns">`; each column is a child `<div>`.

```markdown
<!-- _class: two-col -->

<span class="brand">02 · Findings</span>

# Two-column title

## Optional subtitle.

<div class="columns">
<div>

#### Left column subhead

Short paragraph.

- Bullet
- Bullet

</div>
<div>

#### Right column subhead

Short paragraph.

- Bullet
- Bullet

</div>
</div>

<p class="source">Source: ...</p>
```

Notes:
- Column subheads (`####` → `<h4>`) render in italic terracotta display serif.
- Body text and bullets are scaled down (15px / 14px) inside columns to
  prevent crowding.
- Blank lines around the inner markdown are required so MARP parses bold,
  italics, lists.

## cards

Three-card grid for recommendations, levers, options — anything that fits
a 3-up taxonomy.

```markdown
<!-- _class: cards -->

<span class="brand">03 · Recommendations</span>

# Card-grid title

## Optional subtitle.

<div class="grid">
<div class="card">

<p class="num">Item 01</p>

#### Card title

Short description.

<div class="meta"><span>Label A</span><strong>Value</strong></div>
<div class="meta"><span>Label B</span><strong>Value</strong></div>

</div>
<div class="card">

<p class="num">Item 02</p>

#### Card title

Short description.

<div class="meta"><span>Label A</span><strong>Value</strong></div>
<div class="meta"><span>Label B</span><strong>Value</strong></div>

</div>
<div class="card">

<p class="num">Item 03</p>

#### Card title

Short description.

<div class="meta"><span>Label A</span><strong>Value</strong></div>
<div class="meta"><span>Label B</span><strong>Value</strong></div>

</div>
</div>

<p class="source">Source: ...</p>
```

Card anatomy:
- 3px terracotta accent bar at the top
- `.num` paragraph — small italic terracotta label (e.g., `Lever 01`)
- `h4` title — display serif
- Description paragraph (small)
- One or more `.meta` rows — `<span>label</span><strong>value</strong>`,
  bottom-anchored

Three cards is the design intent. Two will work but look sparse; four
overflow the grid.

## statement

Single large pull-quote slide.

```markdown
<!-- _class: statement -->

<span class="brand">Statement</span>

# The single most important sentence, with *italic emphasis*.
```

`h1` is 76pt, max 18ch. Italic `<em>` inside it renders in terracotta —
use it to mark the load-bearing word.

---

## When to use what

| If you want to... | Use |
|---|---|
| Open a deck | `title` |
| Lay out the table of contents | `agenda` |
| Transition into a new section | `section-divider` |
| State a takeaway with supporting evidence | default (no class) |
| Compare two options or perspectives | `two-col` |
| Show 3 recommendations / levers / options | `cards` |
| Anchor a single statement | `statement` |
