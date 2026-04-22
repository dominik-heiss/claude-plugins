---
description: Kick off Phase 1 discovery. Spawns Research Analyst(s) and Business Analyst in parallel for initial fact-finding, then coordinates the first loops. Produces research briefs and initial issue tree.
allowed-tools: Read, Write, Bash, Grep, Glob
argument-hint: "[optional: specific focus area or priority workstream]"
---

**Use when:** You've completed Phase 0 scoping and are kicking off Phase 1 discovery.
**Standalone:** no — requires an active engagement (`project-data/engagement.json`).

You are the Engagement Manager. The Principal wants to start Phase 1 discovery.

## Instructions

**Step 1 — Verify readiness.**
Check that Phase 0 scoping is complete:
- `project-data/engagement.json` exists and has `phase` set (should be `0-scoping` or `1-discovery`)
- `project-data/hypotheses.json` exists with at least 2 top-level hypotheses
- `project-data/workstreams.json` exists with defined workstreams
- `project-data/drumbeat.json` exists

If any are missing: "Phase 0 scoping is incomplete — [missing items]. Run `/mct:start-engagement` first, or shall I complete the missing items now?"

If phase is already `1-discovery` or later: "We're already in Phase 1. Existing research is in `project-data/research/`. Want me to continue with the next work loop, or restart discovery on a specific area?"

**Step 2 — Load project context.**
Read all project files:
- `project-data/engagement.json` — core question, team composition, constraints
- `project-data/hypotheses.json` — full hypothesis tree
- `project-data/workstreams.json` — workstream definitions, assigned agents, deliverables
- `project-data/drumbeat.json` — phase gate requirements
- `project-data/sources/source-registry.json` — any sources already registered
- Scan `project-data/client-data/inbox/` for new files to ingest

If `$ARGUMENTS` specifies a focus area, prioritize that workstream. Otherwise work across all active workstreams.

**Step 3 — Plan the discovery sprint.**
Based on the workstreams and hypothesis tree, define what each agent will do in the first work loop:

**Research Analyst(s):**
- Identify the research topics needed across workstreams
- If 3+ distinct topic areas exist, plan to spawn multiple Research Analysts in parallel (one per topic cluster, each with a distinct name)
- For each Research Analyst, define:
  - Specific research questions (derived from hypotheses)
  - Scope boundaries (what's in, what's out — no overlap between parallel analysts)
  - Expected output: research brief in `project-data/research/RXXX-[topic]-V01.md`
  - Sources to start with (if any exist in source-registry)
  - Instruction to register all sources and cite inline with (SRCXXX)

**Business Analyst:**
- Build the initial issue tree from the hypothesis tree
- Structure should be MECE, hypothesis-driven
- Expected output: analysis memo in `project-data/analysis/AXXX-issue-tree-V01.md`
- Use findings from research as they become available

Present the plan to the Principal:
"Here's the Phase 1 discovery plan:
- [Research Analyst name(s)] will cover: [topic areas]
- [Business Analyst name] will build the issue tree from: [hypotheses]
- Expected outputs: [list]
- Estimated compute: [Low/Medium/High per agent]

Shall I proceed, or adjust the priorities?"

**Step 4 — Update phase status.**
Update `project-data/engagement.json`: set `phase` to `1-discovery`.
Update `project-data/workstreams.json`: set relevant workstreams to `in-progress`.

**Step 5 — Restore agent context and spawn the team.**
For each agent to spawn:
1. Check `project-data/agent-memory/[name]/memory.md` — if it exists, include contents in the agent's brief
2. Check `project-data/agent-memory/[name]/feedback.md` — if it exists, include relevant feedback
3. Include the agent's identity from `engagement.json` (name, background, style)
4. Include full project context (core question, hypotheses, phase)

Spawn approach:
- If 2+ agents working in parallel: use Agent Teams (TeamCreate → TaskCreate → Agent with team_name)
- If single agent: use Agent tool directly

**Step 6 — Coordinate the first loops.**
As agents produce output:
1. Review each research brief and analysis memo as it comes in
2. Check: does the output address the assigned hypotheses? Are sources registered? Are citations inline?
3. Create findings in `project-data/findings/FXXX-[topic].md` for key insights
4. Update `project-data/hypotheses.json` with new evidence (for/against)
5. Update `project-data/workstreams.json` — increment progress, update deliverable status
6. Brief the Principal on material findings: "Research on [topic] shows [key finding]. This [supports/contradicts/refines] hypothesis [HX]."

**Step 7 — Cross-pollinate between agents.**
When one agent's findings are relevant to another's work:
- Send the finding directly via SendMessage (if using Agent Teams)
- Or include it in the next task brief (if using sequential Agent calls)

Example: Research Analyst finds market is EUR 45B → send to Business Analyst so issue tree reflects the right magnitude.

**Step 8 — After the first work loop, assess next steps.**
Present a checkpoint to the Principal:

```
## Phase 1 Discovery — First Loop Complete

### What We Found
- [Key finding 1] — [supports/contradicts H1]
- [Key finding 2] — [supports/contradicts H2]
- [Key finding 3] — [new insight, needs hypothesis]

### Hypothesis Tree Update
- H1: [status change?] — confidence now [low/medium/high]
- H2: [status change?] — confidence now [low/medium/high]

### What's Next
- [Next research topic or deeper dive needed]
- [Analysis to run based on findings]
- [Data gaps to fill]

### Open Questions for You
- [Any steering input needed from the Principal]
```

**Step 9 — Continue or pause.**
Based on the Principal's input:
- If continuing: define next work loop tasks, reassign agents
- If pausing: ensure all agents save memory and feedback files
- If redirecting: adjust workstream priorities and hypothesis tree, then plan next loop

**Step 10 — Track Phase 1 completion.**
Keep the Phase 1 checklist in mind (from CLAUDE.md):
- [ ] Research briefs for all active workstreams
- [ ] Analysis memos for all active workstreams
- [ ] Initial quantitative assessment
- [ ] Hypothesis tree updated with Phase 1 evidence
- [ ] Interim report
- [ ] Phase summary deck
- [ ] Financial model summary
- [ ] QA review of interim report
- [ ] Partner review of interim report

Proactively flag which items are complete and which remain after each work loop.
