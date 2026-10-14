#!/usr/bin/env python3
"""Scan the public-source snapshot for secret-shaped strings; mask all matches."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
PATTERNS = {
    "live payment key": re.compile(rb"\b(?:sk|pk|dpk|dpay)[_-](?:live|prod)[_-][A-Za-z0-9]{16,}\b", re.IGNORECASE),
    "AWS access key": re.compile(rb"\bAKIA[0-9A-Z]{16}\b"),
    "bearer token": re.compile(rb"(?i)\bBearer\s+([A-Za-z0-9._~-]{32,})"),
}


def masked(value: bytes) -> str:
    text = value.decode("ascii", errors="replace")
    if len(text) <= 12:
        return "[masked]"
    return f"{text[:6]}…{text[-4:]} (len={len(text)})"


def main() -> int:
    found = 0
    for path in sorted(CONTENT.rglob("*.md")):
        for line_number, line in enumerate(path.read_bytes().splitlines(), 1):
            for label, pattern in PATTERNS.items():
                for match in pattern.finditer(line):
                    token = match.group(1) if label == "bearer token" else match.group(0)
                    safe_line = pattern.sub(lambda m: (b"Bearer " if label == "bearer token" else b"") + b"[MASKED]", line)
                    print(f"{path.relative_to(ROOT)}:{line_number}: {label}: {masked(token)} | "
                          f"{safe_line.decode('utf-8', errors='replace')[:180]}")
                    found += 1
    print(f"Secret-shaped matches: {found} (review before publication; raw values were not printed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
