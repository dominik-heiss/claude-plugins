# Feedback System — memory.md, feedback.md, plugin feedback

Load this when writing or reading feedback, or running `/mct:self-improve`.

Every teammate maintains two persistent files in `project-data/agent-memory/[name]/`:
- `memory.md` — what they know and have done
- `feedback.md` — how they and the system can improve

## When to write to feedback.md

Be selective — only entries that genuinely improve future work:

- When a QA or Partner review flags an error or logical gap in their output that required rework.
- When the Principal or EM explicitly corrects their approach or output.
- When they identify a systematic improvement that would materially change how they'd approach the same task type next time.

Do not log routine task completion, minor wording tweaks, or observations with no actionable implication. Feedback files should stay concise and dense with signal.

## Reviewer-to-author feedback

After any review, the reviewer writes 2-3 actionable findings directly into the author's `project-data/agent-memory/[author-name]/feedback.md`. This is more efficient than routing via SendMessage and works regardless of orchestration mode.

## Principal feedback

When the Principal raises a concern about a teammate's output, the EM captures it and passes it in the next task brief: "Principal feedback from previous session: [...]". The EM also writes it directly into the teammate's `feedback.md`.

## Self-improvement

Run `/mct:self-improve` to trigger a synthesis cycle — the EM reads all feedback files, identifies patterns, and proposes targeted updates to agent prompts, skill references, and CLAUDE.md. The Principal reviews and approves before changes are applied.

## Plugin feedback file

The EM maintains `feedback_plugin.md` in the working directory root. This file collects generalizable observations about how the plugin itself could be improved — not project-specific feedback, but systematic patterns about agent behavior, process friction, skill gaps, or missing capabilities.

Write to `feedback_plugin.md` when:
- A review identifies a systematic issue that would apply across engagements (e.g., "agents consistently underestimate implementation complexity in cost models").
- The Principal explicitly gives feedback about how the plugin works (not the project content).
- Agents hit a limitation or produce suboptimal output due to how the plugin is designed.
- The EM notices process friction that a plugin change could resolve.

### Confidentiality rule

Never include client names, project names, engagement descriptions, stakeholder names, financial figures, or any other information that could identify a specific engagement or client. Feedback must be abstract and generalizable. Example: write "Financial Modeler doesn't separate direct personnel from overhead in service line P&Ls" — never "In the HydrogenCo engagement, Alex missed EUR 1.9m in double-counted FTE costs."

### Entry format

```markdown
## Plugin Feedback

### [YYYY-MM-DD] [Short title]
**Category:** [agent-behavior | process | skill-gap | missing-feature | usability]
**Observation:** [What happened, abstractly]
**Suggested improvement:** [What could change in the plugin]
```

This file is designed to be shareable with the plugin maintainer for continuous improvement.

## Inter-agent communication guidelines

**Encourage direct peer communication** — don't force everything through the EM.

Appropriate for direct teammate-to-teammate messages:
- Research Analyst shares a market finding that Business Analyst needs immediately for the issue tree.
- QA Reviewer sends findings directly to Slide Architect after reviewing a deck draft.
- Business Analyst asks Research Analyst to clarify a data point while they work on concurrent tasks.

Always flows through the EM:
- All communication with the Principal.
- Major synthesis and recommendation framing.
- Hypothesis tree updates.
- Phase gate decisions.
- Escalation of unexpected findings that change project direction.

**Status updates:** When teammates complete significant tasks, they should message the EM with a brief summary. The EM synthesizes these into status updates for the Principal (not raw teammate output).
