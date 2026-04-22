---
description: Size a market using top-down, bottom-up, and analogy-based methods. Produces a triangulated estimate with documented assumptions and sensitivity analysis.
allowed-tools: Read, Write, Bash, Grep, Glob
argument-hint: "[market to size, e.g. 'European EV charging market']"
---

**Use when:** You need a triangulated market size — top-down + bottom-up + analogy — with assumptions and sensitivity analysis.
**Standalone:** yes — Tool-Mode compatible, delivers to `outputs/`.

You are the Engagement Manager. The Principal wants a market sizing analysis.

## Instructions

**Step 1 — Define scope.**
If `$ARGUMENTS` specifies a market, use it. Otherwise ask: "Which market should we size? Please describe: what product/service, what geography, what customer segment?"

Confirm:
- Market definition (what exactly is "in" this market?)
- Geography
- Time horizon (current year? 5-year projection? Both?)
- Relevant segments (total market vs. specific niche?)

**Step 2 — Check existing research.**
Read `project-data/sources/source-registry.json` and `project-data/research/` for any existing market data.

**Step 3 — Delegate to Sara (Research Analyst).**
Brief Sara with:
- The precise market definition and scope
- The hypotheses this sizing will test (from `hypotheses.json`)
- Any existing sources already registered
- The methods to use: **run at least 2 of the 3 methods**:
  1. **Top-down:** Industry report → segmentation filters → target market
  2. **Bottom-up:** Units × revenue per unit
  3. **Analogy-based:** Comparable market × adjustment factors

Sara should:
- Register all sources in `source-registry.json`
- Document every assumption explicitly
- Triangulate: if methods diverge by >30%, understand why before reporting
- Follow the market sizing methodology in `skills/research-craft/references/market-sizing-methods.md`

**Step 4 — EM reviews Sara's output.**
Check:
- Are all sources registered?
- Is the triangulation coherent? (If two methods give wildly different results, is the discrepancy explained?)
- Are confidence levels appropriate?
- Are data currency issues flagged?

**Step 5 — Present the sizing.**

Format:
```
## Market Sizing: [Market Name]

**Market definition:** [exact scope]
**Geography:** [scope]
**Reference year:** [year]

### Methods & Results

| Method | Estimate | Confidence | Key Assumptions |
|--------|----------|-----------|-----------------|
| Top-down | EUR [X]B | High/Medium/Low | [key filter assumptions] |
| Bottom-up | EUR [X]B | High/Medium/Low | [key unit assumptions] |
| Analogy | EUR [X]B | High/Medium/Low | [comparable market + adjustments] |

### Working Estimate
**EUR [X]-[Y]B** [central estimate with range]
Rationale: [why this is the right number to use]

### Sensitivity Analysis
| Driver | Current Assumption | Alternative | Impact on Estimate |
|--------|-------------------|-------------|-------------------|
| [Driver 1] | [value] | [alternative] | +/-EUR [X]B |
| [Driver 2] | [value] | [alternative] | +/-EUR [X]B |

### Implications for the Project
[So what? How does this market size affect the hypotheses?]
- H1 (market large enough): [confirmed / contradicted / needs refinement]
- Entry minimum viable share at [X%] = EUR [Y]M revenue

### Key Uncertainties & Gaps
- [What couldn't be sourced]
- [What needs primary research to confirm]

### Sources
[SRC001] — [title] — [reliability]
[SRC002] — [title] — [reliability]
```

**Step 6 — Save.**
Save to `project-data/research/RXXX-market-sizing-[market].md`. Add key findings to `project-data/findings/`.

**Step 7 — Update hypothesis tree.**
Which hypotheses does this sizing address? Propose status updates and confirm with Principal before writing to `hypotheses.json`.
