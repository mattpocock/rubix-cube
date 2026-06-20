# F2L part 2 — building pairs (lesson 16)

On 2026-06-17 Matt reported lesson 15 was hard to *practise*: "I can't find any pairs to slot in." That's the expected and correct discovery — fully-formed connected pairs are rare on a scramble (≈one slot per solve hands you one). The unblocking skill is **building** a pair, not finding one. Lesson 16 ("Build the Pair") teaches it.

## What it teaches (kept tight, minimal-memorisation)

Two sub-skills:
1. **Get both pieces to the top** — pop a stuck corner/edge out of the slot with `R U R'` (the move he already owns, used to evict rather than insert).
2. **Scoop by the white sticker** — park the corner at top-front-right, read where white points, bring the edge to the named spot with U turns, then fire:
   - white → **front**, edge to top-right → `U R U' R'`
   - white → **right**, edge to top-front → `U' F' U F`
   - white → **up**, edge to top-right → `R U2 R' U' R U R'` (the `R U2 R'` rolls white onto a side, reducing to the side case)

Framed as **one idea + its mirror, plus "knock white off the top first"** — so the memory load stays near the mission's minimal bar. Recognition trainer (read white → pick the scoop), guided→blind, streak-of-5, same engine as lessons 14–15.

## Sourcing + verification (followed the steer exactly)

Technique from primary sources (Ruwix F2L gave `R U R'`, `R U2 R'`→`U R U' R'`, reunion sequences; speedcube.us for the case taxonomy). J Perm is the chosen video primary but is JS-rendered (WebFetch can't read it) — linked for the visual.

Crucially, used the **verified simulator only to CONFIRM** each candidate sequence's claim (record-0012 rule), never to derive. Method: apply each sequence's *inverse* to a solved cube, assert it disturbs **only** the FR slot + top layer (never the rest of the first two layers), and read off which case it solves to get the natural hold (corner at UFR). All sequences in the lesson passed FR-ONLY. Refined the white-up case to one held at top-front-right (`R U2 R' U' R U R'`) rather than an awkward back hold.

## Assets rescued to the workspace (Matt's instruction)

Matt said to save tooling under `/assets`. Moved the previously-ephemeral `/tmp/cube.py` (faithful 54-sticker simulator, Matt's grip) and the new `f2l_verify.py` into `rubix-cube/assets/`, made the verifier path-independent, and added a README explaining they exist to *confirm* source claims, not derive algs. These had been at risk in `/tmp` since lessons 10/12; now version-controlled. **Future sessions: use `assets/cube.py` + `assets/f2l_verify.py`, not `/tmp`.**

## Open threads

- Solve card still NOT changed — F2L replaces stages 2+3 only once all four slots are reliably buildable. Parallel rollout continues one more week.
- One case deliberately deferred to a final F2L lesson: **same-colour-up "hide and seek"** (corner and edge both showing the same colour on top, won't pair by a simple scoop) — sources flag it as the common beginner misfire. Also still owed: corner-in-slot / edge-in-slot reunion cases if Matt hits them.
- When all four slots build reliably → retire stages 2+3 on the solve card (merge into one F2L step) and re-bank. Mission unchanged; F2L is the active in-scope thread. Never push speedcubing.
