# Orchestration — Agent Teams vs Individual Subagents

Load this when spawning agents or deciding how to parallelize a task block.

Two orchestration modes are available. **The configured mode in `engagement.json → configuration.orchestration` is authoritative.** The EM does NOT pick the mode per task block — it follows the config. Deviating for a specific task block requires **explicit Principal approval, asked for and received before spawning**. Silent deviation (running Individual Subagents when the config says Agent Team, or vice versa) is a process failure.

## Mode A: Agent Teams

**Enable:** `~/.claude/settings.json` → `{ "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }`

Agent Teams allow teammates to communicate directly with each other — the Research Analyst can share a finding with the Business Analyst immediately without routing through you, the QA Reviewer can send findings directly to the Slide Architect, teammates self-coordinate on concurrent tasks.

**Advantages:** Direct peer communication, true parallelism, less EM bottleneck on high-fan-out phases.

## Mode B: Individual Subagents

Spawn agents individually via the `Agent` tool (no `team_name`). Each agent reports directly back to the EM. The EM coordinates sequencing, passes findings between agents, and synthesizes results.

**Advantages:** Simpler, more stable, full EM control over every handoff, lower overhead for small task blocks.

## Which mode — Phase-0 scoping guidance

This table is input to the **Phase-0 configuration dialog** (see `/mct:start-engagement` Step 4c), where the Principal picks the default for the engagement. After Phase 0, the config is fixed.

| Factor | Favors Individual | Favors Agent Team |
|--------|-------------------|-------------------|
| Task dependencies | Sequential / chained | Independent / parallel |
| Number of concurrent agents | 1-2 | 3+ |
| Peer communication needed | No (EM relays) | Yes (direct exchange) |
| Stability priority | High | Lower (experimental) |
| Token efficiency | Better (less overhead) | Better only at scale |

## Running the configured mode — announce before each task block

The EM announces what's about to run in one sentence (who, how, why) — but the "how" is dictated by the config, not a per-block choice. Example: "Following the configured Agent Team mode, I'll spawn Sara, Tom, and Kim on the parallel research wave." No "I'll run this as individual subagents because…" unless asking for a deviation.

## Requesting a deviation — explicit ask required

If the EM believes a specific task block is genuinely ill-suited to the configured mode (e.g., config says Agent Team but this is a single one-off review with no peer communication), the EM asks:

> "Configured mode is Agent Team, but this is a single QA review with no peers. Propose to run it as an individual subagent instead — approve?"

Wait for approval. Do not proceed until the Principal says yes. If unsure or the Principal is not immediately available, default to the configured mode.

## Agent Team spawn workflow — always in this order

1. **Check for existing team** — before `TeamCreate`, check if a team with that name already exists. If yes, call `TeamDelete` first. Failing to do this causes "Already leading team" errors that block the entire spawn.
2. `TeamCreate` — create the team (team_name, description). Use engagement-scoped names: `[engagement-slug]-[phase]` e.g. `wi-energy-phase1`. This reduces collision risk across sessions.
3. `TaskCreate` — define tasks up front so teammates can claim them.
4. `Agent(subagent_type="general-purpose", team_name=..., name=..., model="sonnet")` — one call per teammate; they join the team and receive tasks via `TaskUpdate` or `SendMessage`.
5. `SendMessage` — assign work, coordinate, receive results.

## subagent_type is always `general-purpose`

Plugin agent definitions provide identity and behavior via the prompt — not via a custom subagent type. Pass the teammate's name, background, style, and task context in the Agent prompt.

## Model selection for spawned agents

- **Default: `sonnet`.** Always pass `model="sonnet"` for standard tasks: market research, regulatory mapping, competitive landscape, issue trees, slide creation, analog case studies.
- **Use `opus` for complex analytical tasks:** financial modeling, strategic options evaluation, capability assessment, M&A analysis, multi-dimensional synthesis, capstone deliverables. The EM decides based on task complexity — no need to ask the Principal each time.
- **Reviews:** QA and Partner reviews use `opus` when the deliverable is high-stakes (phase gate, client-facing). Standard reviews use `sonnet`.
- The EM runs in the main context — no model override needed there.

## One spawn, one task — with one exception

Each agent handles ONE task brief. When the task is complete, the agent writes memory + feedback and is dismissed. Do NOT assign new unrelated tasks to an already-running agent — this grows context indefinitely.

**Exception:** Keep an agent alive through its own review loop (QA feedback → revise → re-submit). Once the revision cycle is closed and the deliverable is approved, dismiss. For the next independent task: new spawn with memory loaded.

## Parallel Research Analysts

When research covers 3+ distinct topic areas simultaneously, spawn multiple Research Analysts in parallel — one per topic cluster. Each gets a distinct name in their task brief (e.g., the Research Analyst's configured name for market sizing, a second instance named "Kim" for regulatory, etc.), a clearly scoped research brief with no overlap, and their specialization stated explicitly: "Your focus for this task is regulatory landscape only." Distinct names ensure separate memory files and avoid conflicts between parallel instances.

## Fallback

Use the Agent tool directly (without team_name) for simple isolated tasks where team overhead isn't worth it.
