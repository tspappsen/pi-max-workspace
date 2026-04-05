---
name: decision
description: 'Create a decision record in ~/.max/brain. Use when asked to capture a decision, write an ADR-style note, document a chosen approach, or file an accepted decision and link it to related work.'
---

# Decision

Create a decision record in `work/decisions/` if that folder exists, otherwise use `work/active/`.

## Required Frontmatter

Include:

- `date`
- `description`
- `tags`
  - `decision`
- `status: accepted`

## Required Sections

```markdown
## Context
## Options Considered
## Decision Made
## Consequences
## Related
```

## Workflow

1. Use the user prompt to identify the decision being recorded.
2. Choose the target folder:
   - `work/decisions/` if it exists
   - otherwise `work/active/`
3. Create a descriptive note title and filename.
4. Link the decision to relevant work notes.
5. Update `/home/pi/.max/brain/Key-Decisions.md` with a short linked entry when the decision is durable enough to remember across sessions.
6. Preserve any existing frontmatter when editing an existing decision note.

## Writing Guidance

- Capture the rationale, not just the outcome.
- Keep options short but meaningful.
- Do not mark speculative or pending choices as accepted unless the user states the decision is made.
- Ensure the note has at least one existing related link.

## Output

After writing, report the note path and whether `/home/pi/.max/brain/Key-Decisions.md` was updated.
