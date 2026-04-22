---
name: research-craft
description: >
  This skill activates when the user asks to "conduct research", "size a market",
  "do market analysis", "run a competitive scan", "build the fact base",
  "research competitors", "find data on industry trends", "triangulate sources",
  "investigate market dynamics", "assess source reliability", or needs
  guidance on research methodology, data quality standards, or handling
  conflicting data from multiple sources.
---

**Use when:** You're conducting research — market sizing, competitive scan, trend analysis, fact-base build — and need triangulation, source-quality judgment, and claim discipline.

# Research Craft — Principles

Every fact is a claim. Claims need evidence. Evidence has quality.

## The Core Standard

**Triangulation.** At least 2 independent sources for every key claim. Not 2 sources that cite the same underlying data — 2 genuinely independent data points that converge on the same conclusion.

If you can't triangulate, label the claim: "Single source (SRC001) — needs triangulation before presenting as established fact."

## Source Skepticism

Every source has a bias. Name it explicitly.

Common bias patterns:
- **Industry association data:** Incentive to show industry growth and importance
- **Consulting firm reports:** Incentive to show complexity requiring their services; sometimes based on proprietary methodologies not disclosed
- **Company-sponsored research:** Results tend to favor the sponsor
- **Sell-side analyst reports:** Optimistic bias on covered companies
- **Government statistics:** Often lagged (1-3 years), methodology varies by country
- **Trade press:** Coverage driven by news value and advertiser relationships

Naming the bias doesn't disqualify the source — it helps calibrate how much weight to give it.

## Source Hierarchy

When sources conflict, weight them in this order:
1. **Primary sources** — raw data, company filings, government statistics, original research
2. **Peer-reviewed academic research** — rigorous methodology, independent validation
3. **Tier-1 consulting/research firm reports** (McKinsey, BCG, Bain, Forrester, Gartner) — credible methodology, but check for bias
4. **Industry association data** — useful for trends, bias as noted above
5. **Quality journalism** (FT, WSJ, Economist, Bloomberg) — current, but secondary synthesis
6. **Trade press** — directionally useful, reliability varies
7. **Uncorroborated web sources, blogs** — use only to find leads, never as evidence

Load `references/source-hierarchy.md` for extended guidance.

## Data Currency

**Default standard: use the most current data available.** For market sizing and competitive analysis, this means data from the current or previous year. If current-year data is not yet available (e.g., annual reports not yet published), use the most recent available and explicitly note: "2025 data not yet published as of [date]; using 2024 figures as latest available."

- **<6 months old:** Ideal — use as primary evidence
- **6-18 months old:** Acceptable — standard for most market data
- **18 months - 3 years old:** Use only if more recent data is unavailable. Flag explicitly: `[latest available — 2024 data not yet published]`
- **>3 years old:** Do not use as primary evidence. May be referenced for historical context only.
- **Exception:** Long-term structural trends (demographics, energy transition) can draw on older data if the trend is clearly established

**Always search for the most recent data first.** Add the current year to search queries (e.g., "European heat pump market size 2026" before trying "2025"). If the latest data is older than expected, document why and confirm with the EM whether to proceed or wait.

Always state the data vintage: "According to [Source] (2025)..." not "According to [Source]..."

## Market Sizing Methods

**Top-down:** Start with the total market (from industry reports), then apply share / segment / penetration filters to reach your target market.

**Bottom-up:** Build from the unit level — number of customers × average spend, or number of transactions × average value.

**Analogy-based:** Compare to a similar market with known size; apply adjustment factors for differences.

Best practice: Run at least two methods and triangulate. If they converge: confidence is high. If they diverge by >30%: understand why before presenting.

Load `references/market-sizing-methods.md` for detailed methodology.

## Source Conflict Protocol

When two credible sources disagree:

1. **Show the range:** "Source A: EUR 30B (2024). Source B: EUR 45B (2023)."
2. **Explain the discrepancy:** Different definition of market scope? Different geography? Different methodology? Different vintage?
3. **Set a working assumption:** Choose the most defensible number with explicit rationale.
4. **Show sensitivity:** "If Source A is correct instead of Source B, Market Y revenue estimate changes from EUR 45M to EUR 30M — this shifts our NPV from positive to marginal."
5. **Flag for validation:** Mark the finding as `needs_validation` in the finding schema.

Never average two conflicting sources without understanding why they differ.

## Source Registration Protocol

Every source used must be registered in `project-data/sources/source-registry.json`:

```json
{
  "id": "SRC001",
  "type": "web|document|database|interview",
  "title": "[full title]",
  "publisher": "[organization]",
  "url": "[url if web]",
  "local_path": "sources/web/SRC001-[title].md",
  "accessed": "[date]",
  "published": "[date or year if known]",
  "reliability": "high|medium|low",
  "bias_note": "[known bias, if any]",
  "key_data_points": ["Market size: EUR 45B", "CAGR 8.2%"]
}
```

**Note:** Do not include `used_in` in the registry. Cite sources inline in documents as `(SRC001)` immediately after each claim.

Archive web pages as HTML in `project-data/sources/web/SRCXXX-[slug].html`.

## Naming Gaps

It is better to say "no reliable source found" than to stretch a weak source.

Explicit gap: "No peer-reviewed data on [X] found. Available sources are industry association reports with potential upward bias. Treating as directional only — not suitable for financial modeling."

## When to Load Reference Files

- Choosing which sources to trust → `references/source-hierarchy.md`
- Running a market sizing → `references/market-sizing-methods.md`
