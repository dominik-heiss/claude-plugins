---
name: team-management
description: >
  This skill should be used when spawning agents for High or Very High compute
  tasks, when managing tasks that risk hitting token limits, when an agent needs
  to produce multi-file output, or when recovering from a session interruption.
  Use for "token limit", "incremental save", "multi-file output", "recover
  session", "context lost", "compaction recovery", "pause agent", "shut down
  team", "register specialist".
---

# Team Management — Token Protection & Agent Lifecycle

**Use when:** You're spawning agents for High / Very High compute tasks, preventing token-limit loss, managing multi-file output, or recovering an interrupted session.

For pause/shutdown/recovery/ad-hoc specialist procedures, see `references/team-lifecycle.md`. This skill focuses on **preventing data loss** and **managing output structure** for complex agent tasks.

## Token Limit Protection

Agents are ephemeral and lose all work if the session hits the token limit before they write output. These rules are mandatory for all agent briefs:

### 1. Incremental Saves

Instruct every agent in their task brief: "Save your output incrementally — write partial results to file after each major section. Do not wait until the task is fully complete to write."

For research briefs: write the research question + key findings first, then add sections progressively.
For analysis memos: write the analytical question + structure first, then fill in analysis by branch.
For financial models: write the summary with headline results first, then add detailed assumptions.

### 2. Task Sizing

Never assign more than **2 deliverables** per agent spawn. If a workstream requires 3+ deliverables, split into separate spawns with distinct task briefs and output paths.

Bad: "Write R002, A002, and A003 plus findings"
Good: "Write R002 and associated findings. Save to project-data/research/R002-topic-V01.md"

### 3. Write-First for Complex Tasks

For High/Very High compute tasks, instruct agents: "Write your initial framework/outline to file first, then fill in each section and save after completing each one."

This means the file exists from the start — even if the session ends mid-task, the framework and completed sections are preserved.

### 4. Multi-File Output Pattern

For reports with extensive analysis, instruct agents to produce multiple files:

| File | Purpose | Write Order |
|------|---------|-------------|
| `[ID]-summary.md` | Executive summary — key findings and implications | **First** (safety net) |
| `[ID]-report-V01.md` | Main report — full analysis | Second |
| `[ID]-appendix-V01.md` | Detailed reasoning, calculations, discarded alternatives | Third (if applicable) |

The summary is the safety net — even if the session ends mid-report, the key findings are preserved. The appendix captures work that was done but doesn't belong in the main report: detailed calculations, alternative approaches considered and rejected, raw data tables, extended reasoning chains.

**When to produce an appendix:**
- The task was High or Very High compute
- Extensive calculations or modeling were performed
- Multiple approaches were evaluated before selecting one
- The main report would exceed ~2000 words if all detail were included

**When NOT to produce an appendix:**
- The task was Low or Medium compute
- The report is already concise and complete
- No significant reasoning or calculations need preservation

## Recovery After Interruption

When a session is interrupted (token limit, crash, network issue):

1. Check `project-data/` for partially written files — these are the agent's incremental saves
2. Check `tasks.json` for tasks that were `in-progress` when the session ended
3. For each incomplete task: check if the output file exists and assess completeness
4. Respawn agents with explicit instructions: "Continue from the existing file at [path]. Read it first — sections [X, Y] are complete, section [Z] needs completion."
5. Brief the Principal on what was recovered and what remains
