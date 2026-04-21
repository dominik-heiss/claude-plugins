# MARP Slide Patterns — Reference Catalog

Each pattern is a layout class applied via `<!-- _class: xxx -->`. All
examples use the `consulting` theme at
`${CLAUDE_PLUGIN_ROOT}/assets/marp-themes/consulting.css`.

## Deck front matter (required once at the top)

```yaml
---
marp: true
theme: consulting
paginate: true
footer: 'ClientCo · Market Entry · Confidential'
---
```

- `paginate: true` — shows the page number on every slide (except those
  that disable it explicitly)
- `footer: '…'` — appears bottom-right on content slides. Keep it short:
  client, engagement, confidentiality marker.

---

## `title` — Title slide

Centered-left layout, oversized headline, no footer, no pagination.

```markdown
<!-- _class: title -->
<!-- _paginate: false -->
<!-- _footer: '' -->

# European Heat Pump Market — Investment Thesis

### Phase 2 Findings · Prepared for the Investment Committee

**[Firm Name] · Engagement Team**
2026-04-21
```

---

## `agenda` — Agenda / table of contents

Numbered list, generous line-height. Use at the start of longer decks.

```markdown
<!-- _class: agenda -->

# Agenda

1. Market opportunity
2. Competitive positioning
3. Strategic options
4. Recommendation
5. Implementation roadmap
6. Risk and next steps
```

---

## `section` — Section divider

Navy background, white 44pt headline, centered-left. Use between major
sections to break a long deck into digestible chunks. Always disable
footer + pagination on section dividers.

```markdown
<!-- _class: section -->
<!-- _paginate: false -->
<!-- _footer: '' -->

# 1. Market opportunity
```

---

## `content` — Default content slide

Action title + subtitle + supporting bullets + source line. The subtitle
uses `##` and is a descriptive one-liner beneath the action title — not
every slide needs one.

```markdown
<!-- _class: content -->

# Market is attractive, with structural tailwinds supporting growth

## European EV-charging market, 2020-2030 outlook

- European EV-charging market grew 38% p.a. from 2020-2024 (SRC001)
- Top 5 operators control only 42% share — market remains fragmented
- Regulation (AFIR) mandates 6× capacity by 2030 (SRC002)
- Unit economics improving: payback period down from 7 to 4 years

<p class="src">Source: Internal analysis, Market Report 2024</p>
```

Rules:
- **Max 5 bullets** — hard ceiling
- **Action title, not topic title** — if you can replace it with
  "Market Overview" and lose nothing, it's not a real action title
- **Inline `(SRCXXX)` citations** — on the claim itself, not just in
  the source line

---

## `two-col` — 2-column comparison

Two `<div class="col">` blocks sit side-by-side with a thin divider
between them. Full-width `h1`, `h2` and `<p class="src">` elements
automatically span both columns.

```markdown
<!-- _class: two-col -->

# Strategic tension between speed and quality drives the market-entry choice

<div class="col">

**Speed**

- Market window closing by 2027
- First movers capture prime locations
- Competitor X raising EUR 500m now
- Every month of delay = locations lost

</div>
<div class="col">

**Quality**

- Hardware reliability defines long-term economics
- Poor install sites drive 30% of churn
- Brand damage from bad sites is hard to reverse
- Capex payback depends on uptime

</div>
```

Tips:
- Put an **empty line between the `<div>` tag and the markdown content**
  inside — without it, MARP may not render bullets correctly
- Keep each column balanced (±1 bullet) — asymmetric columns look wrong

---

## `matrix-2x2` — 2×2 strategic matrix

Four `<div class="quadrant">` blocks with positional classes
`q-tl` / `q-tr` / `q-bl` / `q-br`. Add `q-hl` to a quadrant to highlight
it as the recommended / priority zone (thicker border, soft
background). Axis labels go in a trailing `<p class="src">`.

```markdown
<!-- _class: matrix-2x2 -->

# Prioritize expansion in high-attractiveness, high-fit segments

<div class="quadrant q-tl q-hl">

**Fleet depots**
- High attractiveness
- High fit

</div>
<div class="quadrant q-tr">

**Highway**
- High attractiveness
- Lower fit

</div>
<div class="quadrant q-bl">

**Urban AC**
- Lower attractiveness
- High fit

</div>
<div class="quadrant q-br">

**Retail parking**
- Lower attractiveness
- Lower fit

</div>

<p class="src">x-axis: Strategic fit &nbsp;·&nbsp; y-axis: Market attractiveness</p>
```

Tips:
- Highlight at most **one** quadrant — if two are "priority", the
  message isn't sharp
- Keep each quadrant to 2-3 short bullets — they're sized for
  scannability, not depth
- The outer action title still carries the "so what" — the quadrants
  are evidence

---

## `kpi-row` — KPI row

3-4 big numbers in a horizontal row, each with a value and a label. Use
`<div class="kpi">` with `.kpi-value` and `.kpi-label` inside. Keep to
3-4 KPIs max — more and the row cramps.

```markdown
<!-- _class: kpi-row -->

# Market fundamentals support the investment thesis

<div class="kpi">
  <div class="kpi-value">EUR 2.1B</div>
  <div class="kpi-label">Addressable market 2024</div>
</div>
<div class="kpi">
  <div class="kpi-value">8.4%</div>
  <div class="kpi-label">CAGR 2024-2030</div>
</div>
<div class="kpi">
  <div class="kpi-value">42%</div>
  <div class="kpi-label">Top-5 concentration</div>
</div>
<div class="kpi">
  <div class="kpi-value">4 yrs</div>
  <div class="kpi-label">Payback (improved from 7)</div>
</div>

<p class="src">Source: Internal analysis, 2024</p>
```

Tips:
- KPI values should **fit on one line** (8-12 characters max). "EUR
  2.1B" works; "EUR 2,145 million" doesn't
- Labels are 13pt and muted — the value carries the punch
- Use this pattern for phase-gate openers and executive summaries

---

## `quote` — Stakeholder quote

Single pull-quote, large italic, navy text with a red accent bar on the
left. Attribute the quote directly below.

```markdown
<!-- _class: quote -->

# Expert view reframes the bottleneck

> "Charging is not the bottleneck anymore —
> grid connection is."

— Head of Strategy, Major OEM · Expert interview (SRC003)
```

Tips:
- Keep the quote to **≤2 lines** — longer quotes lose impact
- The attribution is a plain paragraph, not a blockquote
- Use quotes sparingly (max 1-2 per deck) — they lose weight when
  overused

---

## `takeaway` — Recommendation / call-to-action

Soft grey background, accent red headline. Use at the end of each
section and as the governing-thought slide. The action title IS the
recommendation — bullets give the rationale.

```markdown
<!-- _class: takeaway -->

# Enter the market now via asset-light partnership — add full control in Phase 2

- Asset-light model de-risks the first 18 months
- Partnership with utility X gives grid-connection priority
- Optionality: expand to owned operations from 2027 onward
- Capital commitment stays below EUR 80m in Phase 1
```

---

## `back` — Back cover

Navy background, centered, no footer, no pagination. Keep it short —
thank-you, contact, confidentiality marker.

```markdown
<!-- _class: back -->
<!-- _paginate: false -->
<!-- _footer: '' -->

# Thank you

**[Firm Name] · [Engagement Lead Name]**
[email]@[firm].com
```

---

## Combining patterns across a deck

A typical final deck (20-25 slides):

| Slide range | Pattern |
|---|---|
| 1 | `title` |
| 2 | `content` — executive summary (1 slide, the answer) |
| 3 | `agenda` |
| 4 | `section` — "1. Market opportunity" |
| 5-7 | `content` and `kpi-row` — market data |
| 8 | `section` — "2. Competitive positioning" |
| 9-10 | `matrix-2x2`, `content` |
| 11 | `section` — "3. Strategic options" |
| 12-13 | `two-col`, `content` |
| 14 | `section` — "4. Recommendation" |
| 15 | `takeaway` — governing thought + rationale |
| 16 | `quote` — validating stakeholder voice |
| 17 | `content` — risks and mitigations |
| 18 | `content` — next steps |
| 19 | `back` |
| 20+ | Appendix (`content` default) |

## Anti-patterns

- **No action title** → the slide does not earn its place. Replace or
  remove.
- **Mixing time bases** → "Market 2024 / growth 2028-30" without flagging
  the switch. Make the basis explicit or split the slide.
- **Decorative imagery** → top-tier decks have almost no decoration.
  Every image must earn its place as data or evidence.
- **Overflow** → if content runs off the slide in the PDF export, split
  the slide. Never shrink the font below 13pt on the body or 24pt on
  the title.
- **Bullets everywhere** → mix in `kpi-row`, `quote`, `matrix-2x2`,
  `two-col`. A deck of only default content slides feels like a memo.
