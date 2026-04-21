# Project Tracking Discipline — tasks, workstreams, drumbeat, hypotheses

Load this when completing a task, preparing a checkpoint, or closing a phase gate.

**The EM is responsible for keeping all tracking files current. This is not optional — stale tracking files mean the Principal and the team lose situational awareness.**

## After every completed task or loop

The EM must update these files before presenting results to the Principal:

1. **`tasks.json`** — set status to `done`, add `completed` date, update `notes` with summary.
2. **`workstreams.json`** — update workstream `status` (not-started → in-progress → complete), update deliverable statuses, update `last_updated` date.
3. **`drumbeat.json`** — update checklist item statuses (`done`/`skipped`); when all items satisfied, mark the gate `complete` with date.
4. **`hypotheses.json`** — update hypothesis status, evidence arrays, confidence levels, and `last_updated` after any finding that changes the evidence base.
5. **`document-registry.json`** — register every new document with id, type, title, path, author, version, status, created timestamp.

## Trigger points

- Agent completes a task → update `tasks.json` + `workstreams.json` immediately.
- Review completed → update `tasks.json` (review task) + `drumbeat.json` (if gate checklist item).
- Finding changes a hypothesis → update `hypotheses.json` immediately.
- Phase gate passed → update `drumbeat.json` gate status + all workstream statuses.

## Verification at checkpoints

Before presenting any checkpoint or phase gate to the Principal, the EM reads back all tracking files and fixes any inconsistencies. If a workstream shows "in-progress" but all its tasks are "done", fix it before the briefing.

## Dashboard rebuild

Rebuild the dashboard (`bash ${CLAUDE_PLUGIN_ROOT}/assets/dashboard/build-dashboard.sh project-data`) at every phase gate and whenever the Principal requests a status update. The dashboard reads from the tracking files — if they are stale, the dashboard is wrong.

## Task structure

The EM maintains `project-data/tasks.json` — the authoritative list of all tasks in the engagement.

```json
{
  "tasks": [
    {
      "id": "T001",
      "workstream": "WS1",
      "description": "Market sizing — European heat pump market",
      "assigned_to": "[agent name from engagement.json]",
      "role": "research-analyst",
      "status": "in-progress",
      "loops": 2,
      "compute": "High",
      "output_file": "project-data/research/R001-market-sizing-V01.md",
      "created": "2026-04-05",
      "completed": null
    }
  ]
}
```

Status values: `pending` → `in-progress` → `review` → `done`.

## EM responsibilities for tasks

- Create a task entry before spawning an agent.
- Update status after each loop (in-progress → review → done).
- Pass the task ID and output file path explicitly in every agent brief.

## Agent sub-tasks

Agents may break their task into sub-tasks internally. These are tracked in the agent's `memory.md` under "Active Task", not in `tasks.json`. The EM pulls a summary at the end of each loop.
