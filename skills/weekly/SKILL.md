---
name: weekly
description: "Weekly synthesis — cross-session review of brain activity, North Star alignment, patterns, uncaptured wins, and forward priorities. Use when explicitly calling the /weekly skill."
---

Cross-session synthesis of the past week. Bridges daily standup (lightweight) and quarterly review brief (comprehensive). This is ANALYSIS, not verification — find patterns, surface drift, detect uncaptured work.

## Workflow

### 1. Gather Week's Activity
Automated via tools or manual gathering if instructed:
- Check git history: `git log --since="7 days ago" --oneline --no-merges`
- List notes modified in the past 7 days.
- Review notes related to people (`org/people/`) and drafts (`thinking/`) for 1:1 or meeting contexts.
- Check `work/active/` for status updates on active projects.
- Check `work/incidents/` for new or updated incidents.
- Review `/home/pi/.max/brain/Memories.md` and `/home/pi/.max/brain/Key-Decisions.md` for context changes.

### 2. North Star Alignment
Read `/home/pi/.max/brain/North-Star.md` and compare actual activity against stated focus:
- **Aligned work**: which Current Focus items got attention this week?
- **Drift**: work that doesn't map to any stated goal (not necessarily bad — flag it).
- **Silent goals**: focus items with zero commits, zero note updates, zero mentions.
- **Emerging themes**: work patterns suggesting a focus shift that hasn't been written down yet.

### 3. Cross-Day Patterns
Look across the week's notes for:
- Recurring themes (same topic in multiple notes or days).
- Multiple incidents or issues touching the same system/value stream in `reference/value-streams/`.
- Topics appearing in BOTH work notes and people notes (these are signals).
- Context that evolved across sessions (decisions that shifted, understanding that deepened).

### 4. Uncaptured Win Detection
Analyze the week's activity to find uncaptured wins:
- Check for projects that moved to `work/archive/` but weren't highlighted.
- Review `work/incidents/` for swift resolutions or major contributions.
- Assess `org/people/` interactions for uncaptured feedback or kudos.
- Note any new capabilities or decisions stored in `/home/pi/.max/brain/Patterns.md` or `/home/pi/.max/brain/Key-Decisions.md`.

### 5. Forward Look
- Blocked items or upcoming deadlines from `work/active/` notes.
- `North-Star` goals that need attention next week.
- Suggested priority ordering for next week based on goals + momentum + gaps.

### 6. Present Synthesis

Structure the output as:

- **This Week**: 3-5 bullet summary of what actually happened.
- **North Star Check**: alignment status — what's on track, what drifted, what's silent.
- **Patterns**: cross-day themes worth noting.
- **Uncaptured Wins**: anything that should be highlighted as a win or accomplishment.
- **Next Week**: suggested priorities and attention areas.

After presenting, offer:
- "Should I record any emerging patterns in `/home/pi/.max/brain/Patterns.md`?"
- "Should I update `/home/pi/.max/brain/North-Star.md` with any focus shifts?"
- "Want me to save this synthesis as `thinking/weekly-YYYY-MM-DD.md`?"

## Important

- This is transient analysis by default — do NOT create a file unless the user asks.
- Keep the tone analytical, not cheerful. This is a status check, not a celebration.
- Be honest about drift and silent goals — the value is in surfacing what's NOT happening, not just what is.
- Don't duplicate standup (daily, what's next) or wrap-up (session, verify quality). This is SYNTHESIS across days.
- If it was a light week (few commits, no new notes), say so. Don't pad the analysis.