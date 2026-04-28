# Slide patterns

Both bundled themes (`editorial` and `soft-tech`) implement the same
pattern set, so the markdown below renders cleanly under either
theme. Apply via `<!-- _class: NAME -->` at the top of a slide.
Default (no `_class`) is a single-column content slide.

> **These are examples, not a closed catalog.** They cover the common
> shapes (cover, agenda, content, two-col, cards, divider, pull-quote)
> and are the right default when they fit. When the content needs
> something different — a 2×2 matrix, a timeline, a KPI hero, an
> asymmetric split, an annotated chart — **build a custom layout**
> using the design language (CSS variables, typography scale, chrome
> zones). See "Patterns are examples, not a cage" in `SKILL.md` for
> guidance.

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

## three-col / four-col

Same `.columns` wrapper as `two-col`, just more children. Type and gap
scale down with column count so the content stays readable.

```markdown
<!-- _class: three-col -->

<div class="columns">
<div>

#### Column subhead

Short paragraph.

- Bullet
- Bullet

</div>
<div>...</div>
<div>...</div>
</div>
```

For four columns, use `<!-- _class: four-col -->` and four children.
Keep each column to a paragraph plus ~3 bullets — beyond that, type
crowds.

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

Three cards is the design intent for `cards`. For two or four cards use
the dedicated variants — they tune padding and type sizes for the
different column count.

## cards-2

Two larger cards side-by-side. Use when each option deserves more room
(deeper description, more meta rows). Padding and type are scaled up.

```markdown
<!-- _class: cards-2 -->

<span class="brand">03 · Recommendations</span>

# Two larger cards for deeper content

## Optional subtitle.

<div class="grid">
<div class="card">

<p class="num">Option A</p>

#### Card title

Longer description — uses the extra room.

<div class="meta"><span>Investment</span><strong>€2.4M</strong></div>
<div class="meta"><span>Payback</span><strong>14 months</strong></div>

</div>
<div class="card">

<p class="num">Option B</p>

#### Card title

Longer description.

<div class="meta"><span>Investment</span><strong>€3.8M</strong></div>
<div class="meta"><span>Payback</span><strong>22 months</strong></div>

</div>
</div>
```

## cards-4

Four denser cards in a row. Use when you have parallel options that fit
a compact format. Padding and type are scaled down.

```markdown
<!-- _class: cards-4 -->

<div class="grid">
<div class="card"><p class="num">Lever 01</p>
#### Title
Short description.
<div class="meta"><span>Impact</span><strong>High</strong></div>
</div>
<!-- ...repeat for cards 2–4 ... -->
</div>
```

Same `.grid` + `.card` structure as `cards`. Pick the variant by
`_class`. **All three (`cards`, `cards-2`, `cards-4`) use the same
wrappers** — switching is just a class change.

## process

Horizontal N-step **sequential** process. Each step shows the phase
number and title in a paper-2 head box (with the terracotta accent
bar), and the description sits **outside the box** on the paper canvas
below. A terracotta arrow (→) connects each step to the next,
signalling sequentiality and distinguishing this pattern from the
non-sequential cards / column layouts.

**Children flex: 1** — the number of steps is determined by the
number of `<div class="step">` children, no CSS change needed (3–7
work well; beyond that, type starts to crowd).

```markdown
<!-- _class: process -->

<span class="brand">03 · Recommendations</span>

# Five-phase implementation walks the program through one year

## Optional subtitle.

<div class="steps">
<div class="step">
<div class="step-head">
<p class="step-num">Phase 01</p>
<p class="step-title">Mobilize</p>
</div>
<p class="step-desc">Steerco signs charter; workstream leads named.</p>

- Charter signed
- Leads named
- Baseline lock

</div>
<div class="step">
<div class="step-head">
<p class="step-num">Phase 02</p>
<p class="step-title">Pilot</p>
</div>
<p class="step-desc">First two interventions live in two business units.</p>

- Two pilot units
- Weekly readout

</div>
<!-- ...add or remove steps; layout redistributes ... -->
</div>
```

Notes:
- The `.step-head` wrapper is required — it's what becomes the box.
- Keep `.step-desc` as a sibling **outside** `.step-head`; it must not
  sit inside the head, otherwise it'll be drawn on the paper-2 surface.
- An optional `<ul>` sibling below `.step-desc` adds short bullets
  (deliverables, gates, owners). Keep them to 2–4 short items per step
  so the row stays readable.
- The arrow between steps is auto-generated via `::after` on every
  `.step` except the last one. No markup needed.
- `.step-title` looks best at one line. Keep titles short (1–3 words).

## kpi-strip

N KPIs in a row — big numbers, terracotta accent, label, optional delta
caption. **Children flex: 1**, so 3, 4, or 5 stats all distribute
evenly.

```markdown
<!-- _class: kpi-strip -->

<span class="brand">02 · Findings</span>

# Four indicators tell the same story

## Optional subtitle.

<div class="strip">
<div class="stat">
<p class="num"><em>+34%</em></p>
<p class="label">Throughput</p>
<p class="delta">vs. Q4 2024 baseline</p>

- Pilot units only
- Verified Q1 2026

</div>
<!-- ...repeat ... -->
</div>
```

`<em>` inside `.num` paints that segment in accent — useful for
"+12%" patterns where you want the value highlighted.

An optional `<ul>` below `.delta` adds short qualifying notes
(scope, source, exclusions). Keep each to 2–3 short items so the
strip stays scannable.

## timeline

Vertical timeline with date marker + event title + description per row.
**Children flex: 1** — number of events is flexible.

```markdown
<!-- _class: timeline -->

<span class="brand">04 · Next steps</span>

# Milestones over the next six months

<div class="events">
<div class="event">
<p class="when">Apr 2026</p>
<div class="what">

#### Mobilize and align

Steerco signs charter; workstream leads named.

</div>
</div>
<!-- ...repeat ... -->
</div>
```

## matrix

2×2 quadrant for strategic frameworks (impact/feasibility,
effort/value, etc.). Mark the focus quadrant with `class="q highlight"`
to give it a stronger accent bar.

```markdown
<!-- _class: matrix -->

<span class="brand">02 · Findings</span>

# Two dimensions reveal where the opportunity sits

## Optional subtitle.

<div class="quadrants">
<div class="axis-y"><span>Low</span><span>High</span></div>
<div class="q q1">
<h4>Quick wins</h4>
<p>Top-left quadrant description.</p>
</div>
<div class="q q2 highlight">
<h4>Strategic bets</h4>
<p>Top-right quadrant — the focus.</p>
</div>
<div class="q q3">
<h4>Fill-ins</h4>
<p>Bottom-left.</p>
</div>
<div class="q q4">
<h4>Major projects</h4>
<p>Bottom-right.</p>
</div>
<div class="axis-x"><span>Low ← Feasibility</span><span>Feasibility → High</span></div>
</div>
```

`.q1` is upper-left, `.q2` upper-right, `.q3` lower-left, `.q4`
lower-right. Y-axis spans go in display order (first = bottom because
of vertical-rl rendering — so put `Low` first to put it at the bottom
visually).

## kpi-hero

One big headline number with supporting context and up to ~3 sub-stats.

```markdown
<!-- _class: kpi-hero -->

<span class="brand">02 · Findings</span>

# One number captures the size of the prize

## Optional subtitle.

<div class="hero-stat">
<div>
<p class="big"><span class="cur">€</span>42<small>M</small></p>
</div>
<div class="ctx">

<p>Annual run-rate value at maturity — context paragraph.</p>

<div class="sub">
<div><strong>+18 pp</strong><span>Margin uplift</span></div>
<div><strong>2.4×</strong><span>Cycle-time gain</span></div>
<div><strong>14 mo</strong><span>Payback</span></div>
</div>

</div>
</div>
```

Use `<span class="cur">` for currency symbols and `<small>` for
unit suffixes (M, k, %). They render at ~50% / 40% the main number
size and in ink color, so the number itself dominates.

## compare

Two-side "vs" layout with a center divider. Use when the slide is
explicitly about a trade-off between two options.

```markdown
<!-- _class: compare -->

<span class="brand">03 · Recommendations</span>

# Speed versus optionality

## Recommended path picks reversibility over fastest delivery.

<div class="vs">
<div class="side">

#### Build now

Short framing paragraph.

- Bullet
- Bullet

</div>
<div class="divider"></div>
<div class="side">

#### Buy and adapt

Short framing paragraph.

- Bullet
- Bullet

</div>
</div>
```

The empty `<div class="divider">` paints the central rule and the "vs"
marker.

## options

Two-option matrix with the same shape on each side: title bar (with
optional `recommended` badge), short lead paragraph, support bullets,
and a 2×2 KPI grid anchored to the bottom of the column. A center
hairline separates the two sides. Use this when the slide's job is to
**recommend one of two paths** with the trade-off visible at a glance.

```markdown
<!-- _class: options -->

<span class="brand">03 · Recommendations</span>

# Two paths to capture the next 24 months

## Both options reach the same target — they differ in capital, speed, and risk.

<div class="opts">
<div class="opt">

<div class="opt-head">
<div class="opt-title">Option A — Build in-house</div>
<span class="badge recommended">Recommended</span>
</div>

<p class="lead">Short lead — invest in a dedicated team and own the customer relationship end-to-end.</p>

- Bullet point one
- Bullet point two
- Bullet point three

<div class="stats">
<div><p class="k">Time to impact</p><p class="v">14 mo</p></div>
<div><p class="k">Capex</p><p class="v warn">€ 8.4 m</p></div>
<div><p class="k">EBIT lift Yr 3</p><p class="v pos">+ 6.2 pp</p></div>
<div><p class="k">Strategic fit</p><p class="v">High</p></div>
</div>

</div>
<div class="divider"></div>
<div class="opt">

<div class="opt-head">
<div class="opt-title">Option B — Partner & integrate</div>
<span class="badge">Alternative</span>
</div>

<p class="lead">Short lead — license the platform and focus on integration and channels.</p>

- Bullet point one
- Bullet point two
- Bullet point three

<div class="stats">
<div><p class="k">Time to impact</p><p class="v pos">6 mo</p></div>
<div><p class="k">Capex</p><p class="v">€ 2.1 m</p></div>
<div><p class="k">EBIT lift Yr 3</p><p class="v">+ 3.4 pp</p></div>
<div><p class="k">Strategic fit</p><p class="v warn">Medium</p></div>
</div>

</div>
</div>

<p class="source">Source: ...</p>
```

Notes:
- The `.opt-title` is a plain `<div>` (not an h-tag) — this avoids
  conflicting with the slide's own h1/h2.
- `.badge` paints in muted style; add `.recommended` for the accent
  variant on the preferred option.
- Inside `.stats`, mark a value with `class="v pos"` for positive
  framing and `class="v warn"` for caution — the colors come from the
  active theme.
- Keep each column tight — the budget is a one-sentence lead, three
  short bullets, and the four KPIs.
- Differs from `compare`: `compare` is a free-form "vs" layout for
  arguments. `options` is a structured option matrix when the
  audience needs a recommendation.

## quote

Pull-quote with attribution (name + role). Differs from `statement` by
adding the source.

```markdown
<!-- _class: quote -->

<!-- _footer: '' -->

<span class="brand">02 · Findings</span>

<div class="quote-body">

The quote text — the leading and trailing curly quotes are added by
CSS, so don't type them yourself.

</div>

<div class="attribution">
<strong>Person Name</strong>
<span>Role · Organization</span>
</div>
```

## closing

Final slide — Q&A, thanks, and contact details.

```markdown
<!-- _class: closing -->

<!-- _paginate: false -->

<!-- _footer: '' -->

<span class="brand">Q&A</span>

<div class="close-block">

# Discussion *and questions.*

<div class="contact">
<div><span>Lead</span><strong>Name</strong></div>
<div><span>Email</span><strong>name@org.com</strong></div>
<div><span>Date</span><strong>26 April 2026</strong></div>
</div>

</div>
```


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
| Compare two options or perspectives | `two-col`, or `compare` for explicit "vs" framing |
| Recommend one of two options with KPIs | `options` |
| Lay out 3 or 4 themes side-by-side (text, not cards) | `three-col` / `four-col` |
| Show 3 recommendations / levers / options | `cards` |
| Show 2 deeper options / 4 compact options | `cards-2` / `cards-4` |
| Walk through a phased plan (3–7 steps) | `process` |
| Headline a metric with supporting context | `kpi-hero` |
| Show several KPIs side-by-side | `kpi-strip` |
| Plot initiatives on a 2×2 framework | `matrix` |
| Show milestones over time | `timeline` |
| Anchor a single sentence | `statement` |
| Quote a person with attribution | `quote` |
| Close the deck (Q&A / contact) | `closing` |
| Need something else? | Build a custom layout — see `SKILL.md` |

## Custom CSS — frontmatter `style:` works, slide-internal `<style>` doesn't

When a custom layout needs new CSS that lives only with the deck (not
inside `editorial.css`), put it in the **frontmatter `style:` block**:

```yaml
---
marp: true
theme: editorial
style: |
  section.my-custom .row { display: flex; gap: 16px; }
  section.my-custom .row > * { flex: 1; }
---
```

Then use `<!-- _class: my-custom -->` on the slide. MARP injects the
frontmatter `style:` value as a global `<style>` block.

**Slide-internal `<style>` tags get stripped** by the MARP markdown
parser — anything inside `<style>...</style>` placed directly in the
markdown body has no effect. If you find your CSS isn't applying,
this is the most likely cause. See `references/pitfalls.md`.
