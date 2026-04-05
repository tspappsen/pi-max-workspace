---
name: standup
description: Generate a daily standup update from ~/.max/brain. Use when the user asks for a standup, daily update, yesterday/today/blockers summary, or explicitly references the /standup skill.
---

Generate today's standup from brain context.

## Sources

Collect evidence from these sources before drafting the response:

1. Recent entries in `/home/pi/.max/brain/Memories.md`
2. Open tasks and in-flight notes in `work/active/`
3. The last 7 commits from `git --no-pager log --oneline -7`

## Output format

Return only:

```markdown
**Yesterday:** <completed items from git log and closed tasks>
**Today:** <open tasks from work/active/>
**Blockers:** <anything marked blocked or at-risk>
```

## Guidance

- Synthesize, do not dump raw notes or commit messages.
- Prefer concrete work items over vague summaries.
- If a section has no evidence, say `None`.
- Treat `blocked`, `at-risk`, and equivalent wording in active notes as blockers.
- Keep the result concise and ready to paste into a standup update.
