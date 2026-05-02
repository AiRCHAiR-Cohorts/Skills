# Building a Delegate & Elevate Time Audit on Microsoft 365

This guide is for EOS leadership team members who use Microsoft 365 and want to
run an objective, data-driven Delegate & Elevate audit of their own time — the
same exercise Duke runs on his Google Workspace stack.

The idea is simple: instead of guessing where your time goes, pull real data from
the tools you already use every day, categorize it into the four D&E quadrants,
and let the numbers tell you what to delegate.

---

## What You'll Need

- Microsoft 365 account (Business or Enterprise)
- Access to your own Outlook, Calendar, To Do / Planner, and OneDrive
- About 60-90 minutes to do the full exercise
- A spreadsheet (Excel works perfectly)

## The Four Quadrants (Quick Refresher)

| Quadrant | Description | Action |
|----------|-------------|--------|
| **Q1: Love It & Great At It** | Energizes you, excellent results | Protect — aim for 80% of your time |
| **Q2: Like It & Good At It** | Satisfying, solid work | Keep for now, delegate over time |
| **Q3: Don't Like It & Good At It** | Draining but competent | Delegate to someone who loves it |
| **Q4: Don't Like It & Not Good At It** | Neither fun nor good | Eliminate or delegate immediately |

---

## Step 1: Export Your Calendar Data

Your calendar is the most honest record of where your time went.

### Option A: Viva Insights (Recommended if Available)

If your organization has Microsoft Viva Insights (formerly MyAnalytics):

1. Go to **myanalytics.microsoft.com** or open the **Viva Insights** app in Teams
2. Look at the **Time Allocation** dashboard — it already categorizes your time into:
   - Focus time (uninterrupted blocks)
   - Meetings (scheduled)
   - Email/chat time
   - After-hours work
3. Export the data for your chosen period (quarter or month)
4. Use this as your starting point — you'll refine the categories below

### Option B: Manual Calendar Review

1. Open **Outlook Calendar** in the desktop app or web
2. Switch to **List View**: View > Change View > List
3. Set the date range to your audit period (e.g., Q1: Jan 1 - Mar 31)
4. Select all events > Copy > Paste into an Excel spreadsheet
5. You should have columns for: Subject, Start Date, End Date, Duration, Location
6. Add columns for: **Function Category** and **D&E Quadrant**

### Option C: PowerShell Export (Technical Users)

```powershell
# Connect to Exchange Online
Connect-ExchangeOnline -UserPrincipalName you@company.com

# Export calendar events to CSV
Get-CalendarEvents -StartDate "2026-01-01" -EndDate "2026-03-31" |
  Select-Object Subject, Start, End, Duration, Location, Organizer |
  Export-Csv -Path "Q1_Calendar.csv" -NoTypeInformation
```

### Option D: Power Automate Flow

Create a flow that runs monthly:
1. **Trigger:** Schedule — 1st of each month
2. **Action:** Get calendar events from previous month
3. **Action:** Create rows in an Excel table on OneDrive
4. This builds your audit data automatically over time

---

## Step 2: Analyze Your Email Patterns

Email reveals where your communication effort goes — especially the invisible
work between meetings.

### Using Outlook Search

Run these searches and note the approximate counts:

1. **Sent emails in date range:**
   - Search: `from:me sent:>=01/01/2026 AND sent:<=03/31/2026`
   - Note the total count

2. **Emails by key recipients/groups:**
   - Search: `from:me to:clientname` for your major contacts
   - This shows where your email effort concentrates

3. **After-hours email:**
   - In Viva Insights, check "After-hours collaboration"
   - Or search: `from:me sent:>=6:00 PM` (rough approximation)

### Using Viva Insights (if available)

Viva automatically tracks:
- Time spent reading and writing email
- Your most-emailed contacts
- After-hours email patterns
- Response time patterns

Export this data to supplement your calendar analysis.

---

## Step 3: Review Your Task Data

### Microsoft To Do

1. Open **To Do** (todo.microsoft.com)
2. Review completed tasks in your chosen period
3. Note which categories/lists they belong to
4. Map each to a function category

### Microsoft Planner

1. Open any Planner boards you use
2. Switch to **Charts** view to see task distribution by bucket and status
3. Review completed tasks for the period
4. Export the board data: Planner > Schedule > Export to Excel

### OneNote / SharePoint

Search for documents and notes you created or modified during the period:
1. In OneDrive/SharePoint, sort by **Modified Date**
2. Filter to your audit date range
3. Note which documents got the most revision activity

---

## Step 4: Build Your Categorization Spreadsheet

Create an Excel workbook with these columns:

| Activity | Source | Hours | Function Category | Quadrant |
|----------|--------|-------|-------------------|----------|
| Weekly team standup | Calendar | 13h | Team Management | Q2 |
| Client proposal drafting | Calendar + OneDrive | 25h | Business Development | Q1 |
| Expense reports | Calendar + To Do | 6h | Financial Admin | Q4 |
| Reply-all email chains | Viva Insights | 15h | Email Management | Q3 |

### Define Your Own Function Categories

Tailor these to your actual role. Here's a starter list you can modify:

**Common functions for an EOS leadership team member:**
- Strategic Planning
- Team Management / LMA
- Customer/Client Delivery
- Business Development / Sales
- Financial Management
- Operations / Process Work
- Administrative Tasks
- Email & Communication
- Meetings (internal)
- Meetings (external)
- Learning & Development
- Problem Solving / Firefighting

### Assign Quadrants Honestly

For each function, answer two questions:
1. **Do I love it, like it, or not like it?** (Be honest — "good at it" doesn't mean you love it)
2. **Am I great at it, good at it, or not good at it?** (Look at actual results, not just effort)

---

## Step 5: Create Your Pie Chart

### In Excel

1. Create a summary table:

| Quadrant | Hours | Percentage |
|----------|-------|------------|
| Q1: Love & Great | 120 | 48% |
| Q2: Like & Good | 55 | 22% |
| Q3: Don't Like & Good | 50 | 20% |
| Q4: Don't Like & Not Good | 25 | 10% |

2. Select the data > Insert > **Pie Chart** (or Doughnut chart)
3. Format with these colors for consistency:
   - Q1: Green (#2E7D32)
   - Q2: Blue (#1565C0)
   - Q3: Orange (#EF6C00)
   - Q4: Red (#C62828)
4. Add data labels showing both percentage and hours
5. Title: "Delegate & Elevate Time Audit — [Your Name] — [Period]"

### In Power BI (Advanced)

If you want an interactive, auto-updating dashboard:
1. Connect Power BI to your Outlook Calendar, Viva Insights, and Planner data
2. Create a data model that maps events/tasks to function categories
3. Build a dashboard with:
   - Pie chart of quadrant distribution
   - Trend over time (quarter-over-quarter)
   - Drill-down by function category
   - Filter by date range

---

## Step 6: The D&E Conversation

Bring your completed audit to your next 1-on-1 with your manager, your
Implementer, or your accountability partner. Share:

1. **Your current state:** "Here's where my time actually goes"
2. **Your Q1 percentage:** "I'm at X% — the target is 80%"
3. **Your top 3 delegation candidates** from Q3 and Q4
4. **Who could absorb each** — someone who GWCs those responsibilities
5. **A 90-day plan** to delegate one or two items (make it a Rock!)

---

## Automating This for Future Quarters

### Power Automate Recipe

Build a recurring flow that runs quarterly:

1. **Trigger:** Schedule — last week of each quarter
2. **Actions:**
   - Pull calendar events for the quarter
   - Pull email stats from Microsoft Graph API
   - Pull completed tasks from To Do / Planner
   - Populate an Excel template on OneDrive
   - Send you a Teams notification: "Your Q[X] D&E data is ready for review"

### Microsoft Graph API (For IT Teams)

If your IT team wants to build this as a company-wide tool:

```
GET /me/calendarView?startDateTime=2026-01-01&endDateTime=2026-03-31
GET /me/messages?$filter=sentDateTime ge 2026-01-01 and sentDateTime le 2026-03-31
GET /me/planner/tasks?$filter=completedDateTime ge 2026-01-01
```

These endpoints return the raw data needed for the audit. Combine with a
Power App or SharePoint page for a self-service D&E dashboard.

---

## Tips for Success

- **Run the audit quarterly** — make it part of your quarterly prep ritual,
  right before Rocks planning
- **Be brutally honest** about quadrant placement — the value is in the truth,
  not in flattering yourself
- **Start with Q4** — those are the easiest wins. Stop doing them. Today.
- **Q3 is the dangerous one** — you're good at these tasks so nobody complains,
  but they drain your energy. Find someone who *loves* this work.
- **Track your Q1 % over time** — the goal is to see it climb quarter by quarter
- **Share with your team** — when everyone on the LT does this exercise, you
  can match people's Q1s to each other's Q3s and Q4s. That's the magic.
