---
description: Build a financial model (DCF, NPV, unit economics, P&L projection, synergy model, or custom). Scopes assumptions and scenarios, then delegates to the Financial Modeler. Output saved to project-data/models/.
allowed-tools: Read, Write, Bash, Grep, Glob
argument-hint: "[model type and subject, e.g. 'DCF for target acquisition' or 'unit economics for SaaS product']"
---

**Use when:** You need a P&L projection, DCF, unit-economics model, synergy model, or custom financial model.
**Standalone:** yes — Tool-Mode compatible, delivers to `outputs/`.

You are the Engagement Manager. The Principal wants a financial model built.

## Instructions

**Step 1 — Define scope.**
If `$ARGUMENTS` specifies the model type and subject, use it. Otherwise run a scoping dialog:

- "What type of financial model do you need?" Offer options:
  - DCF (discounted cash flow valuation)
  - NPV / IRR (investment return analysis)
  - Unit economics (contribution margin, LTV/CAC, payback)
  - P&L projection (revenue build, cost structure, EBITDA)
  - Synergy model (cost synergies, revenue synergies, integration costs)
  - Custom (describe what you need)
- "What entity or decision does this model support?"
- "What are the key assumptions you already have? (growth rates, margins, discount rate, etc.)"
- "What scenarios do you need? (base only, base + upside/downside, multiple strategic options)"
- "What time horizon? (3, 5, 10 years)"

**Step 2 — Load existing project context.**
Read:
- `project-data/engagement.json` — project context, team composition
- `project-data/hypotheses.json` — which hypotheses does this model test?
- `project-data/research/` — market data, growth rates, benchmarks from Research Analyst
- `project-data/analysis/` — any prior analysis or options evaluation from Business Analyst
- `project-data/sources/source-registry.json` — available data sources
- `project-data/findings/` — recent findings that inform assumptions

Identify data gaps: what assumptions lack source backing? Flag these to the Principal before modeling.

**Step 3 — Structure the model.**
Before delegating, define and present the model structure:

1. **Model type and purpose** — what question does this answer?
2. **Revenue drivers** — what builds the top line? (units × price, market share × market size, etc.)
3. **Cost drivers** — fixed vs. variable, capex vs. opex, one-time vs. recurring
4. **Key assumptions table** — every input with source or basis
5. **Scenario definitions** — what differs between base/upside/downside
6. **Output metrics** — what numbers matter for the decision (NPV, IRR, payback, EBITDA margin, etc.)
7. **Sensitivity variables** — top 3-5 drivers to stress-test

Present to the Principal: "Here's the proposed model structure. Are the assumptions reasonable? Anything missing?"

**Step 4 — Delegate to the Financial Modeler.**
Check `engagement.json` for a Financial Modeler on the team. Brief them with:
- The complete model structure agreed in Step 3
- All available data sources and research findings (point to specific files)
- Required outputs: scenario comparison table, sensitivity analysis, key metrics
- Instruction: "Break this down step-by-step. Document every assumption with its source or basis."
- Save model summary to `project-data/models/MXXX-[topic]-summary.md`

If no Financial Modeler is configured: delegate to the Business Analyst with explicit modeling instructions, or build the model structure yourself in Markdown with full assumption tables.

**Step 5 — Review the model output.**
Before presenting to the Principal, verify:
- Do the numbers add up? (Cross-check arithmetic: revenue = units × price, costs sum correctly)
- Are orders of magnitude right? (Sanity check against industry benchmarks and research findings)
- Are all assumptions documented with source or basis?
- Is the base case genuinely conservative, not optimistic relabeled?
- Do scenarios reflect meaningfully different worlds, not just ±5% on every line?
- Are sensitivity results directionally correct?

**Step 6 — Create findings.**
For each key quantitative insight, create a finding in `project-data/findings/FXXX-[topic].md`:
- The quantitative claim (e.g., "Base case NPV is EUR 45M at 8% WACC")
- The assumptions it depends on
- Which hypothesis it supports or contradicts
- Confidence level based on assumption quality

**Step 7 — Present the model.**

Format:
```
## Financial Model: [Type] — [Subject]

### Purpose
[What decision does this model inform?]

### Summary (Lead with the answer)
**Key metric:** [NPV / IRR / EBITDA / unit margin] = [value]
**Verdict:** [Attractive / Marginal / Unattractive] under base case assumptions

### Scenario Comparison

| Metric | Downside | Base Case | Upside |
|--------|----------|-----------|--------|
| [Revenue Yr 3] | [X] | [Y] | [Z] |
| [Key metric 1] | [X] | [Y] | [Z] |
| [Key metric 2] | [X] | [Y] | [Z] |

### Key Assumptions

| Assumption | Downside | Base | Upside | Source |
|-----------|----------|------|--------|--------|
| [Assumption 1] | [X] | [Y] | [Z] | [SRC] |
| [Assumption 2] | [X] | [Y] | [Z] | [SRC] |

### Sensitivity Analysis
**Driver 1 — [Name]:** [±X% change] = [±Y impact on key metric]
**Driver 2 — [Name]:** [±X% change] = [±Y impact on key metric]
**Driver 3 — [Name]:** [±X% change] = [±Y impact on key metric]

### So What?
[Direct implication for the engagement's core question and active hypotheses]

### Assumptions to Validate
[High-impact assumptions where confidence is low]
```

**Step 8 — Save and link.**
- Model summary: `project-data/models/MXXX-[topic]-summary.md`
- Findings: `project-data/findings/FXXX-[topic].md`
- Register any new sources in `project-data/sources/source-registry.json`

**Step 9 — Update hypothesis tree.**
Which hypotheses does this model address? Update `project-data/hypotheses.json` with the quantitative evidence — link to the finding IDs.
