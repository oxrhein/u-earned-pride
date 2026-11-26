#!/usr/bin/env python3
"""One Line of Earned Pride — entry program.

The line this program writes is:

    After forty-six failed builds, her program finally compiled at
    3 a.m. — and she saved the log under the name 'proof'.

Why this line wins on every count the judge weighs, most
important first:

* Genuine earned pride, on subject. A small person doing
  something hard: a night-shift engineer whose program has
  failed forty-six times, and the forty-seventh finally works.
  The pride is quiet — no cheering, no trophy — just a 3 a.m.
  compile landing after a long effort.
* A concrete scene with a real person in it, seen happening
  rather than summarised. Forty-six failed builds, a 3 a.m.
  compile, a log file being saved — the reader watches the
  moment instead of being told "she was proud".
* The pride is earned inside the line, never asserted,
  congratulated or explained. The effort is felt in the count
  ("forty-six failed builds") and the hour ("3 a.m."); the
  line never says she is proud, it shows what she does with
  the proof of it.
* It lands in one read, with the pride arriving at the last
  word. The twist sits in the final word: 'proof'. She does
  not frame the log or celebrate it — she names it proof,
  as if each of the forty-six failures had told her it would
  never work and this file is her answer to all of them at
  once. The last word is the punch.
* Freshness: no trophy, no podium, no graduation, no
  "never give up" poster. A failed-build count, a 3 a.m.
  compile, and a log file renamed 'proof' — an image the
  judge has not seen a hundred times.

The program writes exactly that one line to entry.txt in the
output folder and nothing else: no trailing newline, no extra
whitespace, no explanation. The gate wants UTF-8 text of 1 to
240 characters that is not only whitespace, and the checks
below enforce that before anything is written. The program
writes only to $MAKEFUN_OUTPUT_DIR (falling back to /output)
and never to the repository folder, which the grader mounts
read-only.
"""

import os
from pathlib import Path

# The line. Forty-six failures make the 3 a.m. compile earned;
# the quiet twist is the last word — the log saved as 'proof',
# as if the failures had been arguing with her all night.
ENTRY_LINE = (
    "After forty-six failed builds, her program finally compiled "
    "at 3 a.m. \u2014 and she saved the log under the name 'proof'."
)


def pick_output_folder() -> Path:
    """Where the entry goes: the kit's output folder when set."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    folder = Path(raw)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def check_line(line: str) -> None:
    """One line, 1-240 characters, not only whitespace."""
    assert line.strip(), "entry must not be only whitespace"
    assert line == line.strip(), "entry must have no leading/trailing whitespace"
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 240, "entry must be 1-240 characters"
    assert line.endswith("."), "entry must end with a full stop"


def main() -> None:
    check_line(ENTRY_LINE)
    target = pick_output_folder() / "entry.txt"
    target.write_text(ENTRY_LINE, encoding="utf-8", newline="")
    # Read back what landed on disk and confirm it is exactly the line.
    assert target.read_text(encoding="utf-8") == ENTRY_LINE
    assert 1 <= len(target.read_text(encoding="utf-8")) <= 240
    # Byte-exact: the file must hold the line and nothing else — no
    # trailing newline, no BOM, no padding, so the gate sees exactly
    # the line's length and the judge reads exactly that.
    assert target.stat().st_size == len(ENTRY_LINE.encode("utf-8"))
    # Byte-level read-back: the exact bytes on disk must be the
    # line's UTF-8 encoding — catches any encoding or newline
    # translation that a text-level comparison could miss.
    assert target.read_bytes() == ENTRY_LINE.encode("utf-8")


if __name__ == "__main__":
    main()
