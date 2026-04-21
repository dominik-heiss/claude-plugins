---
name: hypothesis-thinking
description: >
  This skill activates when the user asks to "build a hypothesis tree",
  "decompose a problem into sub-questions", "check MECE completeness",
  "structure an issue tree", "test a hypothesis against evidence",
  "prioritize analysis branches", or needs guidance on hypothesis-driven
  analysis, problem structuring, or avoiding cognitive biases in structuring.
---

# Hypothesis Thinking — Principles

You reason hypothesis-first. Always.

## The Core Principle

**Start with an answer, then prove or disprove it.** Never start with data collection and wait to see where it leads. This is the fundamental difference between consulting-grade analysis and academic research.

A hypothesis is a specific, testable answer to a question: "I believe X is true because of Y. Here's how we would know if I'm wrong."

A hypothesis is NOT: a research question, a topic to explore, or a vague expectation.

## Building the Hypothesis Tree

**Top-down always.** Never bottom-up.

```
Core Question (What decision does this project answer?)
├── Hypothesis H1: [Specific answer to part of the question]
│   ├── H1a: [Sub-hypothesis — more specific assertion]
│   └── H1b: [Sub-hypothesis]
├── Hypothesis H2: [Alternative or complementary answer]
│   ├── H2a: [Sub-hypothesis]
│   └── H2b: [Sub-hypothesis]
└── Hypothesis H3: [Another dimension of the answer]
```

**Critical path rule:** Which 2-3 hypotheses drive 80% of the answer? Label them as high-priority. Don't let the team spend equal time on all branches.

**Naming convention:** Hypotheses get IDs (H1, H1a, H2, etc.) that are referenced in all findings, analysis memos, and slides.

## MECE in Hypothesis Trees

**Mutually exclusive:** No two hypotheses should cover the same ground. If confirming H1 automatically confirms H2, they're not independent — restructure.

**Collectively exhaustive:** The hypothesis tree covers all possible answers to the core question. If there's a plausible answer that doesn't fit under any hypothesis, add a branch.

80% MECE is good enough for the first pass. Name the gap explicitly: "This tree covers the main drivers. Area not yet covered: [X]."

## Testing Hypotheses

A hypothesis is tested by finding evidence that would either confirm or contradict it. To test H1:
1. What data would confirm H1? → go collect it
2. What data would contradict H1? → go collect that too
3. What's the minimum evidence needed to make a judgment?

**Hypotheses have an expiration date.** When data contradicts a hypothesis:
- Do not soften the conclusion ("the market seems to be slightly smaller than expected")
- Say it directly: "H1 is rejected. Evidence shows [X]. Revised hypothesis: [new H1]"
- Update the hypothesis tree immediately

**Status vocabulary:**
- `confirmed` — evidence strongly supports the hypothesis
- `testing` — evidence gathering in progress, no conclusion yet
- `refined` — hypothesis is partially correct but needed adjustment
- `rejected` — evidence contradicts the hypothesis

## Prioritization: The 80/20 Rule

Not all branches of the issue tree deserve equal attention. Before delegating research:

1. Rank hypotheses by decision impact: which sub-answers would most change the recommendation?
2. Rank by uncertainty: which hypotheses are most uncertain given current knowledge?
3. Prioritize where both are high: high impact + high uncertainty = critical to analyze
4. Deprioritize where impact is low or confidence is already high

State your prioritization explicitly: "H1 and H2a are the critical path. H3 is low priority — likely confirmatory."

## Common Traps

**Confirmation bias** — searching for evidence that supports the hypothesis and discounting contradictory evidence. Counter: explicitly assign someone to find evidence AGAINST each hypothesis.

**Boiling the ocean** — generating a complete, perfectly MECE issue tree before any analysis. Counter: a rough tree with a clear critical path is worth more than a perfect tree with no prioritization.

**Circular reasoning** — using the hypothesis as evidence for itself. Counter: always trace every piece of evidence back to a primary source.

**Anchoring on the first hypothesis** — the initial hypothesis shapes all subsequent analysis even when early evidence contradicts it. Counter: force an explicit "hypothesis update" checkpoint after Phase 1 findings.

**False precision** — stating hypotheses so specifically that small variations in data lead to constant restructuring. Counter: hypotheses should be specific enough to be testable but not so specific that they can't survive data noise.

## When to Load Reference Files

- Building an issue tree for a specific problem type → `references/issue-tree-patterns.md`
- Checking MECE completeness of a structure → `references/mece-checklist.md`
- Worried about reasoning quality or team biases → `references/cognitive-biases.md`
