---
name: sop-history-ingest
description: 'Ingest diary-style history files from SopHistory into copilot-mind. Use when asked to incorporate SopHistory notes, import diary files, convert historical markdown into vault notes, preserve raw history while extracting decisions/incidents/project updates, or backfill the vault from old working notes.'
---

# SOP History Ingest

Import diary-style files from `SopHistory/` into the vault without treating the source files as canonical vault notes.

## Purpose

`SopHistory/` is a raw history archive. The files there may contain valuable project updates, decisions, incidents, architecture notes, and links worth preserving in the vault, but the original diary files should remain untouched unless the user explicitly asks to rewrite them.

## Workflow

1. Read the target file or files from `SopHistory/`.
2. Extract the durable information:
   - project/work updates
   - decisions
   - incidents
   - architecture or reference material
   - noteworthy links to people, teams, systems, or existing notes
3. Decide how to incorporate the content into the vault:
   - `work/active/` or `work/archive/YYYY/` for project notes and status updates
   - `work/incidents/` for incidents
   - `work/decisions/` if it exists, otherwise `work/active/` for decision records
   - `reference/` for durable technical knowledge
   - `brain/Key-Decisions.md` and `brain/Patterns.md` when the diary entry reveals cross-session knowledge worth remembering
4. Preserve or add required frontmatter on any note you create or update:
   - `date`
   - `description`
   - `tags`
   - `status` for work notes
5. Add `[[wikilinks]]` to at least one existing related note for every note you create. Note: `[[wikilinks]]` are not clickable on GitHub—use `[Page Name](Page%20Name.md)` for hyperlinks.
6. Keep the source `SopHistory/` file unchanged unless the user explicitly asks to transform or move it.

## Ingestion Rules

- Treat `SopHistory/` as a source archive, not as the final destination.
- Prefer extracting and merging into existing vault notes over duplicating the full diary entry.
- If a diary file contains multiple independent concepts, split them into atomic notes instead of forcing everything into one file.
- Preserve factual nuance; do not flatten a decision, incident, and project update into a single vague summary.
- If the diary content is mainly transient and not durable, summarize it into the most relevant work note instead of creating unnecessary new notes.

## Decision Heuristics

- Create or update a **decision note** when the file contains a chosen approach, accepted tradeoff, or rationale that should be reusable later.
- Create or update an **incident note** when the file describes a breakage, outage, failure, recovery, or root-cause investigation.
- Create or update a **work note** when the file is primarily implementation context, progress, findings, or next steps for an active or archived project.
- Create or update a **reference note** when the strongest value is reusable technical understanding rather than project status.
- Update `brain/Key-Decisions.md` or `brain/Patterns.md` only for durable cross-session knowledge, not one-off status.

## When to Ask the User

Ask before writing if:

- the destination note is ambiguous
- the entry should be split into several notes or kept as one
- the content looks sensitive and needs confirmation before being summarized
- the user has not said whether to ingest one file or the entire folder

## Output

When you finish, report:

1. which `SopHistory/` file or files were processed
2. which vault notes were created or updated
3. what durable knowledge was extracted
