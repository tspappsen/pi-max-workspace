---
name: github-repository-analysis
description: Clone and analyze curated GitHub repositories focused on AI, agentic workflows, coding assistants, LLM tooling, and related infrastructure. Use when the user shares a GitHub repo URL and wants Max to clone it, deeply inspect it through an AI/agent lens, and produce a study-grade analysis.
---

# AI & Agentic Repository Analysis

Use this workflow when the user provides a GitHub repository URL and wants Max to clone it, inspect it, and produce an AI-focused technical analysis.

## Context

These repositories are **hand-picked** by the user. They are always in the domain of:

- **AI agents and agentic workflows** (autonomous task execution, multi-agent orchestration, tool use)
- **Coding assistants and developer tools** (Copilot-like systems, code generation, IDE integrations)
- **LLM infrastructure** (prompt engineering frameworks, RAG pipelines, embedding systems, vector stores)
- **MCP servers and tool ecosystems** (Model Context Protocol, function calling, plugin architectures)
- **AI-native applications** (chat UIs, knowledge bases, AI-powered CLIs)

Every analysis should be written through this lens. Don't just describe what the code does — explain **how it advances or implements agentic/AI patterns**, what design decisions are interesting for someone building AI systems, and what ideas are worth borrowing.

## Goal

Turn a repository URL into a fast, AI-focused engineering study:

1. Clone the repo into `~/opensource/<user>/<repo>`
2. Inspect the codebase with an AI/agentic lens
3. Identify the stack, architecture patterns, and AI-specific design decisions
4. Write a deep analysis to `~/study/<user>/<repo>/README.md`

## When to Use

Use this skill when the user:

- Pastes a GitHub repository URL
- Says things like "analyze this repo", "look through this repository", "intake this codebase", or "tell me how this project works"
- Wants a first-pass technical summary before coding starts

## High-Level Behavior

This is a coding/file-system task, so delegate it to a worker session.

- Create a worker session immediately
- Use a descriptive worker name based on the repo, like `github-repository-analysis-foo`
- Put the full workflow in the initial prompt
- Acknowledge briefly, then wait for the background result

## Clone Location

Use `~/opensource/<user>/<repo>` as the local path (e.g. `~/opensource/dmccreary/claude-skills`).

> **Note:** This path is outside the agent workspace. If sandbox restrictions are active, use a workspace-relative path like `./opensource/<user>/<repo>` instead.

Clone when you need to read actual code files. `web_fetch` may suffice for README-only work, but prefer cloning for any non-trivial analysis.

If the user gives a destination directory, use it.
If the repository already exists locally, inspect the existing clone instead of recloning unless the user asks for a fresh clone.

## Output Location

Save the final analysis markdown to `~/study/<user>/<repo>/README.md` (e.g. `~/study/dmccreary/claude-skills/README.md`).

Create the directory if it does not exist. This keeps cloned source code (`~/opensource/`) separate from your study notes (`~/study/`).

## Worker Prompt Template

Give the worker a prompt like this, adapted to the actual repo URL and destination:

- Clone the repository from the provided GitHub URL into the target directory if it is not already present.
- If the directory already exists and is a git repository for the same remote, reuse it.
- Inspect the repository without making code changes.
- Read the top-level docs and configuration first.
- Identify:
  - what the project does and **what AI/agentic problem it solves**
  - primary language(s) and framework(s)
  - package manager / build system
  - likely entry points
  - test/lint/build commands
  - important folders
  - notable risks, gaps, or unknowns
- Pay special attention to:
  - **Agent architecture** — how agents are defined, orchestrated, and composed
  - **Tool/function calling patterns** — how tools are registered, dispatched, and sandboxed
  - **LLM integration** — which models, how prompts are built, how context is managed
  - **Memory and state** — conversation history, vector stores, caching, persistence
  - **MCP or plugin systems** — extensibility patterns, protocol implementations
  - **Prompt engineering** — system messages, few-shot examples, structured output
  - **RAG pipelines** — retrieval, chunking, embedding, reranking strategies
  - **Safety and guardrails** — content filtering, sandboxing, auth boundaries
- Produce a concise but AI-focused analysis.
- Save the analysis as a markdown file to `~/study/<user>/<repo>/README.md`, creating the directory if needed.

## What the Worker Should Look For

Have the worker inspect these first, when present:

- `README*`
- `package.json`, `pnpm-lock.yaml`, `yarn.lock`, `package-lock.json`
- `pyproject.toml`, `requirements.txt`
- `Cargo.toml`, `go.mod`, `pom.xml`, `build.gradle*`
- `Dockerfile`, `docker-compose*`
- `.github/workflows/`
- top-level `src/`, `app/`, `cmd/`, `server/`, `api/`, `docs/`, `specs/`

Then the worker should search for:

- application entry points
- environment variable requirements (especially API keys for LLM providers)
- database or external service dependencies (vector stores, model APIs, embedding services)
- test commands
- deployment clues

Additionally, prioritize AI-specific files and patterns:

- `**/prompt*`, `**/system-message*`, `**/instructions*` — prompt templates
- `**/agent*`, `**/orchestrat*`, `**/router*`, `**/planner*` — agent architecture
- `**/tool*`, `**/function*`, `**/mcp*`, `**/plugin*` — tool/function calling
- `**/embed*`, `**/chunk*`, `**/vector*`, `**/rag*`, `**/retriev*` — RAG pipeline
- `**/memory*`, `**/context*`, `**/history*`, `**/session*` — state management
- `**/model*`, `**/llm*`, `**/openai*`, `**/anthropic*`, `**/provider*` — LLM integration

## Expected Output Format

**Always include the source GitHub URL at the top.**

Ask the worker to return a summary using this template:

```
# Repository: <user>/<repo>

**URL:** https://github.com/<user>/<repo>

## 1. What It Does
[One-paragraph overview — lead with the AI/agentic problem it solves]

## 2. AI/Agent Architecture
[How agents, tools, and LLMs are wired together. Orchestration patterns,
tool dispatch, prompt construction, context management. This is the most
important section — go deep.]

## 3. Key Design Decisions
[Interesting or unusual choices: model selection, streaming approach,
memory strategy, safety boundaries, MCP usage, plugin architecture, etc.
Explain *why* these matter for someone building AI systems.]

## 4. Project Structure
[Directory tree with descriptions, highlighting AI-relevant modules]

## 5. Tech Stack
[Bullet list — call out LLM SDKs, vector stores, embedding models,
framework choices. Use bullet list, not table, for Discord compatibility.]

## 6. Patterns Worth Borrowing
[Concrete techniques, abstractions, or approaches from this repo that
could be reused in our own agentic work. Be specific — reference files.]

## 7. Gaps, Risks, and Limitations
[What's missing, what's fragile, what would need to change at scale]

## 8. How to Run It
[Pre-requisites, env vars (especially API keys), install + start commands]
```

## Guardrails

- Do not modify the repository during intake unless the user explicitly asks for changes
- Do not install dependencies unless the user asks, or unless installation is necessary to answer the question and the user clearly expects that depth
- Prefer reading and summarizing over heavy execution
- If auth, secrets, or private submodules block inspection, explain exactly what is missing
- If the URL is not a GitHub repository URL, fall back to normal reasoning rather than forcing this skill

## Good Acknowledgment Examples

- "On it — I'll clone it and send back a quick intake."
- "Looking through that repo now — I'll report back with the stack and structure."

## Good Summary Style

Be concise, practical, and engineer-friendly. The user wants orientation, not a novel.

Always bias toward **AI/agentic insights**. Don't waste space on generic web-framework boilerplate — focus on the parts that make this repo interesting from an AI, agent orchestration, or developer tooling perspective. If the repo has a novel approach to tool calling, prompt management, context windows, or multi-agent coordination, that should dominate the analysis.
