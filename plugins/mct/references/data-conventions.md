# Data Model Conventions — File Naming, Numbering, Sources, Registry

Load this when creating new documents, registering sources, or looking up past work.

All teammates must follow these conventions.

## engagement.json is config only

It holds project structure, team composition, stakeholders, and constraints — **never analytical data**. Station counts, financial figures, market sizes, projections — all of these belong in findings or analysis memos once agents process them. Reference data (taxonomies, segment definitions) is fine.

## File naming

- Research briefs: `project-data/research/RXXX-[topic]-V[NN].md`
- Analysis memos: `project-data/analysis/AXXX-[topic]-V[NN].md`
- Findings: `project-data/findings/FXXX-[topic].md` (no versioning — superseded findings are marked `superseded` with a pointer to their replacement)
- Reviews: `project-data/reviews/REVXXX-[reviewer]-[subject]-V[NN].md`
- Models: `project-data/models/MXXX-[topic].xlsx` + `MXXX-[topic]-summary.md`
- Deliverables: `project-data/deliverables/[type]-V[NN].[ext]`
- MARP presentations: `project-data/deliverables/presentations/PXXX-[topic]/PXXX-[topic]-V[NN].md` with sibling `assets/` (inline images) and `exports/` (generated PDF/HTML — regenerated, not versioned). Use P-prefix for presentation IDs. See the `marp-presentation` skill for theme, patterns and the `/mct:marp-export` workflow.

## Numbering discipline — no gaps, no jumps

IDs within each type increment by **+1, strictly sequential**. R001, R002, R003 … never skip to a new hundreds digit (no R099 → R200; no A012 → A100). Before creating a new document, the author scans `document-registry.json` for the highest existing ID of that type and uses the next integer. Same rule for F (findings), A (analysis memos), M (models), REV (reviews), P (MARP presentations) and SRC (sources in `source-registry.json`, which also tracks `next_id`). If the author is unsure of the highest existing ID, they ask the EM rather than guessing a higher number.

## Standard file header

Every document created by an agent must begin with:

```
# [Title]
**Date:** [YYYY-MM-DD HH:MM]  |  **Author:** [Agent Name] ([Role])  |  **Version:** V[NN]
**Research Question / Objective:** [What this document answers or achieves]
```

The date/time is when the document was first created. On revisions, add a revision line below.

## Versioning

Always two digits with leading zero: `V01`, `V02`, not `V1`, `V2`. When a document is revised after review, increment the version — do not overwrite the prior version.

## Finding lifecycle

Findings are atomic, citable claims. They do not have version numbers. When a finding is corrected or refined:

1. Create a new finding (next FXXX ID) with the updated claim.
2. Set the old finding's `status` to `superseded` and add a note: `"Superseded by FXXX"`.
3. Update any hypothesis references to point to the new finding.

Every agent that produces analytical output (Research Analyst, Business Analyst, Financial Modeler) must create findings for key insights. A finding is warranted when the insight directly confirms, refutes, or refines a hypothesis.

## Source discipline

- Every source → registered in `project-data/sources/source-registry.json`.
- Source ID format: `SRC001`, `SRC002`, etc.
- **Agents register sources themselves — not the EM.** The Research Analyst, Business Analyst, and Financial Modeler each write their new sources directly to `source-registry.json` at the end of their task. This is more efficient than routing through the EM. If two agents register sources in the same session, they coordinate on the next available ID (read the current `next_id` value before writing).
- **URL is mandatory — hard rule.** A source entry without a non-empty, valid URL MUST NOT be written to the registry. If you cannot find a URL, do NOT register the source — instead, note it as a gap in your output ("Claim X could not be sourced — needs follow-up"). Do not use placeholder URLs, "TBD", empty strings, or internal references. The `/mct:download-sources` pipeline, QA review, and dashboard all depend on every entry having a resolvable URL.
- For interviews and primary research (no public URL), use `type: "interview"` or `type: "primary-research"` and set `url` to an internal reference string starting with `internal://` (e.g. `internal://interview-expert-2026-04-17`). These are the only cases where a non-http URL is acceptable.
- Cite sources inline: every fact gets `(SRC001)` immediately after the claim. Footer lists alone are not sufficient.
- Each source carries a `"downloaded": false` flag. Set to `true` and populate `local_path` when a file is saved locally.
- **Download policy:** If an agent must fetch a PDF or page to extract data during research, save it immediately to `project-data/sources/web/` or `project-data/sources/documents/` and mark `downloaded: true`. Otherwise, defer downloading to `/mct:download-sources` — don't add extra fetching overhead during analysis.

## Document registry

The EM maintains `project-data/document-registry.json` — a master index of all documents created during the engagement. After every task completion, register the output document with: id, type, title, description, path, author, version, status, created timestamp, workstream, and hypotheses addressed. This enables efficient information retrieval as the project grows. Template: `${CLAUDE_PLUGIN_ROOT}/assets/templates/document-registry.json`.

### Description field — write it to be useful for lookup

- **3-4 sentences minimum** describing what the document actually says (not just the topic).
- Plus **3-4 bullet points** with the key findings, numbers, or conclusions.
- Target: a reader should know whether the document is relevant to their question without opening the file.
- Too short ("Analysis of European market") is useless. Too long (the full abstract) bloats context. Aim for ~6-10 lines.
- When the document is superseded or revised, update the description to reflect the new content.
- Agents write their own descriptions at task completion — the EM only fills in if an agent forgets.

## Lookup-first rule — how to find past work

When the Principal references a prior deliverable ("the analysis from last week", "our take on the synergy model"), the EM MUST:

1. Read `document-registry.json` first and scan descriptions.
2. Return the match based on the description alone if possible.
3. Only open the full document if the registry description is insufficient to answer the question.
4. If descriptions are too thin to be useful, flag this and propose enriching the entry on next update — do not resort to batch-reading all deliverables.
5. When deeper search is needed (cross-document synthesis, open-ended "have we looked at X" questions, finding something that's not a single document), spawn an `Explore` subagent via the `Agent` tool (`subagent_type="Explore"`) with a precise question and a scoped file list. Explore is read-only and token-efficient — it searches, summarizes, and returns a compact answer. **Never batch-read findings, analysis memos, or research briefs into the EM's main context** — that is exactly what caused context exhaustion in past sessions.

This rule also applies when spawning agents: pass relevant registry entries in the task brief, not full document contents, unless the document is directly the input to the task.

## Inbox monitoring

- On session start, scan `project-data/client-data/inbox/` for new files.
- If new files found, delegate to Research or Business Analyst for processing.
- Report what was ingested and its implications for active hypotheses.
