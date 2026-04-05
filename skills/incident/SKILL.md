---
name: incident
description: 'Create a new incident note in ~/.max/brain. Use when asked to log an incident, open an incident note, capture an outage, record a production issue, or file incident context with ticket, severity, role, and related links.'
---

# Incident

Create a new incident note in `work/incidents/`.

## Required Frontmatter

Include:

- `date`
- `description`
- `tags`
  - `incident`
- `ticket`
- `severity`
- `role`

## Required Sections

```markdown
## Context
## Root Cause
## Timeline
## Impact
## Related
```

Set `Root Cause` to `TBD` when it is not yet known.

## Workflow

1. Gather the incident description from the user prompt.
2. If `ticket`, `severity`, or `role` are missing, ask the user before writing the note.
3. Create the note in `work/incidents/` with a descriptive filename based on the ticket or incident title.
4. Add links to relevant people in `org/people/` and related active projects in `work/active/` when they exist.
5. Preserve brain conventions for frontmatter and wikilinks.

## Writing Guidance

- Keep the initial note factual and concise.
- Do not invent a root cause.
- Prefer explicit timelines over prose paragraphs when enough facts are available.
- Ensure the new note links to at least one existing related note.

## Output

After writing the note, report the file path and any required follow-up metadata still missing.
