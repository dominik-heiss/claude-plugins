---
name: quantitative-modeling
description: >
  This skill activates when the user asks to "build a financial model",
  "build a market sizing model", "run a sensitivity analysis", "construct scenarios",
  "model unit economics", "estimate returns", "build a business case",
  "triangulate estimates", or needs guidance on quantitative analysis,
  assumption documentation, or presenting numerical results.
---

# Quantitative Modeling — Principles

Every number tells a story. Your job is to make it a defensible one.

## The Core Principle

**A model is an argument expressed in numbers.** It exists to answer a question — "Is this market large enough?", "Does this investment return above hurdle?", "Which lever moves the outcome most?" If you can't state what question the model answers, don't build it.

Every model output is only as good as its weakest assumption. Document every assumption. Source every assumption. Challenge every assumption.

## Modeling Approaches

**Build-up (bottom-up):** Start from granular, observable units and aggregate upward. Unit count x price x frequency = revenue. Best when you have reliable micro-level data. Tends to underestimate because it misses segments.

**Top-down:** Start from total market and apply share/penetration assumptions downward. Total market x addressable share x penetration rate = revenue. Best for quick sizing and sanity checks. Tends to overestimate because it assumes frictionless capture.

**Analogy-based:** Use comparable companies, markets, or transactions as reference points. "Company X achieved Y penetration in a similar market in Z years." Best when direct data is scarce but analogies are available.

**Always triangulate.** Never rely on a single approach. Build at least two independent estimates and compare. If they diverge by more than 30%, investigate — one set of assumptions is wrong. If they converge, confidence increases.

## Assumption Documentation

Every assumption in the model needs three things:

1. **The value** — what number you're using
2. **The source** — where it comes from (SRC reference or "team estimate" with rationale)
3. **The sensitivity** — how much the output changes if this assumption is wrong by 20%

Organize assumptions into tiers:
- **Tier 1 — Grounded:** Based on verifiable data (public filings, industry reports, client data). These are facts.
- **Tier 2 — Informed estimates:** Based on analogies, expert judgment, or partial data. Defensible but debatable.
- **Tier 3 — Assumptions:** Based on judgment with limited evidence. These are the ones to stress-test hardest.

Flag Tier 3 assumptions visibly in every model output. They are where the model breaks.

## Sensitivity Analysis

**Always show sensitivity to the top 3 drivers.** Identify which assumptions have the most impact on the output through one-at-a-time variation.

**Tornado chart:** Vary each key assumption by a defined range (e.g., +/- 20%) and show which moves the output most. This tells you where to focus diligence.

**Two-way sensitivity table:** Pick the two most impactful assumptions and show the output across a matrix of values. This reveals interaction effects.

**Never present a single point estimate without a range.** A market size of "EUR 12B" is less useful than "EUR 9-15B, with EUR 12B as the base case driven primarily by penetration rate assumptions."

## Scenario Construction

Three scenarios minimum:

- **Base case:** Most likely outcome given current evidence. This is your working answer.
- **Upside case:** What happens if key tailwinds materialize. Not "everything goes right" — pick the 2-3 most plausible positive developments.
- **Downside case:** What happens if key risks materialize. Not "everything goes wrong" — pick the 2-3 most likely negative developments.

Each scenario must be internally consistent. You cannot have "low market growth" paired with "high pricing power" unless you explain why.

**Scenario narratives matter.** Each scenario should be a plausible story, not just a set of numbers. "In the downside case, regulatory tightening delays adoption by 2 years, reducing 2030 penetration from 15% to 8%."

## Unit Economics

For any business model, the unit economics must work before the aggregate numbers matter.

Key questions:
- What is the unit? (Customer, transaction, product, location)
- What is the revenue per unit?
- What is the variable cost per unit?
- What is the contribution margin?
- What are the fixed costs that must be covered?
- How many units to break even?

If the unit economics don't work at scale, no amount of volume assumptions will save the model.

## Presenting Quantitative Results

**Lead with the answer, then show the math.** "The market is EUR 12B and growing at 8% CAGR" — then show how you got there.

**Bridge charts** for explaining how you get from one number to another (revenue bridges, cost bridges, value creation bridges).

**Always contextualize numbers.** EUR 500M means nothing without "which is 3x the current run rate" or "which represents 12% of the addressable market."

**Round appropriately.** A market size of EUR 11,847M implies false precision. Say EUR 12B. A margin of 23.7% is fine if supported; 23.71% is not.

## Common Traps

**False precision** — presenting outputs to 4 decimal places when inputs are Tier 3 estimates. The output precision cannot exceed the input precision.

**Hockey stick projections** — growth that magically accelerates in year 3-5 with no structural reason. Every inflection point needs a driver.

**Anchoring on the first number** — the first estimate you calculate becomes the reference point for all subsequent work. Counter: build the second estimate independently before comparing.

**Ignoring the denominator** — "Revenue grew 40%" is meaningless without knowing the base. Growth from EUR 1M to EUR 1.4M is not the same as growth from EUR 100M to EUR 140M.

**Circular reasoning in models** — revenue drives costs which drive investment which drives revenue. Break the circularity by fixing one variable and iterating, or by using prior-period values.

**Survivorship bias in analogies** — comparing to successful companies only. The failed companies that tried the same thing are equally informative.
