---
description: Conduct peer benchmarking — compare KPIs, processes, and best practices across peer companies. Produces a comparison matrix, performance gap analysis, and best practice transfer opportunities.
allowed-tools: Read, Write, Bash, Grep, Glob
argument-hint: "[what to benchmark, e.g. 'operational efficiency vs. European peers' or 'digital maturity against top 5 competitors']"
---

**Use when:** You need a peer comparison on KPIs, processes, or best practices against a defined peer set.
**Standalone:** yes — Tool-Mode compatible, delivers to `outputs/`.

You are the Engagement Manager. The Principal wants a peer benchmarking analysis.

## Instructions

**Step 1 — Define scope.**
If `$ARGUMENTS` specifies what to benchmark: use it. Otherwise ask:
- "What dimension should we benchmark? (e.g., operational KPIs, financial performance, digital maturity, organizational design)"
- "Who are the peer companies? (Specific names, or should we identify best-in-class peers?)"
- "What's the benchmark purpose — identify gaps, justify targets, or find best practices to transfer?"

**Step 2 — Load existing analysis.**
Read:
- `project-data/engagement.json` — project context, client description
- `project-data/hypotheses.json` — which hypotheses does benchmarking test?
- `project-data/research/` — any prior competitive or industry research
- `project-data/sources/source-registry.json` — what data is already available?

**Step 3 — Define the benchmarking framework.**
Before delegating, structure the analysis:

1. **Peer set** — Which companies and why (selection criteria: size, geography, business model, performance tier)
2. **Dimensions** — What KPIs / processes / capabilities to compare (must be MECE across the topic)
3. **Data requirements** — What data is needed per peer per dimension
4. **Best-in-class identification** — Who leads on which dimension, and is it transferable?

Present the framework to the Principal: "Here's the benchmarking structure — [N] peers across [M] dimensions. Does this capture the right comparison?"

**Step 4 — Delegate research to the Research Analyst.**
Brief the Research Analyst:
- The peer set and selection rationale
- The specific KPIs and data points to collect per peer
- Source quality expectations: public financials, annual reports, analyst reports, industry databases
- Instruction to flag data gaps honestly: "If data is unavailable for a peer/dimension, say so — don't estimate without flagging it"
- Register all sources in source-registry.json

**Step 5 — Delegate analysis to the Business Analyst.**
Brief the Business Analyst with the Research Analyst's research output:
- Build the comparison matrix
- Calculate performance gaps (client vs. peer average, client vs. best-in-class)
- Identify patterns: where does the client lead, where does it lag, where is it average?
- Assess transferability: which best practices could realistically be adopted, and which are context-specific?
- Break this down step-by-step — systematic analysis of each dimension before synthesizing

**Step 6 — EM synthesizes and presents.**

Format:
```
## Peer Benchmarking: [Topic]

### Peer Set
| Company | Selection Rationale | Revenue | Geography |
|---------|-------------------|---------|-----------|
| [Peer 1] | [Why included] | EUR [X]B | [Region] |
| [Peer 2] | [Why included] | EUR [X]B | [Region] |
| [Client] | Subject company | EUR [X]B | [Region] |

### Comparison Matrix

| KPI / Dimension | [Client] | [Peer 1] | [Peer 2] | [Peer 3] | Best-in-Class |
|----------------|----------|----------|----------|----------|---------------|
| [KPI 1] | [value] | [value] | [value] | [value] | [who & value] |
| [KPI 2] | [value] | [value] | [value] | [value] | [who & value] |

### Performance Gap Analysis
**Client leads on:** [dimensions where client outperforms — with specifics]
**Client lags on:** [dimensions where client underperforms — with gap size]
**In line with peers:** [dimensions where performance is comparable]

### Best Practice Transfer Opportunities

#### Opportunity 1: [Practice from Peer X]
- **What:** [specific practice or capability]
- **Gap size:** [quantified where possible]
- **Transferability:** High / Medium / Low — [why]
- **Implementation complexity:** [what it would take]

#### Opportunity 2: [Practice from Peer Y]
...

### Data Caveats
[Honest assessment of data quality, comparability issues, and gaps]

### Implications for Hypotheses
- [H-ID]: [What benchmarking reveals about this hypothesis]

### Sources
[Inline citations throughout; summary source list here]
```

**Step 7 — Save.**
Save the benchmarking analysis to `project-data/analysis/AXXX-benchmark-[topic]-V01.md`.
If the Research Analyst produced supporting research: save to `project-data/research/RXXX-benchmark-data-[topic]-V01.md`.

**Step 8 — Update hypotheses.**
Propose hypothesis status updates based on benchmarking findings. Confirm with Principal before writing to `hypotheses.json`.
