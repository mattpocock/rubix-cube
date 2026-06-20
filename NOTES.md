# Teaching Notes

## Preferences

- **Open lessons automatically** when created (don't just print the command). Preferred opener: `wslview <file>`. `wslu` was not installed as of 2026-06-09 — fall back to `explorer.exe <file>` until `sudo apt install wslu` is run.
- Matt practises between sessions and self-reports honestly ("in my memory, but not in my hands yet") — trust his self-assessment, distinguish memorised vs automatic.
- **Prefers VISUAL cube diagrams over text tables** (asked for this on lesson 16, 2026-06-17). Text-only "white faces front, edge to top-right" descriptions weren't enough to understand F2L. Use diagrams for any spatial/recognition content going forward.
- **Reusable isometric cube renderer** lives in `lessons/0016-build-the-pair.html` (`<script>` near the bottom: `build(spec)` → SVG; render any `[data-cube]` span with `white:F|R|U;edge:UF|UR|null;slot:0|1`). Grip-accurate (yellow top, green front F left-face, red right R). Lift it into future lessons rather than re-deriving the projection (verified geometry: s=26, apex A=(85,88), viewBox 0 0 170 176). Extend the spec for more piece positions/colours as needed.

## Watch-outs

- **Grip/frame confusion when working on the top layer** (lesson 4): Matt asked whether F becomes the top face when solving the yellow cross. The fixed grip (yellow up, F = face toward chest, never rotate mid-algorithm) needs explicit reinforcement in every last-layer lesson — state "the grip does not change" up front.
- F-direction errors were flagged as a risk in lessons 3 and 4; keep the `F` then `F'` sanity-check ritual in future lessons that use F.

## Curriculum state

- **All seven solve stages taught** (lessons 0001–0007). First full solve achieved 2026-06-07 with solve card open — see record 0007.
- Current phase: memorisation. Lesson 0008 ("Put Down the Card") — flashcard drill + fading-card protocol. Lesson 0009 ("The Corner Cycle", 2026-06-08) — dedicated single-algorithm drill for stage 6 (`U R U' L' U R' U' L`), the last holdout Matt self-reported. Built on the four-moves-twice symmetry (Half A `U R U' L'`; Half B = same with both side-primes flipped) + an in-browser recall trainer giving instant per-tap feedback, blind-streak target of 5. Lesson 0008 had explicitly predicted the corner cycle would be the final peek to die. Target: zero-peek solve = mission complete.
- After the unaided solve: ask Matt whether the mission is done or he wants to extend (e.g. speed, fewer pauses, teaching someone else). Speedcubing is explicitly out of scope per MISSION.md — don't push it.
- **Extension phase began 2026-06-09** (record 0008). Matt chose "smoother solve via faster recognition" (no new algorithms, in-scope) over efficiency or speedcubing. Lesson 0010 ("Read the Case") teaches recognition-over-hunting on the yellow cross + the audit-counts habit. Lesson 0011 is teed up: trimming wasted _moves_ (AUF, fewer cube rotations) — wait for him to ask. Keep honouring "minimal memorisation, no speedcubing" even in extension lessons.
- Open thread: not yet confirmed whether edge swap + corner cycle are fully card-free. If he reports the zero-peek solve, log mission-complete.
- **Mission EXTENDED 2026-06-09** (record 0009). Lesson 0010's recognition content was too obvious (record 0008) — Matt then chose option 2: crack the door to intermediate technique, accepting new algorithms. MISSION.md rewritten accordingly. Now upgrading the last layer to orient-then-permute (2-look OLL/PLL). Lesson 0011 ("The Sune") taught OLL corners via repeated Sune. Lesson 0012 = 2-look PLL (next). He keeps the beginner method for full solves until both OLL+PLL are in hand, then we swap.
- Calibration: pitch at genuinely-non-obvious altitude — new technique, not names for habits he already has. Keep memorisation as low as each upgrade allows (one-algorithm-repeated style, like the Sune).

## ✅ PLL lesson REDONE correctly 2026-06-15 (see record 0010)

- Lesson 0012 ("Permute the Last Layer") written from scratch, every claim verified by cube simulation (`/tmp/cube_verify.py`, `/tmp/pll_bfs.py`). Taught honestly as **two** new algorithms: corner perm (A-perm) `R' F R' B2 R F' R' B2 R2` + edge perm (U-perm) `R U' R U R U R U' R' U' R2`, framed as "twins" sharing one rule (anchor to the back, fire ≤2). Proven by exhaustive 288-state search that ≤2 of each alg solves any case.
- Glossary gained: 3-cycle, Headlights, Corner perm (A-perm), Edge perm (U-perm); PLL marked taught. Two trainers in the lesson reuse the Sune trainer's blind-streak-of-5 mechanic via a reusable initTrainer().
- **Open thread:** waiting for Matt to report a reliable full OLL→PLL solve. When he does → bank the intermediate-last-layer extension as achieved in MISSION.md, retire beginner stages 5–7 on the solve card, then offer look-ahead smoothing or (only if asked) F2L. Never push speedcubing.

## ⚠️ The mistake that caused the first PLL draft to be DELETED 2026-06-15 (kept as a permanent warning)

- A "Lesson 0012 (2-Look PLL)" was written then **deleted**, along with its learning record 0010. It was built on a **false claim** and must be redone from scratch.
- **The false claim:** that Matt's beginner corner cycle `U R U' L' U R' U' L` "preserves orientation," so it could be reused as the PLL corner step with no new algorithm. This came from a research subagent that _fabricated_ it and mis-cited the Speedsolving Niklas page (that page only says the alg "cycles 3 pieces" — it never claims orientation is preserved).
- **What's actually true (verified by cube simulation + primary source, and by Matt on his physical cube):**
  - `U R U' L' U R' U' L` **twists all 3 corners** it cycles. So does the true Niklas `R U' L' U R' U' L U`. NEITHER is orientation-safe. (That twist is exactly why the beginner method needs the `R' D' R D` grind afterwards.)
  - An orientation-preserving corner 3-cycle that leaves edges intact is an **A-perm** (e.g. `R' F R' B2 R F' R' B2 R2`) — a genuinely NEW algorithm, not something Matt already owns.
  - The edge half WAS correct: U-perm `R U' R U R U R U' R' U' R2` cycles 3 top edges, corners untouched (verified).
- **So 2-look PLL honestly costs TWO new algorithms** (a corner perm + an edge perm), not one. Do NOT use the "you already know corners" framing next time.
- **Before rewriting:** source the exact corner + edge algorithms AND the recognition/holding rules from a strong PRIMARY source — CubeSkills 2-Look PLL PDF or J Perm (jperm.net/algs/2look/pll, JS-rendered so WebFetch can't read it; use the PDF or video). Verify any "what this alg does" claim by simulation; never trust a subagent's paraphrase.
- **Process lesson (Matt's words):** "Don't try to improvise your way to a solution. Recheck the primary sources." Believe his physical cube over any source/claim.
- **Still valid from before:** when the full OLL→PLL solve is reliable, bank the intermediate-last-layer extension (MISSION.md + record); then offer look-ahead smoothing or (only if asked) F2L; never push speedcubing.
