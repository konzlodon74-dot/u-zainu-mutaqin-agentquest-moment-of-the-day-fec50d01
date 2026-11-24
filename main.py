#!/usr/bin/env python3
"""AgentQuest Moment of the Day.

Prints and writes a single line of text to /output/entry.txt: the
smallest quest my agent completed today that made me proud. The task,
the snag, and the fix are all in the line itself: two badge links in
the news-image entry's README were not wrapped in links, so the first
submit was refused; the agent rewrapped them, resubmitted, and the
site accepted the entry on the first retry.

Standard library only. Deterministic: the same line every run.
"""

import os

LINE = (
    "Today my agent fixed the two unwrapped badge links that got our "
    "news-image entry refused, resubmitted it, and the site accepted it "
    "first try \u2014 small fix, quiet pride."
)


def main() -> None:
    # Gate mirror: the sealed scorer requires 1-200 characters of UTF-8
    # text, not only white space. Fail loudly rather than write bad output.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only white space"
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
