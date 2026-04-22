# Management Consulting Team — Claude Code Plugin

Turn Claude into a full strategy consulting team. Seven specialist agents — research, analysis, financial modeling, slide creation, QA, partner review — work together on your problem using the same hypothesis-driven methodology that top-tier firms use on real engagements.

This is not a prompt template or a chatbot wrapper. It is a structured orchestration system where agents communicate directly, review each other's work, maintain memory across sessions, and produce traceable, sourced deliverables through a multi-phase engagement process.

## Getting Started — Three Entry Paths

When you open Claude Code in an empty folder with this plugin installed, the Engagement Manager (Marcus) greets you and offers three ways to proceed:

**① Team Mode — full consulting project.**
Structured end-to-end: scoping → hypothesis tree → workstreams → discovery → analysis → synthesis. Marcus orchestrates the team, runs review cascades, rebuilds the dashboard at every phase gate. Right for decision-shaping, multi-workstream problems.
→ `/mct:start-engagement Should we acquire TargetCo at 8x EBITDA?`

**② Tool Mode — one skill for a specific task.**
Pick a single consulting tool: market sizing, issue tree, business case, RFP analysis, pitch deck, framework application. No engagement setup, deliverable lands in `outputs/`. Marcus actively offers a QA review after the result.
→ `/mct:size-market industrial heat pumps >100kW in Europe`
→ `/mct:issues why did our EBIT margin drop 4 points in FY25`
→ `/mct:apply-framework porter European battery cells`

**③ Tour — 5-minute walkthrough.**
Marcus explains the team, both modes, the dashboard, output formats, and how Claude Code handles permissions. No commitment.
→ `/mct:tour`

**Still unsure?** Describe the situation in plain language — Marcus recognises whether your task fits Team or Tool Mode and proposes accordingly before running anything.

**See all commands:** `/mct:help` lists the full catalog with a `[Solo]` tag on every command that works in Tool Mode without engagement setup.

## Why This Exists

Most AI tools give you one generalist that does everything. This plugin gives you a **team of specialists** who collaborate:

- **Hypothesis-driven, not prompt-driven.** Every engagement starts with a testable hypothesis tree. Research confirms or contradicts specific hypotheses — it never just "explores a topic."
- **Built-in quality control.** A three-stage review cascade (QA Reviewer → Partner Advisor → Client Lens) catches logical gaps, unsupported claims, and weak storylines before you see the output.
- **Persistent memory.** Agents write memory files at the end of every session. When you return tomorrow, the team picks up where it left off — context intact, no re-explanation needed.
- **Full engagement lifecycle.** 30+ slash commands cover everything from RFP analysis and scoping through discovery, analysis, synthesis, and implementation planning.
- **Every claim is sourced.** All sources are registered with URLs, cited inline as `(SRC001)` at the point of each claim, and downloadable for verification.
- **Structured output.** Research briefs, analysis memos, findings, financial models, and slide decks — all in a consistent file structure with version tracking.
- **Interactive dashboard.** A self-contained HTML dashboard gives you a visual overview of the entire project — hypotheses, workstreams, findings, team status, and phase gate progress — at any time.

## The Team

| Role | Default Name | What They Do |
|------|-------------|-------------|
| Research Analyst | Sara | Market sizing, competitive intelligence, regulatory research |
| Business Analyst | Tom | Issue trees, hypothesis structuring, MECE analysis |
| Slide Architect | Lisa | Storylines, PowerPoint decks, executive summaries |
| QA Reviewer | James | Logic, source quality, MECE completeness, devil's advocate |
| Financial Modeler | Alex | Business cases, DCF, unit economics, scenario analysis |
| Partner Advisor | Maria | Strategic sharpness, IC/board readiness, senior challenge |
| Client Lens | — | Simulated client perspective (CEO/CFO/CTO/COO) |

You interact with the **Engagement Manager** (EM), who orchestrates the team. Agents communicate directly with each other via Agent Teams — Sara can share a finding with Tom immediately without routing through the EM.

Agent names and backgrounds are configured per engagement during `/mct:start-engagement`. The system proposes backgrounds tuned to your engagement type (M&A → financial due diligence backgrounds, Market Entry → sector expertise, Cost Reduction → operations/Lean backgrounds). You can adjust before the project starts.

## Dashboard

The plugin generates a self-contained HTML dashboard from your project data. It shows:

- **Engagement overview** — project name, core question, current phase, autonomy level
- **Hypothesis tree** — visual status with color coding (confirmed/testing/rejected)
- **Workstream progress** — status per workstream with deliverables
- **Team overview** — each agent's role, background, and current assignment
- **Key findings** — timeline of discoveries with source links
- **Phase gate checklists** — what's done vs. outstanding before the next gate
- **Source registry** — all sources used with reliability ratings

Generate it anytime:
```
/mct:dashboard
```

The dashboard is written to `project-data/dashboard.html`. Open it in any browser — no server needed, everything is embedded in a single HTML file. If automatic opening doesn't work on your system, just open the file manually:
```bash
# The file is always at:
open project-data/dashboard.html        # macOS
xdg-open project-data/dashboard.html    # Linux
start project-data/dashboard.html       # Windows
```

The dashboard is rebuilt from scratch each time — it's a snapshot, not a live view. The EM also rebuilds it automatically at every phase gate.

## Requirements

- **Claude Code** (latest version)
- **Agent Teams enabled** — add to `~/.claude/settings.json`:
  ```json
  { "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }
  ```
- **Python 3.6+** for HTML dashboard generation and financial modeling
- **Internet access** for research tasks (WebSearch / WebFetch)

### Recommended local tools

The plugin works without these, but installing them upfront avoids delays and manual approval prompts when agents need them mid-task.

**Python packages (Excel handling for the Financial Modeler):**

```bash
pip install openpyxl formulas
```

- `openpyxl` — Excel file generation and read/write (`.xlsx`). Required for any financial model output.
- `formulas` — pure-Python Excel formula parser and evaluator. Lets the Financial Modeler build workbooks with **computed formulas**, not just static values — so you can open the file and poke at assumptions in Excel directly.

Agents can install these on demand if `Bash(pip3 install:*)` is in your permissions (see "Recommended Setup" below) — but pre-installing is faster and avoids approval prompts during a task.

**MARP presentations (client-ready decks via the `/mct:marp-export` command):**

```bash
sudo apt install -y nodejs npm chromium-browser     # Ubuntu / WSL
# macOS: brew install node; Chrome installed via the DMG
```

- `nodejs` 18+ — required to run `npx @marp-team/marp-cli`. No global npm install needed.
- `chromium-browser` (or `google-chrome-stable`) — required for PDF and PPTX export from MARP. HTML export works without it.
- **Marp for VS Code** extension — install via VS Code Extensions pane. Gives live slide preview while editing `.md` decks. Optional but strongly recommended for iterating on slide content.

The plugin's `consulting.css` theme (Navy + sparse red accent, Inter/Helvetica, 16:9) ships at `assets/marp-themes/consulting.css` and is applied automatically by `/mct:marp-export`. See `skills/marp-presentation/` for the full pattern catalog and export workflow.

**Other useful CLI tools:**

- `tmux` — split the terminal to watch multiple agents work in parallel. See "Monitoring agent work with tmux" below.
- `jq` — inspect and pretty-print JSON tracking files (`tasks.json`, `hypotheses.json`, `workstreams.json`, etc.) from the command line.
- `xdg-open` (Linux) / `wslview` (WSL) / `open` (macOS) — open the generated HTML dashboard from the terminal. Referenced by the dashboard build script.

## Installation

Install via the marketplace (recommended):

```
/plugin marketplace add dominik-heiss/claude-plugins
/plugin install mct@dh-claude-plugins
```

Or clone and use locally (useful if you want to customize or improve the plugin):
```bash
git clone https://github.com/dominik-heiss/claude-plugins.git
claude --plugin-dir /path/to/claude-plugins/plugins/management-consulting-team
```

## Recommended Setup

For a smooth experience, configure these permissions in `~/.claude/settings.json` so agents can work without constant approval prompts:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  },
  "permissions": {
    "allow": [
      "Bash(git *)",
      "Bash(ls:*)",
      "Bash(cat:*)",
      "Bash(head:*)",
      "Bash(tail:*)",
      "Bash(wc:*)",
      "Bash(chmod:*)",
      "Bash(mkdir:*)",
      "Bash(cp:*)",
      "Bash(mv:*)",
      "Bash(bash:*)",
      "Bash(python3:*)",
      "Bash(pip3 install:*)",
      "Bash(xdg-open:*)",
      "Bash(wslview:*)",
      "WebSearch",
      "WebFetch"
    ]
  }
}
```

**What this allows:**
- Git operations (committing project snapshots)
- File system operations (reading, copying, organizing project data)
- Script execution (dashboard generation, data processing)
- Web research (market data, competitor analysis, source fetching)

**What still requires confirmation (by design):**
- `rm` — file deletion always asks first
- `sudo` — system-level operations always ask first
- `git push --force` — destructive git operations always ask first

**Tip:** If you prefer to approve things incrementally, skip the permissions block above. Claude will ask on first use of each tool — choose "Always allow" to build up your permission list over time.

## Resuming Work

When you return after a break, resume or continue the last session:

```bash
claude --resume                    # Select from recent sessions interactively
claude --continue                  # Continue the most recent session directly
claude --resume SESSION_ID         # Resume a specific session by ID
```

**Tip:** `--continue` is the fastest way to pick up where you left off — it skips the selection menu and jumps straight into your last session. Use `--resume` when you need to choose between multiple sessions.

The EM will reload all project context automatically (`engagement.json`, hypothesis tree, workstreams, recent findings) and brief you on current status.

## Claude Code Basics (useful for this plugin)

A few Claude Code features that make the plugin more usable — not a full tutorial, just the highlights.

### Naming your sessions

Sessions show up in `claude --resume` by session ID, which is hard to recognize. Use `/rename [name]` inside a session to give it a meaningful label:

```
/rename phase1-heat-pump-analysis
```

Names survive across session exits and show up in the resume list. Good names make it obvious which session belongs to which engagement.

### Monitoring agent work with tmux

When the EM spawns 3+ parallel subagents (e.g. during `/mct:discover`), it can be hard to see what each one is doing. Claude Code can be launched inside a tmux session so you can split the window and watch logs:

```bash
tmux new -s consulting
# Inside tmux:
claude --plugin-dir /path/to/management-consulting-team
```

Use `Ctrl-b %` to split vertically, `Ctrl-b "` to split horizontally, `Ctrl-b d` to detach, `tmux a -t consulting` to reattach. Not required, but handy for long-running engagements where you want a second pane for git status, log tailing, or running the dashboard build manually.

### Checking the plugin is loaded

If `/mct:start-engagement` or other `/mct:*` commands don't appear in the slash menu, the plugin is not active. The `start-engagement` command writes a `CLAUDE.md` marker into your project directory — if you open a session in an existing engagement directory and see a warning about plugin activation, restart with `claude --plugin-dir /path/to/management-consulting-team`.

### Permission modes

By default Claude asks before every tool use. For smoother flow, the permissions block in `~/.claude/settings.json` (see "Recommended Setup" above) pre-approves the common operations. You can also toggle modes with:

- `/permissions` — review/edit current permissions
- `--dangerously-skip-permissions` — approve everything (only for trusted workflows)

### Slash commands and argument hints

All plugin commands show inline hints when you type `/mct:`. Example: `/mct:build-case [topic]` expects a one-line description. You can also inspect any command's behavior with `/help`.

### Session transcripts

All session transcripts are stored under `~/.claude/projects/` keyed by working directory. If you ever need to recover a conversation, the `.jsonl` files there are the authoritative log.

## Quick Start

Open an empty folder in Claude Code with the plugin loaded. Marcus greets you with the three-path opener. Pick one:

### Path A — Team Mode (full engagement)

```
/mct:start-engagement Should a PE fund acquire a European heat pump manufacturer?
```

Marcus runs the scoping dialog — context, constraints, stakeholders, your initial hypothesis. At the end you see: governing question, 2–3 top-level hypotheses with sub-hypotheses (MECE), 3–4 proposed workstreams, a team composition tuned to the engagement type, and a loop-based drumbeat. You confirm, then Phase 1 discovery begins.

What you run next in Team Mode:

```
/mct:discover                                           # fan out research across workstreams
/mct:size-market European heat pump market              # triangulated market sizing
/mct:scan-competitors Top 5 heat pump OEMs in DACH      # competitive landscape
/mct:build-case Acquisition of TargetCo at 8x EBITDA    # NPV, IRR, scenarios
/mct:present-status                                     # where we stand
/mct:dashboard                                          # rebuild the HTML dashboard
/mct:review <file>                                      # manual review of any deliverable
/mct:storyline                                          # pyramid-structured argument
/mct:present-final                                      # final client deck
```

Review cascade (QA → Partner → Client Lens) runs automatically before milestones; you can trigger it manually on any deliverable via `/mct:review`, `/mct:challenge`, `/mct:simulate-client`.

### Path B — Tool Mode (single skill, no engagement)

Drop a slash command in any folder. No scoping, no `engagement.json`. Marcus spawns the right teammate, the deliverable lands in `outputs/`, and Marcus offers a QA review before finishing.

```
/mct:size-market industrial heat pumps >100kW in Europe
/mct:issues why did EBIT margin drop 4 points in FY25
/mct:apply-framework porter European battery cells
/mct:evaluate-options market entry options for SEA pharma pipeline
/mct:build-case acquisition TargetCo at 450M
/mct:draft-pitch strategy & operations offering for mid-cap industrials
/mct:analyze-rfp path/to/rfp.pdf
/mct:review path/to/my-draft.md
```

Every command tagged **[Solo]** in `/mct:help` works in Tool Mode. If a command needs an active engagement (e.g. `/mct:discover`, `/mct:steerco`), Marcus tells you and suggests either starting one or picking a Solo command instead.

### Path C — Tour

```
/mct:tour
```

5-minute walkthrough. No commitments, no files created.

### Switching modes later

Starting in Tool Mode and want the full engagement structure later? Just say so — Marcus converts existing `outputs/` into the Team-Mode project structure and runs scoping on top of your prior work.

## Commands

The `Mode` column shows which commands work standalone in an empty folder (**[Solo]** → Tool Mode, no engagement needed) and which need an active engagement (**[Team]**). For the interactive catalog, run `/mct:help` in Claude Code. For a guided introduction, run `/mct:tour`.

### Engagement Setup
| Command | What It Does | Mode |
|---------|-------------|------|
| `/mct:start-engagement [description]` | Run scoping dialog, create project files, assemble team | [Team — creates state] |
| `/mct:map-stakeholders` | Stakeholder map with influence/interest matrix | **[Solo]** |
| `/mct:setup-governance` | RACI, steerco structure, reporting cadence | **[Solo]** |

### Research & Discovery
| Command | What It Does | Mode |
|---------|-------------|------|
| `/mct:discover` | Run discovery phase: interviews, data requirements, quick wins | [Team] |
| `/mct:size-market` | Market sizing (top-down + bottom-up, triangulated) | **[Solo]** |
| `/mct:scan-competitors` | Map competitive landscape | **[Solo]** |
| `/mct:prep-interview` | Prepare expert interview guide | **[Solo]** |
| `/mct:download-sources` | Batch-download cited sources to local storage | [Team] |

### Structuring & Analysis
| Command | What It Does | Mode |
|---------|-------------|------|
| `/mct:hypotheses` | Build or update the hypothesis tree | **[Solo]** |
| `/mct:issues` | Build or update the issue tree (MECE decomposition) | **[Solo]** |
| `/mct:apply-framework` | Apply strategic framework (Porter, 7S, SWOT, etc.) | **[Solo]** |
| `/mct:benchmark` | Peer benchmarking on KPIs and best practices | **[Solo]** |
| `/mct:evaluate-options` | Generate, evaluate, and prioritize strategic options | **[Solo]** |

### Financial & Quantitative
| Command | What It Does | Mode |
|---------|-------------|------|
| `/mct:build-case` | Build business case or investment thesis | **[Solo]** |
| `/mct:model-financials` | P&L projection, DCF, cash flow analysis | **[Solo]** |

### Synthesis & Deliverables
| Command | What It Does | Mode |
|---------|-------------|------|
| `/mct:storyline` | Develop pyramid-structured storyline | **[Solo]** |
| `/mct:steerco` | Generate steering committee presentation (add `--marp` for client-ready PDF via MARP) | [Team] |
| `/mct:present-final` | Create final presentation with full evidence chain (add `--marp` for client-ready PDF via MARP) | [Team] |
| `/mct:marp-export [path]` | Export a MARP deck to PDF / HTML / PPTX using the consulting theme | **[Solo]** |
| `/mct:write-report` | Create strategic report (executive summary + analyses) | **[Solo]** |
| `/mct:chart-roadmap` | Create implementation roadmap | **[Solo]** |

### Quality & Review
| Command | What It Does | Mode |
|---------|-------------|------|
| `/mct:review [file]` | QA review of any deliverable (6-dimension check) | **[Solo]** |
| `/mct:challenge` | Strategic partner review (sharpness, IC readiness) | [Team] |
| `/mct:simulate-client` | Simulated client reaction from configured C-level perspective | [Team] |

### Implementation
| Command | What It Does | Mode |
|---------|-------------|------|
| `/mct:plan-implementation` | Detailed implementation plan | **[Solo]** |
| `/mct:plan-change` | Change management plan | **[Solo]** |
| `/mct:design-org` | Organizational design | **[Solo]** |
| `/mct:design-tom` | Target operating model design | **[Solo]** |

### Project Management
| Command | What It Does | Mode |
|---------|-------------|------|
| `/mct:present-status` | Project status: hypotheses, workstreams, next steps | [Team] |
| `/mct:dashboard` | Generate HTML dashboard from project data | [Team] |
| `/mct:track-risks` | Risk register with likelihood/impact scoring | **[Solo]** |
| `/mct:self-improve` | Analyze feedback files, propose plugin improvements | [Meta] |
| `/mct:tour` | 5-minute guided walkthrough of the plugin | Any |
| `/mct:help` | Command catalog with mode tags | Any |

### Business Development
| Command | What It Does | Mode |
|---------|-------------|------|
| `/mct:analyze-rfp` | Analyze RFP with go/no-go recommendation | **[Solo]** |
| `/mct:draft-proposal` | Create consulting proposal | **[Solo]** |
| `/mct:draft-pitch` | Build client pitch deck | **[Solo]** |

## How It Works

### Phases

```
Phase 0: Scoping      → engagement.json, hypotheses.json, workstreams.json, drumbeat.json
Phase 1: Discovery    → research briefs, interview guides, data compendium
Phase 2: Analysis     → analysis memos, business cases, updated hypothesis tree
Phase 3: Synthesis    → storyline, slide deck, executive summary
```

Each phase gate requires deliverable completion, QA review, and Partner sign-off before proceeding.

### Engagement Rhythm

Work is organized in three nested structures — not calendar weeks:
- **Loop**: Delegate task → output → hypothesis update → next task. Most tasks take 2 loops.
- **Checkpoint**: EM presents findings, you provide steering input. Frequency depends on autonomy level.
- **Phase Gate**: End of phase — full deliverable set + QA + Partner review → your go/no-go

### Review Cascade

Before any deliverable reaches you:
1. QA Reviewer → logic, MECE, sources, numbers
2. Partner Advisor → strategic sharpness, IC/board readiness
3. Client Lens (if configured) → feasibility, political implications
4. Revision → address critical/major findings
5. Partner sign-off

### Orchestration

The EM chooses between two orchestration modes per task block:

- **Individual subagents** (default for simple tasks): Each agent reports directly to the EM. Lower overhead, full EM control.
- **Agent Teams** (for parallel work with 3+ agents): Agents communicate directly with each other. Higher throughput, less EM bottleneck.

The EM announces the chosen approach before each task block.

### Persistent Memory

Each agent writes `memory.md` and `feedback.md` at the end of every session. The EM reloads their context automatically on the next session — teammates don't start from zero. Memory is stored in `project-data/agent-memory/[agent-name]/`.

### Source Discipline

Every source used by any agent is registered in `source-registry.json` with a mandatory URL. Sources are cited inline in documents as `(SRC001)` at the point of the claim — not just listed at the bottom. Download cited sources on demand:
```
/mct:download-sources          # Download high/medium reliability, cited sources
/mct:download-sources all      # Download everything
```

## Autonomy Levels

Set in `engagement.json` under `autonomy_level`:

| Level | Behavior |
|-------|----------|
| `standard` | Work through tasks, checkpoint after each loop, reviews at phase gates (default) |
| `diligence` | Everything in standard, plus reviews after every loop — for M&A, regulatory, high-stakes |
| `autonomous` | Work through phases independently, pause only at critical findings and phase gates |

## Project Structure

### Team Mode

```
project-data/
├── engagement.json          # Project metadata, team, phase
├── hypotheses.json          # Hypothesis tree (continuously updated)
├── workstreams.json         # Workstream assignments and status
├── tasks.json               # Task tracking (status, assignments, output files)
├── drumbeat.json            # Phase gates and checkpoint log
├── document-registry.json   # Master index of all created documents
├── dashboard.html           # Generated dashboard (open in browser)
├── research/                # Research briefs (RXXX-topic-V01.md)
├── analysis/                # Analysis memos (AXXX-topic-V01.md)
├── findings/                # Individual findings (FXXX-topic.md)
├── reviews/                 # QA and Partner reviews (REVXXX-...)
├── models/                  # Financial models (MXXX-topic.xlsx + summary.md)
├── deliverables/            # Final deliverables (decks, reports)
│   └── presentations/       # MARP decks (PXXX-topic/ with source .md, assets/, exports/)
├── sources/                 # Source registry + downloaded sources
│   ├── source-registry.json
│   ├── web/                 # Downloaded HTML sources
│   └── documents/           # Downloaded PDFs
├── client-data/
│   └── inbox/               # Drop client files here for processing
└── agent-memory/
    ├── marcus/              # Engagement Manager memory
    ├── sara/                # Research Analyst memory (per configured name)
    ├── tom/                 # Business Analyst memory
    └── ...
```

### Tool Mode

```
outputs/
├── RXXX-market-sizing-heat-pumps.md        # One deliverable per Solo command
├── AXXX-porter-battery-cells.md
├── MXXX-business-case-targetco.md
├── REVXXX-qa-heat-pump-sizing.md           # QA reviews (when accepted)
├── source-registry.json                    # Created on demand if multiple runs share sources
└── .agent-memory/
    ├── sara/                               # Teammates keep memory across Tool-Mode runs
    ├── tom/
    └── ...
```

Flat structure, no phase gates, no hypothesis tree, no dashboard. If you decide mid-session that a Tool-Mode folder should become a full engagement, just say so — Marcus migrates the existing `outputs/` into the Team-Mode project structure.

## Design Decisions

Key architectural choices and why they were made:

| Decision | Rationale |
|----------|-----------|
| **Agents are ephemeral** | Agents lose context between sessions. Memory files in `agent-memory/` provide persistence — more robust than agent resumability (survives crashes, is readable, versionable). |
| **One spawn = one task** | Each agent handles one task brief, then writes memory and is dismissed. Reusing agents for new tasks grows context indefinitely and causes compaction issues. |
| **Memory by name, not role** | Agent memory is stored under the configured name (e.g., `sara/`, not `research-analyst/`). This prevents conflicts when multiple agents of the same role run in parallel. |
| **Principles-first, not templates** | Agent prompts define how agents think, not what they produce. Skills provide domain knowledge. Commands give assignments. This avoids rigid, repetitive output. |
| **Loops + compute, not calendar time** | Planning uses loops (iterations) and compute level (Low/Medium/High/Very High) instead of weeks or days. Agent execution doesn't map to calendar time. |
| **Review cascade is mandatory** | Every deliverable passes QA → Partner → revision before reaching you. Reviews can only be skipped with explicit confirmation. |
| **Inline source citation** | Sources are cited as `(SRC001)` at the point of each claim, not just in a footer. This makes every fact traceable. |
| **Findings are atomic** | Each finding is a separate file with a single claim, evidence, confidence level, and hypothesis linkage. Findings don't have versions — when corrected, a new finding supersedes the old one. |
| **Client Lens is one agent** | One agent adopts different C-level perspectives (CEO/CFO/CTO) rather than separate agents per role. Deeper review per perspective, more token-efficient. |
| **EM decides orchestration mode** | The EM evaluates each task block and chooses individual subagents vs. Agent Teams based on dependencies, parallelism, and efficiency — not a fixed rule. |

## Known Limitations

- **Agents cannot spawn sub-agents.** Flat hierarchy — the EM handles all delegation.
- **Excel/PowerPoint quality.** Programmatic generation has formatting limits. External Slide AI integration is planned.
- **Token costs.** 7 agents (2 on Opus for reviews) mean significant API costs under intensive use.
- **Context window.** For very large projects, agent context may compress. Incremental saves and memory files mitigate this.
- **Simulated clients are not real clients.** The Client Lens is a support tool, never a substitute for real feedback.

## Status

**v1.0** — Full agent team with 7 agents, 30+ commands, 11 skills:
- End-to-end engagement: Scoping → Discovery → Analysis → Synthesis
- Agent Teams orchestration with direct peer communication
- Review cascade: QA → Partner → Client Lens → Revision
- Financial modeling with scenario analysis
- Project persistence across sessions
- Source registry with inline citations
- HTML dashboard for project overview
- BD commands (RFP analysis, proposals, pitch decks)
- Implementation support (org design, change management, TOM)
