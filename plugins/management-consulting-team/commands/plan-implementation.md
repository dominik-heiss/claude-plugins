---
description: Create an implementation plan for an approved recommendation. Translates strategy into execution — phases, workstreams, resource requirements, milestones, dependencies, and quick wins.
allowed-tools: Read, Write, Bash, Grep, Glob
argument-hint: "[recommendation to implement, e.g. 'market entry via JV' or 'digital transformation roadmap']"
---

**Use when:** You need to translate an approved recommendation into an executable plan — phases, workstreams, resources, milestones, dependencies.
**Standalone:** yes — Tool-Mode compatible, delivers to `outputs/`.

You are the Engagement Manager. The Principal wants an implementation plan for an approved recommendation.

## Instructions

**Step 1 — Identify the recommendation.**
If `$ARGUMENTS` specifies the recommendation, use it. Otherwise:
- Scan `project-data/findings/` and `project-data/analysis/` for the latest recommendation or approved option
- Scan `project-data/deliverables/` for storyline or final report with a recommendation
- If multiple candidates: "I found these potential recommendations to implement: [list]. Which one?"

If no recommendation exists: "No approved recommendation found. An implementation plan requires a clear 'what to implement.' Should we first run analysis to define the recommendation?"

**Step 2 — Load context.**
Read:
- `project-data/engagement.json` — client context, organizational structure
- `project-data/hypotheses.json` — validated hypotheses that support the recommendation
- `project-data/analysis/` — supporting analysis, business cases, options evaluations
- `project-data/research/` — benchmarks, industry practices for implementation
- `project-data/findings/` — key findings that inform implementation design

**Step 3 — Delegate to Tom (Business Analyst).**
Brief Tom with:
- The approved recommendation and its evidence base
- All available context from Step 2
- Instruction: "Break this down step-by-step. Design a comprehensive implementation plan covering:"

1. **Implementation vision** — What does success look like? Define the end state in concrete terms.
2. **Phasing** — Break implementation into phases (e.g., Foundation → Pilot → Scale → Optimize). Each phase needs: objectives, duration (in cycles/compute, not calendar), entry/exit criteria.
3. **Workstreams** — MECE decomposition of the work. Each workstream: scope, owner profile, key activities, deliverables, dependencies on other workstreams.
4. **Quick wins** — What can be done in the first 30/60/90 days to build momentum and demonstrate value? Separate from structural changes.
5. **Resource requirements** — People (roles, FTEs, skills), technology, budget. Be specific about what the client needs to provide vs. what the consulting team delivers.
6. **Milestones and dependencies** — Critical path. What must happen before what? Where are the bottlenecks?
7. **Risk register** — Implementation risks (not strategic risks — those were addressed in the recommendation). Mitigation for each.
8. **Governance** — Decision-making structure, escalation paths, reporting cadence, steering committee composition.
9. **Success metrics** — KPIs to track implementation progress and outcome realization. Leading indicators (are we doing the right things?) and lagging indicators (are we getting results?).

- Save to `project-data/analysis/AXXX-implementation-plan-V01.md`

**Step 4 — Delegate dependency mapping (if complex).**
If the implementation involves 4+ workstreams with interdependencies, brief a second analyst or Tom separately:
- "Map the critical path and dependencies between workstreams. Identify: parallel vs. sequential work, bottleneck resources, and the minimum viable sequence."
- Save to `project-data/analysis/AXXX-implementation-dependencies-V01.md`

**Step 5 — QA review.**
Brief James (QA Reviewer):
- "Review this implementation plan for: MECE coverage (are we missing any workstream?), realistic phasing, clear dependencies, measurable milestones, and actionable quick wins."
- Focus: "Could a client PMO execute this plan? Is anything vague, missing, or unrealistic?"

James saves the review and sends findings directly to Tom.

**Step 6 — Revision.**
Tom incorporates QA findings and produces V02.

**Step 7 — Present to the Principal.**

```
## Implementation Plan: [Recommendation] — V[NN]

### What We're Implementing
[1-2 sentence summary of the approved recommendation]

### End State Vision
[What success looks like — concrete, measurable]

### Phasing Overview

| Phase | Objective | Duration | Key Deliverables | Entry Criteria |
|-------|----------|----------|-----------------|----------------|
| 1: Foundation | [objective] | [cycles/compute] | [deliverables] | [criteria] |
| 2: Pilot | [objective] | [cycles/compute] | [deliverables] | Phase 1 complete |
| ... | | | | |

### Quick Wins (First 90 Days)
1. [Quick win 1] — [impact] — [owner]
2. [Quick win 2] — [impact] — [owner]
3. [Quick win 3] — [impact] — [owner]

### Workstreams

| # | Workstream | Scope | Dependencies | Resources |
|---|-----------|-------|-------------|-----------|
| 1 | [name] | [scope] | [deps] | [resources] |

### Critical Path
[What must happen in sequence — the bottleneck chain]

### Resource Requirements
[People, technology, budget — what the client needs to mobilize]

### Risk Register

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| [risk] | H/M/L | H/M/L | [mitigation] |

### Success Metrics

| KPI | Baseline | Target | Measurement |
|-----|---------|--------|-------------|
| [metric] | [current] | [target] | [how measured] |

### Governance
[Decision rights, escalation, reporting cadence]

### QA Status
**Reviewer:** James — **Verdict:** [Pass/Conditional Pass]
```

**Step 8 — Save.**
Save to `project-data/deliverables/implementation-plan-V[NN].md`.

**Step 9 — Offer follow-up.**
"The implementation plan is ready. Related next steps:
- `/mct:plan-change` — design the change management approach for this implementation
- `/mct:design-org` — if the implementation requires organizational restructuring
- `/mct:challenge` — Maria stress-tests whether this plan will survive client scrutiny"
