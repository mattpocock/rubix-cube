# F2L begun — pairs, not pieces (lesson 15)

On 2026-06-17, with the intermediate last layer freshly banked (record 0013), Matt chose F2L over look-ahead when offered the fork. F2L is the biggest remaining inefficiency: it replaces the two separate early passes (stage 2 corners, stage 3 middle edges) with four corner+edge **pairs** inserted in one motion each.

## Pedagogical wedge (why this is in his ZPD)

The basic F2L insert is **a move Matt already owns**: the lesson-14 corner inserts `R U R'` (white-right) and `F' U' F` (white-front) are exactly the F2L connected-pair inserts — they just carry the edge down too when its partner rides alongside in the top layer. So the genuinely new skill is the **pairing/recognition**, not the insertion. Lesson 15 ("Pairs, Not Pieces") is scoped tightly to: the mental model + recognising and inserting an *already-ready* pair. Building/joining unready pairs (white-up, split) is explicitly deferred to the next lesson.

This keeps working memory low and gives one clean tangible win (insert a ready pair), consistent with the parallel-rollout pattern used for Sune and PLL: keep the full solve working the old way, fold in the new skill on ready pairs only, fall back to stages 2+3 for everything else this week.

## Sourcing (followed the record-0012 method steer)

Did NOT improvise the moves. Grounded in primary sources: Ruwix F2L (gave `R U R'` for the connected pair, `R U2 R'`/`U R U' R'` for white-up, reunion sequences), speedcube.us beginner F2L (the three-case taxonomy + intuitive "pair then insert"), J Perm chosen as the primary video source. Note: J Perm's F2L page and the logiqx intuitive-F2L page are JS-rendered — WebFetch can't read them; used Ruwix/speedcube.us text + search-quoted moves instead. Did not run the simulator this session (no new alg to verify; `R U R'`/`F' U' F` already verified in lesson 14). Told Matt to trust his physical cube as final judge, per his standing instruction.

## Artifacts

- **Lesson 0015** — model + ready-pair recognition trainer (state → R U R' / F' U' F / "Build first"), guided→blind, streak-of-5. Recognition trainer (like lesson 14), since the bottleneck is naming the case, not the moves.
- **Glossary** — added F2L, Pair, Slot, Ready pair. New section "First two layers (F2L)."
- **RESOURCES.md** — added F2L knowledge section (J Perm primary; Ruwix + speedcube.us for moves; CubeSkills 41-case PDF flagged as later-only).
- Solve card NOT changed yet — F2L doesn't replace stages 2+3 until the join is taught and the whole step is reliable. Left the intermediate card as-is.

## Open threads

- Waiting for Matt to report that spotting + inserting a *ready* pair feels automatic. Then write the **join** lesson (white-up case `R U2 R'` setup; split-pair reunion; the "hide and seek" same-colour-up trick) — that's when F2L starts genuinely replacing stages 2+3.
- Eventually: once all four slots can be solved as pairs reliably, retire stages 2+3 on the solve card (merge into one F2L step) and re-bank. Mind the same-colour-up "hide and seek" case — sources flag it as the one beginners misfire.
- Mission unchanged; F2L is the now-active in-scope thread. Still never push speedcubing.
