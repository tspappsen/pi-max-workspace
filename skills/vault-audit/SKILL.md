---
name: vault-audit
description: 'Audit this Obsidian vault for hygiene issues. Use when asked to audit ~/.max/brain, check note quality, find missing frontmatter, detect orphaned notes, locate broken wikilinks, or identify stale active work.'
---

# Vault Audit

Inspect ~/.max/brain for structural and metadata hygiene issues.

## Audit Scope

Report these categories:

1. **Orphaned notes**: Markdown files with no outbound `[[wikilinks]]`
2. **Missing frontmatter**: Notes missing `date`, `description`, or `tags`
3. **Stale active work**: Files in `work/active/` not modified in 7 or more days
4. **Broken wikilinks**: `[[references]]` that do not match any existing note title

## Workflow

1. Search only within ~/.max/brain.
2. Exclude templates and session-log artifacts unless the user explicitly wants them audited.
3. Use note titles derived from filenames when validating wikilinks.
4. When reporting issues, group findings by category and include file paths.
5. If a category has no findings, say `None`.

## Reporting Guidance

- Be concise and actionable.
- Prefer exact file paths or note names over vague descriptions.
- Do not make changes unless the user asks for fixes after the audit.
