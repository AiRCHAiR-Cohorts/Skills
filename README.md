# AirChAiR Cohort — Skills Library

A starter library of Claude Skills for the AirChAiR Cohort — professionals reskilling with AI.

These are working examples from a real practice, adapted for cohort use. They are designed to be **studied, customized, and rebuilt** — not just copy-pasted.

## What's a Claude Skill?

A Claude Skill is a folder containing:
- A `SKILL.md` file with frontmatter (name, description) and a body of instructions
- Optional supporting files: scripts, reference docs, examples

When the skill is loaded into Claude (via Settings → Capabilities → Skills), Claude reads the `SKILL.md` file when its trigger phrases appear in conversation, and follows the instructions inside.

Skills are how you teach Claude to behave like an expert for a specific recurring task — running a 1-3-1 decision, auditing your time, building a roadmap, stress-testing a decision against multiple perspectives, conducting research.

## What's in This Repo

| Skill | What it does |
|---|---|
| `one-three-one` | A structured decision-making framework. Defines the problem, the desired outcome, three potential paths, and a recommended one — driven by a five-question interview. |
| `delegate-and-elevate-audit` | Pulls data from Gmail, Google Calendar, and a task app to inventory where your time went, categorizes activities into the four EOS Delegate-and-Elevate quadrants, generates a pie chart, and outputs a structured audit report. |
| `cwrf` | Crawl-Walk-Run-Fly phased change framework. Builds roadmaps for organizational transformation across four domains: methodology rollout, AI agent adoption, exit readiness, and general change. |
| `board-of-advisors` | Multi-perspective decision review. Eight advisor archetypes review a decision independently, then an Integrator voice synthesizes their input into a recommended action. |
| `research-with-confidence` | Multi-source research with confidence scoring and cross-source fact-checking. Outputs a structured research brief with a mandatory "what's NOT clear yet" section. |

## How to Use a Skill

### Option 1: Use as-is

1. Click the **green "Code" button** at the top of this repo, then **"Download ZIP"**
2. Unzip the file on your computer
3. Each subfolder (e.g., `one-three-one/`) is one skill. Rezip just that folder.
4. In Claude.ai → Settings → Capabilities → Skills → **Upload skill**
5. Upload the zip
6. Start a new conversation and use one of the trigger phrases listed in the skill description

### Option 2: Customize, then use

The whole point of this cohort is to teach you to *build*, not just install. See `CUSTOMIZE.md` for step-by-step guidance on adapting these skills to your own work, tools, and voice.

## Requirements to Get Full Value

Some skills (especially `delegate-and-elevate-audit` and `research-with-confidence`) work best when Claude has connected access to your tools:
- **Email** (Gmail, Outlook)
- **Calendar** (Google Calendar, Outlook Calendar)
- **Task management** (Trello, Todoist, ClickUp, Asana, Notion, etc.)
- **Drive / cloud storage** (Google Drive, OneDrive, Dropbox)
- **Web search** (built into Claude.ai)

You connect these in Claude.ai → Settings → Connectors. Each skill notes which tools it expects.

## License

These skills are released under the [Creative Commons Attribution 4.0 International](LICENSE) license. You're free to copy, modify, and redistribute them — including for commercial purposes — as long as you provide attribution.

## Feedback

Found a bug, have a suggestion, or built an interesting variant? Open an issue or pull request. The point of a public repo is that the library improves over time.

## A Word on Customization

These skills come from a real working practice. They reference frameworks (EOS), tools (Trello, Gmail), and judgment calls that may not match yours. That's the feature, not the bug. Reading a skill that was built for someone else's work and figuring out which parts to keep, change, or replace is one of the fastest ways to learn how to build skills for your own work.

The `CUSTOMIZE.md` file walks through this. Start there.
