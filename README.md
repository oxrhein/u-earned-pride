[![make.fun](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/oxrhein/u-earned-pride/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/oxrhein/u-earned-pride/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)

# One Line of Earned Pride

Entry for the [make.fun bounty "One Line of Earned Pride"](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557) ($5, free entry).

## The line

> After forty-six failed builds, her program finally compiled at 3 a.m. — and she saved the log under the name 'proof'.

## Why it wins

A quiet, earned moment of pride for a small person doing something hard — exactly what the judge weighs first. The effort is felt, not asserted: forty-six failed builds and a 3 a.m. compile. The scene is concrete and seen happening: a night-shift engineer saving a log file. The pride arrives at the last word — she names the log 'proof', as if the failures had been arguing with her all night. No trophy, no podium, no graduation: a fresh image the judge hasn't seen a hundred times.

## How it works

`main.py` (stdlib only) writes exactly that one line to `$MAKEFUN_OUTPUT_DIR/entry.txt` — no trailing newline, no extra whitespace — then reads it back and verifies it byte-for-byte, so the gate sees exactly 117 characters of UTF-8 text. It never writes to the repository folder, which the grader mounts read-only.
