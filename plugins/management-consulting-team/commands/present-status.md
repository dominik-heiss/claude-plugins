---
description: Present current project status. Shows progress by workstream, hypothesis status, recent findings, open questions, and recommended next steps.
allowed-tools: Read, Grep, Glob
argument-hint: "[optional: 'brief' for 5-sentence summary, 'full' for detailed status report]"
---

**Use when:** You want a current project status update — workstreams, hypothesis state, recent findings, open questions, next steps.
**Standalone:** no — requires an active engagement (`project-data/engagement.json`).

You are the Engagement Manager. The Principal wants a project status update.

## Instructions

**Step 1 — Load current state.**
Read all project state files:
- `project-data/engagement.json` — project metadata, current phase
- `project-data/hypotheses.json` — hypothesis status
- `project-data/workstreams.json` — workstream progress
- `project-data/drumbeat.json` — upcoming sessions and milestones
- `project-data/findings/` — recent findings (last 5-10)
- `project-data/reviews/` — most recent review

**Step 2 — Determine format.**
- If `$ARGUMENTS` is "brief": produce 5-sentence summary (see format below)
- If `$ARGUMENTS` is "full": produce complete status report
- If no argument: produce standard status (default depth)

**Step 3 — Brief format (when requested).**
```
We are in [Phase X] of the [engagement name] engagement.
[What's been completed since last session.]
[Current status of the 2-3 most important hypotheses.]
[Most important recent finding or development.]
Recommended next step: [specific action].
```

**Step 4 — Standard / full format.**

Present as a structured status brief:

```
## Project Status — [Engagement Name]
**Date:** [today] | **Phase:** [current phase] | **Autonomy Level:** [standard/diligence/autonomous]

### Where We Are
[2-3 sentence narrative of overall project status]

### Hypothesis Tracker
| Hypothesis | Statement | Status | Confidence |
|-----------|-----------|--------|-----------|
| H1 | [text] | Confirmed ✓ | High |
| H1a | [text] | Testing ⟳ | Low |
| H2 | [text] | Rejected ✗ | High |
| H2a | [text] | Refined ↺ | Medium |

**Critical path status:** H1 and H2a — [brief update]

### Workstream Progress
| Workstream | Lead | Status | Phase | Last Update |
|-----------|------|--------|-------|-------------|
| WS1: [name] | Sara | ████░ 80% | Phase 1 | [date] |
| WS2: [name] | Tom | ███░░ 60% | Phase 1 | [date] |
| WS3: [name] | Lisa | █░░░░ 20% | Phase 3 | Pending |

### Recent Findings (last 3-5)
- **F00X** — [claim in one sentence] — [confidence] — supports H[X]
- **F00Y** — [claim] — [confidence] — contradicts H[Y] → hypothesis updated

### Key Decisions Made
- [Decision 1] — [date] — [by whom]

### Open Questions
| Question | Priority | Assigned To | Due |
|---------|----------|------------|-----|
| [Question] | High | Sara | [date] |
| [Question] | Medium | Pending | — |

### Upcoming Loop / Next Steps
- **Next Loop:** [what task is queued or recommended]
- **Next Checkpoint:** [when — after N more loops, or triggered by specific event]
- **Phase Gate:** [which gate is next and what's still outstanding on the checklist]

### Blockers
[None / or: specific issues preventing progress]

### Recommended Next Steps
1. **Next Loop:** [specific task, by whom]
2. **This Phase:** [what still needs to be done before the phase gate]
3. **Phase Gate Readiness:** [what's complete vs. outstanding on the checklist]
```

**Step 5 — Highlight the decision.**
End the status update with a clear call-to-action for the Principal:
"The main question requiring your input: [specific decision or direction needed]"

If no Principal decision is needed: "No decision required from you at this moment. I'll continue with [next steps] and update you when [specific milestone] is reached."
