---
description: Trigger a self-improvement cycle. Reads all agent feedback files, identifies recurring patterns, and proposes targeted updates to agent prompts, skills, and CLAUDE.md. Principal reviews and approves before any changes are applied.
allowed-tools: Read, Write, Glob, Grep
argument-hint: "[optional: 'apply' to apply previously approved changes, or leave empty to run analysis only]"
---

You are the Engagement Manager. The Principal has triggered a self-improvement cycle.

## Instructions

**Step 1 — Collect all feedback.**
Read all files matching `project-data/agent-memory/*/feedback.md`. Also read `project-data/agent-memory/engagement-manager/memory.md` for EM-level notes.

List which agents have feedback files and which do not.

**Step 2 — Identify patterns.**
Across all feedback files, look for:
- Recurring quality issues (same type of problem appears in multiple agents or multiple rounds)
- Systematic gaps (something that should be in a prompt or skill but isn't)
- Principal feedback that was logged but not yet acted on systemically
- Efficiency improvements that an agent identified but that would benefit others too

Group findings by theme, not by agent.

**Step 3 — Propose targeted changes.**
For each pattern, propose the minimum change that addresses it. Changes can target:
- An agent prompt file (`agents/[role].md`) — add or clarify a capability, constraint, or behavior
- A skill reference file (`skills/[skill]/references/[file].md`) — add a pattern, example, or anti-pattern
- `CLAUDE.md` — update a convention, routing rule, or process instruction
- A template (`assets/templates/`) — update a schema or structure

Present proposals as a structured list:

```
## Self-Improvement Proposals

### Pattern: [Name]
Source: [which feedback files / agents flagged this]
Proposed change: [file] → [what to add/change/remove]
Rationale: [why this addresses the pattern]
Impact: [which future tasks or agents benefit]
```

Do NOT apply changes yet. Present to the Principal for review.

**Step 4 — Apply approved changes (if `$ARGUMENTS` = "apply").**
If the Principal has reviewed and approved specific proposals (by number or name), apply only those changes. For each:
1. Read the target file
2. Make the minimum targeted edit
3. Confirm the change was applied

Do not apply unapproved proposals. Do not refactor or expand beyond the approved scope.

**Step 5 — Log the cycle.**
Append a brief entry to `project-data/agent-memory/engagement-manager/memory.md`:
- Date of the self-improvement cycle
- Number of proposals generated
- Number applied
- Key themes addressed
