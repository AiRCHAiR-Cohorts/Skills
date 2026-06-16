# AirChAiR Personal Operating System

Build a folder on your desktop that tells any AI tool who you are, how you work, and what matters to you. Build it once, and every chat, agent, and tool you use afterward gets sharper, because it reads your context instead of guessing.

This is from AirChAiR Session 2. If you can answer questions about your own work, you can build one.

## Quickest path (recommended): install the skill

The skill turns Claude into an interviewer that builds the whole thing for you. No copy and paste. These steps are written for Claude Desktop on a Free, Pro, or Max plan. Follow them in order.

**Step 1: turn on code execution (one time).**
In Claude, click your name in the bottom left, then **Settings**, then **Capabilities**. Switch on **Code execution and file creation**. Skills will not appear until this is on.

**Step 2: download the skill file.**
In this repo, click the file **`personal-operating-system-skill.zip`**, then click **Download** (the download icon near the top right of the file view). Save it somewhere you can find it, like your Downloads folder. Do not unzip it. Claude wants the ZIP as-is.

**Step 3: upload the skill.**
1. Open the **Cowork** tab in Claude, then click **Customize** in the left sidebar.
2. Open the **Skills** tab.
3. Click the **+** button, then **+ Create skill**, then **Upload a skill**.
4. Choose the `personal-operating-system-skill.zip` file you just downloaded.
5. The skill appears in your list. Make sure its toggle is **on**.

**Step 4: connect a desktop folder.**
Still in Cowork, connect a folder on your desktop (this is where your Operating System will be saved). If you have never done this, Claude will prompt you to pick a folder when you start.

**Step 5: run it.**
Open a new Cowork chat and type: **build my personal operating system**

Answer the questions. Use voice dictation if you can, it is faster and better. In 30 to 60 minutes you will have a complete Operating System folder on your desktop.

> On a Team or Enterprise plan? An owner has to enable Skills in Organization settings first. If the Skills tab is missing or greyed out, that is why. Ask your admin, or use the paste-the-protocol path below.

## No-install path: paste the protocol

If you cannot install the skill, you can paste the instructions instead.

1. Open `protocol/build-protocol.md`.
2. Copy the whole file.
3. Paste it into a new Claude chat with a desktop folder connected.
4. Answer the questions the same way.

## What's in this repo

- **`personal-operating-system-skill.zip`**: the ready-to-upload skill file (start here, see Step 2 above)
- **`skills/personal-operating-system/`**: the unzipped skill, if you want to read it first
- **`protocol/build-protocol.md`**: the same instructions as a paste-in fallback
- **`example-brett-os/`**: a finished example so you can see what you are building toward. Open it and look around. Brett is a made-up marketing director.
- **`booklet/`**: the Session 2 summary and the one-page quick-start card

## How it works (the short version)

The build runs in three phases:

1. **Interview**: Claude asks you questions and drafts ten short files: who you are, your work plan, your role, your projects, your people, your tools, your writing voice, your rules, your expertise, and how you make decisions. You react, it revises.
2. **Operator**: a task that runs each day, pulls what changed in your work, writes you a brief, and updates files that went stale.
3. **Optimizer**: a task that runs weekly, cleans up duplicates and bloat, and flags anything stale or off-voice for you to fix.

## Three things to remember after you build it

- Keep the folder connected in every new chat so the AI can use it.
- When something important changes, just tell Claude and it saves it to the right file.
- Give it time. Version one is about 70 percent right. Patch it as you notice gaps. In a few weeks it knows you cold.

You are not learning a tool here. You are building the foundation every tool you ever use will stand on.
