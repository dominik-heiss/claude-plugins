---
marp: true
theme: editorial
paginate: true
size: 16:9
header: ""
footer: "Lorem ipsum 2026 · Dolor sit amet · Confidential"
---

<!-- ===========================================================
     EDITORIAL — REFERENCE DECK
     Demonstrates every layout pattern in the editorial theme.

     Core patterns (apply via `_class:` per slide):
       title              → cover slide (hero)
       agenda             → numbered agenda with descriptions
       section-divider    → between sections — agenda layout, current item highlighted
       statement          → large pull-quote / single statement
       two-col            → two-column content (with .columns wrapper)
       cards              → three-card grid (.grid + 3× .card)
       cards-2            → two-card grid (larger cards, more breathing room)
       cards-4            → four-card grid (denser type for tighter content)

     Scalable patterns (children get flex: 1, add/remove items freely):
       process            → horizontal N-step process (.steps + N× .step)
       kpi-strip          → N KPIs in a row (.strip + N× .stat)
       timeline           → vertical events (.events + N× .event)

     Specialty patterns:
       matrix             → 2x2 quadrant (axes + 4× .q)
       kpi-hero           → one big number + supporting context
       compare            → side-by-side "vs" comparison
       quote              → pull-quote with attribution
       closing            → Q&A / thanks / contact

     Default (no _class)  → single-column content slide

     Brand marker convention: every non-title slide opens with
       <span class="brand">SECTION NAME</span>
     reflecting the current agenda section. Update it per slide.

     None of these are mandatory — they are design starting points.
     When the content needs a different shape, build a custom layout
     using the design language (see SKILL.md / "Patterns are examples,
     not a cage"). The frontmatter `style:` block is the right place
     for slide-class-specific CSS — slide-internal <style> tags are
     stripped by MARP. See references/pitfalls.md.
=========================================================== -->


<!-- _class: title -->
<!-- _paginate: false -->
<!-- _footer: "" -->

<div class="t-top">

### Optional eyebrow

</div>

<div class="t-hero">

# Lorem ipsum dolor *sit amet*

</div>

<div class="t-sub">

## Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua — ut enim ad minim veniam quis nostrud exercitation ullamco.

</div>

<div class="t-meta">

<div><span>Date</span><strong>25 April 2026</strong></div>
<div><span>Author</span><strong>Lorem Ipsum Advisory</strong></div>

</div>

---

<!-- _class: agenda -->

<span class="brand">Agenda</span>

# Agenda

1. Context*Dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.*
2. Findings*Veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure.*
3. Recommendations*Cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum sed ut perspiciatis.*
4. Next steps*Voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione.*

---

<!-- _class: section-divider -->

<span class="brand">01 · Context</span>

# Agenda

<ol>
<li class="current">Context<em>Dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</em></li>
<li>Findings<em>Veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure.</em></li>
<li>Recommendations<em>Cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum sed ut perspiciatis.</em></li>
<li>Next steps<em>Voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione.</em></li>
</ol>

---

<span class="brand">01 · Context</span>

# Lorem ipsum dolor sit amet consectetur adipiscing elit

## Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

<p class="lead">Quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat — duis aute irure dolor in reprehenderit in voluptate.</p>

- **Lorem ipsum** dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
- **Ut enim ad minim** veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure.
- **Duis aute irure** dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat.

<p class="source">Source: Lorem ipsum analysis, market data 2024–2026; n=42 client interviews, Q1 2026.</p>

---

<!-- _class: two-col -->

<span class="brand">02 · Findings</span>

# Duis aute irure dolor in reprehenderit voluptate

## Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia.

<div class="columns">
<div>

#### Lorem ipsum dolor

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa quae ab illo inventore veritatis.

- Nemo enim ipsam voluptatem quia voluptas sit aspernatur
- Neque porro quisquam est qui dolorem ipsum quia dolor sit
- Ut enim ad minima veniam quis nostrum exercitationem ullam

</div>
<div>

#### Consectetur adipiscing

At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias.

- Excepturi sint occaecati cupiditate non provident similique
- Temporibus autem quibusdam et aut officiis debitis aut rerum
- Itaque earum rerum hic tenetur a sapiente delectus reiciendis

</div>
</div>

<p class="source">Source: Lorem ipsum dolor sit amet, consectetur adipiscing elit — Q1 2026.</p>

---

<!-- _class: cards -->

<span class="brand">03 · Recommendations</span>

# Tres principia ad transformationem operativam

## Quae sequuntur — singula cum effectu, conatu et praerequisitis quae explicantur.

<div class="grid">
<div class="card">

<p class="num">Lever 01</p>

#### Lorem ipsum dolor sit amet consectetur

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium totam rem aperiam.

<div class="meta"><span>Impact</span><strong>High</strong></div>
<div class="meta"><span>Effort</span><strong>6 months</strong></div>

</div>
<div class="card">

<p class="num">Lever 02</p>

#### Adipiscing elit sed do eiusmod tempor

Eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo nemo enim ipsam.

<div class="meta"><span>Impact</span><strong>Medium</strong></div>
<div class="meta"><span>Effort</span><strong>9 months</strong></div>

</div>
<div class="card">

<p class="num">Lever 03</p>

#### Incididunt ut labore et dolore magna

Voluptatem quia voluptas sit aspernatur aut odit aut fugit sed quia consequuntur magni dolores eos qui ratione.

<div class="meta"><span>Impact</span><strong>High</strong></div>
<div class="meta"><span>Effort</span><strong>12 months</strong></div>

</div>
</div>

<p class="source">Source: Lorem ipsum prioritization workshop, March 2026.</p>

---

<!-- _class: cards-2 -->

<span class="brand">03 · Recommendations</span>

# Two larger cards for deeper content

## When two options need the room — pros, cons, and rationale on each side.

<div class="grid">
<div class="card">

<p class="num">Option A</p>

#### Lorem ipsum dolor sit amet consectetur

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.

<div class="meta"><span>Investment</span><strong>€2.4M</strong></div>
<div class="meta"><span>Payback</span><strong>14 months</strong></div>

</div>
<div class="card">

<p class="num">Option B</p>

#### Adipiscing elit sed do eiusmod tempor

Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt neque porro quisquam est qui dolorem ipsum.

<div class="meta"><span>Investment</span><strong>€3.8M</strong></div>
<div class="meta"><span>Payback</span><strong>22 months</strong></div>

</div>
</div>

<p class="source">Source: Business case modeling, Q1 2026.</p>

---

<!-- _class: cards-4 -->

<span class="brand">03 · Recommendations</span>

# Four compact cards for parallel options

## Same shape across four — denser type, tighter padding, faster scan.

<div class="grid">
<div class="card">

<p class="num">Lever 01</p>

#### Lorem ipsum dolor

Sed ut perspiciatis unde omnis iste natus error sit voluptatem.

<div class="meta"><span>Impact</span><strong>High</strong></div>

</div>
<div class="card">

<p class="num">Lever 02</p>

#### Adipiscing elit sed

Eaque ipsa quae ab illo inventore veritatis et quasi architecto.

<div class="meta"><span>Impact</span><strong>Med</strong></div>

</div>
<div class="card">

<p class="num">Lever 03</p>

#### Eiusmod tempor incididunt

Voluptatem quia voluptas sit aspernatur aut odit aut fugit sed quia.

<div class="meta"><span>Impact</span><strong>High</strong></div>

</div>
<div class="card">

<p class="num">Lever 04</p>

#### Labore et dolore magna

Consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.

<div class="meta"><span>Impact</span><strong>Med</strong></div>

</div>
</div>

<p class="source">Source: Initiative inventory, March 2026.</p>

---

<!-- _class: process -->

<span class="brand">03 · Recommendations</span>

# Five-phase implementation walks the program through one year

## Each step has a clear owner, deliverable, and gate before the next phase opens.

<div class="steps">
<div class="step">
<p class="step-num">Phase 01</p>
<p class="step-title">Lorem ipsum</p>
<p class="step-desc">Sed ut perspiciatis unde omnis iste natus error sit voluptatem.</p>
</div>
<div class="step">
<p class="step-num">Phase 02</p>
<p class="step-title">Dolor sit amet</p>
<p class="step-desc">Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit.</p>
</div>
<div class="step">
<p class="step-num">Phase 03</p>
<p class="step-title">Consectetur</p>
<p class="step-desc">Voluptatem sequi nesciunt neque porro quisquam est qui dolorem.</p>
</div>
<div class="step">
<p class="step-num">Phase 04</p>
<p class="step-title">Adipiscing elit</p>
<p class="step-desc">Quia dolor sit amet consectetur adipisci velit sed quia non.</p>
</div>
<div class="step">
<p class="step-num">Phase 05</p>
<p class="step-title">Tempor incidunt</p>
<p class="step-desc">Numquam eius modi tempora incidunt ut labore et dolore magnam.</p>
</div>
</div>

<p class="source">Source: Implementation roadmap, March 2026 — scaling 3 → 7 phases works the same way.</p>

---

<!-- _class: matrix -->

<span class="brand">02 · Findings</span>

# Two dimensions reveal where the real opportunity sits

## Initiatives in the upper right combine high impact with high feasibility.

<div class="quadrants">
<div class="axis-y"><span>Low</span><span>High</span></div>
<div class="q q1">
<h4>Quick wins</h4>
<p>Lorem ipsum dolor sit amet — three initiatives, modest investment, near-term payback.</p>
</div>
<div class="q q2 highlight">
<h4>Strategic bets</h4>
<p>Consectetur adipiscing elit — flagship moves, larger commitment, defining outcomes.</p>
</div>
<div class="q q3">
<h4>Fill-ins</h4>
<p>Sed do eiusmod tempor — defer or delegate; mostly hygiene, small upside.</p>
</div>
<div class="q q4">
<h4>Major projects</h4>
<p>Ut labore et dolore — high effort, distant payback; sequence carefully.</p>
</div>
<div class="axis-x"><span>Low ← Feasibility</span><span>Feasibility → High</span></div>
</div>

<p class="source">Source: Impact-feasibility scoring, prioritization workshop March 2026.</p>

---

<span class="brand">02 · Findings</span>

<!-- _class: kpi-hero -->

# One number captures the size of the prize

## Headline metric for the executive readout — supporting figures keep it grounded.

<div class="hero-stat">
<div>
<p class="big"><span class="cur">€</span>42<small>M</small></p>
</div>
<div class="ctx">

<p>Annual run-rate value at maturity — assuming the recommended program hits its targets across all five workstreams.</p>

<div class="sub">
<div><strong>+18 pp</strong><span>Margin uplift</span></div>
<div><strong>2.4×</strong><span>Cycle-time gain</span></div>
<div><strong>14 mo</strong><span>Payback</span></div>
</div>

</div>
</div>

<p class="source">Source: Business case model v3, March 2026 — base-case assumptions, sensitivity ±20%.</p>

---

<!-- _class: kpi-strip -->

<span class="brand">02 · Findings</span>

# Four indicators tell the same story from different angles

## Each metric improved between the baseline and the latest measurement window.

<div class="strip">
<div class="stat">
<p class="num"><em>+34%</em></p>
<p class="label">Throughput</p>
<p class="delta">vs. Q4 2024 baseline</p>
</div>
<div class="stat">
<p class="num"><em>−42%</em></p>
<p class="label">Cycle time</p>
<p class="delta">median, ticket-to-resolution</p>
</div>
<div class="stat">
<p class="num"><em>+12pp</em></p>
<p class="label">CSAT</p>
<p class="delta">rolling 90-day average</p>
</div>
<div class="stat">
<p class="num"><em>−€1.8M</em></p>
<p class="label">Run cost</p>
<p class="delta">annualized, exit run-rate</p>
</div>
</div>

<p class="source">Source: Operations dashboard, January–March 2026; n ≈ 18,400 transactions.</p>

---

<!-- _class: compare -->

<span class="brand">03 · Recommendations</span>

# Two paths, one decision — the trade-off is speed versus optionality

## Recommended path picks reversibility over fastest delivery.

<div class="vs">
<div class="side">

#### Build now

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt.

- Faster time-to-value (≈4 months)
- Higher up-front investment
- Locks in the current process design

</div>
<div class="divider"></div>
<div class="side">

#### Buy and adapt

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea.

- Lower up-front, higher run-rate
- Faster to pilot, slower to scale
- Preserves optionality through year two

</div>
</div>

<p class="source">Source: Vendor evaluation, March 2026; weighted criteria — speed, cost, reversibility, fit.</p>

---

<!-- _class: quote -->

<!-- _footer: '' -->

<span class="brand">02 · Findings</span>

<div class="quote-body">

The hardest part wasn't picking the right answer — it was building the conviction to *stop debating the question*.

</div>

<div class="attribution">
<strong>Lorem Ipsum</strong>
<span>Chief Operating Officer · Dolor Sit Amet GmbH</span>
</div>

---

<!-- _class: timeline -->

<span class="brand">04 · Next steps</span>

# Milestones over the next six months keep momentum visible

## Four checkpoints with a clear deliverable at each — easy to add or compress.

<div class="events">
<div class="event">
<p class="when">Apr 2026</p>
<div class="what">

#### Mobilize and align

Steerco signs charter; workstream leads named; baseline data lock.

</div>
</div>
<div class="event">
<p class="when">Jun 2026</p>
<div class="what">

#### Pilot two design changes

First two interventions live in two business units; weekly readout.

</div>
</div>
<div class="event">
<p class="when">Aug 2026</p>
<div class="what">

#### Decision gate · go / no-go

Pilot evidence reviewed; expand, adjust, or stop. Owner: COO.

</div>
</div>
<div class="event">
<p class="when">Oct 2026</p>
<div class="what">

#### Scale across BUs

Roll-out wave 1 — three additional units; training and tooling.

</div>
</div>
</div>

<p class="source">Source: Programme roadmap v2, March 2026 — easily compressed to 3 events or extended to 6+.</p>

---

<!-- _class: closing -->

<!-- _paginate: false -->

<!-- _footer: '' -->

<span class="brand">Q&A</span>

<div class="close-block">

# Discussion *and questions.*

<div class="contact">
<div><span>Lead</span><strong>Lorem Ipsum</strong></div>
<div><span>Email</span><strong>lorem@dolor-sit.amet</strong></div>
<div><span>Date</span><strong>26 April 2026</strong></div>
</div>

</div>
