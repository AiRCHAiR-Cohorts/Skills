# CUSTOMIZE.md

How to adapt these skills to your work, your tools, and your voice.

## The Anatomy of a Skill

Open any `SKILL.md` file. You'll see two parts:

**1. Frontmatter (the YAML block at the top, between `---` lines):**
```yaml
---
name: skill-name
description: >
  When to use this skill. Trigger phrases. What it produces.
---
```

The `description` is what tells Claude *when* to use this skill. Trigger phrases like "run a 1-3-1 on this" or "audit my time" go here. Claude scans descriptions of all available skills to pick the right one for any given user message.

**2. Body (everything below the second `---`):**
The actual instructions — what to do, in what order, what to produce. This is where the real work lives.

## What to Customize First

For each skill, three things are most likely to need updating:

### 1. Tool integrations

Some skills assume specific apps. The most common swap is the task manager.

- **`delegate-and-elevate-audit`** assumes Trello as the task source.
  - To use Todoist, ClickUp, Asana, Notion, etc.: open `SKILL.md`, search for "Trello," and replace with your tool's name. Make sure you've connected that tool to Claude.ai under Settings → Connectors.
  - If your task tool isn't supported by an MCP connector yet, you can have Claude pull data from a CSV export instead — adjust the SKILL.md to say "the user will paste or upload a CSV export from their task manager."

- **Email and calendar references** generally assume Gmail and Google Calendar. If you're on Microsoft 365, search for "Gmail" → "Outlook" and "Google Calendar" → "Outlook Calendar." There's already an M365 reference doc in `delegate-and-elevate-audit/references/m365-client-instructions.md` showing the patterns.

### 2. Personal context (especially in `board-of-advisors` and `cwrf`)

Several skills include placeholders or generic language that you should replace with your own specifics:

- **`board-of-advisors`**: The eight advisor archetypes are starting points. Most people customize them by replacing each archetype with a specific named figure they admire (a mentor, an author, a personal hero whose voice they can channel). The skill's own `Customization` section walks through this.

- **`cwrf`**: References "the practitioner" and "the coach" generically. If you're using this for your own work, swap in your name and your role. If you're using it inside an organization, swap in your org's terminology.

### 3. Domain language

These skills are built around EOS (the Entrepreneurial Operating System). If you don't operate inside EOS:

- The framework concepts still apply (Rocks = 90-day priorities, L10 = weekly leadership team meeting, V/TO = strategic plan, Accountability Chart = org chart with roles)
- Search the skill for EOS-specific terms and either translate them to your language or strip them
- `research-with-confidence` and `cwrf` reference EOS lenses; remove or replace if not relevant
- `delegate-and-elevate-audit` is built on the EOS Delegate-and-Elevate framework specifically. The four-quadrant logic (Love/Great, Like/Good, Don't Like/Good, Don't Like/Not Good) is universal even if you don't call it "EOS"

## How to Edit a SKILL.md

Skills are just text files. You can edit them in any text editor:
- **VS Code, Sublime Text, Notepad++** — best for editing
- **TextEdit (Mac), Notepad (Windows)** — works fine for small edits, but make sure they save as plain text, not RTF
- **Cursor or Claude Code** — if you have access to either, you can ask the AI to make the edits for you

## Testing Your Customized Skill

After editing:

1. **Zip up just the skill folder** (e.g., `cwrf/`), not the whole repo
2. In Claude.ai → Settings → Capabilities → Skills → Upload skill
3. Start a new conversation
4. Use one of the trigger phrases from the skill description
5. See what happens

If Claude doesn't pick up your skill:
- Check that the trigger phrase you used appears in the skill's description
- Check that the YAML frontmatter is well-formed (the `---` lines, the `name:` line, the `description: >` block)
- Try a more explicit phrase like "use the cwrf skill on this"

If Claude picks up the skill but the output is wrong:
- The skill body is probably the issue. Read what Claude actually did, then go edit the SKILL.md to give clearer instructions for the part it got wrong.

## Tips Worth Knowing

**Description is everything.** A poorly-described skill will never trigger. A well-described skill will trigger reliably even on phrasing variations. When in doubt, add more trigger phrases to the description.

**Specific beats general.** Skills that try to do too many things often do all of them poorly. A skill that does one thing well is more useful than one that's vague.

**Iterate.** Your first version of a skill will be okay. Your fifth version will be good. Your tenth version will be the one you actually use every week.

**Read other people's skills.** This repo is one source. The official Anthropic skills directory and other shared libraries are others. Reading skills written by people who think differently than you do will sharpen your own.

**Keep `SKILL.md` short.** The documented limit is roughly 500 lines and a description under ~100 words. Long, sprawling skills perform worse than tight, focused ones. If you find yourself adding a fifth section, ask whether that section should be its own skill.

## What to Build Next

Once you've customized one of these skills and used it for real work, you'll start noticing recurring tasks in your week that could become their own skills. That's the moment to start building from scratch.

Anthropic publishes a `skill-creator` skill that walks you through building a new skill from a blank page. That's the next step after this cohort starter pack.
