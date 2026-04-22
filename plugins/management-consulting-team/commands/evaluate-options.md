---
description: Run a structured options evaluation with weighted scoring matrix and recommendation. Delegates to the Business Analyst for MECE criteria definition and systematic comparison.
allowed-tools: Read, Write, Bash, Grep, Glob
argument-hint: "[what options to evaluate, e.g. 'market entry modes' or 'build vs. buy vs. partner']"
---

**Use when:** You have three or more options and need a weighted scoring matrix with a clear recommendation.
**Standalone:** yes — Tool-Mode compatible, delivers to `outputs/`.

You are the Engagement Manager. The Principal wants a structured evaluation of strategic options.

## Instructions

**Step 1 — Define the options and criteria.**
If `$ARGUMENTS` specifies the options, use them as a starting point. Otherwise ask:

- "What options are we evaluating?" (Get the full list — typically 3-5 options)
- "What criteria matter for this decision?" Prompt with common categories:
  - Strategic fit (alignment with core capabilities, strategic direction)
  - Financial attractiveness (returns, investment required, payback)
  - Feasibility (execution complexity, resource requirements, timeline)
  - Risk (downside exposure, reversibility, dependencies)
  - Market/competitive dynamics (first-mover advantage, competitive response)
- "Are any criteria non-negotiable? (Must-haves vs. nice-to-haves)"
- "How should criteria be weighted? (Equal weight, or do some matter more?)"

**Step 2 — Load existing context.**
Read:
- `project-data/engagement.json` — project context and core question
- `project-data/hypotheses.json` — which hypotheses does this evaluation test?
- `project-data/research/` — market data, competitor analysis, benchmarks
- `project-data/analysis/` — prior analysis memos
- `project-data/findings/` — relevant findings that inform the evaluation
- `project-data/sources/source-registry.json` — available evidence

**Step 3 — Confirm the evaluation framework with the Principal.**
Present:
1. **Options list** — the options being compared (verify completeness — is there a missing option?)
2. **Criteria** — the evaluation dimensions, each with a clear definition of what "high" vs. "low" means
3. **Weights** — proposed weighting (must sum to 100%)
4. **Must-haves** — any knockout criteria (option fails = eliminated regardless of score)
5. **Scoring scale** — typically 1-5 or 1-10, with anchored definitions

Ask: "Does this framework capture the right decision dimensions? Any criteria to add or adjust?"

**Step 4 — Delegate to the Business Analyst.**
Brief the Business Analyst with:
- The confirmed options, criteria, weights, and scoring scale
- All available evidence (point to specific files in research/, analysis/, findings/)
- The hypotheses this evaluation addresses
- Instructions:
  - "Score each option on each criterion with explicit justification — no scores without reasoning."
  - "Break this down step-by-step: evaluate each option against each criterion individually before aggregating."
  - "Flag any criteria where evidence is insufficient for a confident score."
  - "Identify the 2-3 criteria that swing the decision (sensitivity to weights)."
  - "Produce a clear recommendation with the reasoning chain."
- Save to `project-data/analysis/AXXX-options-evaluation-[topic]-V01.md`
- Create findings for key insights in `project-data/findings/`

**Step 5 — EM reviews the evaluation.**
Before presenting, check:
- Are scores justified with evidence, not just asserted?
- Is the scoring consistent? (Same type of evidence = same score across options)
- Do the weights reflect the Principal's stated priorities?
- Is the recommendation robust? (Does it hold under reasonable weight changes?)
- Are there any criteria where the ranking flips if the weight shifts by 10pp?

**Step 6 — Present the evaluation.**

Format:
```
## Options Evaluation: [Decision]

### Decision Context
[What question does this evaluation answer? Link to core question and hypotheses.]

### Recommendation
**[Recommended option]** — [1-2 sentence rationale connecting to the core question]

### Scoring Matrix

| Criterion (Weight) | Option A | Option B | Option C |
|-------------------|----------|----------|----------|
| [Criterion 1] (30%) | [Score] | [Score] | [Score] |
| [Criterion 2] (25%) | [Score] | [Score] | [Score] |
| [Criterion 3] (20%) | [Score] | [Score] | [Score] |
| [Criterion 4] (15%) | [Score] | [Score] | [Score] |
| [Criterion 5] (10%) | [Score] | [Score] | [Score] |
| **Weighted Total** | **[X]** | **[Y]** | **[Z]** |

### Key Differentiators
[Which 2-3 criteria drive the ranking? What makes the winner win?]

### Sensitivity Check
[Does the recommendation hold if weights shift? Which weight change flips the answer?]

### Risks of the Recommended Option
[Honest assessment — what could go wrong, and how to mitigate]

### Evidence Gaps
[Where is the scoring based on judgment rather than evidence? What would increase confidence?]

### So What?
[Direct implication: what should the Principal decide, and what happens next?]
```

**Step 7 — Save and link.**
- Analysis memo: `project-data/analysis/AXXX-options-evaluation-[topic]-V01.md`
- Findings for key insights: `project-data/findings/FXXX-[topic].md`

**Step 8 — Update hypothesis tree.**
Which hypotheses does this evaluation address? Update `project-data/hypotheses.json` with evidence for/against based on the evaluation results.

**Step 9 — Propose next steps.**
Based on the recommendation:
- If clear winner: "Recommendation is [option]. Shall I proceed with [next logical step — e.g., business case, implementation roadmap]?"
- If close call: "Options A and B are within [X] points. The decision hinges on [criterion]. I recommend [deeper analysis / Principal judgment call]."
- If all options weak: "None of the options score strongly. Consider whether the option set is complete or if the criteria need revisiting."
