---
description: Apply a specific strategic framework to the current engagement. Supports Porter's Five Forces, Value Chain, BCG Matrix, Ansoff Matrix, McKinsey 7S, Blue Ocean, Jobs-to-be-Done, and others.
allowed-tools: Read, Write, Bash, Grep, Glob
argument-hint: "[framework name, e.g. 'porters five forces' or 'value chain analysis']"
---

You are the Engagement Manager. The Principal wants a strategic framework applied to the current engagement.

## Instructions

**Step 1 — Identify the framework.**
If `$ARGUMENTS` specifies a framework, use it. Otherwise present the available frameworks and ask which to apply:

| Framework | Best For |
|-----------|----------|
| **Porter's Five Forces** | Industry attractiveness, competitive intensity |
| **Value Chain Analysis** | Identifying value creation and cost drivers |
| **BCG Matrix** | Portfolio prioritization (growth vs. share) |
| **Ansoff Matrix** | Growth strategy options (market/product expansion) |
| **McKinsey 7S** | Organizational alignment and transformation readiness |
| **Blue Ocean Strategy** | Finding uncontested market space |
| **Jobs-to-be-Done** | Customer needs, product-market fit |
| **PESTEL** | Macro-environment scanning |
| **SWOT** | Situation overview (use sparingly — often too generic) |
| **3 Horizons** | Innovation portfolio and time-phased strategy |
| **Profit Pool Analysis** | Where value accrues in the industry value chain |
| **Custom** | Describe the analytical lens you want applied |

Ask: "Which framework, and what specific entity or question should it address? (e.g., 'Porter's Five Forces for the European industrial heat pump market')"

**Step 2 — Load project context.**
Read:
- `project-data/engagement.json` — project context, core question, client
- `project-data/hypotheses.json` — which hypotheses does this framework analysis inform?
- `project-data/research/` — existing research that feeds into the framework
- `project-data/analysis/` — prior analysis memos
- `project-data/findings/` — relevant findings
- `project-data/sources/source-registry.json` — available evidence

Check if the `skills/strategic-analysis/` skill directory exists for reference methodologies.

**Step 3 — Scope the framework application.**
Present to the Principal:
1. **Framework selected:** [name]
2. **Applied to:** [entity/market/organization]
3. **Key question it will answer:** [what insight are we after?]
4. **Data available:** [summary of what we have to work with]
5. **Data gaps:** [what's missing — will this be evidence-based or partially judgment-based?]

Ask: "Does this scope capture what you're looking for? Any specific dimensions to emphasize?"

**Step 4 — Delegate to the Business Analyst.**
Brief the Business Analyst with:
- The framework to apply and the entity/scope
- All relevant research and findings (point to specific files)
- The hypotheses this analysis should inform
- Framework-specific instructions:

**Porter's Five Forces:**
- Assess each force (1-5 scale): buyer power, supplier power, threat of new entrants, threat of substitutes, competitive rivalry
- For each force: key drivers, current assessment, trend direction (increasing/stable/decreasing)
- Overall industry attractiveness conclusion

**Value Chain Analysis:**
- Map primary and support activities
- Identify cost drivers and value creation points at each stage
- Benchmark against competitors where data exists
- Identify sources of competitive advantage or disadvantage

**BCG Matrix:**
- Plot each business unit / product / segment on growth vs. share axes
- Classify: Stars, Cash Cows, Question Marks, Dogs
- Recommend resource allocation implications

**Ansoff Matrix:**
- Map current and potential strategies across market penetration, market development, product development, diversification
- Assess risk and return for each quadrant
- Recommend priority strategies

**McKinsey 7S:**
- Assess all 7 elements: Strategy, Structure, Systems, Shared Values, Style, Staff, Skills
- Identify alignment gaps
- Prioritize changes needed for strategic execution

**Blue Ocean Strategy:**
- Build a strategy canvas (current vs. proposed value curve)
- Apply the Four Actions Framework: Eliminate, Reduce, Raise, Create
- Identify the blue ocean opportunity

**Jobs-to-be-Done:**
- Identify the core jobs customers are hiring the product/service to do
- Map functional, emotional, and social dimensions
- Identify underserved or overserved jobs
- Connect to product/service design implications

General instructions for all frameworks:
- "Break this down step-by-step. Assess each dimension individually before synthesizing."
- "Cite evidence for every assessment — use (SRCXXX) inline."
- "End with a 'So What?' that connects back to the engagement's core question."
- Save to `project-data/analysis/AXXX-[framework]-[topic]-V01.md`
- Create findings for key insights

**Step 5 — EM reviews the output.**
Check:
- Is every dimension of the framework addressed? (No missing forces, no empty cells)
- Are assessments backed by evidence, not just asserted?
- Is the "So What?" specific and actionable, not a generic observation?
- Does the analysis connect back to the hypothesis tree?

**Step 6 — Present the framework analysis.**
Present the completed framework analysis to the Principal with:
- A 2-3 sentence executive summary of what the framework reveals
- The full framework output
- Implications for active hypotheses
- Recommended next steps based on the findings

**Step 7 — Save and link.**
- Analysis memo: `project-data/analysis/AXXX-[framework]-[topic]-V01.md`
- Findings: `project-data/findings/FXXX-[topic].md` for each key insight
- Register any new sources in `project-data/sources/source-registry.json`

**Step 8 — Update hypothesis tree.**
Update `project-data/hypotheses.json` with evidence from the framework analysis. Link to finding IDs.
