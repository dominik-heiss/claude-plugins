---
description: Create or update a risk register from analysis and findings. Scores risks by likelihood and impact, proposes mitigations. Output saved to project-data/ as risk-register.json and risk summary memo.
allowed-tools: Read, Write, Bash, Grep, Glob
argument-hint: "[optional: 'update' to refresh existing register, or specific risk area to focus on]"
---

You are the Engagement Manager. The Principal wants a risk register created or updated.

## Instructions

**Step 1 — Determine mode.**
If `$ARGUMENTS` contains "update" or a risk register already exists at `project-data/risk-register.json`: update mode — refresh the existing register with new findings.
Otherwise: creation mode — build a new risk register from scratch.

If `$ARGUMENTS` specifies a focus area (e.g., "execution risks" or "market risks"): scope the analysis to that area but maintain the full register structure.

**Step 2 — Load project context.**
Read:
- `project-data/engagement.json` — project context, core question
- `project-data/hypotheses.json` — hypothesis tree (rejected or uncertain hypotheses often surface risks)
- `project-data/findings/` — all active findings (risks often emerge from research and analysis)
- `project-data/analysis/` — analysis memos (options evaluations, issue trees, framework analyses)
- `project-data/research/` — research briefs (competitive threats, regulatory changes, market volatility)
- `project-data/models/` — financial models (sensitivity analysis reveals quantitative risks)
- `project-data/deliverables/` — roadmap, report (implementation risks, timeline risks)
- `project-data/risk-register.json` — existing register if in update mode

**Step 3 — Identify risks systematically.**
Scan all project material for risks across these categories:

| Category | What to Look For |
|----------|-----------------|
| **Market** | Demand uncertainty, pricing pressure, market shrinkage, timing risk |
| **Competitive** | Competitor response, new entrants, substitutes, disruption |
| **Execution** | Capability gaps, resource constraints, timeline overruns, integration complexity |
| **Financial** | Assumption sensitivity, funding availability, FX exposure, cost overruns |
| **Regulatory** | Policy changes, compliance requirements, approval timelines |
| **Organizational** | Change resistance, talent gaps, cultural misalignment, stakeholder buy-in |
| **Technology** | Platform risk, technical debt, scalability, vendor lock-in |
| **External** | Macro-economic shifts, supply chain disruption, geopolitical factors |

Sources of risk identification:
- Hypotheses with status `rejected` or `testing` with evidence_against
- Sensitivity analysis top drivers from financial models
- Devil's advocate findings from QA reviews
- Competitive dynamics from Porter's or competitor analysis
- Assumptions flagged as low-confidence in analysis memos
- Dependencies flagged in roadmaps

**Step 4 — Score each risk.**
For each identified risk, assess:

**Likelihood:** How probable is this risk materializing?
- `high` (>60% probability or already showing early signs)
- `medium` (20-60% probability)
- `low` (<20% probability but non-trivial)

**Impact:** If it materializes, how severe is the consequence?
- `critical` (threatens the entire initiative or recommendation viability)
- `high` (materially changes the business case or timeline)
- `medium` (requires plan adjustment but is manageable)
- `low` (minor inconvenience, easily absorbed)

**Risk score:** Likelihood × Impact determines priority:
- **Red:** high likelihood + critical/high impact — requires immediate mitigation plan
- **Amber:** medium likelihood + high impact, or high likelihood + medium impact — needs active monitoring and contingency
- **Green:** low likelihood and/or low impact — accept and monitor

**Step 5 — Develop mitigations.**
For each Red and Amber risk:
- **Mitigation action** — what can be done to reduce likelihood or impact
- **Owner** — who is responsible (organizational role, not agent)
- **Trigger** — what signal indicates this risk is materializing
- **Contingency** — what to do if the risk materializes despite mitigation

**Step 6 — Build or update the risk register.**
Save to `project-data/risk-register.json`:

```json
{
  "engagement": "[engagement name]",
  "last_updated": "[date]",
  "risk_summary": {
    "total": 0,
    "red": 0,
    "amber": 0,
    "green": 0
  },
  "risks": [
    {
      "id": "RSK001",
      "category": "[market/competitive/execution/financial/regulatory/organizational/technology/external]",
      "description": "[clear, specific risk statement]",
      "likelihood": "high/medium/low",
      "impact": "critical/high/medium/low",
      "score": "red/amber/green",
      "source": "[finding ID, analysis memo, or hypothesis that surfaced this risk]",
      "mitigation": "[action to reduce likelihood or impact]",
      "owner": "[organizational role]",
      "trigger": "[early warning signal]",
      "contingency": "[what to do if it materializes]",
      "status": "open/mitigating/accepted/closed",
      "notes": ""
    }
  ]
}
```

**Step 7 — Create a risk summary memo.**
Save to `project-data/analysis/AXXX-risk-assessment-V01.md`:

```
## Risk Assessment: [Engagement Name]

### Risk Profile Summary
**Total risks identified:** [N]
**Red risks:** [N] — [brief list]
**Amber risks:** [N] — [brief list]
**Green risks:** [N]

### Top Risks (Red)

**RSK001: [Risk Title]**
- **Description:** [What could happen]
- **Likelihood:** [H/M/L] — [why]
- **Impact:** [Critical/High/Medium/Low] — [what it affects]
- **Source:** [Finding/analysis that identified this]
- **Mitigation:** [What to do about it]
- **Trigger:** [How to know it's happening]

[Repeat for each Red risk]

### Amber Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|----|------|-----------|--------|------------|
| RSK00X | [Description] | M/H | H/M | [Action] |

### Green Risks (Monitor)
[Brief list — accepted risks with low priority]

### Risk Interdependencies
[Are any risks correlated? Does one risk materializing increase the likelihood of others?]

### Implications for the Recommendation
[How do these risks affect the overall recommendation? Does the risk profile change the preferred option?]

### Monitoring Plan
[How often should the register be reviewed? What data points to track?]
```

**Step 8 — Present to the Principal.**
Present a concise risk summary:
"Risk register is [created/updated] — [N] risks identified: [X] red, [Y] amber, [Z] green.

Top concerns:
1. [Red risk 1] — mitigation: [action]
2. [Red risk 2] — mitigation: [action]

Key question: [any risk that requires a Principal decision — e.g., accept the risk, invest in mitigation, or adjust the recommendation]"

**Step 9 — Update hypothesis tree.**
Risks may surface new hypotheses or change confidence levels on existing ones. Update `project-data/hypotheses.json` if warranted.

**Step 10 — Link to other deliverables.**
- If a roadmap exists: cross-reference risks with implementation phases
- If a business case exists: connect financial risks to sensitivity drivers
- If a report is being assembled: note that risk assessment should be included
- Update `project-data/workstreams.json` with risk assessment deliverable status
