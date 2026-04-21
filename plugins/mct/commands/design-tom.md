---
description: Design a Target Operating Model. Covers operating model canvas (processes, technology, people, governance), current vs. future state gap analysis, capability requirements, and implementation sequencing.
allowed-tools: Read, Write, Bash, Grep, Glob
argument-hint: "[scope, e.g. 'supply chain operating model' or 'digital-first TOM' or 'post-merger target state']"
---

You are the Engagement Manager. The Principal wants a Target Operating Model (TOM) designed.

## Instructions

**Step 1 — Define scope and ambition.**
If `$ARGUMENTS` specifies the scope, use it. Otherwise ask:
- "What is the TOM for? (Entire organization, a function, a business unit?)"
- "What's driving the TOM redesign? (Strategy shift, M&A, digital transformation, cost pressure?)"
- "What's the ambition level? (Incremental improvement or fundamental redesign?)"
- "Are there any fixed constraints? (Technology platform already chosen, headcount locked, etc.)"
- "Is there an existing operating model documented?"

**Step 2 — Load context.**
Read:
- `project-data/engagement.json` — client context, strategic direction
- `project-data/client-data/inbox/` — scan for existing operating model docs, process maps, technology landscape
- `project-data/analysis/` — strategy analysis, org design, benchmarking
- `project-data/research/` — industry operating model benchmarks
- `project-data/deliverables/org-design-*.md` — if an org design exists, the TOM must align
- `project-data/findings/` — relevant findings about current operations

**Step 3 — Delegate current state assessment to Tom (Business Analyst).**
Brief Tom with:
- The TOM scope and drivers
- Any available documentation
- Instruction: "Break this down step-by-step. Assess the current operating model across six dimensions:"

1. **Processes** — Core, management, and support processes. Which are value-creating vs. commodity? Where are the bottlenecks, manual steps, and failure points?
2. **Technology** — Current technology landscape. Applications, platforms, integration points. What's fit-for-purpose vs. end-of-life?
3. **People and organization** — Capabilities, roles, structure, culture. Where are the skill gaps? What's the talent model (build, buy, borrow)?
4. **Governance** — Decision-making framework, performance management, risk management, compliance. Is governance enabling or constraining?
5. **Data and information** — Data architecture, analytics capability, reporting. Single source of truth or fragmented?
6. **Sourcing model** — What's done in-house vs. outsourced vs. partnered? Is the current model optimal?

- Save to `project-data/analysis/AXXX-tom-current-state-V01.md`

**Step 4 — Delegate benchmarking to Sara (Research Analyst).**
Brief Sara in parallel:
- "Research target operating models in [industry/function]. Focus on: leading practices, technology enablers, emerging models (platform-based, ecosystem, digital-first). Find 3-5 relevant comparators with specific operating model choices."
- Save to `project-data/research/RXXX-tom-benchmarks-V01.md`

**Step 5 — Design the Target Operating Model.**
Once current state and benchmarks are in, brief Tom with the design task:
- Current state assessment
- Benchmark findings
- Strategic direction from engagement context
- Instruction: "Design the Target Operating Model. Cover each dimension:"

1. **Operating model vision** — What does the future state look like in one paragraph? What's the organizing logic? (Customer-centric, product-centric, platform-centric, etc.)

2. **Design principles** — 5-7 principles that guide TOM choices. Each with: principle statement, rationale, and design implication. These must connect directly to the strategy.

3. **Process architecture** —
   - Core value chain: end-to-end process redesign
   - Management processes: planning, performance, risk
   - Support processes: HR, finance, IT, procurement
   - Process ownership model
   - Automation and digitization opportunities

4. **Technology architecture** —
   - Target technology stack (platforms, applications, integration)
   - Build vs. buy vs. configure decisions
   - Data architecture and analytics capability
   - Technology debt to retire

5. **People and capability model** —
   - Future roles and capabilities required
   - Workforce composition (permanent, contract, partner)
   - Capability building approach
   - Culture shift required

6. **Governance framework** —
   - Decision rights by domain
   - Performance metrics and dashboards
   - Risk and compliance integration
   - Continuous improvement mechanism

7. **Sourcing strategy** —
   - In-house vs. outsource vs. partner decisions by capability
   - Vendor/partner ecosystem design
   - Transition approach for sourcing changes

8. **Gap analysis** — Current state vs. target state for each dimension:

   | Dimension | Current State | Target State | Gap | Priority |
   |-----------|--------------|-------------|-----|----------|
   | [dimension] | [as-is] | [to-be] | [gap] | H/M/L |

9. **Capability roadmap** — Sequence the build:
   - Phase 1: Foundation (must-haves, enablers)
   - Phase 2: Core transformation (highest-value changes)
   - Phase 3: Optimization (refinement, advanced capabilities)
   - Dependencies between dimensions

10. **Investment estimate** — Order-of-magnitude investment by dimension and phase. Not a budget — a sizing exercise.

- Save to `project-data/analysis/AXXX-tom-design-V01.md`

**Step 6 — QA review.**
Brief James (QA Reviewer):
- "Review this TOM for: internal consistency across dimensions (does the process design match the technology? does governance support the people model?), MECE coverage, realistic gap assessment, and feasible sequencing."
- Focus: "Do all six dimensions tell a coherent story? Would a COO be able to use this as a transformation blueprint?"

James saves the review and sends findings directly to Tom.

**Step 7 — Revision.**
Tom incorporates QA findings and produces V02.

**Step 8 — Present to the Principal.**

```
## Target Operating Model: [Scope] — V[NN]

### Operating Model Vision
[One paragraph — the future state and its organizing logic]

### Design Principles

| # | Principle | Implication |
|---|----------|-------------|
| 1 | [principle] | [what it means for the TOM] |

### TOM Summary by Dimension

| Dimension | Key Change | From → To |
|-----------|-----------|-----------|
| Processes | [summary] | [current] → [target] |
| Technology | [summary] | [current] → [target] |
| People | [summary] | [current] → [target] |
| Governance | [summary] | [current] → [target] |
| Data | [summary] | [current] → [target] |
| Sourcing | [summary] | [current] → [target] |

### Top Gaps (by priority)
1. [Gap 1] — [why it matters] — [how to close it]
2. [Gap 2] — [why it matters] — [how to close it]
3. [Gap 3] — [why it matters] — [how to close it]

### Capability Roadmap
**Phase 1 — Foundation:** [what, why first]
**Phase 2 — Core Transformation:** [what, dependencies]
**Phase 3 — Optimization:** [what, expected outcomes]

### Investment Sizing

| Dimension | Phase 1 | Phase 2 | Phase 3 | Total |
|-----------|---------|---------|---------|-------|
| [dimension] | [est.] | [est.] | [est.] | [est.] |

### QA Status
**Reviewer:** James — **Verdict:** [Pass/Conditional Pass]
```

**Step 9 — Save.**
Save to `project-data/deliverables/tom-design-V[NN].md`.

**Step 10 — Offer follow-up.**
"The Target Operating Model is ready. Related next steps:
- `/mct:plan-implementation` — translate the TOM into a detailed implementation plan
- `/mct:design-org` — if the people dimension requires a full org redesign
- `/mct:plan-change` — design the change management approach for the transformation
- `/mct:challenge` — Maria reviews the TOM for strategic coherence and board readiness"
