---
name: cos-coding
description: Chief of Staff orchestration loop for all coding work. Apply whenever handling a code change, feature, fix, refactor, or any dev task.
---

# CoS Coding Orchestration

All coding work follows the **DECIDE → ACT → VERIFY → ADAPT** loop. Always close the loop.

## Tier Classification

State the tier in one sentence with the reason before doing anything.

- **Trivial** — one-file or near one-file change, low risk, obvious verification
- **Routine** — known pattern, same subsystem, modest blast radius
- **Risky** — architecture, concurrency, migrations, external integrations, broad refactors, hard rollback

If in doubt, treat as Routine.

## DECIDE — Clarify only when blocking

Ask questions only when ambiguity is **blocking** or likely to cause rework. Max 3 concise questions. If the request is clear enough to act safely, don't ask — state working assumptions as a short bullet list instead.

## ACT — Planning depth by tier

- **Trivial** — inline plan in chat, execute directly in a worker. No plan.md required.
- **Routine** — generate `specs/<slug>/plan.md` in the target repo, then hand off to a coder worker.
- **Risky** — generate `specs/<slug>/plan.md` with explicit goal, tier, files to edit, read-only context, implementation steps, verification steps, risks/assumptions. Then hand off to a coder worker.

**Plan checkpoint:** After producing a plan for any non-trivial tier, present it and get explicit agreement before implementation begins. Skip only if the user already said "proceed" in the same conversation.

### Execution brief format (plan.md)

For Routine and Risky work, `specs/<slug>/plan.md` must include:
- **Goal**
- **Tier**
- **Files to edit**
- **Read-only context files**
- **Implementation steps**
- **Verification**
- **Risks / assumptions**

Only add `tasks.md` when there are multiple phases, parallel coders, or file ownership needs to be explicit.

## Delegation rules

When handing off to a coder worker:
- Forward relevant plan details verbatim
- Explicitly list editable files
- Explicitly list read-only context files when important
- State what to verify before returning
- Keep scope narrow — sequence tasks that touch the same file

## VERIFY — QA proportional to risk

- **Trivial** — targeted verification inside the coder worker; escalate only if result is uncertain
- **Routine** — verify build and relevant tests pass
- **Risky** — verify broader build/test scope; review docs/config if public behavior changed

## ADAPT — When verification fails

1. Route the concrete failure back to the coder worker for one focused repair cycle
2. If the same class of failure persists, stop and explain: what failed, what was tried, what decision is needed next
3. Do not loop into a crater

## Issue & Board Hygiene

When a coding task is tied to a GitHub issue (Max project or any tracked repo):
1. Close the issue on completion: `gh issue close <N> --repo <owner>/<repo>`
2. Confirm the issue's status on the project board reflects **Done**: check https://github.com/users/tspappsen/projects/7
3. Do this as the final step of every completed task — not optional.

## Documentation

After significant code changes, ask: **"Would you like me to check if documentation needs updating?"** — but only when the change affects setup, public behavior, commands, config, or architecture. Skip for tiny edits.

## Memory

Capture only useful learnings from a coding run:
- hidden dependencies
- compound tasks discovered mid-execution
- failure patterns likely to recur

If no reusable lesson emerged, write nothing.

## Autonomy

Never ask trivial questions. Make the call, inform after. Approval gates apply only for: destructive changes, migrations/data rewrites, large multi-subsystem refactors, ambiguous product behavior, or >5 files / 2+ subsystems.
