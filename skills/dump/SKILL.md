---
name: dump
description: 'File a brain dump into ~/.max/brain. Use when asked to capture notes, classify a brain dump, save freeform text, file a project update, record a win, log an incident, or turn rough thoughts into a properly linked brain note.'
---

# Dump

Convert freeform user text into a properly filed brain note.

## When to Use This Skill

Use this skill when the user wants to save rough text, a brain dump, a project update, a win, a decision, or an incident into ~/.max/brain.

## Workflow

1. Read the input text and classify it using the patterns in `hooks/classify-message.py`.
2. Route the note to the appropriate folder using the repo conventions:
   - `DECISION` -> `work/decisions/` when available, otherwise `work/active/`
   - `INCIDENT` -> `work/incidents/`
   - `WIN` -> `work/active/` or `work/archive/YYYY/` depending on whether the work is still active
   - `ARCHITECTURE` -> `reference/`
   - `PERSON` or `1ON1` -> `org/people/` or `thinking/`, depending on whether the note is durable
   - `PROJECT_UPDATE` -> `work/active/`
   - If nothing matches cleanly, choose the best brain location from the operating manual and explain the choice briefly.
3. Create or update the target note with YAML frontmatter. At minimum include:
   - `date`
   - `description`
   - `tags`
   - `status` for work notes
4. Use the existing note template conventions from `templates/note.md` when they apply.
5. Add `[[wikilinks]]` to at least one existing related note. A note without links is a bug.
6. Preserve existing frontmatter if editing an existing note.

## Writing Guidance

- Synthesize the input into clear notes rather than copying raw text unless the user asked to preserve wording.
- Generate a descriptive filename from the note title.
- Prefer atomic notes when the content contains multiple unrelated ideas.
- Keep tags in frontmatter, not inline.
- If the right destination is ambiguous, ask the user before writing.

## Output

After filing the note, report the file path and the classification used.
