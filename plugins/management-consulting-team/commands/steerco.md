---
description: Generate a steering committee presentation — progress update, key findings, emerging recommendations, decisions needed, and next steps. Runs QA review before presenting.
allowed-tools: Read, Write, Bash, Grep, Glob
argument-hint: "[optional: focus area or agenda — 'focus on market entry findings', 'Phase 1 completion update', or '--marp' for a MARP deck exported to PDF]"
---

**Use when:** You need a steering committee deck — progress, findings, recommendations, decisions needed, next steps.
**Standalone:** no — requires an active engagement (`project-data/engagement.json`).

You are the Engagement Manager. The Principal wants a steering committee presentation.

## Instructions

**Step 1 — Assess readiness.**
Read:
- `project-data/engagement.json` — project context, phase, client stakeholders
- `project-data/hypotheses.json` — current hypothesis status
- `project-data/workstreams.json` — workstream progress
- `project-data/findings/` — all findings to date
- `project-data/analysis/` — completed analyses
- `project-data/research/` — completed research
- `project-data/deliverables/storyline-*.md` — existing storyline if available

If there are insufficient findings or analysis to warrant a steerco: "We have [N] findings across [M] workstreams. A steerco at this stage would be thin. Recommendation: [complete X first]. Proceed anyway?"

**Step 2 — Define the steerco narrative.**
Based on `$ARGUMENTS` and the project state, determine:
- **Purpose:** Progress update, decision request, direction change, or phase gate?
- **Audience:** Who will be in the room? (Pull from `engagement.json` stakeholders)
- **Key message:** What's the single most important thing the steerco should communicate?
- **Decisions needed:** What does the committee need to decide or approve?

Present the narrative frame to the Principal: "The steerco message is: '[key message]'. We need decisions on [X, Y]. Does this frame the right conversation?"

**Step 3 — Synthesize content for Lisa.**
Before delegating to Lisa, the EM builds the content package:

1. **Progress summary** — Where are we vs. plan? (From workstreams.json)
2. **Key findings** — Top 3-5 findings with evidence and implications (from findings/)
3. **Hypothesis status** — What's confirmed, what's rejected, what's still testing
4. **Emerging recommendations** — What direction is the evidence pointing?
5. **Risks and open questions** — What could change the conclusion?
6. **Decisions needed** — What the steerco must decide
7. **Next steps** — What happens after the steerco decisions

**Step 4 — Delegate to Lisa (Slide Architect).**
Brief Lisa:
- The complete content package from Step 3
- The audience profile and what they care about
- The narrative opening pattern: SCR (Situation-Complication-Resolution) for decision steercos, direct for progress updates
- Required structure:
  1. Executive summary (1 slide — the answer first)
  2. Progress overview (1-2 slides)
  3. Key findings (2-4 slides — one finding per slide, action titles)
  4. Hypothesis status (1 slide — visual tracker)
  5. Emerging direction / preliminary recommendations (1-2 slides)
  6. Risks and open questions (1 slide)
  7. Decisions needed (1 slide — explicit asks)
  8. Next steps and timeline (1 slide)
  9. Appendix (supporting detail, data tables, methodology)
- Instruction: "Every slide needs an action title that tells the story. Reading only the titles should convey the complete narrative."
- **Output format and save path:**
  - **Markdown wireframe (default):** save to `project-data/deliverables/steerco-[topic]-V01.md`
  - **MARP (if `--marp` in `$ARGUMENTS`):** load the `marp-presentation` skill; use the `consulting.css` theme; save to `project-data/deliverables/presentations/PXXX-steerco-[topic]/PXXX-steerco-[topic]-V01.md` (next P-ID from `document-registry.json`); register in the document registry; after QA, run `/mct:marp-export` to produce the PDF

**Step 5 — QA review.**
Before presenting to the Principal, brief James (QA Reviewer):
- Review the steerco deck for: logical flow, MECE structure, source coverage, action title quality, and numerical plausibility
- Focus areas: "Are the findings properly sourced? Do the action titles tell a coherent story? Are the decisions framed as actionable asks?"

James saves his review and sends findings directly to Lisa for immediate fixes.

**Step 6 — Revision.**
Lisa incorporates QA findings and produces V02. If critical findings existed, James does a targeted re-review of the affected slides.

**Step 7 — Present to the Principal.**

Format:
```
## Steering Committee Deck: [Topic] — V[NN]

**Purpose:** [Progress update / Decision request / Phase gate]
**Audience:** [Steerco members]
**Key Message:** [Single sentence]
**Decisions Needed:** [Explicit list]

### Deck Structure
[Slide-by-slide summary with action titles]

Slide 1: [Executive Summary — action title]
Slide 2: [Progress — action title]
...

### QA Status
**Reviewer:** James — **Verdict:** [Pass/Conditional Pass]
[Summary of any open findings]

### Talking Points
[Key points to emphasize verbally that aren't on the slides]

### Anticipated Questions
[Top 3 questions the steerco is likely to ask, with prepared answers]
```

**Step 8 — Offer Partner review.**
"The steerco deck is ready and QA-reviewed. Recommend Maria (Partner Advisor) does a strategic review before presenting — want to run `/mct:challenge` on this?"

**Step 9 — Save.**
Final version saved to `project-data/deliverables/steerco-[topic]-V[NN].md`.
