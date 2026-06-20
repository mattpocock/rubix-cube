# F2L reset — re-taught from first principles (lesson 19)

On 2026-06-17 Matt said he was "really not understanding ANY of the F2L lessons" (15–18) and asked for it re-explained from first principles. That "any" is the signal: the problem isn't a detail in one lesson, it's that the **foundation under all of them was never concretely planted**.

## Diagnosis (why 15–18 didn't land)

Lessons 15–18 are each well-scoped, but every one of them *assumes* a mental model that lesson 15 tried to establish in ~2 paragraphs and one box, then abandoned for recognition trainers and a stack of algorithms. Three first-principles gaps, all aligned with Matt's stated preference (NOTES) for **real-colour visuals over abstract description**:

1. **"The first two layers" was never shown as a whole.** No picture of top = workbench / bottom two = goal. Every diagram zooms straight into the front-right corner, so the *why are we doing this* never had a frame.
2. **The pairing rule was asserted, never worked in real colour.** "A corner + the edge sharing its two side colours" lives only in the glossary. Lessons 15–16 draw the corner/edge in **abstract grey + blue**, so "this piece" never connected to "the actual white-green-red piece in my hand."
3. **Why pairs beat the old way was told, not shown.**

## What lesson 19 does (the reset)

Pure foundation, **no new algorithm** (explicitly), short, ZPD = "make the picture, not the moves":
- §1 three-layer stack schematic — top layer = free workbench, bottom two = the goal; the one-pass-vs-two-passes win.
- §2 the goal = four identical "fill a slot" jobs; shows the empty front-right slot with real centre colours.
- §3 **the pairing rule worked in real colour** (the part 15–18 skipped): a slot between green+red wants the white-green-red corner + green-red edge; generalised to any two side colours.
- §4 the one idea: join the partners on the workbench, drop both together (vs old corner-in-then-knock-out). Shows a real-colour joined pair above its slot.
- §5 **reframes lessons 15–18** as "four ways to reach that joined-pair picture, then the same insert" — explicitly mapping each, so the lessons he found confusing become re-readable.
- Win: a "name-the-pair" recognition trainer (slot's two side colours → pick the corner+edge that wear them), guided→blind, streak-of-5. Drills the rule from §3, the thing the whole method stands on.

## Assets / sourcing

- Extended the shared renderer `assets/cube-render.js` (backward-compatible): `centers:1` paints the real centre stickers (U yellow, F green, R red) to anchor which faces a slot lies between; `real:1` draws the loose corner/edge in true white/green/red instead of abstract grey/blue. Lesson 19 uses both. No change to existing lessons' renders.
- No new technique to verify — this is conceptual foundation, grounded in the F2L sources already in RESOURCES (Ruwix, speedcube.us, J Perm primary). Did not run the simulator (no algorithm claim). Told Matt to trust his physical cube, per standing instruction.
- Glossary untouched — Pair / Slot / F2L already defined correctly; lesson 19 just teaches them properly for the first time.

## Open threads

- **Wait for Matt's read on whether the *picture* now makes sense** before doing anything else. If §3's pairing rule + §4's join-first idea land, point him back to re-read 15→18 in order. If a specific step is still a leap, slow that one down further (offer is in the lesson footer).
- Solve card STILL unchanged — parallel rollout continues; F2L replaces stages 2+3 only once all four slots are reliable end-to-end.
- Still deferred: same-colour-up "hide and seek" case (take it last, after the foundation is solid).
- Mission unchanged; F2L is the active in-scope thread. Never push speedcubing.
