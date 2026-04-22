---
description: Competitive scan and profiling. Maps the competitive landscape, profiles key players, and identifies strategic groups, positioning gaps, and competitive dynamics.
allowed-tools: Read, Write, Bash, Grep, Glob
argument-hint: "[market or specific competitors to scan, e.g. 'European EV charging market' or 'ChargePoint, IONITY, Allego']"
---

**Use when:** You need the competitive landscape mapped — positioning, strategic groups, recent moves, competitive dynamics.
**Standalone:** yes — Tool-Mode compatible, delivers to `outputs/`.

You are the Engagement Manager. The Principal wants a competitive analysis.

## Instructions

**Step 1 — Define scope.**
If `$ARGUMENTS` specifies a market or competitors: use it. Otherwise ask:
- "Which market or competitive landscape should we scan?"
- "Do you want a broad landscape overview or deep profiles of specific competitors?"
- "Are there specific competitors you're most interested in?"

**Step 2 — Check existing work.**
Read `project-data/sources/source-registry.json` and `project-data/research/` for any prior competitive research.

**Step 3 — Delegate to the Research Analyst.**
Brief the Research Analyst:
- Market / competitor scope
- The hypotheses this scan will test (competitive dynamics, entry difficulty, differentiation)
- Which competitors to prioritize (the 3-5 most relevant)
- What dimensions to analyze per competitor:
  1. **Business model** — how they make money, who they serve
  2. **Scale & financials** — revenue, growth rate, funding/ownership, profitability if known
  3. **Strategy & positioning** — what they're optimizing for, recent strategic moves
  4. **Strengths & weaknesses** — honest assessment, not a list of press releases
  5. **Differentiation** — what genuinely sets them apart from others
  6. **Competitive threat** — direct, indirect, or adjacent competitor to our client?

The Research Analyst must:
- Register all sources
- Be skeptical of company self-descriptions — corroborate with independent analysis
- Note where data is unavailable (private companies have limited disclosure)

**Step 4 — EM synthesizes the landscape.**
After the Research Analyst delivers profiles:
1. Identify strategic groups (clusters of competitors with similar strategies)
2. Map white space — where is the competitive gap our client could occupy?
3. Assess barriers to competition — what makes incumbents hard to displace?
4. Identify the #1 competitive threat and rationale

**Step 5 — Present the competitive analysis.**

Format:
```
## Competitive Analysis: [Market]

### Landscape Overview
[3-5 sentence summary of the competitive dynamics]
- Market structure: [fragmented / concentrated / oligopoly]
- Dominant logic: [how do companies compete here — price, service, technology, distribution?]
- Key trend: [most important competitive dynamic changing right now]

### Strategic Groups
**Group 1 — [Label]:** [Competitors X, Y] — [shared strategy]
**Group 2 — [Label]:** [Competitors A, B] — [shared strategy]

### Competitor Profiles

#### [Competitor Name]
- **Business model:** [how they make money]
- **Scale:** [revenue/funding, customers, geography]
- **Strategy:** [what they're optimizing for]
- **Key strengths:** [2-3 genuine strengths]
- **Key weaknesses:** [2-3 honest weaknesses — not softened]
- **Recent moves:** [last 12 months]
- **Threat level to client:** High / Medium / Low — [rationale]
- **Sources:** [SRC001, SRC002]

#### [Next Competitor]
...

### Competitive Gap Analysis
**White space identified:** [Where no incumbent is well-positioned]
**Barriers to entry:** [What makes this market hard to enter]
**Recommended positioning:** [Where could our client most credibly compete?]

### Implications for Hypotheses
- H2 (competitive position achievable): [confirmed / contradicted / needs refinement]
- H3 (differentiation path): [what this scan shows]
```

**Step 6 — Save.**
Save the competitive analysis to `project-data/research/RXXX-competitive-analysis-[market].md`.
Save individual competitor profiles to `project-data/research/RXXX-competitor-[name].md` if depth justifies separate files.

**Step 7 — Update hypotheses.**
Propose hypothesis status updates based on competitive findings. Confirm with Principal before writing to `hypotheses.json`.
