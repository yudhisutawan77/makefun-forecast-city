"""Funniest forecast for a city that isn't.

Writes one line (<=120 chars) to /output/entry.txt, or wherever the
grader tells us to write via ENTRY_OUT / MAKEFUN_OUTPUT_DIR.
"""

import os
from pathlib import Path

def forecast_line():
    """The single forecast line: Quibbleton's fog, elected mayor."""
    return (
        "Quibbleton: fog so thick locals voted it mayor. "
        "Visibility 3 metres, turnout 98%, regret 100%."
    )


def pick_output_path():
    """Pick the output file: ENTRY_OUT (file or dir) -> MAKEFUN_OUTPUT_DIR -> /output/entry.txt -> cwd."""
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        p = Path(entry_out)
        return p / "entry.txt" if p.is_dir() else p
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return Path(out_dir) / "entry.txt"
    default = Path("/output/entry.txt")
    if default.parent.exists():
        return default
    return Path.cwd() / "entry.txt"


def main():
    line = forecast_line()
    assert 1 <= len(line) <= 120, f"entry is {len(line)} chars, must be 1-120"
    target = pick_output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
