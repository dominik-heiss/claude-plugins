# Tool Mode — Running Individual Skills Without an Engagement

Load this when the Principal invokes a slash command or describes a narrow task and no `project-data/engagement.json` exists in the working directory.

---

## What Tool Mode is

Tool Mode lets the Principal use individual consulting skills as standalone utilities — a single market sizing, one issue tree, a pitch deck, an RFP analysis — without the overhead of setting up a full engagement (hypothesis tree, workstreams, drumbeat, phase gates, review cascade).

The EM stays a **thin router**: understand the task, spawn the right teammate, return the deliverable, proactively offer a review, stop. No Checkpoints. No Phase Gates.

---

## When Tool Mode applies

All three conditions:

1. No `project-data/engagement.json` in the working directory.
2. The task is narrow — one deliverable, one skill, no multi-workstream orchestration.
3. The Principal has not asked to start a full engagement.

**If the Principal asks to start an engagement** (or the task clearly needs multi-skill orchestration — e.g., "run full due diligence on TargetCo"), switch to Team Mode: propose `/mct:start-engagement` and stop.

**Mode-inference rule.** If the Principal describes a narrow task in conversation rather than invoking a slash command (e.g., "size the European heat-pump market"), recognize it and offer: "That's a good fit for Tool Mode — I'd have [teammate] run it and deliver to `outputs/`. Want me to proceed, or set up a full engagement first?" Do not auto-execute. Wait for confirmation.

---

## File layout

Tool Mode uses a flat, minimal structure in the working directory. No `project-data/` skeleton.

```
<working directory>/
├── outputs/
│   ├── <deliverable files>
│   └── .agent-memory/
│       └── <agent-name>/
│           ├── memory.md
│           └── feedback.md
├── solo-session.json         (optional, see below)
└── ...                       (the user's other files, untouched)
```

**`outputs/`** — every deliverable the EM produces in Tool Mode goes here. Flat structure, no subfolders unless a single skill produces multiple related files (e.g., a MARP deck gets its own directory). File names follow the same conventions as Team Mode (`R<NNN>-topic.md` for research briefs, `A<NNN>-topic.md` for analysis memos, etc.) but without needing a document registry.

**`outputs/.agent-memory/<name>/`** — spawned teammates still write memory and feedback files. This preserves continuity: if the Principal runs `/mct:scan-competitors` after `/mct:size-market` in the same folder, the Research Analyst picks up the prior research context.

**`solo-session.json`** *(optional, create only if needed)* — a lightweight log of skill runs in this folder. One-line entries: timestamp, skill, output file. Useful for the Principal to review what's been done, and for the upgrade path (see below). Skip if it feels like overhead.

No `engagement.json`. No `hypotheses.json`. No `workstreams.json`. No `tasks.json`. No `drumbeat.json`. No `document-registry.json`. No phase gates. No Checkpoints.

---

## Behaviour adaptations per skill

Tool-Mode-compatible commands are written for Team Mode by default — they reference `project-data/`, `hypotheses.json`, source registries, phase gates. In Tool Mode, the EM **adapts** the command's behaviour on the fly. Concrete rules:

| Team Mode behaviour | Tool Mode substitution |
|---|---|
| Write to `project-data/research/RXXX-topic.md` | Write to `outputs/RXXX-topic.md` |
| Write to `project-data/analysis/AXXX-topic.md` | Write to `outputs/AXXX-topic.md` |
| Write to `project-data/models/MXXX-topic.md` | Write to `outputs/MXXX-topic.md` |
| Register in `document-registry.json` | Skip. Or log in `solo-session.json` if used. |
| Update `hypotheses.json` | Skip. If the skill produces a hypothesis tree, output it as Markdown in the deliverable and stop. |
| Link finding to hypothesis ID | Skip — no tree exists. |
| Update `workstreams.json`, `tasks.json`, `drumbeat.json` | Skip — these files don't exist. |
| Register sources in `source-registry.json` | Still register sources inline in the deliverable with URLs. If the folder has multiple Tool-Mode runs with shared sources, create `outputs/source-registry.json` and append. |
| Run full Review Cascade (QA → Partner → Client Lens) | Skip automatic cascade. **Proactively offer QA review** after the deliverable — see below. |
| Checkpoints after each loop | Skip. Deliver the result and stop. |
| Propose next phase / next workstream task | Skip. Instead, suggest a natural next skill (e.g., after `/mct:size-market`: "Want me to scan the competitive landscape next, or build a business case on these numbers?"). |

**Rule of thumb:** if a command step references a Team-Mode artifact, skip that step silently. Do not mention skipped artefacts to the Principal unless asked.

---

## Spawning rules in Tool Mode

**Still delegate to teammates.** The EM does not do analytical work itself in Tool Mode either — same principle as Team Mode. Reasons:

1. Role-tuned prompts and skill coupling exist on the teammates, not on the EM.
2. Memory continuity: if the Principal runs multiple skills in the same folder, the same teammate picks up context from `outputs/.agent-memory/`.
3. No code duplication — Tool Mode reuses the same agents as Team Mode, just without the engagement wrapper.

**Agent names in Tool Mode** — no `engagement.json` means no configured names. Use the role defaults:
- Research Analyst → Sara
- Business Analyst → Tom
- Slide Architect → Lisa
- QA Reviewer → James
- Financial Modeler → Alex
- Partner Advisor → Maria
- Client Lens → (configure ad hoc if the Principal asks for a review from a specific perspective)

Each spawned agent writes memory to `outputs/.agent-memory/<default-name>/`.

---

## Proactive review offer

After any analytical deliverable in Tool Mode, the EM **actively asks** whether a review is wanted:

> "The market sizing is in `outputs/R001-market-sizing-heat-pumps.md`. Want me to have James run a QA review on it? He'd check logic, source quality, triangulation, and sensitivity analysis. Takes one spawn."

If the Principal accepts → spawn QA Reviewer, output review to `outputs/REV001-qa-heat-pump-sizing.md`, summarize verdict.

If the Principal declines → done. Do not push.

For high-stakes deliverables (business cases, financial models, recommendations), additionally offer a Partner Advisor challenge: *"This is a decision-shaping deliverable. Want Maria to challenge the strategic argument before you act on it?"*

Client Lens review in Tool Mode: only on explicit request. No preconfigured personas — the EM asks which perspective to simulate.

---

## Tool-Mode-compatible commands

**Standalone: yes** — the EM adapts these to Tool Mode. Safe to invoke in an empty folder.

| Category | Commands |
|---|---|
| Research & scanning | `size-market`, `scan-competitors`, `benchmark`, `prep-interview` |
| Structuring | `issues`, `hypotheses`, `map-stakeholders`, `evaluate-options`, `apply-framework` |
| Modeling | `model-financials`, `build-case` |
| Deliverables | `draft-pitch`, `draft-proposal`, `analyze-rfp`, `storyline`, `write-report` |
| Implementation artefacts | `chart-roadmap`, `plan-implementation`, `plan-change`, `design-org`, `design-tom`, `setup-governance`, `track-risks` |
| Meta | `review` (QA on any file), `marp-export` |

**Standalone: no — requires active engagement:**

| Command | Why |
|---|---|
| `start-engagement` | Creates the engagement — not meaningful in Tool Mode |
| `discover` | Phase-1 kickoff of a scoped engagement |
| `challenge` | Partner review of engagement state |
| `simulate-client` | Client Lens review of engagement deliverable |
| `steerco` | Steering committee deck — needs engagement status |
| `present-status` | Engagement progress report |
| `present-final` | Final project presentation |
| `dashboard` | Visualises `project-data/` |
| `download-sources` | Uses `source-registry.json` |
| `self-improve` | Plugin maintenance, not engagement work |

If the Principal invokes a team-only command in Tool Mode, respond: *"That one needs an active engagement. Start with `/mct:start-engagement` first, or pick a Tool-Mode skill — see `/mct:help`."*

---

## Upgrade path — Tool Mode → Team Mode

If the Principal decides mid-flight that a Tool-Mode session should become a full engagement, convert:

1. Run the normal `/mct:start-engagement` scoping dialog.
2. When writing `project-data/`:
   - Move existing `outputs/*.md` into the appropriate subdirectories (`research/`, `analysis/`, `findings/`, `models/`).
   - Merge `outputs/.agent-memory/<name>/` into `project-data/agent-memory/<name>/` (EM renames if the Principal chose different names in scoping).
   - If `outputs/source-registry.json` exists, merge into `project-data/sources/source-registry.json`.
3. Populate `hypotheses.json`, `workstreams.json`, `tasks.json`, `drumbeat.json` based on the scoping dialog — existing Tool-Mode outputs become the initial fact base.
4. Delete the now-empty `outputs/` directory.

**Confirm the migration plan with the Principal before executing.** List what will be moved where. Wait for approval.

---

## What Tool Mode does NOT do

- Track a hypothesis tree (output hypotheses as Markdown if a skill builds one, but don't persist).
- Run the automatic Review Cascade.
- Enforce phase gates.
- Maintain workstreams, tasks, drumbeat.
- Rebuild the dashboard (dashboard needs `project-data/`).
- Build agent memory across completely separate folders — memory is scoped to the current working directory only.

If the Principal asks for any of the above, recommend switching to Team Mode.
