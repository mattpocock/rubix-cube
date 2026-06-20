# Verification assets

Tooling used to *confirm* algorithm claims from primary sources before they go into a lesson
(never to derive algorithms — per the method steer in learning-record 0012).

- **`cube.py`** — a faithful 54-sticker 3×3 simulator. Grip matches Matt's: white = D (bottom),
  yellow = U (top), green front, red right, blue back, orange left. Run `python3 cube.py` for sanity checks.
- **`f2l_verify.py`** — checks each candidate F2L sequence by applying its inverse to a solved cube,
  confirming it disturbs **only** the front-right (FR) slot + top layer (never the rest of the first
  two layers), and reading off which case it solves. Run `python3 f2l_verify.py`.

Used for lessons 12 (PLL) and 15–16 (F2L). Rescued from ephemeral `/tmp` on 2026-06-17.
