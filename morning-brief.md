---
name: morning-briefing
description: >
  Use when the user says "morning brief", "start my day",
  "daily briefing", "what's on today", "catch me up", or at
  the start of any new work session where no specific task is
  given. Also triggers on "what should I focus on today",
  "give me my priorities", "morning report", "daily standup",
  "what's happening this week", or "brief me". Pulls from
  Trello board (via Claude in Chrome), recent Google Docs in
  EOS client folder, Google Calendar, and conversation
  history to generate a structured daily brief. Do NOT use
  for specific task requests like "prep email for [client]"
  or "build a dossier" — those have their own skills. This
  skill is the daily command center overview.
---

# Morning Briefing

This skill generates Duke Revard's structured daily briefing by pulling from four data sources, synthesizing them into a prioritized action plan, and optionally saving the output as a Google Doc.

## Why This Matters

Duke operates as a solo practitioner across EOS, Harvester, AirChAiR, and Eden. Without a team or EA, the morning briefing is how he creates his own accountability structure — a daily L10 with himself. The briefing surfaces what's active, what's at risk, and what deserves today's energy so the Fact Finder 9 in him has the information he needs to commit and execute.

## Data Sources

The skill pulls from four sources in this order:

### Source 1: Trello Board — "EOS Next Actions"
- **URL:** https://trello.com/b/MktR462s/eos-next-actions
- **Method:** Claude in Chrome (navigate, read page content via `get_page_text` or `read_page`)
- **What to capture:** Card titles from all active lists (everything except "Done")

The board has 13 lists. For the morning briefing, organize cards into priority tiers:

**Tier 1 — Active Execution (surface first):**
- Doing
- 90 Day World (Q1 Rocks)

**Tier 2 — Queued Work (surface key items):**
- To Do List
- Waiting on Others

**Tier 3 — Domain Pipelines (summarize counts + any due items):**
- Education Priority
- Clarity Break
- Content
- One Year Plan
- Ask for a Referral
- Proactive Calls
- AiR ChAiR
- Skills to Build

**Skip entirely:**
- Done

### Source 2: Google Drive — Recent EOS Client Docs
- **Folder ID:** `1AeH8dsGe3fedCfSjCwROpIzDNspTDCQr`
- **Method:** `google_drive_search` with `modifiedTime` filter for last 14 days
- **Query:** Search within the EOS client folder for documents modified in the last 14 days
- **What to capture:** Document titles, last modified dates, and links — these signal which clients have active work

Use this search approach:
```
api_query: '1AeH8dsGe3fedCfSjCwROpIzDNspTDCQr' in parents and modifiedTime > '[14 days ago in RFC3339]'
order_by: modifiedTime desc
```

If results are sparse, broaden to the parent folder or search without folder restriction using `fullText contains 'EOS'` and the date filter.

### Source 3: Google Calendar — Today + Next 3 Days
- **Method:** `gcal_list_events` for today's events (full detail) and next 3 days (condensed)
- **Timezone:** America/Chicago
- **What to capture:** Event summaries, times, locations, attendee counts, and any EOS session indicators (Quarterly, Annual, Focus Day, VB1, VB2, 90-Minute Meeting)

For today's events, use `condenseEventDetails: false` to get full attendee lists and descriptions — this matters for session prep.

For the next 3 days, use `condenseEventDetails: true` to keep the response concise.

### Source 4: Conversation History — Pending Items
- **Method:** `recent_chats` (last 5 conversations) + `conversation_search` for "pending", "follow up", "to do", "next step"
- **What to capture:** Any unfinished tasks, commitments Duke made, or items flagged for follow-up

This is the lowest-fidelity source — treat it as supplementary. Surface items only if they're clearly actionable and not already represented in Trello or Calendar.

## Steps

1. Open the Trello board in Claude in Chrome and extract card titles from all active lists
2. Search Google Drive for recently modified docs in the EOS client folder (last 14 days)
3. Pull today's calendar events (full detail) and next 3 days (condensed)
4. Search recent conversation history for pending items
5. Identify the **top 3 priorities** for today based on urgency, deadlines, calendar events, and active Rocks
6. Flag any **conflicts or collisions** in the schedule
7. Surface **items at risk** of falling through the cracks (Waiting on Others items older than 7 days, Rocks approaching quarter-end, upcoming sessions without prep)
8. Generate the briefing in the format below

## Trello Scanning Instructions

The Trello board requires Claude in Chrome to read. Here's the exact workflow:

1. Use `tabs_context_mcp` to get available tabs (create a tab group if needed)
2. Navigate to `https://trello.com/b/MktR462s/eos-next-actions`
3. Wait 3 seconds for the board to load
4. If a cookie consent dialog appears, click "Only necessary" to dismiss it
5. Use `get_page_text` to extract all text content from the page — this is faster and more reliable than `read_page` for getting card titles
6. Parse the text to identify list headers and their cards
7. If `get_page_text` output is too large or unclear, fall back to `read_page` with `depth: 5` and focus on the board content area

**Important:** The board may have many cards in "Done" — skip that list entirely. If the page text is very long, focus on extracting from Tier 1 and Tier 2 lists first.

**If Chrome is unavailable:** Say so honestly — "I couldn't access your Trello board today" — and generate the briefing from the other three sources. Never fabricate Trello data.

## Output Format

Generate the briefing directly in the conversation using this structure:

```
## Your Day — [Day of Week], [Month] [Day], [Year]

### Top 3 Priorities
1. [Priority] — why it matters today
2. [Priority] — why it matters today
3. [Priority] — why it matters today

### Calendar Overview
[Time blocks with prep notes for key meetings. For EOS sessions, note the client name, session type, and any prep needed. For calls, note who and context.]

### Active Execution (Trello: Doing + Rocks)
[Cards currently in "Doing" and "90 Day World" lists — these are what Duke has committed to executing]

### Queued & Waiting
[Key items from "To Do List" that are ready to move to Doing, plus "Waiting on Others" items with any noted staleness]

### Pipeline Snapshot
[One-line summary per domain list: "Content: 12 cards | Ask for a Referral: 5 cards | Proactive Calls: 10 cards" etc. — just card counts unless something has a due date or label worth calling out]

### Recently Active Docs
[Google Docs modified in last 14 days — doc title, last modified date, and link. Group by client if possible.]

### Watch List
[Items at risk: pending decisions, approaching deadlines, Rocks nearing quarter-end, sessions in next 7 days without prep, Waiting on Others items that are stale]

### Quick Wins
[Small tasks you can knock out between meetings — pulled from To Do List items that appear low-effort]
```

### Formatting Rules
- Use the output format above as a guide, not a rigid template. If a section has nothing to report, omit it rather than writing "None"
- Top 3 Priorities should synthesize across all sources — don't just list the first 3 Trello cards
- Calendar Overview should include today's events with times and any relevant context, not just titles
- Keep the tone direct and actionable — this is Duke's daily operational brief, not a report for someone else
- If an EOS session (Quarterly, Annual, Focus Day, 90-Minute Meeting) is today or within the next 3 days, flag it prominently and note any prep actions needed
- Prioritize signal over noise — Duke doesn't need to see every single card, just the ones that matter today

## Saving as Google Doc (Optional)

After presenting the briefing in the conversation, offer: "Want me to save this as a Google Doc in your Drive?"

If Duke says yes:
1. Create a well-formatted Google Doc using the `google_drive_search` / doc creation workflow
2. Title it: "Morning Briefing — [Date]"
3. Save it to Duke's Drive (no specific folder required — he can organize later)
4. Provide the link

Alternatively, Duke may ask for a markdown file or a doc created via the computer tools. Follow his preference.

## Gotcha Section

- **Don't fabricate calendar events** — if you can't access the calendar, say so and focus on Trello and Drive
- **Don't fabricate Trello data** — if Chrome can't load the board (auth issues, network), say so clearly
- **Don't repeat yesterday's briefing with minor edits** — each briefing should reflect genuinely current data from all sources
- **Priorities should reflect CURRENT context**, not cached assumptions from previous conversations
- **If any data source fails**, note which one and continue with what you have — a partial briefing is better than no briefing
- **Quarter boundaries matter** — if it's near the end of a quarter (roughly last 2-3 weeks of March, June, September, December), flag any Rocks that appear incomplete
- **Session prep lead time** — if an EOS session is within 7 days and Duke hasn't run the quarterly-prep-email skill for that client, flag it as a Watch List item
- **The "Doing" list is gospel** — these are Duke's current commitments. They always appear prominently.
- **Trello board name may update** — the list structure (Doing, To Do, etc.) is more stable than the board name. If the board URL works, use it regardless of title changes.
