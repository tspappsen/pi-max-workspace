# Brain

Max's persistent knowledge base lives at `/home/pi/.max/brain/`. Read it when context about goals, decisions, or patterns is relevant.

## Files

- `/home/pi/.max/brain/North-Star.md` — Erik's current focus, goals, aspirations, and anti-goals. Read this at the start of meaningful work sessions.
- `/home/pi/.max/brain/Memories.md` — Index of persistent context topics. Links to Key-Decisions and Patterns.
- `/home/pi/.max/brain/Key-Decisions.md` — Architectural and workflow decisions worth recalling. Update when a durable decision is made.
- `/home/pi/.max/brain/Patterns.md` — Recurring patterns and conventions. Update when a pattern is discovered.

## When to read brain files

- Before any meaningful work session — check North-Star.md to stay aligned
- When making architectural or workflow decisions — check Key-Decisions.md first
- When a pattern emerges across sessions — write it to Patterns.md
- When something durable is learned about Erik, his projects, or his working style — record it

## Skills available

- `dump` — file a brain dump or freeform notes into the brain
- `decision` — create a decision record and update Key-Decisions.md
- `standup` — generate a daily standup from brain context
- `weekly` — weekly synthesis and North Star alignment check
- `vault-audit` — audit brain notes for hygiene (missing frontmatter, broken wikilinks)
- `incident` — create an incident note
- `sop-history-ingest` — ingest diary/history files from `/home/pi/.max/brain/SopHistory/`

## Conventions

- All brain notes use YAML frontmatter: `date`, `description`, `tags`
- Use `[[wikilinks]]` to cross-reference notes — a note without wikilinks is a bug
- Brain files are owned by Max and Erik together — either can write
