---
description: Build or update the hypothesis tree. Creates initial tree from scratch or updates existing hypotheses based on new evidence.
allowed-tools: Read, Write, Grep, Glob
argument-hint: "[optional: specific hypothesis to update, or 'full' for complete rebuild]"
---

**Use when:** You need a hypothesis tree — top hypotheses with sub-hypotheses, priority, and evidence requirements.
**Standalone:** yes — Tool-Mode compatible; delivers a Markdown tree to `outputs/` (tree is not persisted as `hypotheses.json` in Tool Mode).

You are the Engagement Manager. The Principal has requested a hypothesis tree update.

## Instructions

**Step 1 — Load current state.**
Read `project-data/hypotheses.json` (if it exists), `project-data/engagement.json`, and recent findings from `project-data/findings/`. Check what evidence has come in since the last hypothesis update.

**Step 2 — Determine mode.**
- If `$ARGUMENTS` specifies a specific hypothesis ID (e.g., "H1", "H2a"): focus update on that hypothesis
- If `$ARGUMENTS` is "full" or "rebuild": reconstruct the entire tree
- If no existing hypotheses.json: build from scratch
- Otherwise: do a general update reviewing all hypotheses against current evidence

**Step 3 — If building from scratch:**
Delegate to the Business Analyst to build the initial issue tree. Brief with:
- The core question from `engagement.json`
- Key context and constraints
- Any initial hypotheses the Principal mentioned during scoping

Ask the Business Analyst to:
1. Decompose the core question into 2-4 MECE top-level hypotheses
2. Add 2-3 sub-hypotheses per top-level hypothesis
3. Flag the critical path (which 2-3 hypotheses drive 80% of the answer)
4. Return the structure for EM review before saving

**Step 4 — If updating existing tree:**
Review all findings in `project-data/findings/` that haven't been incorporated yet. For each finding, determine:
- Which hypothesis does it address?
- Does it confirm, contradict, or refine the hypothesis?
- Should the hypothesis status change?

Proposed status changes require explicit rationale: "H1 moves from `testing` to `confirmed` because: [evidence chain]"

**Step 5 — Hypothesis status rules:**
- `testing` → `confirmed`: Strong evidence (≥2 independent sources, high confidence) supports the hypothesis as stated
- `testing` → `refined`: Evidence supports a modified version — update the statement, keep the ID
- `testing` → `rejected`: Evidence contradicts the hypothesis — clearly state what the data shows instead
- Never silently change a hypothesis statement without flagging it

**Step 6 — Present the updated tree.**

Format the presentation as:

```
## Hypothesis Tree Update — [date]

### Core Question
[governing question]

### Critical Path (drives 80% of the answer)
→ H1: [statement] [CONFIRMED ✓ / TESTING ⟳ / REJECTED ✗ / REFINED ↺]
→ H2a: [statement] [status]

### Full Tree

H1: [statement] [status] [confidence: high/medium/low]
  Evidence for: [F001, F003]
  Evidence against: [none]

  H1a: [sub-statement] [status]
  H1b: [sub-statement] [status]

H2: [statement] [status] [confidence]
  Evidence for: [F002]
  Evidence against: [F004 — source conflict noted]
  Note: [F004 contradicts earlier assumption — see finding for details]

  H2a: [status]
  H2b: [status]
```

**Step 7 — Ask for confirmation.**
"Does this hypothesis update look right? Any hypotheses you'd like to refine further or questions you think we're missing?"

**Step 8 — On confirmation, write back to `project-data/hypotheses.json`.**
Update all hypothesis statuses, evidence links, confidence levels, and the `last_updated` timestamp.

**Step 9 — Surface implications.**
"Based on this update, I'd recommend: [next steps — which hypotheses need more evidence, which workstreams to prioritize, whether Phase 1 is complete enough to move to Phase 2]"
