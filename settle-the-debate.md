---
name: settle-the-debate
description: >
  Structured debate analysis and adjudication. Use this skill whenever the user uploads, pastes, or describes two opposing arguments, positions, essays, or viewpoints and wants an objective analysis. Trigger on: "settle this debate", "who wins this argument", "analyze these two positions", "compare these arguments", "who has the stronger case", "adjudicate this", "score this debate", "who's right here", "break down both sides", "who makes the better argument", "referee this", "judge these two views", or any situation where the user presents two conflicting perspectives and wants a structured, scored analysis with a declared winner. Also trigger when someone says "I'm having a debate with someone about X" or "my colleague says X and I say Y, who's right?" Do NOT trigger for general research tasks, single-sided persuasive writing, or simple factual questions.
---

# Settle the Debate

A structured framework for analyzing two opposing arguments, scoring them point by point, and declaring an overall winner based on argument quality — not personal opinion.

---

## Inputs

The user will provide one of the following:
- Two uploaded documents (text, PDF, or pasted content)
- A summary of two opposing views
- Two named positions (e.g., "Side A says X, Side B says Y")

If the user provides only one side or a vague topic, ask them to clarify both positions before proceeding.

---

## Step 1: Identify the Positions

State each side clearly and neutrally before any analysis:

```
POSITION A: [Name or Label] — [One sentence summary of their core claim]
POSITION B: [Name or Label] — [One sentence summary of their core claim]
```

If the positions have named authors, use their names. Otherwise label them Position A and Position B.

---

## Step 2: Extract Main Points

Identify 3–6 main argument points being debated. Each main point should represent a distinct claim, premise, or line of reasoning that both sides address (directly or implicitly).

Format:
```
MAIN POINT 1: [Neutral label for the point being contested]
MAIN POINT 2: ...
```

Do not editorialize at this stage. Simply surface what the debate is actually about.

---

## Step 3: Points of Agreement

Before scoring, identify where the two sides actually agree. This grounds the analysis and narrows the real dispute.

```
COMMON GROUND:
- [Shared assumption or concession both sides make]
- [Areas where both agree, even if they draw different conclusions]
```

---

## Step 4: Fact-Check the Claims

Before scoring any point, verify the factual claims made by both sides. This is the most important step — a well-argued falsehood still loses.

**Invoke the `research-with-confidence` skill** for any claim that is:
- Empirical (statistics, studies, historical events, scientific consensus)
- Disputed between the two sides
- Central to a main point (not peripheral color)

For each fact-checked claim, assign a confidence rating:
- **VERIFIED** — 3+ independent quality sources confirm it. Award it full weight.
- **DISPUTED** — Sources conflict, or the claim is contested among experts. Treat as partial credit; note the ambiguity.
- **UNSUPPORTED** — No credible sources found, or the claim contradicts available evidence. It weakens that side's position on this point.
- **UNVERIFIABLE** — Opinion, prediction, or normative claim that cannot be fact-checked. Set aside for Step 5 logical analysis only.

Document the fact-check results inline for each main point before issuing a ruling.

---

## Step 5: Score Each Main Point

For each main point:

1. **Summarize each side's argument** on that point (2–4 sentences each)
2. **Show fact-check results** — which claims were verified, disputed, unsupported, or unverifiable
3. **Score the point** — award it to Position A, Position B, or call it a Draw
4. **Explain the ruling** — lead with factual accuracy, then logic

Use this format for each point:

---
**MAIN POINT [#]: [Label]**

*Position A argues:* [Summary]

*Position B argues:* [Summary]

*Fact-check:*
- [Claim from A]: VERIFIED / DISPUTED / UNSUPPORTED / UNVERIFIABLE — [brief note]
- [Claim from B]: VERIFIED / DISPUTED / UNSUPPORTED / UNVERIFIABLE — [brief note]

*Ruling:* Position A / Position B / Draw

*Reason:* [2–3 sentences. Lead with what the facts show, then any logical or relevance considerations.]

---

Scoring criteria (in strict priority order):
1. **Factual accuracy** — Are the claims verified by independent sources? Unsupported claims are penalized. Disputed claims are treated as neutral.
2. **Logical consistency** — Does the argument hold together internally, given what's actually true?
3. **Relevance** — Does the argument address the actual point being contested?
4. **Engagement with counterarguments** — Does the side acknowledge and respond to the other's strongest evidence?

Style, rhetoric, and persuasiveness are explicitly NOT scoring criteria. A plain, accurate argument beats an eloquent inaccurate one every time.

Do NOT score based on personal preference, political lean, or which side you find more sympathetic.

---

## Step 6: Aggregate Scoreboard

Tally the point-by-point wins.

```
SCOREBOARD
──────────────────────────────
Position A wins: [#] points
Position B wins: [#] points
Draws: [#]
──────────────────────────────
OVERALL WINNER: [Position A / Position B / Draw]
```

---

## Step 7: Overall Winner Declaration

Declare the winner and provide a 3–5 sentence synthesis explaining:
- Which side had more factually verified claims
- Which side's unsupported or disputed claims cost them points
- The most significant factual weakness of the losing side
- Any important caveat — e.g., "Position B won on argument quality but several of its central claims were unverifiable; if those claims are later proven false, the ruling may change"

Be direct. Don't hedge the declaration.

---

## Tone and Voice

- Objective, factual, and direct — like a referee, not a debate coach
- Lead every ruling with what the evidence actually shows
- Never moralize or insert personal opinion on the underlying topic
- Plain language over elegant language — accuracy over style applies to the output too

---

## Edge Cases

- **Lopsided debate**: If one side's claims are consistently unsupported and the other's are verified, say so plainly. Don't manufacture false balance.
- **Both sides make unsupported claims**: Call it a draw on that point. Note both sides are arguing from assertion rather than evidence.
- **Unverifiable topic** (pure opinion, values, predictions): Note upfront that fact-checking will be limited. Score primarily on logical consistency and internal coherence for those points.
- **One side ignores a point entirely**: Award the point to the side that addressed it and note the omission.
- **Incomplete inputs**: If the user provides only one side, ask for the opposing view before proceeding.

