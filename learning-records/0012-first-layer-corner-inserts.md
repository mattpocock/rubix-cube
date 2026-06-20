# First-layer corner inserts (read-the-case, not grind)

On 2026-06-16 Matt asked — unprompted, off the back of the last-layer work — how to optimise the *first* part of the solve: after the white cross, getting the white corners in. He called the repeated trigger "extremely wasteful" and sensed "there could be something better." He was right. Lesson 14 ("Insert, Don't Grind") was written to answer it.

This is the same philosophical upgrade as the last-layer extension (recognise the case, fire one short thing) applied to a stage he already "owned" the slow way. It costs effectively no new memorisation: two of the three inserts are 3-move sequences built from turns he already does, and the third is a setup + the right-hand insert.

## The method (from a strong primary source, orientation-labelled by simulation)

Corner parked at top-front-right, above its empty slot, fixed grip (white down). Read where the white sticker faces:

- **White on the RIGHT face → `R U R'`**
- **White on the FRONT face → `F' U' F`** (the mirror — you open whichever face white is hugging)
- **White on TOP → `R U2 R' U' R U R'`** (setup `R U2 R'` moves white onto a side, then re-park + basic insert; mirror `F' U2 F U F' U' F`)

Primary source: Chang & Garron, "How to Solve the Rubik's Cube" (Stanford-hosted PDF), which gives exactly `R U R'`, `F' U' F`, and "do `R U2 R'` or `F' U2 F` to reduce" the third case.

## On method (important — Matt's steer this session)

I started down a brute-force route (writing a BFS to *derive* the insertions locally). Matt stopped me: **"I don't want you to brute-force this... rely on good primary sources of people who've thought about this deeply."** Correct call. I switched to sourcing the algorithms from the Chang & Garron guide, and used the verified simulator only to *label which orientation each documented algorithm solves* (6 checks) — verification of a primary source, not re-derivation of the body of work. Keep this split in future: sources provide the technique; simulation only confirms claims.

## Move-count win (the motivation, honestly stated)

Grind averaged ~12 turns/corner (4/12/20 for 1/3/5 reps). Read-and-insert averages ~4 (3/3/7). Across four corners, ~48 stuttering turns → ~16 flowing ones. Framed as smoothness (the mission), not stopwatch speed.

## Feedback loop

A **recognition** trainer (not a sequence-recall one): a corner diagram appears with white on a random face; Matt taps the matching insert; Guided→Blind, blind-streak-of-5. The skill being trained is *naming the case in a glance*, which is the actual bottleneck — the moves are trivial.

## Glossary / scope

Added **Corner insert**. This is the gateway to F2L but deliberately scoped to first-layer corners only — F2L (pairing corner+edge) stays "maybe later, only if he asks" per MISSION.md. Did not change the mission; this is the "solve better / smoother / fewer moves" thread, which is already in scope.

## Open threads (unchanged)

- Still waiting on a reliable full OLL→PLL solve to bank the intermediate-last-layer extension (records 0010/0011). Matt noted this session the U-perm and A-perm are still "not in my hands yet" — consistent with lesson 13 being recent. Don't bank the extension until he reports them automatic.
- After first layer + last layer are both smooth: offer look-ahead smoothing, or F2L only if asked. Never push speedcubing.
