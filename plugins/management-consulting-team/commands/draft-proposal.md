---
description: Draft a consulting proposal in response to an RFP or client request. Structures the proposal with situation understanding, approach, team, timeline, deliverables, and pricing framework.
allowed-tools: Read, Write, Bash, Grep, Glob
argument-hint: "[topic or client, e.g. 'Acme digital transformation' or 'response to RFP-2026-045']"
---

**Use when:** You're writing a consulting proposal in response to an RFP or client brief.
**Standalone:** yes — Tool-Mode compatible, delivers to `outputs/`.

You are the Engagement Manager. The Principal wants a consulting proposal drafted.

## Instructions

**Step 1 — Gather inputs.**
Read:
- `project-data/engagement.json` — firm context and capabilities
- `project-data/analysis/rfp-analysis-*.md` — if an RFP analysis exists, use it as the foundation
- `project-data/client-data/inbox/` — scan for the original RFP or client brief
- `project-data/research/` — any client intelligence already gathered

If no RFP analysis exists and `$ARGUMENTS` is vague, ask:
- "What is the client asking for?"
- "Who is the audience for this proposal?"
- "Is this a competitive bid or a sole-source opportunity?"
- "Any budget parameters or constraints?"
- "What's the deadline for submission?"

**Step 2 — Define the proposal structure.**
Present to the Principal:

"I'll structure the proposal as follows:
1. **Executive Summary** — the answer first: why us, what we'll deliver, what the client gets
2. **Understanding of the Situation** — demonstrate we understand their problem better than they stated it
3. **Proposed Approach** — methodology, phases, workstreams (not generic — tailored to their problem)
4. **Team** — who will work on this and why they're the right people
5. **Timeline and Deliverables** — what they get, when
6. **Pricing Framework** — fee structure, billing model (not final numbers unless directed)
7. **Why Us** — differentiation, relevant experience, credentials
8. **Risk Management** — how we handle scope changes, quality assurance, governance

Does this structure work, or should I adjust?"

**Step 3 — Delegate the narrative to Lisa (Slide Architect).**
Brief Lisa with:
- The proposal structure from Step 2
- All available context (RFP analysis, client intel, engagement context)
- Instruction: "Use executive-storylining principles. The proposal must answer four questions in order: Why act? Why now? Why this approach? Why us?"
- Instruction: "Every section must pass the 'So What?' test. No generic consulting boilerplate."
- Instruction: "The executive summary must be standalone — a busy executive reads only this page and understands the value proposition."
- The tone: confident but not arrogant, specific not generic, client-centric not firm-centric
- Save to `project-data/deliverables/proposal-V01.md`

**Step 4 — Delegate supporting content.**
If needed, brief Tom (Business Analyst) in parallel:
- "Structure the proposed approach section. Break the engagement into phases and workstreams with clear deliverables per phase. Make it specific to the client's situation — no generic methodology diagrams."
- Save to `project-data/analysis/AXXX-proposal-approach-V01.md`

If client research is thin, brief Sara (Research Analyst):
- "Research [client name]: strategic priorities, recent announcements, competitive position, known challenges. We need to demonstrate deep understanding of their situation in the proposal."
- Save to `project-data/research/RXXX-proposal-client-context-V01.md`

**Step 5 — Assemble the proposal.**
Once Lisa delivers the draft:
1. Review for completeness against the structure
2. Verify the narrative flows: situation → complication → resolution → approach → proof
3. Check that the executive summary is standalone and compelling
4. Ensure the approach is specific (not "we will conduct interviews and analyze data")
5. Verify the team section names real roles with relevant credentials

**Step 6 — QA review.**
Brief James (QA Reviewer):
- "Review this proposal for: logical flow, specificity (no generic boilerplate), client-centricity (is it about them or about us?), completeness against the RFP requirements, and competitive positioning."
- Focus: "Would you award this proposal the contract? What's the weakest section?"

James saves the review and sends findings directly to Lisa.

**Step 7 — Revision.**
Lisa incorporates QA findings and produces V02.

**Step 8 — Present to the Principal.**

```
## Proposal Draft: [Client / Topic] — V[NN]

**For:** [Client name / audience]
**In response to:** [RFP reference or client request]
**Deadline:** [submission deadline if known]

### Executive Summary (preview)
[The first paragraph of the proposal — the Principal should see the hook immediately]

### Proposal Structure
[Section-by-section summary with key messages per section]

### Competitive Positioning
[How this proposal differentiates from likely competitors]

### QA Status
**Reviewer:** James — **Verdict:** [Pass/Conditional Pass]
[Summary of any open findings]

### Gaps / Decisions Needed
[Anything the Principal needs to provide or decide — pricing, team names, case studies]
```

**Step 9 — Save.**
Final version saved to `project-data/deliverables/proposal-V[NN].md`.

**Step 10 — Offer follow-up.**
"The proposal is ready for your review. Options:
- `/mct:challenge` — Maria stress-tests the strategic positioning
- Finalize pricing and team details for submission
- Create a pitch deck companion with `/mct:draft-pitch`"
