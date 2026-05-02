---
name: delegate-and-elevate-audit
description: >
  Objective time-audit using the EOS Delegate and Elevate framework. Pulls data
  from Gmail, Google Calendar, and Google Drive to inventory where Duke's time
  went, categorizes every activity into the four D&E quadrants (Love/Great,
  Like/Good, Don't Like/Good, Don't Like/Not Good), assigns function labels,
  produces a pie chart, and outputs a structured audit report. Trigger on:
  delegate and elevate, D&E audit, time audit, where did my time go, delegate
  elevate, quarterly time review, monthly time audit, how am I spending my time,
  audit my calendar, audit my time, review my Q1, review my March, what should
  I delegate, what am I doing that I shouldn't be, run the D&E, or any request
  to objectively analyze how Duke is spending his time against EOS D&E quadrants.
  Also trigger on "pull my time data" or "analyze my activities." Do NOT trigger
  for general EOS glossary lookups or helping clients run their own D&E exercise.
---

# EOS Delegate & Elevate Time Audit

This skill performs an objective, data-driven audit of where Duke's time actually
went over a defined period, then categorizes every activity into the four EOS
Delegate & Elevate quadrants. The output is an honest mirror — the data tells
the story, and Duke decides what to do with it.

## The D&E Framework (Quick Reference)

The Delegate and Elevate tool is a 2x2 matrix measuring two dimensions:
- **Vertical axis — Enjoyment**: Love/Like it vs. Don't Like it
- **Horizontal axis — Competence**: Great/Good at it vs. Not Good at it

### The Four Quadrants

| Quadrant | Label | What It Means | Action |
|----------|-------|---------------|--------|
| Q1 | **Love It & Great At It** | Your Unique Ability zone. Energizing work where you produce exceptional results. | **Protect and expand** — aim for 80%+ of time here |
| Q2 | **Like It & Good At It** | Solid contributions but not your highest and best use. | **Keep for now, delegate over time** as the right person emerges |
| Q3 | **Don't Like It & Good At It** | The dangerous quadrant. You're competent (often self-taught through necessity) but the work drains you. | **Delegate first** — find someone who loves this work |
| Q4 | **Don't Like It & Not Good At It** | Energy black hole. You're neither enjoying it nor excelling. | **Eliminate or delegate immediately** |

The goal: every leader should spend ~80% of their time in Q1. Most start at ~20%.

## On Load — Ask the User

When this skill triggers, immediately ask:

> **Do you want the Quarter Audit or the Month Audit?**
>
> - **Quarter Audit** — Full Q1 2026 (Jan 1 – Mar 31). Broader patterns, strategic view.
> - **Month Audit** — March 2026 only. More granular, recent-memory accuracy.
>
> (You can also specify a custom date range.)

Wait for Duke's answer before pulling data. The date range determines all queries below.

## Function Categories

Every activity gets tagged with one of these precise function labels. These are
role-level categories (not individual tasks) — the right granularity for D&E.

### EOS Implementer Functions
- **Session Facilitation** — Running Quarterlies, Annuals, Focus Days, VB1/VB2, 90-Minute Meetings
- **Session Preparation** — Pre-session research, agenda planning, prep emails, running-log review
- **Session Follow-Up** — Post-session emails, debrief notes, homework tracking
- **EOS Tool Teaching** — Preparing and delivering toolbox deep-dives during sessions
- **Client Coaching** — Between-session calls, texts, emails advising LT members
- **Client Relationship Management** — Check-ins, relationship nurturing, retention conversations
- **Prospecting & Business Development** — 90-Minute Meetings, referral asks, outreach, dossier research
- **EOS Community & Learning** — Implementer community calls, continuing education, EOS conferences

### Business Operations Functions
- **Administrative & Scheduling** — Calendar management, booking logistics, travel planning
- **Financial Management** — Invoicing, expense tracking, bookkeeping, tax prep
- **Email Management** — Inbox processing, routine correspondence (not client coaching)
- **Technology & Tools** — Ninety.io setup, CRM updates, tool configuration, troubleshooting
- **Content Creation** — LinkedIn posts, articles, thought leadership writing
- **Marketing & Brand** — Website updates, social media strategy, personal brand

### Strategic & Personal Functions
- **Strategic Thinking & Clarity Breaks** — Dedicated reflection, journaling, planning
- **Skill Building & AI** — Claude Code skills, automation building, learning new tools
- **Board/Advisory Work** — AirChAiR, Eden Project, other ventures
- **Personal Development** — Reading, courses, health/fitness during work hours
- **Networking** — Non-prospecting relationship building, events, lunches

## Data Collection Workflow

Pull data from all four sources in parallel where possible. The date range comes
from the user's Quarter vs. Month choice.

### Source 1: Google Calendar (Primary Time Source)

Calendar is the most objective time record — it shows what Duke committed hours to.

**How to pull:**
- Use `gcal_list_events` with the chosen date range
- For Quarter audits, pull one month at a time (3 calls) to stay within API limits
- **timeMin / timeMax format:** RFC3339 *without* timezone suffix — e.g. `2026-01-01T00:00:00`
- **timeZone:** `America/Chicago` (separate parameter — do NOT append to timeMin/timeMax)
- Set `condenseEventDetails: false` to get full event details (titles, attendees, descriptions)
- Set `maxResults: 250` to capture busy months
- **Pagination:** If the response includes a `nextPageToken`, call again with `pageToken` set to that value. Repeat until no token is returned. This is critical for busy months.

**Example call (January 2026):**
```
gcal_list_events(
  calendarId: "primary",
  timeMin: "2026-01-01T00:00:00",
  timeMax: "2026-02-01T00:00:00",
  timeZone: "America/Chicago",
  condenseEventDetails: false,
  maxResults: 250
)
```

**What to extract per event:**
- Event title (maps to function category)
- Duration in hours (calculate from start/end times)
- Attendees (signals client vs. internal vs. solo)
- Location (in-person vs. virtual signals)
- Recurring vs. one-time

**Categorization logic:**
- Events with client names + "Quarterly/Annual/Focus Day/VB/90-Minute" → Session Facilitation
- Events with "prep" or day-before sessions → Session Preparation
- Events with "Clarity Break" → Strategic Thinking
- Events with "call" + client name → Client Coaching
- Events with prospect names or "90-Minute Meeting" → Prospecting
- Events with "Eden" / "AirChAiR" → Board/Advisory Work
- Events with "Bus Dev Prime Time" or "Help 1st" → Prospecting & Business Development
- Events with "L10" or "Scorecard" → Strategic Thinking & Clarity Breaks
- Events with "Admin" or "Administration" → Administrative & Scheduling
- Blocked "focus time" or "deep work" → categorize by what Duke was likely doing (ask if ambiguous)

**Important:** Separate personal events (church, social, family, moving, errands, routine)
from business events. Track personal time separately — it's useful context but doesn't
go into the D&E quadrant calculation.

### Source 2: Gmail (Activity & Effort Indicator)

Email volume and recipients reveal where communication effort goes — especially
the invisible between-session client work.

**How to pull:**
- Use `gmail_search_messages` with date range filters
- Search query: `after:YYYY/MM/DD before:YYYY/MM/DD from:me`
- Set `maxResults: 200` (max allowed: 500) for broad coverage
- **Pagination:** If the response includes a `nextPageToken`, call again with `pageToken` set to that value. Repeat until all sent emails are captured.
- Use `gmail_read_message` on a sample of threads to understand context

**Example call (Q1 2026):**
```
gmail_search_messages(
  q: "after:2026/01/01 before:2026/04/01 from:me",
  maxResults: 200
)
```

**What to extract:**
- Count of sent emails per recipient domain/person
- Thread topics (map to function categories)
- Time-of-day patterns (are emails bleeding into evenings?)
- Cluster recipients into: EOS clients, prospects, EOS community, vendors, personal

**Important:** Email doesn't directly equal hours, but volume and recipient patterns
reveal where Duke's *attention* goes. Use email data to supplement calendar, not replace it.

### Source 3: Google Drive (Deep Work & Document Indicator)

Documents reveal where Duke's deep-work and creative hours went. Search ALL of
Drive, not just the client folder — content drafts, AirChAiR strategy docs,
invoices, articles, and personal documents tell the complete story.

**How to pull:**
- Use `google_drive_search` with the `api_query` parameter
- **Important constraint:** When `api_query` contains `fullText`, you MUST set `order_by: "relevance desc"`. When filtering only by `modifiedTime` (no `fullText`), you CAN use `order_by: "modifiedTime desc"`.
- Set `page_size: 20` and `request_page_token: true` for pagination
- **Pagination:** If the response includes a `page_token`, call again with that token AND the identical `api_query`.

**Example calls:**

Modified documents in date range (no fullText — can sort by modifiedTime):
```
google_drive_search(
  api_query: "modifiedTime > '2026-01-01T00:00:00' and modifiedTime < '2026-04-01T00:00:00' and mimeType = 'application/vnd.google-apps.document'",
  order_by: "modifiedTime desc",
  page_size: 20,
  request_page_token: true
)
```

Documents in the EOS client folder (ID: `1AeH8dsGe3fedCfSjCwROpIzDNspTDCQr`):
```
google_drive_search(
  api_query: "'1AeH8dsGe3fedCfSjCwROpIzDNspTDCQr' in parents",
  order_by: "modifiedTime desc",
  page_size: 20,
  request_page_token: true
)
```

Full-text search (MUST use relevance ordering):
```
google_drive_search(
  api_query: "fullText contains 'quarterly session'",
  order_by: "relevance desc",
  page_size: 20,
  request_page_token: true
)
```

**What to extract:**
- Document titles and last-modified dates
- Document content snippets (from search results) to categorize function
- Group by type: invoices → Financial Management, session logs → Session Follow-Up,
  articles → Content Creation, strategy docs → Board/Advisory, dossiers → Prospecting, etc.

### Source 4: Trello Board (Task & Priority Indicator)

Duke's "EOS Next Actions" board shows what he's actively working on and queuing up.

**How to pull:**
- Use Claude in Chrome to navigate to `https://trello.com/b/MktR462s/eos-next-actions`
- Extract card titles from all lists (except "Done")
- Note which list each card is in (Doing, To Do, 90 Day World, etc.)

**If Chrome is unavailable:** Skip Trello and note the gap. The audit is still
valuable with Calendar + Gmail + Docs.

## Analysis & Categorization

After collecting all data, synthesize into a single activity inventory.

### Step 1: Build the Activity Inventory

Create a comprehensive list of every distinct activity with:
- **Function label** (from the categories above)
- **Estimated hours** (calendar = direct hours; email/docs = estimated based on volume)
- **Data source(s)** that evidenced this activity
- **D&E quadrant assignment**

Integrate across sources — a calendar event "[Client] AC Help" plus a Drive doc
"[Client] - AC Help 1st" plus email threads to that client's domain all combine
into one Client Coaching entry with aggregated hours.

### Step 2: Assign D&E Quadrants

Use these validated baseline assignments (confirmed by Duke, April 2026):

**Q1 — Love & Great At It:**
- Session Facilitation
- Client Coaching
- Strategic Thinking & Clarity Breaks
- EOS Tool Teaching
- Content Creation

**Q2 — Like & Good At It:**
- Board/Advisory Work
- Prospecting & Business Development
- EOS Community & Learning
- Networking
- Skill Building & AI
- Client Relationship Management

**Q3 — Don't Like & Good At It:**
- Session Preparation (logistics portion)
- Session Follow-Up (routine portions)
- Email Management
- Administrative & Scheduling
- Technology & Tools

**Q4 — Don't Like & Not Good At It:**
- Financial Management
- Marketing & Brand

Present the assignments to Duke and let him adjust before generating charts.

### Step 3: Calculate Time Distribution

For each quadrant, sum the estimated hours:
- **Q1 total hours** and **% of total business hours**
- **Q2 total hours** and **% of total**
- **Q3 total hours** and **% of total**
- **Q4 total hours** and **% of total**

Track personal time separately — don't include in the quadrant percentages.

### Step 4: Generate the Pie Chart

Run the bundled script to create the pie chart visualization:

```bash
python3 "SKILL_DIR/scripts/generate_pie_chart.py" \
  --q1 <hours> \
  --q2 <hours> \
  --q3 <hours> \
  --q4 <hours> \
  --title "D&E Time Audit — [Period]" \
  --output "/tmp/de_audit_pie_chart.png" \
  --details '<JSON of function breakdowns per quadrant>'
```

Replace `SKILL_DIR` with the actual path to this skill's directory. If the script
isn't found at the skill path, check `/Users/dukerevard/Desktop/delegate-and-elevate-audit/scripts/`.

The `--details` flag generates a second horizontal bar chart showing each function
sorted by hours with quadrant color-coding. Format:
`'{"Q1": ["Function: Xh", ...], "Q2": [...], "Q3": [...], "Q4": [...]}'`

After generating, display both charts to Duke inline.

### Step 5: Present the Full Audit Report

Structure the output as follows:

```
## Delegate & Elevate Time Audit — [Period]

### Time Distribution Summary
[Pie chart image]
[Function breakdown bar chart image]

| Quadrant | Hours | % of Total | Target | Gap |
|----------|-------|------------|--------|-----|
| Q1: Love & Great | XX | XX% | 80% | -XXpp |
| Q2: Like & Good | XX | XX% | 15% | +XXpp |
| Q3: Don't Like & Good | XX | XX% | 5% | +XXpp |
| Q4: Don't Like & Not Good | XX | XX% | 0% | +XXpp |
| **Total** | **XX** | **100%** | | |

### The Big Story
[2-3 sentences identifying the dominant pattern — where is time going and why?]

### Q1: Love It & Great At It (XX%)
[List each function, hours, and evidence]

### Q2: Like It & Good At It (XX%)
[List each function, hours, and evidence]

### Q3: Don't Like It & Good At It (XX%) — DELEGATE THESE
[List each function, hours, and evidence]
**Delegation opportunities:** [Specific suggestions]

### Q4: Don't Like It & Not Good At It (XX%) — ELIMINATE OR DELEGATE NOW
[List each function, hours, and evidence]
**Immediate actions:** [Specific suggestions]

### Patterns & Insights
- [Client concentration — which clients consume the most time?]
- [Invisible work — activities not on calendar but evidenced in email/docs]
- [Weekend/evening work patterns]
- [Rocks alignment — is time allocation supporting current quarter Rocks?]

### The Gap
- Current Q1 time: XX%
- Target Q1 time: 80%
- Gap to close: XX percentage points
- The real lever: [What category shift would have the most impact?]

### Recommended Rocks
1. [Most impactful delegation opportunity]
2. [Second most impactful]
3. [Quick win — something to stop or automate immediately]
```

## Edge Cases

- **Ambiguous calendar events:** If a title is vague (e.g., "Meeting" or "Call"),
  check attendees and description. If still unclear, add to "Uncategorized" and ask Duke.
- **All-day events:** Usually placeholders or travel days, not 8-hour blocks. Don't count as hours.
- **Recurring events:** Count every instance within the date range.
- **Cancelled/declined events:** Exclude them.
- **Weekend/evening work:** Flag separately — may signal capacity overflow.
- **Custom date range:** Adapt all queries accordingly.
- **Missing data source:** Proceed with what you have, note the gap in the report.
- **Large calendar output:** If the API returns too much data, process with Python/jq
  rather than trying to read it all into context.

## For Duke's Clients on Microsoft 365

Duke's EOS clients often want to run their own D&E time audit but use Microsoft
365 instead of Google Workspace. See `references/m365-client-instructions.md`
for a complete guide Duke can share with clients who want to build this same
capability using Outlook, Microsoft Calendar, Microsoft To Do / Planner, and
OneDrive/SharePoint.
