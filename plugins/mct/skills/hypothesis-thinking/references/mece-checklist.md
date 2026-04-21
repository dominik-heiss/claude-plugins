# MECE Checklist — Reference

Use this to audit any structure (issue tree, slide outline, options list, workstream plan) for MECE quality.

---

## Mutually Exclusive Check

For each pair of branches/elements, ask:

- [ ] **No definitional overlap:** Is it possible for a finding to fit under both branches simultaneously? If yes, the branches overlap — restructure.
- [ ] **No double-counting:** If summing across branches (e.g., market segments), does each unit of analysis appear exactly once?
- [ ] **Consistent level of abstraction:** Are all branches at the same conceptual level, or is one branch a sub-case of another?

**Common ME violations:**
- "Products" and "Services" when the company sells both bundles
- "Cost reduction" and "Efficiency improvement" (synonyms at different abstraction levels)
- "Europe" and "UK" in a geographic breakdown (UK is part of Europe)
- "New customers" and "Acquisition" (second is a means to achieve the first)

---

## Collectively Exhaustive Check

Ask: "If all branches are negative/false/small, is the question answered? Or is there a scenario not covered?"

- [ ] **Cover all plausible outcomes:** Does the tree include all reasonable answers to the core question?
- [ ] **Cover all stakeholder perspectives:** For strategic questions, does the tree capture market, competitive, financial, and organizational dimensions?
- [ ] **Cover edge cases:** What happens in extreme scenarios (market collapses, technology disruption, regulatory reversal)?

**Common CE failures:**
- Market entry tree that doesn't include "don't enter" as a valid conclusion
- Growth strategy that doesn't consider M&A when the industry is consolidating
- Cost reduction tree that misses external factors (input price inflation)

---

## Level Consistency Check

- [ ] **Same depth of analysis:** Are some branches much more decomposed than others without justification?
- [ ] **Parallel structure:** Do all branches answer the same type of question (all are "reasons why" or all are "options for action")?

---

## Practical MECE Guidance

**80% is good enough.** A structure with a clear critical path and named gaps is more useful than a perfect structure that takes twice as long to build.

**Name your gaps explicitly:** "This tree does not cover [X] — proposing to address in Phase 2 if relevant."

**Prioritization over perfection:** Even a non-MECE tree is valuable if it identifies the critical path. Get the top 2-3 branches right first.

---

## Quick MECE Test

Read out the branches to a colleague:
1. "If Branch A, Branch B, and Branch C are all false, does that mean the core question is answered?" → If yes, collectively exhaustive.
2. "Can a single finding simultaneously fit under Branch A AND Branch B?" → If yes, not mutually exclusive.
