# Management Consulting Team — Claude Code Plugin

Turn Claude into a full strategy consulting team. Seven specialist agents — research, analysis, financial modeling, slide creation, QA, partner review — work together on your problem using the same hypothesis-driven methodology that top-tier firms use on real engagements.

This is not a prompt template or a chatbot wrapper. It is a structured orchestration system where agents communicate directly, review each other's work, maintain memory across sessions, and produce traceable, sourced deliverables through a multi-phase engagement process.

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

```bash
claude plugin install dominik-heiss/management-consulting-team
```

Or clone and use locally (useful if you want to customize or improve the plugin):
```bash
git clone https://github.com/dominik-heiss/management-consulting-team.git
claude --plugin-dir /path/to/management-consulting-team
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

```bash
claude --plugin-dir /path/to/management-consulting-team
```

### Scope the engagement

```
/mct:start-engagement Should a PE fund acquire a European heat pump manufacturer?
```

The EM runs a scoping dialog — asking about context, constraints, and success criteria — then proposes a hypothesis tree, workstream plan, and team composition tuned to your engagement type. You review and confirm before any work begins.

### Run discovery

```
/mct:discover
```

Research Analysts fan out across your workstreams in parallel — market sizing, competitive landscape, regulatory environment. Each finding is logged, sourced, and linked back to a hypothesis. The EM briefs you on material findings as they come in.

### Go deeper

```
/mct:size-market European heat pump market
/mct:scan-competitors Top 5 heat pump OEMs in DACH
/mct:build-case Acquisition of TargetCo at 8x EBITDA
```

Targeted commands for specific analytical tasks. Market sizing triangulates top-down and bottom-up. Competitor scans map the landscape with positioning analysis. Business cases include scenario modeling and sensitivity analysis.

### Check status

```
/mct:present-status
/mct:dashboard
```

See where each workstream stands, which hypotheses have been confirmed or contradicted, and what's next.

### Review before presenting

```
/mct:review project-data/deliverables/interim-report-V01.md
/mct:challenge
/mct:simulate-client
```

The review cascade runs automatically before milestones, but you can trigger it manually on any deliverable. QA checks logic and sources. Partner review tests strategic sharpness. Client Lens simulates how your audience will react.

### Build the final deliverable

```
/mct:storyline
/mct:present-final
```

The Slide Architect builds a pyramid-structured storyline, then creates the deck. Every slide has an action title, supporting evidence, and source citations. The full review cascade runs before you see the output.

## Commands

### Engagement Setup
| Command | What It Does |
|---------|-------------|
| `/mct:start-engagement [description]` | Run scoping dialog, create project files, assemble team |
| `/mct:map-stakeholders` | Stakeholder map with influence/interest matrix |
| `/mct:setup-governance` | RACI, steerco structure, reporting cadence |

### Research & Discovery
| Command | What It Does |
|---------|-------------|
| `/mct:discover` | Run discovery phase: interviews, data requirements, quick wins |
| `/mct:size-market` | Market sizing (top-down + bottom-up, triangulated) |
| `/mct:scan-competitors` | Map competitive landscape |
| `/mct:prep-interview` | Prepare expert interview guide |
| `/mct:download-sources` | Batch-download cited sources to local storage |

### Structuring & Analysis
| Command | What It Does |
|---------|-------------|
| `/mct:hypotheses` | Build or update the hypothesis tree |
| `/mct:issues` | Build or update the issue tree (MECE decomposition) |
| `/mct:apply-framework` | Apply strategic framework (Porter, 7S, SWOT, etc.) |
| `/mct:benchmark` | Peer benchmarking on KPIs and best practices |
| `/mct:evaluate-options` | Generate, evaluate, and prioritize strategic options |

### Financial & Quantitative
| Command | What It Does |
|---------|-------------|
| `/mct:build-case` | Build business case or investment thesis |
| `/mct:model-financials` | P&L projection, DCF, cash flow analysis |

### Synthesis & Deliverables
| Command | What It Does |
|---------|-------------|
| `/mct:storyline` | Develop pyramid-structured storyline |
| `/mct:steerco` | Generate steering committee presentation (add `--marp` for client-ready PDF via MARP) |
| `/mct:present-final` | Create final presentation with full evidence chain (add `--marp` for client-ready PDF via MARP) |
| `/mct:marp-export [path]` | Export a MARP deck to PDF / HTML / PPTX using the consulting theme |
| `/mct:write-report` | Create strategic report (executive summary + analyses) |
| `/mct:chart-roadmap` | Create implementation roadmap |

### Quality & Review
| Command | What It Does |
|---------|-------------|
| `/mct:review [file]` | QA review of any deliverable (6-dimension check) |
| `/mct:challenge` | Strategic partner review (sharpness, IC readiness) |
| `/mct:simulate-client` | Simulated client reaction from configured C-level perspective |

### Implementation
| Command | What It Does |
|---------|-------------|
| `/mct:plan-implementation` | Detailed implementation plan |
| `/mct:plan-change` | Change management plan |
| `/mct:design-org` | Organizational design |
| `/mct:design-tom` | Target operating model design |

### Project Management
| Command | What It Does |
|---------|-------------|
| `/mct:present-status` | Project status: hypotheses, workstreams, next steps |
| `/mct:dashboard` | Generate HTML dashboard from project data |
| `/mct:track-risks` | Risk register with likelihood/impact scoring |
| `/mct:self-improve` | Analyze feedback files, propose plugin improvements |

### Business Development
| Command | What It Does |
|---------|-------------|
| `/mct:analyze-rfp` | Analyze RFP with go/no-go recommendation |
| `/mct:draft-proposal` | Create consulting proposal |
| `/mct:draft-pitch` | Build client pitch deck |

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
