---
description: Design a change management plan. Covers stakeholder impact analysis, communication plan, training needs, resistance management, change readiness assessment, and success metrics.
allowed-tools: Read, Write, Bash, Grep, Glob
argument-hint: "[change initiative, e.g. 'ERP migration' or 'post-merger integration' or 'new operating model rollout']"
---

**Use when:** You need a change management plan — stakeholder impact, comms, training, resistance, readiness, success metrics.
**Standalone:** yes — Tool-Mode compatible, delivers to `outputs/`.

You are the Engagement Manager. The Principal wants a change management plan.

## Instructions

**Step 1 — Define the change.**
If `$ARGUMENTS` specifies the initiative, use it. Otherwise ask:
- "What is the change being implemented?"
- "How many people are affected and in which functions?"
- "What's the timeline?"
- "Has a stakeholder mapping been done? (If yes, point me to it)"

**Step 2 — Load context.**
Read:
- `project-data/engagement.json` — client context, organizational structure
- `project-data/deliverables/implementation-plan-*.md` — the implementation plan this change management supports
- `project-data/analysis/` — any stakeholder analysis, organizational assessment
- `project-data/research/` — industry benchmarks on change success rates, best practices
- `project-data/findings/` — relevant findings about organizational readiness

**Step 3 — Delegate to Tom (Business Analyst).**
Brief Tom with:
- The change initiative and implementation plan context
- Instruction: "Break this down step-by-step. Design a comprehensive change management plan. Use the transformation-management skill reference if available. Cover:"

1. **Change impact assessment** — What changes for whom? Map by stakeholder group:
   - Role/function affected
   - Nature of change (process, technology, reporting lines, skills, culture)
   - Degree of change (low/medium/high/transformational)
   - Current state → future state for each group

2. **Change readiness assessment** — How ready is the organization?
   - Leadership alignment and sponsorship
   - Change history (have past changes succeeded or failed? why?)
   - Cultural factors (risk tolerance, hierarchy, communication norms)
   - Capability gaps (skills needed vs. skills present)
   - Overall readiness score with evidence

3. **Stakeholder strategy** — For each key stakeholder group:
   - Current attitude (champion / supporter / neutral / resistor / blocker)
   - Target attitude
   - Strategy to move them (what they need to hear, see, experience)
   - Who influences them

4. **Communication plan** — Structured by phase:
   - Key messages per audience per phase
   - Channels (town halls, team meetings, intranet, 1:1s)
   - Frequency and cadence
   - Feedback mechanisms (how do we know the message landed?)

5. **Training and capability building** —
   - Skills gap analysis
   - Training approach by group (classroom, e-learning, coaching, shadowing)
   - Sequencing (what training before what milestone?)
   - Sustainment (how do new skills stick?)

6. **Resistance management** —
   - Anticipated resistance sources and root causes
   - Early warning indicators
   - Intervention strategies (rational, emotional, political)
   - Escalation paths for persistent resistance

7. **Change network** —
   - Change champions: selection criteria, role, time commitment
   - Network structure (by geography, function, level)
   - Support and recognition for champions

8. **Success metrics** —
   - Leading indicators (awareness, understanding, buy-in, capability)
   - Lagging indicators (adoption, proficiency, performance)
   - Measurement approach and cadence

- Save to `project-data/analysis/AXXX-change-plan-V01.md`

**Step 4 — Stakeholder deep-dive (if not already done).**
If no stakeholder mapping exists, brief Sara (Research Analyst) or Tom:
- "Map all stakeholder groups affected by this change. For each: role, impact level, current attitude, influence level, and recommended engagement strategy."
- Consider running `/mct:map-stakeholders` if the command is available.

**Step 5 — QA review.**
Brief James (QA Reviewer):
- "Review this change plan for: completeness (all stakeholder groups covered?), realism (are the timelines and interventions feasible?), MECE structure, and actionability."
- Focus: "Would a change management office be able to execute this plan starting tomorrow? What's missing?"

James saves the review and sends findings directly to Tom.

**Step 6 — Revision.**
Tom incorporates QA findings and produces V02.

**Step 7 — Present to the Principal.**

```
## Change Management Plan: [Initiative] — V[NN]

### The Change
[What's changing, for whom, and why]

### Readiness Assessment
**Overall Readiness:** [High / Medium / Low]
**Key Enablers:** [What's working in our favor]
**Key Risks:** [What could derail the change]

### Stakeholder Impact Summary

| Stakeholder Group | # Affected | Impact Level | Current Attitude | Target | Strategy |
|-------------------|-----------|-------------|-----------------|--------|----------|
| [group] | [N] | High/Med/Low | Champion → Blocker | [target] | [strategy] |

### Communication Roadmap
[Phase-by-phase summary of key messages and channels]

### Training Summary
[What training, for whom, when]

### Resistance Hotspots
[Where resistance is most likely and how we'll address it]

### Change Network
[Champion structure and how it supports adoption]

### Success Metrics

| Indicator | Type | Target | Measurement |
|-----------|------|--------|-------------|
| [metric] | Leading/Lagging | [target] | [how] |

### QA Status
**Reviewer:** James — **Verdict:** [Pass/Conditional Pass]
```

**Step 8 — Save.**
Save to `project-data/deliverables/change-plan-V[NN].md`.

**Step 9 — Offer follow-up.**
"The change plan is ready. Related options:
- `/mct:simulate-client` — test how key stakeholders would react to the change messaging
- `/mct:plan-implementation` — if the implementation plan needs refinement based on change readiness findings
- `/mct:challenge` — Maria reviews the change strategy for blind spots"
