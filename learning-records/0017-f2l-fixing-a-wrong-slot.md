# F2L part 4 — fixing a filled-but-wrong slot (lesson 18)

On 2026-06-17 Matt asked specifically: "what happens when the edge is in the right spot but twisted the wrong way?" I answered inline (it's just a trapped piece → `R U R'` → rebuild), but he then said it needs its **own lesson**. Correct instinct: the flipped edge belongs to a whole family — the **filled-but-wrong slot** — that's easy to skate past because the slot *looks* occupied. Lesson 18 ("Fix a Wrong Slot") owns it.

## What it teaches (recognition-first, one fix)

Two halves:
1. **Read the tell.** A solved slot has clean colour runs down its two visible faces (green down the front, red down the right) and no white on a side. The three defects:
   - **Edge flipped** — the edge's two colours are swapped (red breaks the green run).
   - **Corner twisted** — white shows on a side instead of the bottom.
   - **Wrong piece** — colours that don't belong to this slot at all (reads the same).
2. **One fix for all.** You can't flip/twist a piece in place (no single-piece-only move exists), so empty the slot and rebuild: `R U R'` (the lesson-17 evict) lifts whatever's jammed up to the top, then pair (L16) and insert. Reassurance baked in: if a correct piece shared the slot it comes out too — expected, not a regression.

Framed so Matt never has to *diagnose which* defect it is: clean → leave; broken → `R U R'`. Binary recognition trainer (Clean → leave / Wrong → R U R'), guided→blind, streak-of-5.

## Sourcing + verification (record-0012 steer)

Technique from J Perm (pull a mis-set piece out with a trigger rather than fight it in place) + Ruwix. Simulator used only to CONFIRM:
- `R U R'` clears a **flipped edge** (→ top, cross intact), a **twisted corner** (→ top, cross intact), and **random junk** in FR (cross intact). All verified this session.

## Assets — renderer extended again (shared component)

Added a **real-face-colour slot view** to `assets/cube-render.js`: `fr:'solved'|'flip'|'twist'|'wrong'` fills the FR slot column with literal green/red/white so the colour-mismatch tells are *visible* (previous specs used abstract blue/grey pieces, which can't show a colour swap). Used with `corner:0`. This is the first lesson to need literal colours; the later hide-and-seek lesson will reuse it. L18 links the shared asset via `<script src>` (L17 already does; L16 keeps its inline copy).

## Edits to neighbouring artifacts

- **L17** trimmed: the flipped-edge callout I'd added there is now a one-line forward-pointer to L18 (avoids duplication, keeps L17 focused on the basic evict).
- **Glossary** gained "Wrong slot (filled-but-wrong)".

## Open threads

- Solve card STILL unchanged — parallel rollout. Matt can now build any slot AND repair a wrong one. Trigger to retire stages 2+3 is close: when the four-slot scan + rebuild is automatic and reliable end-to-end.
- Last deferred F2L case: same-colour-up "hide and seek" (corner + edge same colour on top, won't pair by simple scoop). Take it last, then retire stages 2+3 and re-bank.
- Mission unchanged; F2L is the active in-scope thread. Never push speedcubing.
