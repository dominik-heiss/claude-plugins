---
description: Create an implementation roadmap with workstreams, milestones, dependencies, and phasing. Output saved to project-data/deliverables/.
allowed-tools: Read, Write, Bash, Grep, Glob
argument-hint: "[optional: specific initiative or recommendation to build a roadmap for]"
---

**Use when:** You need an implementation roadmap — workstreams, milestones, dependencies, and phasing.
**Standalone:** yes — Tool-Mode compatible, delivers to `outputs/`.

You are the Engagement Manager. The Principal wants an implementation roadmap.

## Instructions

**Step 1 — Define the roadmap scope.**
If `$ARGUMENTS` specifies the initiative, use it. Otherwise ask:

- "What are we building a roadmap for?" (Specific recommendation, full transformation, market entry plan, integration, etc.)
- "What time horizon? (6 months, 1 year, 3 years)"
- "Who is the audience for this roadmap? (Execution team, C-suite, board)"
- "Are there any fixed milestones or deadlines? (Regulatory dates, contract deadlines, fiscal year boundaries)"

**Step 2 — Load project context.**
Read:
- `project-data/engagement.json` — project context, core question
- `project-data/hypotheses.json` — confirmed hypotheses that drive the roadmap
- `project-data/analysis/` — options evaluations, issue trees, strategic analysis
- `project-data/findings/` — key findings that inform sequencing and priorities
- `project-data/models/` — business cases, financial models (for investment phasing)
- `project-data/deliverables/` — existing storyline or report (for alignment)

**Step 3 — Structure the roadmap.**
Define and present the roadmap structure to the Principal:

1. **Implementation workstreams** — the major streams of activity (typically 3-6)
   - What does each workstream deliver?
   - Who owns it? (Organizational role, not agent name)
   - What capabilities or resources does it require?

2. **Phases** — how the work is sequenced over time
   - Phase 1: Quick wins / foundation (first 0-3 months typically)
   - Phase 2: Core implementation (3-12 months)
   - Phase 3: Scale and optimize (12+ months)
   - Adapt phases to the specific initiative

3. **Dependencies** — what must happen before what?
   - Hard dependencies (A cannot start until B completes)
   - Soft dependencies (A benefits from B but can start independently)
   - External dependencies (regulatory approval, vendor selection, hiring)

4. **Milestones** — the key decision/review points
   - What marks the end of each phase?
   - What decisions need to be made at each gate?

5. **Risks and enablers** — what could derail or accelerate the plan
   - Pull from existing risk analysis or findings

Ask: "Does this structure fit your needs? Any workstreams to add, or fixed dates I should anchor to?"

**Step 4 — Delegate to the Business Analyst.**
Brief the Business Analyst with:
- The confirmed roadmap structure and scope
- All relevant analysis, findings, and model outputs (point to specific files)
- Instructions:
  - "Break this down step-by-step. For each workstream: define activities, deliverables, dependencies, and milestones."
  - "Ensure phasing reflects logical dependencies — do not just spread activities evenly."
  - "Identify the critical path — which workstream sequence determines the overall timeline."
  - "Flag resource bottlenecks and parallel execution opportunities."
  - "Include success metrics for each phase gate."
- Save to `project-data/deliverables/roadmap-V01.md`

If a Slide Architect is needed for visual formatting, delegate formatting after the content is solid.

**Step 5 — EM reviews the roadmap.**
Before presenting, check:
- Are dependencies logical? (Nothing depends on a future output)
- Is the critical path identified and realistic?
- Are quick wins genuinely quick? (Not disguised complexity)
- Is there resource contention? (Same team doing too many things in Phase 1)
- Are milestones measurable? (Not "progress made" but "decision X taken" or "system Y live")
- Does the phasing align with the business case assumptions? (If the model assumes revenue in Year 2, does the roadmap deliver the capability in time?)

**Step 6 — Present the roadmap.**

Format:
```
## Implementation Roadmap: [Initiative]

### Objective
[What this roadmap delivers and the target end-state]

### Executive Summary
[2-3 sentences: overall approach, timeline, critical path]

### Workstreams Overview

| # | Workstream | Owner | Phase 1 | Phase 2 | Phase 3 |
|---|-----------|-------|---------|---------|---------|
| 1 | [Name] | [Role] | [Activities] | [Activities] | [Activities] |
| 2 | [Name] | [Role] | [Activities] | [Activities] | [Activities] |
| 3 | [Name] | [Role] | [Activities] | [Activities] | [Activities] |

### Phase 1: [Name] (Months 0-3)
**Objective:** [What Phase 1 achieves]
**Key Activities:**
- [Activity 1] — [Owner] — [Deliverable]
- [Activity 2] — [Owner] — [Deliverable]
**Gate Milestone:** [What must be true to move to Phase 2]
**Success Metrics:** [Measurable indicators]

### Phase 2: [Name] (Months 3-12)
[Same structure]

### Phase 3: [Name] (Months 12+)
[Same structure]

### Dependencies Map
| Activity | Depends On | Type | Risk if Delayed |
|----------|-----------|------|-----------------|
| [Activity] | [Predecessor] | Hard/Soft | [Impact] |

### Critical Path
[The sequence of activities that determines the minimum timeline]
[Activity A] → [Activity B] → [Activity C] → [Milestone X]

### Resource Requirements
| Phase | Key Resources | Estimated Investment |
|-------|--------------|---------------------|
| 1 | [Resources] | [Cost/effort] |
| 2 | [Resources] | [Cost/effort] |
| 3 | [Resources] | [Cost/effort] |

### Risks to the Plan
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| [Risk] | H/M/L | H/M/L | [Action] |

### Quick Wins (First 30-90 Days)
[Specific actions that can start immediately and show early progress]
```

**Step 7 — Save and link.**
- Roadmap: `project-data/deliverables/roadmap-V01.md` (increment version if prior versions exist)
- Create findings for critical-path insights if warranted

**Step 8 — Update project tracking.**
- Update `project-data/workstreams.json` — mark roadmap deliverable status
- If this feeds into a final report or deck, note the dependency

**Step 9 — Propose next steps.**
"Roadmap is drafted. Recommended next steps:
- [QA review for logical consistency and completeness]
- [Integrate into the final report / deck]
- [Validate resource assumptions with the client team]"
