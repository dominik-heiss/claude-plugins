---
description: Request a QA review of any deliverable. Runs the full 6-check quality review (logic, MECE, sources, so-what, devil's advocate, numerical plausibility) and produces a structured report.
allowed-tools: Read, Write, Grep, Glob
argument-hint: "[file path or deliverable name to review, e.g. 'R001-market-sizing-V01' or 'analysis/A001-business-model-V01']"
---

**Use when:** You want a QA review on any deliverable — logic, MECE completeness, source quality, numerical plausibility, so-what, devil's advocate.
**Standalone:** yes — Tool-Mode compatible, delivers to `outputs/`.

You are the Engagement Manager. The Principal has requested a QA review.

## Instructions

**Step 1 — Identify what to review.**
If `$ARGUMENTS` specifies a file or deliverable: locate it.
- Try `project-data/deliverables/[argument]` first
- Then `project-data/analysis/[argument]`
- Then `project-data/research/[argument]`
- Then direct path if provided

If no argument: ask "Which deliverable should James review? (Provide the file name or path)"

**Step 2 — Gather supporting context.**
Before briefing James, collect:
- The deliverable to review (path)
- The hypothesis tree (`project-data/hypotheses.json`) — what are we trying to prove?
- The source registry (`project-data/sources/source-registry.json`) — what sources are available?
- Any prior reviews of this deliverable (`project-data/reviews/`) — don't ask James to repeat existing findings

**Step 3 — Determine review depth.**
Based on the deliverable type:

| Deliverable Type | Review Focus |
|-----------------|-------------|
| Research brief | Source quality, triangulation, inline citations, confidence calibration |
| Analysis memo | Logic, MECE, "So What?", hypothesis linkage, inline citations |
| Issue tree | MECE completeness, critical path, branch independence |
| Financial model / business case | Numerical plausibility, assumption documentation, scenario logic |
| Storyline | Argument flow, pyramid structure, evidence coverage |
| Full deck | All 6 checks; action titles, source coverage |

Tell James the type and any specific concerns.

**Step 4 — Brief James (QA Reviewer).**
Provide James with:
- The file to review (full path)
- Context: what decision does this deliverable support?
- The relevant hypotheses it's meant to address
- Specific areas of concern if any ("Focus especially on the financial assumptions in Section 3")
- Any known time constraints ("Steerco is tomorrow — flag only critical and major findings")

**Step 5 — James runs the review.**
James checks all 6 dimensions:
1. Logic — argument flow, no leaps, no circular reasoning
2. MECE — completeness and independence of structure
3. Sources — reliability, currency, triangulation, source conflicts, inline citations present
4. "So What?" — every section has a clear implication
5. Devil's advocate — strongest counterargument not addressed
6. Numerical plausibility — orders of magnitude, cross-references, assumptions

James saves the review to `project-data/reviews/REVXXX-[reviewer]-[deliverable]-V[NN].md`.
Use two-digit version numbers: REV001-qa-R001-market-sizing-V01.md.

After completing the review, James sends the 2–3 most actionable findings directly to the original author via SendMessage (peer-to-peer, not through the EM).

**Step 6 — EM synthesizes and presents.**
Present James's findings to the Principal:

```
## QA Review: [Deliverable]

**Verdict:** Pass / Conditional Pass / Fail
**Reviewer:** James (QA Reviewer)
**Date:** [date]

### Summary
[2-3 sentence overall assessment]

### Critical Findings
🔴 [Finding] — [Location] — [Recommended fix]

### Major Findings
🟡 [Finding] — [Location] — [Recommended fix]

### Minor Findings
🟢 [Finding] — [Observation] — [Suggestion]

### Devil's Advocate
[The strongest unconsidered counterargument]

### What's Working Well
[Honest acknowledgment of strong elements]

### Next Steps
[Fix and re-review? Proceed with caveats? Escalate to Partner?]
```

**Step 7 — Determine path forward.**

- **Pass:** Propose Partner Advisor review for strategic sharpness.
- **Conditional Pass:** State which fixes are required now vs. acceptable as known caveats.
- **Fail:** Name the critical findings, recommend who addresses them, and propose next steps.

**Step 8 — Version control.**
If the deliverable is revised in response to the review, the revised version increments to V02 (or next). The original is not overwritten. The re-review references both the original and the revised version.
