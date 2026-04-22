---
description: Create a stakeholder map with influence/interest matrix, engagement strategy per stakeholder, and communication plan. Essential for Phase 0 scoping and implementation planning.
allowed-tools: Read, Write, Grep, Glob
argument-hint: "[optional: context, e.g. 'for market entry decision' or 'for post-merger integration' or 'update with new stakeholders']"
---

**Use when:** You need a stakeholder influence/interest map with an engagement strategy per stakeholder.
**Standalone:** yes — Tool-Mode compatible, delivers to `outputs/`.

You are the Engagement Manager. The Principal wants a stakeholder analysis.

## Instructions

**Step 1 — Define scope.**
If `$ARGUMENTS` provides context: use it. Otherwise ask:
- "What decision or initiative is this stakeholder map for?"
- "Are we mapping internal stakeholders (client organization), external (market, regulators), or both?"
- "Do you have an initial list of key stakeholders, or should Tom identify them from the project context?"

**Step 2 — Load project context.**
Read:
- `project-data/engagement.json` — existing stakeholder information, client description
- `project-data/hypotheses.json` — what are we recommending? (Stakeholder positions depend on the recommendation)
- `project-data/research/` — any organizational or industry research that identifies stakeholders
- `project-data/findings/` — findings that reveal stakeholder interests or positions

**Step 3 — Delegate to Tom (Business Analyst).**
Brief Tom:
- The decision or initiative the stakeholder map supports
- Any known stakeholders from `engagement.json`
- The emerging recommendation direction (stakeholder reactions depend on what we're proposing)
- Instruction to produce:

  1. **Stakeholder identification** — Comprehensive list of all relevant stakeholders (individuals and groups). Think systematically: decision makers, influencers, implementers, affected parties, external parties.
  2. **Influence/Interest matrix** — Classify each stakeholder on two dimensions:
     - **Influence:** High / Medium / Low (power to affect the decision or block implementation)
     - **Interest:** High / Medium / Low (degree to which they are affected or care)
  3. **Position assessment** — For each stakeholder: current position (Supporter / Neutral / Opponent / Unknown), rationale, and what would move them
  4. **Engagement strategy** — Tailored approach per quadrant:
     - High influence, high interest → Manage closely (regular engagement, involve in decisions)
     - High influence, low interest → Keep satisfied (inform proactively, don't overwhelm)
     - Low influence, high interest → Keep informed (regular updates, channel for input)
     - Low influence, low interest → Monitor (periodic check-ins)
  5. **Communication plan** — Who needs what message, when, through what channel

  Break this down step-by-step — analyze each stakeholder systematically before building the matrix.

**Step 4 — EM reviews.**
Before presenting, check:
- Is the stakeholder list comprehensive? (No obvious missing parties — board, unions, regulators, customers, suppliers?)
- Are influence/interest assessments realistic? (Not everyone is "high/high")
- Are engagement strategies actionable? (Not generic "keep informed" — specific actions)
- Does the map account for the recommendation direction? (A cost-cutting recommendation changes stakeholder dynamics vs. a growth recommendation)

**Step 5 — Present the stakeholder map.**

Format:
```
## Stakeholder Map: [Decision/Initiative]

### Influence/Interest Matrix

|  | **High Interest** | **Low Interest** |
|--|-------------------|------------------|
| **High Influence** | [MANAGE CLOSELY] | [KEEP SATISFIED] |
|  | • [Stakeholder A] | • [Stakeholder D] |
|  | • [Stakeholder B] | • [Stakeholder E] |
| **Low Influence** | [KEEP INFORMED] | [MONITOR] |
|  | • [Stakeholder C] | • [Stakeholder F] |
|  | • [Stakeholder G] | |

### Stakeholder Profiles

#### [Stakeholder A] — [Role/Title]
- **Influence:** High — [why: decision authority, budget control, political capital]
- **Interest:** High — [why: directly affected, has strong views]
- **Current position:** Supporter / Neutral / Opponent
- **Key concern:** [What they care most about]
- **What moves them:** [What would shift their position]
- **Engagement strategy:** [Specific actions — not generic]
- **Communication:** [Channel, frequency, message framing]

#### [Stakeholder B] — [Role/Title]
...

### Coalition Analysis
**Natural allies:** [Stakeholders likely to support — and how to mobilize them]
**Likely opponents:** [Stakeholders likely to resist — and how to address concerns]
**Swing stakeholders:** [Could go either way — what tips them]
**Recommended sequence:** [Who to engage first, second, third — and why the order matters]

### Communication Plan

| Stakeholder | Message | Channel | Timing | Owner |
|-------------|---------|---------|--------|-------|
| [Name] | [Key message tailored to their concerns] | [1:1 / group / written] | [When relative to decision] | [Who delivers] |

### Risks
[Stakeholder-related risks: key person leaves, political shift, unexpected opposition]
```

**Step 6 — Save.**
Save to `project-data/analysis/AXXX-stakeholder-map-V01.md`.

**Step 7 — Update engagement.json.**
If the stakeholder map identified stakeholders not yet in `engagement.json`, propose additions: "The analysis identified [N] stakeholders not in the current project config. Want me to update `engagement.json` with the complete stakeholder list?"

**Step 8 — Connect to client lens.**
If the stakeholder analysis reveals important C-level dynamics: "The stakeholder map shows [CEO] and [CFO] may have divergent views on this. Want to configure them as Client Lens personas for simulation?"
