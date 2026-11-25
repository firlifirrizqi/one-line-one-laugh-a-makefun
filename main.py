"""One Line, One Laugh — Make.fun entry.

Writes the selected one-liner to /output/entry.txt.

The line (99 characters, UTF-8, single line, self-contained):

    I proved I'm not a robot by clicking every traffic light, and now
    the robots think I'm one of them.

Why this line: the CAPTCHA test exists to prove you are human, and the
twist flips it — passing the test so thoroughly that the robots claim
you as one of their own. One setup, one reversal, nothing to trim.
"""

import os

LINE = (
    "I proved I'm not a robot by clicking every traffic light, "
    "and now the robots think I'm one of them."
)


def check_line(line: str) -> bool:
    """Validate the chosen line itself before anything is written."""
    if not 1 <= len(line) <= 140:
        print(f"  [FAIL] line is {len(line)} chars, must be 1-140")
        return False
    if not line.strip():
        print("  [FAIL] line is only whitespace")
        return False
    print(f"  [OK] line is {len(line)} chars, within the 1-140 gate")
    return True


def verify() -> bool:
    """Check the written file against the competition gate.

    Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
    not only white space. Returns True only if every check passes.
    """
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    checks = {
        "utf-8 decodes": True,
        "1-140 chars": 1 <= len(text) <= 140,
        "not only whitespace": bool(text.strip()),
        "single line": "\n" not in text,
        "read-back byte-identical": raw == LINE.encode("utf-8"),
    }
    for name, ok in checks.items():
        print(f"  [{'OK' if ok else 'FAIL'}] {name}")
    print(f"  length: {len(text)} chars, {len(raw)} bytes")
    return all(checks.values())


def main() -> None:
    if not check_line(LINE):
        raise SystemExit("line check FAILED")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote /output/entry.txt ({len(LINE)} chars)")
    print("verifying:")
    if not verify():
        raise SystemExit("gate check FAILED")
    print("gate check PASSED")


if __name__ == "__main__":
    main()
