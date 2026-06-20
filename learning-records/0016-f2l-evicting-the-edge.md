# F2L part 3 — bringing the edge up (lesson 17)

On 2026-06-17 Matt said lessons 15–16 were clear, but asked: "how do I bring the edge up?" Exactly the right gap. Lessons 15–16 both *assume the edge is already in the top layer* (every diagram shows the edge at UF/UR). On a real scramble the partner edge is usually **trapped in the middle row** — in the correct slot but flipped, or in a wrong slot. Nothing yet taught the extraction step. Lesson 17 ("Bring the Edge Up") closes it.

## What it teaches (one new beat only)

The "workbench rule": you can only build a pair in the top layer, so step zero of every slot is a recognition — **is my edge up top, or trapped?**

- **Up top** → already a Lesson-16 case, scoop it.
- **Trapped** → evict first: rotate the slot to front-right, fire **`R U R'`** once. The edge lands in the top layer, white cross untouched.

Key minimal-memorisation wedge (same spirit as the whole F2L thread): the eviction move is the **same `R U R'` he already owns** — no new algorithm, just a new *use* (evict, not insert). And it's not surgical: if the corner is jammed in the slot too, the same `R U R'` lifts both pieces out at once, so there's never a need for an "edge-only" trick.

Trainer: binary recognition (Up top → pair / Trapped → R U R'), guided→blind, streak-of-5, same engine as lessons 14–16.

## Sourcing + verification (followed the record-0012 steer)

Technique grounded in J Perm (the chosen F2L primary — pulling a piece out of a slot with a trigger before re-pairing) + Ruwix. Used the simulator only to **confirm**, never derive:
- `R U R'` on a solved FR slot lifts corner→UFL and edge→UF, cross intact.
- `R U R'` on a **flipped** FR edge lifts it to UF, cross intact.
- (Survey of `R U' R'`, `R U2 R'`, `F' U F`, `F' U' F` confirmed they all lift the FR edge to the top without breaking the cross — chose `R U R'` for continuity with lesson 16.)

## Assets — renderer lifted to a shared component

Per the workspace reuse rule (the isometric cube renderer was about to be inlined in a 3rd lesson), I extracted it from lesson 16 into **`assets/cube-render.js`** and linked it from lesson 17 via `<script src>`. Extended the spec with **`trap:edge`** (draws the partner edge wedged in the front-right slot's middle row, corner spot dashed) and a `corner:0` toggle. Lesson 16 keeps its own inline copy (not refactored — no need to touch a banked lesson); lesson 17 onward should link the asset.

## Open threads

- Solve card STILL unchanged — parallel rollout continues. Now Matt can build *any* slot (free the edge → pair → insert), so the trigger to retire stages 2+3 is close: when all four slots feel reliable end-to-end, retire them on the solve card (merge into one F2L step) and re-bank.
- Still deferred to a final F2L lesson: the **same-colour-up "hide and seek"** case (corner + edge showing the same colour on top, won't pair by a simple scoop). Take it last.
- Mission unchanged; F2L is the active in-scope thread. Never push speedcubing.
