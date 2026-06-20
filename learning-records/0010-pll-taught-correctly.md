# PLL taught — correctly, on the second attempt

On 2026-06-15 Lesson 0012 ("Permute the Last Layer") was written, replacing the deleted first draft (see the NOTES.md warning of the same date). This record captures the corrected, verified facts so the mistake can never recur.

## What was wrong before

The deleted draft claimed Matt's beginner corner cycle `U R U' L' U R' U' L` "preserves orientation" and could be reused as the PLL corner step — so PLL would cost only one new algorithm. That claim was fabricated by a research subagent and is false.

## What is true (independently verified this session by cube simulation)

A facelet cube simulator (`/tmp/cube_verify.py`, `/tmp/pll_bfs.py`) was written and sanity-checked (move·inverse = identity; trigger×6 = identity), then used to verify every claim:

- **Beginner corner cycle `U R U' L' U R' U' L` TWISTS corners** — top is no longer all-yellow afterwards. NOT orientation-safe. Same for the true Niklas. Confirms it cannot be the PLL corner step.
- **Corner perm (A-perm) `R' F R' B2 R F' R' B2 R2`**: clean 3-cycle of corners (UBL→UBR→UFR, front-left fixed), top stays all-yellow (orientation preserved), edges untouched.
- **Edge perm (U-perm) `R U' R U R U R U' R' U' R2`**: clean 3-cycle of edges (front→right→left, back edge fixed), corners untouched, orientation preserved. (Matches J Perm's Ua.)
- **Exhaustive search over all 288 PLL states**: every corner case solvable with **≤2 A-perms**, every edge case with **≤2 U-perms**, every full state solvable with these two algs + AUF. So the "fire each at most twice" guarantee is proven, not asserted.
- **Recognition geometry** (verified for these exact variants): corner anchor = headlights held at the **back**; edge anchor = solved edge held at the **back**. Diagonal/H/Z cases (no anchor) → fire once to create an anchor, re-aim, fire again.

## So: 2-look PLL honestly costs TWO new algorithms

A corner perm + an edge perm. The lesson says so plainly and frames them as "twins" sharing one rule (anchor to the back, ≤2 fires) to keep the cognitive load down — the minimal-memorisation spirit, without lying about the count.

## Process lesson banked (Matt's words)

"Don't try to improvise your way to a solution. Recheck the primary sources." Every "what this alg does" claim is now verified by simulation before teaching, and the lesson footer says so. Believe the physical cube over any source.

## State of the mission

- The full intermediate last layer is now taught: OLL (lessons 4 + 11) → PLL (lesson 12). Four looks replace beginner stages 5–7.
- Matt keeps the beginner method for full solves until OLL → PLL is reliable, then we retire stages 5–7 and update the solve card.

## Next

- Wait for Matt to report the full OLL → PLL solve is reliable. Then: bank the intermediate-last-layer extension (MISSION.md says the upgrade is in scope; mark it achieved), rebuild/trim the solve card to the four-look last layer, and offer look-ahead smoothing or — only if he asks — F2L. Never push speedcubing.
