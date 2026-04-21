---
description: Create a pitch deck for a prospective engagement. Covers problem framing, proposed approach, team credentials, relevant experience, and expected outcomes. Pyramid structure throughout.
allowed-tools: Read, Write, Bash, Grep, Glob
argument-hint: "[topic or client, e.g. 'Acme Corp market entry strategy' or 'PE due diligence capabilities']"
---

You are the Engagement Manager. The Principal wants a pitch deck created.

## Instructions

**Step 1 — Define the pitch context.**
If `$ARGUMENTS` specifies the topic, use it. Otherwise ask:
- "Who is the audience for this pitch?"
- "What are we pitching? (A specific engagement, a capability, a relationship-building conversation?)"
- "What does the audience already know about us?"
- "What's their most likely objection or hesitation?"
- "Is there a specific meeting date or context?"

**Step 2 — Load available context.**
Read:
- `project-data/engagement.json` — firm context, capabilities
- `project-data/analysis/rfp-analysis-*.md` — if responding to an RFP
- `project-data/deliverables/proposal-*.md` — if a proposal exists, the pitch should complement it
- `project-data/research/` — any client or market intelligence

**Step 3 — Design the pitch narrative.**
Before delegating, define the narrative arc for the Principal:

"The pitch narrative is:
- **Hook:** [The client's problem, stated more sharply than they would state it themselves]
- **Stakes:** [Why this matters now — what's at risk if they don't act]
- **Insight:** [Our unique perspective on the problem — what we see that others miss]
- **Approach:** [How we'd tackle it — specific enough to be credible, concise enough to be clear]
- **Proof:** [Why we're the right team — credentials, relevant experience, results]
- **Ask:** [What we want from this meeting — next steps, follow-up, engagement]

Does this framing resonate, or should I adjust the angle?"

**Step 4 — Delegate to Lisa (Slide Architect).**
Brief Lisa with:
- The narrative arc from Step 3
- All available context (client intel, proposal, RFP analysis)
- Required deck structure:
  1. **Title slide** — client name, pitch topic, date
  2. **The problem** (1-2 slides) — framed from the client's perspective, with specifics
  3. **Why now** (1 slide) — market forces, competitive pressure, regulatory change
  4. **Our perspective** (1-2 slides) — the insight that differentiates our approach
  5. **Proposed approach** (2-3 slides) — phases, workstreams, key activities (not generic)
  6. **Expected outcomes** (1 slide) — what the client gets, quantified where possible
  7. **Team** (1 slide) — who will do the work, relevant credentials
  8. **Relevant experience** (1-2 slides) — case studies or proof points (anonymized as needed)
  9. **Next steps** (1 slide) — clear ask
  10. **Appendix** — supporting detail, methodology, firm credentials
- Instruction: "Every slide has an action title. Reading only the titles tells the complete pitch story."
- Instruction: "Pyramid structure — lead with the answer on every slide. Detail supports, not replaces, the headline."
- Instruction: "No slide with more than 3 key points. Ruthlessly prioritize."
- Save to `project-data/deliverables/pitch-deck-V01.md`

**Step 5 — QA review.**
Brief James (QA Reviewer):
- "Review this pitch deck for: narrative coherence, action title quality, specificity (no generic slides), persuasiveness, and flow."
- Focus: "If you were the client, would you take the next meeting? What's the weakest slide?"

James saves the review and sends findings directly to Lisa.

**Step 6 — Revision.**
Lisa incorporates QA findings and produces V02.

**Step 7 — Present to the Principal.**

```
## Pitch Deck: [Client / Topic] — V[NN]

**Audience:** [Who will be in the room]
**Context:** [Meeting type — intro, follow-up, competitive pitch]
**Objective:** [What we want from this meeting]

### Narrative Arc
**Hook:** [Problem statement]
**Insight:** [Our differentiated perspective]
**Ask:** [What we want next]

### Deck Structure
[Slide-by-slide with action titles]

Slide 1: [Title]
Slide 2: [Problem — action title]
Slide 3: [Why now — action title]
...

### QA Status
**Reviewer:** James — **Verdict:** [Pass/Conditional Pass]
[Summary of any open findings]

### Talking Points
[Key points to emphasize verbally — what's not on the slides but matters]

### Anticipated Objections
[Top 3 objections the audience might raise, with prepared responses]
```

**Step 8 — Offer Partner review.**
"The pitch deck is QA-reviewed. Want Maria (Partner Advisor) to stress-test the strategic positioning before the meeting? Run `/mct:challenge`."

**Step 9 — Save.**
Final version saved to `project-data/deliverables/pitch-deck-V[NN].md`.
