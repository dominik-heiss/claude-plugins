# Team Lifecycle — Initialization, Pausing, Shutdown, Recovery

Load this when starting a session, pausing/resuming teammates, or recovering after context loss.

**Teammates are ephemeral** — they have no memory across sessions. Before spawning teammates, you must restore their context, and you must ensure they write memory before being dismissed.

## Initialization (every spawn)

1. For each teammate you're about to spawn:
   - Check if `project-data/agent-memory/[name]/memory.md` exists (use the agent's configured **name** from `engagement.json` — e.g., `sara/`, `tom/` — not the role name). This prevents conflicts when multiple agents of the same role run in parallel.
   - If yes: include its contents in that teammate's first task brief as context.
   - Example: "Before starting your task, here is your memory from previous sessions on this engagement: [contents]"
2. Include the teammate's identity from `engagement.json` in their task brief:
   - Their configured `name`, `background`, and `style`.
   - The current project context (core question, active hypotheses, phase).
3. **Always specify the exact output file path in every task brief.** Example: "Save your output to `project-data/research/R002-market-sizing-V01.md`." Do not let the agent choose the filename. Read `workstreams.json` to determine what files are planned; pass those paths explicitly. This prevents duplicate files with slightly different names when agents are respawned.

This ensures every teammate starts each session informed, not from zero.

## Pausing vs shutdown

**Pausing a teammate** ("stop", "hold"): Send "Pause. Save all in-progress output to file now. Write memory and feedback files." Wait for confirmation. Leave running — do NOT shutdown. **Default: "stop" = pause, not shutdown.**

**Shutting down a teammate** (session end, phase complete): Confirm memory + feedback written → send `shutdown_request` → wait for `shutdown_approved`.

## Recovery after context loss

1. `TeamDelete` for orphaned teams.
2. Load `workstreams.json` + `tasks.json`.
3. Check existing deliverables on disk.
4. Respawn with explicit file paths.
5. Brief Principal.

## Ad-hoc specialists

Register in `engagement.json` under `extended_team` before spawning. Instruct to write memory to `project-data/agent-memory/[name]/memory.md`.

## EM memory

After any session where you ran the scoping dialog, made significant synthesis decisions, or updated the hypothesis tree, write a brief entry to `project-data/agent-memory/marcus/memory.md`. This is your reasoning log — it captures what is NOT already derivable from the project files.

### What belongs in EM memory (delta information only)

- The *reasoning* behind key decisions (why option A was chosen over B, what trade-off was made).
- Open questions and unresolved tensions not yet captured anywhere.
- Stakeholder observations that should inform future interactions (e.g., what a specific Principal stakeholder reacted positively/negatively to).
- Pattern insights across sessions (e.g., "Principal consistently pushes back on M&A framing").
- What changed since the last session and why.

### What does NOT belong in EM memory

- Content already in `engagement.json` (team, stakeholders, constraints, client description).
- Content already in `hypotheses.json` (hypothesis statements, evidence, status).
- Content already in `workstreams.json` (workstream descriptions, deliverables, key questions).
- Summaries of what was done — that's in the files themselves.

Keep entries short and high-signal. A good EM memory entry reads like a senior partner's handwritten note between sessions — not a project summary.

## Memory folder naming rule

All memory lives at `project-data/agent-memory/[name]/` where `[name]` is the configured name (e.g., `sara/`, `tom/`, `marcus/` for the EM). Never use role names as folder names — this avoids collisions when multiple agents of the same role run in parallel. The EM's folder is always `marcus/`, never `engagement-manager/`.
