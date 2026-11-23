#!/usr/bin/env python3
"""Write one one-line joke about office life to /output/entry.txt.

Competition: u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a (make.fun)
Deterministic, no network, no randomness, no clock: every run writes
exactly the same bytes.
"""
import os
from pathlib import Path

LINE = (
    "Our fifteen-minute standup takes fourteen minutes of Dave "
    "explaining why his \u201cquick question\u201d needs a slide deck, "
    "a spreadsheet, and a second meeting."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
