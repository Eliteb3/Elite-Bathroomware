#!/usr/bin/env python3
"""Check Elite radio scripts against the house rules.

Input: a text file of scripts, each starting with a header line
    ### <name> (<seconds>s)
followed by the script body. Speaker labels like "VO:" are ignored in counts.

Usage: python3 script_check.py scripts.txt
Exit code 1 if any script fails.
"""
import re
import sys

# spoken words, excluding SFX / MUSIC / JINGLE lines
BUDGET = {10: 25, 15: 35, 20: 50, 30: 75, 45: 110}
WPS = 2.6  # NZME two-hander pace; jingle + SFX add ~6s on top

BANNED = [
    "huge range", "one-stop shop", "one stop shop", "look no further",
    "whatever your style", "whatever your budget", "every budget",
    "something for everyone", "all under one roof", "new year, new bathroom",
    "new year new bathroom", "new year's resolution", "new years resolution",
    "unique designs", "dream bathroom", "don't miss out", "hurry in",
    "amazing deals", "unbeatable", "cheapest", "won't find anywhere else",
    "won't find just anywhere", "got you covered",
]
OUT_OF_SCOPE = ["code interiors", "eliteoutlet", "elite outlet", "clearance", "seconds"]
PRICE = re.compile(r"(\$\s?\d|\d+\s?%|per ?cent|percent|\bsale\b|\boff\b)", re.I)
SPEAKER = re.compile(r"^\s*(VO|Voice \d+|V\d|SFX|MUSIC)\s*[:\-–]\s*", re.I | re.M)


def check(name, secs, body):
    issues, warns = [], []
    spoken = "\n".join(
        l for l in body.splitlines() if not re.match(r"^\s*(SFX|MUSIC|JINGLE)\b", l, re.I)
    )
    spoken = SPEAKER.sub("", spoken)
    words = len(re.findall(r"[A-Za-zĀāĒēĪīŌōŪū0-9'’]+", spoken))
    low = spoken.lower()

    budget = BUDGET.get(secs)
    if budget and words > budget:
        issues.append(f"{words} words — over the {budget}-word budget for {secs}s")
    for p in BANNED:
        if p in low:
            issues.append(f'banned phrase: "{p}"')
    for p in OUT_OF_SCOPE:
        if re.search(r"\b" + re.escape(p) + r"\b", low):
            issues.append(f'out of scope for Elite radio: "{p}"')
    if re.search(r"\b59\b(?!\s*a\b)", low):
        issues.append('address says "59" — must be 59A')
    if re.search(r"tamaki", low):
        issues.append('"Tamaki" missing macron — write Tāmaki')
    if "59a" in low.replace(" ", "") and "tāmaki" not in low:
        warns.append("address given without East Tāmaki")
    if "elite bathroomware" not in low:
        issues.append("brand name 'Elite Bathroomware' not said")
    full = body.lower()
    jingle = [l for l in body.splitlines() if re.match(r"^\s*JINGLE\b", l, re.I)]
    if not jingle:
        issues.append('no JINGLE line — "Speak to Elite. We make bathrooms simple."')
    elif "we make bathrooms simple" not in jingle[0].lower():
        issues.append('jingle must read "Speak to Elite. We make bathrooms simple."')
    if "big blue store" not in full:
        issues.append('"The big blue store" missing from sign-off')
    first = next((l for l in body.splitlines() if l.strip()), "").lower()
    if "bathrooms simple" in first or "bathrooms made simple" in first:
        issues.append('"bathrooms made simple" used as an opener — it closes the spot')
    if not (re.search(r"hear that\?", low) or re.search(r"zone", low)):
        warns.append('not in an NZME frame — no "Hear that?" or Zone opener')
    if PRICE.search(spoken):
        warns.append("price/discount language found — sale phase only, Dean sign-off needed")
    brands = [b for b in ["methven", "caroma", "plumbline", "greens", "voda", "grohe",
                          "hansgrohe", "pavia", "buddy"] if b in low]
    if len(brands) > 1:
        issues.append(f"brand list ({', '.join(brands)}) — one brand max per spot")
    return words, issues, warns


def main(path):
    text = open(path, encoding="utf-8").read()
    blocks = re.split(r"^###\s*", text, flags=re.M)[1:]
    if not blocks:
        sys.exit("No scripts found — each must start with '### <name> (<n>s)'")
    failed = False
    for b in blocks:
        head, _, body = b.partition("\n")
        m = re.search(r"\((\d+)\s*s\)", head)
        secs = int(m.group(1)) if m else None
        words, issues, warns = check(head.strip(), secs, body)
        est = words / WPS
        status = "FAIL" if issues else "PASS"
        failed |= bool(issues)
        print(f"[{status}] {head.strip()} — {words} words, ~{est:.0f}s read")
        for i in issues:
            print(f"   ✗ {i}")
        for w in warns:
            print(f"   ! {w}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
