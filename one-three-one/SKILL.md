---
name: one-three-one
description: Duke Revard's structured decision-making framework. Use this skill whenever Duke says "1-3-1", "one three one", "give me a 1-3-1", "run a 1-3-1 on this", "do a 1-3-1", "frame this as a 1-3-1", "I need a 1-3-1", or asks for a structured decision framework. Also trigger when Duke is wrestling with a decision and explicitly asks for a structured way to think it through with three options and a recommendation. The skill defines the problem, the desired outcome, presents three potential paths, and recommends one — driven by a five-question interview where Claude proposes its own answer first, lets Duke edit or approve, and only then proceeds to the next question. Do NOT trigger for general advice, brainstorming, or open-ended exploration where Duke hasn't asked for the 1-3-1 structure specifically.
---

# 1-3-1 Decision Framework

A 1-3-1 is Duke's preferred structure for working through any non-trivial decision. The output has three parts:

1. **The Problem** — one clear statement of what is actually being decided
2. **The Outcome** — one clear statement of what success looks like
3. **Three Paths** — three meaningfully distinct options
4. **One Recommendation** — Claude's recommended path, with reasoning

The "1-3-1" name refers to: 1 problem, 3 paths, 1 recommendation. The outcome statement sits inside the framing of the problem.

## The Five-Question Interview

Before producing the 1-3-1, Claude conducts a five-question interview with Duke to gather what's needed. This is NOT a passive Q&A — Claude follows the **answer-first protocol** Duke prefers across all his interview-based skills:

> For each of the five questions, Claude proposes its own answer based on what it already knows about Duke, the situation, and the surrounding context. Duke then edits, approves, or replaces the answer. Only after the answer is locked does Claude move to the next question.

This protocol matters because Duke is Kolbe Fact Finder 9 — he wants thorough analysis, but he also wants the analyst to do the thinking work first and bring him a proposal to react to, not a blank prompt.

## The Five Questions

Ask these one at a time. After each, propose an answer, wait for Duke's edit or approval, then move on.

### Question 1: What is the actual decision being made?
*Answer-first: Claude proposes the cleanest one-sentence framing of the decision based on context. Surface any ambiguity — e.g., "Are you deciding whether to do X, or how to do X?" Distinguish the surface decision from the underlying decision when relevant.*

### Question 2: What does a good outcome look like 6–12 months from now?
*Answer-first: Claude proposes a concrete success picture. Include observable signals (revenue, time spent, energy, client satisfaction, how Duke feels showing up to the work). When Duke's vocational throughline is relevant, include whether the outcome keeps him "in the room" with leadership teams or pulls him out.*

### Question 3: What are the constraints and non-negotiables?
*Answer-first: Claude proposes the constraints visible in context — time, money, capacity, family commitments, existing client load, spouse or partner involvement, the EOSI guardrails, anything in his Kolbe profile that creates a real wall (e.g., low Quick Start means no improvise-from-scratch options). Flag any constraint Claude is guessing at.*

### Question 4: What's already been tried, considered, or ruled out?
*Answer-first: Claude proposes what it knows from prior conversations, memories, or context — past sprints, prior skills built, decisions made earlier in the year. If Claude doesn't have visibility into prior attempts, name that explicitly rather than guessing.*

### Question 5: What's the gut-check answer Duke is leaning toward?
*Answer-first: Claude proposes its read of where Duke is leaning based on the conversation, language, energy, and any tells in how he framed the problem. This isn't to bias the recommendation — it's so the final recommendation can either confirm Duke's instinct (with reasoning) or push back honestly (with reasoning). Both are valuable; neither is the default.*

## Producing the 1-3-1

After the interview, deliver the 1-3-1 in this exact structure:

```
## Problem
One sentence. What is being decided.

## Desired Outcome
One sentence. What success looks like.

## Three Paths

### Path A: [Distinct strategic name]
- What it means in practice
- What it costs (time, money, energy, opportunity)
- What it gets Duke
- Key risk

### Path B: [Distinct strategic name]
- What it means in practice
- What it costs
- What it gets Duke
- Key risk

### Path C: [Distinct strategic name]
- What it means in practice
- What it costs
- What it gets Duke
- Key risk

## Recommendation
[Path A / B / C]

Why: [2–4 sentences of honest reasoning, including any tradeoff Duke should be aware of. If the recommendation diverges from the gut-check answer in Question 5, name that explicitly and explain why.]

## What to do this week
[1–3 concrete next actions if Path is approved]
```

## Quality Guardrails

**Three paths must be meaningfully distinct.** Not "do it fast / do it slow / do it medium." Each path should represent a different strategic posture — for example, "build it solo / partner with X / outsource entirely" or "go narrow and deep / go broad / sequence narrow-then-broad." If Claude can't articulate a real strategic difference, the path doesn't belong.

**Don't pad with a strawman.** Three legitimate options. If only two real options exist, surface that and say so — don't invent a third path just to fill the structure. In that case, the 1-3-1 becomes a 1-2-1 and Claude should say so explicitly rather than fake symmetry.

**The recommendation is honest, not safe.** Claude's job is to recommend the path that best fits Duke's stated outcome and constraints, not the path that is least likely to ruffle feathers. If the recommendation involves a hard truth (e.g., "stop pursuing this venture and focus on the core practice"), say it cleanly and own it.

**Lens-check against Duke's wiring.** Before finalizing the recommendation, scan against the `duke-revard` skill if relevant: Does this path play to Wonder + Tenacity, or does it pull Duke into Galvanizing/Enablement frustration territory? Does it respect Quick Start 2 (no improvise-from-scratch)? Does it require structural environments where leadership teams face what they're avoiding (his vocational throughline), or does it pull him out of that room?

## When NOT to use the 1-3-1

- When Duke is brainstorming or thinking out loud — stay open and exploratory
- When the decision is already obviously made and Duke just needs validation or execution help
- When the problem is technical implementation (use a different framework)
- When fewer than three real options exist — say so and offer a 1-2-1 instead
