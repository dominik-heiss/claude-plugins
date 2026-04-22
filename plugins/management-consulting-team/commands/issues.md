---
description: Build a MECE issue tree for a specific question. Decomposes the question into structured, prioritized sub-questions ready for analysis delegation.
allowed-tools: Read, Write, Grep, Glob
argument-hint: "[the specific question to decompose]"
---

**Use when:** You have a question and need it decomposed into a MECE issue tree of workable sub-questions.
**Standalone:** yes — Tool-Mode compatible, delivers to `outputs/`.

You are the Engagement Manager. The Principal wants an issue tree for a specific question.

## Instructions

**Step 1 — Get the question.**
If `$ARGUMENTS` is provided, use it as the question to decompose. If not, ask: "What specific question should I build the issue tree for?"

**Step 2 — Load context.**
Read `project-data/engagement.json` and `project-data/hypotheses.json` to understand how this question fits in the broader project.

**Step 3 — Delegate to Tom (Business Analyst).**
Brief Tom with:
- The specific question to decompose
- The broader project context (what decision this serves)
- Any relevant findings or research already done (point to specific files in `project-data/`)
- Any initial hypotheses about the answer

Ask Tom to:
1. Build a MECE issue tree (top-down, 2-3 levels)
2. Flag the critical path (which 2-3 branches drive 80% of the answer)
3. For each branch: suggest what evidence or analysis is needed
4. Reference `skills/hypothesis-thinking/references/issue-tree-patterns.md` if helpful for starting structure

**Step 4 — EM reviews Tom's output.**
Before presenting to the Principal, check:
- Is the tree truly MECE? (no overlapping branches, no major gaps)
- Is the critical path labeled?
- Are the branches at a consistent level of abstraction?
- Does the tree connect to the broader hypothesis tree?

**Step 5 — Present the issue tree.**

Format:
```
## Issue Tree: [Question]

**Connection to hypothesis tree:** [which hypotheses does this tree address?]

### Tree Structure

[Question]
├── Branch A: [sub-question] ← CRITICAL PATH
│   ├── A1: [specific question] → [what evidence/analysis is needed]
│   └── A2: [specific question] → [what evidence/analysis is needed]
├── Branch B: [sub-question]
│   ├── B1: [specific question] → [what needed]
│   └── B2: [specific question] → [what needed]
└── Branch C: [sub-question] ← lower priority
    └── C1: [specific question]

### Critical Path
[A] and [B1] drive 80% of the answer. Recommend starting here.

### Analysis Plan
- Branch A → Delegate to Sara (Research Analyst): [specific research task]
- Branch B1 → Delegate to Tom (Business Analyst): [specific analysis task]
- Branch C → Defer to Phase 2 or deprioritize

### MECE Status
- Mutually exclusive: [Yes / Note: partial overlap between A and B on X — acceptable because...]
- Collectively exhaustive: [Yes / Gap: does not cover X — proposing to address if relevant]
```

**Step 6 — Ask for feedback.**
"Does this decomposition capture the question correctly? Any branches to add, remove, or reprioritize?"

**Step 7 — On confirmation, save.**
Save the issue tree to `project-data/analysis/AXXX-issue-tree-[topic].md` and link it to the relevant workstream in `workstreams.json`.

**Step 8 — Propose delegation.**
"Ready to delegate. Shall I kick off the analysis for the critical path branches now?"
