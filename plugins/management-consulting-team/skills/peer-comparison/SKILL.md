---
name: peer-comparison
description: >
  This skill activates when the user asks to "benchmark against competitors",
  "compare peer performance", "build a competitive landscape", "normalize KPIs",
  "assess relative positioning", "map the competitive field", or needs guidance
  on peer set selection, like-for-like comparison methodology, or presenting
  competitive analysis.
---

# Peer Comparison — Principles

Comparison without normalization is just a list of numbers.

## The Core Principle

**Always state the basis of comparison.** A comparison is only meaningful when the reader knows what is being compared, on what metric, and why those specific peers were chosen. Unstated selection criteria lead to cherry-picked peer sets and misleading conclusions.

Every peer comparison must answer three questions up front:
1. Who is in the peer set and why?
2. What metrics are being compared and why those?
3. What normalization has been applied to make the comparison fair?

## Peer Set Selection

**Start with the universe, then narrow with explicit criteria.** Document the selection logic:

- **Industry classification** — same NACE/SIC codes, same value chain position
- **Size band** — revenue within 0.5x to 3x of the target (wider ranges distort comparisons)
- **Geography** — same operating markets or comparable market structures
- **Business model** — same revenue model (subscription vs. transactional, B2B vs. B2C)
- **Lifecycle stage** — mature vs. high-growth companies behave differently on every metric

**Peer set size:** 5-8 peers is the sweet spot. Fewer than 4 lacks statistical meaning. More than 12 dilutes the signal and overwhelms the audience.

**Always include at least one aspirational peer** — a company that represents "best in class" even if not a direct competitor. This anchors the upper bound of what's possible.

**Document who was excluded and why.** "We excluded Company X because its revenue includes a large services division not comparable to the target's product business." This preempts the inevitable question.

## KPI Selection and Normalization

**Select KPIs that answer the question.** Don't benchmark everything — benchmark what matters for the decision.

Common dimensions:
- **Growth:** Revenue CAGR, organic vs. inorganic, volume vs. price
- **Profitability:** EBITDA margin, gross margin, ROIC, conversion ratio
- **Efficiency:** Revenue per employee, asset turnover, working capital as % of revenue
- **Scale:** Revenue, market share, geographic footprint
- **Valuation:** EV/EBITDA, EV/Revenue, P/E (for listed peers only)

**Normalize for comparability:**
- **Size:** Use ratios (margin, per-employee metrics) rather than absolutes
- **Geography:** Adjust for purchasing power, labor cost differences, regulatory burden
- **Business model:** Separate product and service revenues when models differ
- **Accounting:** Adjust for IFRS vs. GAAP differences, capitalization policies, lease treatment
- **Currency:** Use constant currency or specify the conversion date
- **Time period:** Align fiscal year ends; use trailing twelve months when fiscal years differ

## Dealing with Data Gaps

Data will always be incomplete. Handle gaps explicitly:

- **State what's missing.** "Margin data unavailable for Company C and E (private companies)."
- **Use proxies when justified.** "We use gross margin as a proxy for EBITDA margin for private companies, noting this overstates profitability by approximately 5-8pp based on listed peer patterns."
- **Show the comparison with and without the gapped peers** if the gap affects a critical metric.
- **Never interpolate silently.** If you estimate a missing data point, mark it as an estimate and state the method.

## Presenting Competitive Positioning

**Spider/radar charts** — useful for multi-dimensional comparison of 3-5 peers on 4-6 metrics. Normalize all axes to the same scale (e.g., percentile rank within the peer set).

**Scatter plots** — best for showing the relationship between two key dimensions (e.g., growth vs. profitability). Label quadrants with strategic implications.

**Indexed bar charts** — set the target company at 100 and show peers relative to it. Immediately clear where the target over- or under-performs.

**Ranking tables** — simple, effective for 3-4 metrics across a peer set. Highlight the target's position. Color-code quartile performance.

**The "so what" for every comparison:** Don't just show where the target ranks — explain why it matters. "Target's EBITDA margin is bottom quartile at 12% vs. peer median of 18% — closing half this gap represents EUR 30M in annual EBITDA improvement."

## Common Traps

**Cherry-picking peers** — selecting only peers that make the target look good (or bad, depending on the narrative). Counter: define selection criteria before looking at the data.

**Comparing absolutes across different-sized companies.** Revenue of EUR 500M vs. EUR 5B tells you nothing about relative performance. Always normalize.

**Ignoring business model differences.** A marketplace with 80% gross margins is not comparable to a distributor with 20% gross margins — even if they serve the same end market.

**Snapshot bias** — comparing a single year when one peer had an exceptional or terrible year. Use 3-year averages for structural metrics.

**Treating the peer median as the target.** The median is a reference point, not a goal. The right target depends on the company's strategic ambition and starting position.

**Confusing correlation with causation in peer analysis.** "Top-quartile companies all invest heavily in R&D" does not mean R&D investment causes top-quartile performance.
