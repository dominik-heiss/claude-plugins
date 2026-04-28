---
marp: true
theme: editorial          # or `soft-tech` — both ship with the plugin
paginate: true
size: 16:9
header: ""
footer: "Project name 2026 · Subtitle · Confidential"
---

<!-- ===========================================================
     STARTER DECK — minimal scaffold with the core patterns:
       title, agenda, section-divider, default content, two-col, cards

     For the full pattern catalog (cards-2, cards-4, process, matrix,
     kpi-hero, kpi-strip, compare, quote, timeline, closing) see:
       examples/reference-deck.md  →  rendered: examples/reference-deck.pdf
       skills/marp-presentation/references/slide-patterns.md

     None of the patterns are mandatory. When the content needs a
     different shape, build a custom layout. For deck-local CSS
     (e.g., a custom variant), use the frontmatter `style:` block
     above — slide-internal <style> tags get stripped by MARP.

     Example custom-CSS frontmatter:
       style: |
         section.my-custom .row { display: flex; gap: 16px; }
         section.my-custom .row > * { flex: 1; }
=========================================================== -->


<!-- _class: title -->
<!-- _paginate: false -->
<!-- _footer: "" -->

<div class="t-top">

<!-- Optional eyebrow — leave the t-top div empty (or omit it) if you don't want one -->

</div>

<div class="t-hero">

# Project title with *italic accent*

</div>

<div class="t-sub">

## Subtitle line — one or two sentences of context that frame the deck.

</div>

<div class="t-meta">

<div><span>Date</span><strong>25 April 2026</strong></div>
<div><span>Author</span><strong>Author / organization</strong></div>

</div>

---

<!-- _class: agenda -->

<span class="brand">Agenda</span>

# Agenda

1. Section one*Short description of what this section covers.*
2. Section two*Short description of what this section covers.*
3. Section three*Short description of what this section covers.*
4. Section four*Short description of what this section covers.*

---

<!-- _class: section-divider -->

<span class="brand">01 · Section one</span>

# Agenda

<ol>
<li class="current">Section one<em>Short description of what this section covers.</em></li>
<li>Section two<em>Short description of what this section covers.</em></li>
<li>Section three<em>Short description of what this section covers.</em></li>
<li>Section four<em>Short description of what this section covers.</em></li>
</ol>

---

<span class="brand">01 · Section one</span>

# Action title states the takeaway in one sentence

## Optional subtitle for context.

<p class="lead">Lead paragraph — one sentence that frames the slide before the bullets.</p>

- **Evidence point one** — short supporting sentence with the why behind it.
- **Evidence point two** — quantitative claim, source-backed.
- **Evidence point three** — final supporting beat.

<p class="source">Source: ...</p>

---

<!-- _class: two-col -->

<span class="brand">02 · Section two</span>

# Two-column comparison title

## Optional subtitle.

<div class="columns">
<div>

#### Left column subhead

Short paragraph in the left column.

- Bullet
- Bullet
- Bullet

</div>
<div>

#### Right column subhead

Short paragraph in the right column.

- Bullet
- Bullet
- Bullet

</div>
</div>

<p class="source">Source: ...</p>

---

<!-- _class: cards -->

<span class="brand">03 · Section three</span>

# Card-grid title

## Optional subtitle.

<div class="grid">
<div class="card">

<p class="num">Item 01</p>

#### Card title

Short description of this card.

<div class="meta"><span>Label A</span><strong>Value</strong></div>
<div class="meta"><span>Label B</span><strong>Value</strong></div>

</div>
<div class="card">

<p class="num">Item 02</p>

#### Card title

Short description of this card.

<div class="meta"><span>Label A</span><strong>Value</strong></div>
<div class="meta"><span>Label B</span><strong>Value</strong></div>

</div>
<div class="card">

<p class="num">Item 03</p>

#### Card title

Short description of this card.

<div class="meta"><span>Label A</span><strong>Value</strong></div>
<div class="meta"><span>Label B</span><strong>Value</strong></div>

</div>
</div>

<p class="source">Source: ...</p>
