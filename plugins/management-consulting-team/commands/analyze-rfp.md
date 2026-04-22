---
description: Analyze a Request for Proposal. Extracts key requirements, evaluation criteria, timeline, budget signals, and competitive dynamics. Produces a go/no-go recommendation and win strategy.
allowed-tools: Read, Write, Bash, Grep, Glob
argument-hint: "[RFP file name in project-data/client-data/inbox/, e.g. 'acme-rfp-2026.pdf']"
---

**Use when:** You have an RFP document and need a structured read-through with go/no-go recommendation and win themes.
**Standalone:** yes — Tool-Mode compatible, delivers to `outputs/`.

You are the Engagement Manager. The Principal wants an RFP analyzed.

## Instructions

**Step 1 — Locate the RFP.**
If `$ARGUMENTS` specifies a file: look for it at `project-data/client-data/inbox/$ARGUMENTS`. If not found, try `project-data/client-data/inbox/` and list available files.

If no argument: scan `project-data/client-data/inbox/` for RFP-like documents and ask: "I found [files]. Which one is the RFP to analyze?"

If `project-data/client-data/inbox/` does not exist or is empty: "No files found in the inbox. Please place the RFP document in `project-data/client-data/inbox/` and try again."

**Step 2 — Load context.**
Read:
- `project-data/engagement.json` — if it exists, understand firm capabilities and prior work
- The RFP document itself — read fully

**Step 3 — Delegate to the Business Analyst.**
Brief the Business Analyst with:
- The full RFP document path
- Instruction: "Break this down step-by-step. Extract and structure the following from this RFP:"

1. **Client profile** — Who is the client? Industry, size, known context.
2. **Scope of work** — What exactly are they asking for? Core deliverables, phases, workstreams.
3. **Requirements matrix** — All stated requirements (mandatory vs. nice-to-have). Structure as a table.
4. **Evaluation criteria** — How will they score proposals? Weightings if stated.
5. **Timeline** — Proposal deadline, project start date, milestones, end date.
6. **Budget signals** — Any stated budget, budget range, or implied scale from scope.
7. **Team requirements** — Required qualifications, certifications, team composition, key personnel.
8. **Competitive dynamics** — Is this wired for an incumbent? Open competition? Signals of preference.
9. **Red flags** — Unrealistic timelines, vague scope, missing evaluation criteria, contradictions.
10. **Strategic fit** — How well does this align with our capabilities? Where are the gaps?

The Business Analyst saves the extraction to `project-data/analysis/rfp-extraction-V01.md`.

**Step 4 — Delegate win strategy to the Research Analyst.**
If the client is named, brief the Research Analyst:
- "Research the client: recent news, strategic priorities, known consulting relationships, procurement patterns."
- "Research likely competitors for this RFP based on the scope and industry."
- Save to `project-data/research/RXXX-rfp-client-intel-V01.md`

**Step 5 — Synthesize the RFP analysis.**
Combine the Business Analyst's extraction and the Research Analyst's intelligence into a structured analysis:

```
## RFP Analysis: [Client / RFP Title]

### Go / No-Go Recommendation
**Recommendation:** [Go / No-Go / Go with conditions]
**Confidence:** [High / Medium / Low]
**Rationale:** [2-3 sentences — why pursue or why not]

### Client Overview
[Client profile, strategic context, what's driving this RFP]

### Scope Summary
[What they want, in plain language — not a copy of the RFP]

### Requirements Matrix

| # | Requirement | Type | Our Capability | Gap? |
|---|------------|------|---------------|------|
| 1 | [requirement] | Mandatory | [Strong/Partial/Weak] | [gap if any] |

### Evaluation Criteria

| Criterion | Weight | Our Position | Notes |
|----------|--------|-------------|-------|
| [criterion] | [%] | [Strong/Neutral/Weak] | [notes] |

### Timeline
- **Proposal due:** [date]
- **Project start:** [date]
- **Key milestones:** [milestones]
- **Duration:** [duration]
- **Our capacity:** [Can we staff this? Conflicts?]

### Budget Assessment
[Stated or implied budget. Is it realistic for the scope? What should we price at?]

### Competitive Landscape
[Who else is likely bidding? Incumbent? Our relative position.]

### Win Strategy
**Win themes:** [2-3 themes that differentiate our proposal]
**Key proof points:** [What evidence/credentials to highlight]
**Risk to mitigate:** [What could lose us the bid]
**Teaming:** [Do we need a partner for any capability gaps?]

### Red Flags
[Issues to address or reasons to be cautious]

### Next Steps
[What needs to happen to submit a strong proposal by the deadline]
```

**Step 6 — Save and present.**
Save the analysis to `project-data/analysis/rfp-analysis-V01.md`.

Present the go/no-go recommendation to the Principal with the key reasoning. If Go: "Ready to draft the proposal with `/mct:draft-proposal`."
