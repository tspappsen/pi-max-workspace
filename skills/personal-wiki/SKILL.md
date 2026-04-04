# Personal Wiki

Maintain a persistent, LLM-authored knowledge wiki in ~/study/. Use when ingesting articles/gists/URLs, querying accumulated knowledge, or linting the wiki for gaps and contradictions.

The wiki lives at `/home/pi/study/`. It is a compounding knowledge base — **not** a RAG system. Knowledge is synthesized once and kept current, not re-derived on every query. Inspired by Karpathy's LLM wiki pattern.

## Structure

```
/home/pi/study/
├── README.md          ← index (you maintain this)
├── log.md             ← append-only chronological log (you maintain this)
├── {org}/{repo}/      ← GitHub repo analyses (from github-repository-analysis skill)
│   └── README.md
└── articles/          ← standalone article/gist/URL analyses
    └── {slug}/
        └── README.md
```

**README.md** is the content index. Every page in the wiki has an entry here — link, one-line summary, TL;DR. Organized by category. Update it on every ingest.

**log.md** is append-only. Every operation gets an entry: `## [YYYY-MM-DD] {operation} | {title}`. If log.md doesn't exist yet, create it.

## Operations

### INGEST — Adding a new source

When the user shares a URL (article, gist, blog post, paper):

1. Fetch and read the full content
2. Determine slug: kebab-case title (e.g. `karpathy-llm-wiki-pattern`)
3. Create `~/study/articles/{slug}/README.md` with this structure:

```markdown
# {Title}

**Source:** {URL}
**Author:** {author if known}
**Date ingested:** {YYYY-MM-DD}

## What It Is
[One paragraph — what problem/idea this addresses]

## Core Ideas
[Bullet list of key insights, ranked by importance]

## Patterns Worth Using
[Concrete techniques applicable to our own work]

## Connections
[Links to other wiki pages this relates to — use relative markdown links]

## Raw Notes
[Anything worth preserving verbatim — quotes, key quotes, code snippets]
```

4. Update `README.md` index — add entry under the appropriate section (create section if needed)
5. Scan existing wiki pages for related content — update their `## Connections` sections if relevant
6. Append to `log.md`: `## [{date}] ingest | {title}`
7. Git commit and push: `Add {title}\n\nCo-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>`

### QUERY — Answering questions from the wiki

1. Read `README.md` index to find relevant pages
2. Read those pages
3. Synthesize an answer with citations (relative links)
4. If the answer is non-trivial and reusable, offer to file it back as a new wiki page

### LINT — Health-checking the wiki

Scan for:
- Pages in the index that don't exist on disk
- Pages on disk not in the index
- Empty or missing `## Connections` sections where obvious links exist
- Contradictions between pages on the same topic
- Concepts mentioned repeatedly but lacking their own dedicated page

Report as a prioritized list. Offer to fix each one.

## Conventions

- All files are markdown
- Internal links use relative paths: `[title](../org/repo/README.md)`
- GitHub repo analyses live under `{org}/{repo}/` — don't duplicate, just cross-reference from articles
- Articles/gists/blog posts live under `articles/{slug}/`
- README.md sections should reflect actual content taxonomy — reorganize as the wiki grows
- When a section gets more than ~8 entries, consider splitting

## Index entry format (match existing style in README.md)

```markdown
- [{title}]({relative-path}) — {one-line description}
  - **TL;DR:** {2-3 sentence synthesis of the most important insight}
```

## Trigger conditions

- User shares a URL that is NOT a GitHub repo → INGEST as article
- User asks "what do we know about X" → QUERY
- User says "clean up the wiki", "lint", or "health check" → LINT
- After any ingest: always update index + log + cross-references + commit
