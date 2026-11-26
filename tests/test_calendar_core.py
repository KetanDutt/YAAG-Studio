"""Exercise pure date/color helpers extracted from the app's inline script."""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "index.html"
HELPERS = {"hexRgb", "hexColor", "lum", "readableAccent", "monthLength", "weekNumber", "parseEvents"}


def main() -> None:
    node = shutil.which("node")
    if not node:
        print("SKIP  core behavior tests require Node.js")
        return
    script_match = re.search(r"<script>(.*?)</script>", APP.read_text(encoding="utf-8"), re.S)
    if not script_match:
        raise SystemExit("inline app script not found")
    lines = script_match.group(1).splitlines()
    funcs = {line.split("(", 1)[0].split()[1] for line in lines if line.startswith("function ")}
    missing = HELPERS - funcs
    if missing:
        raise SystemExit("pure helper(s) not found in app: " + ", ".join(sorted(missing)))
    source = "\n".join(line for line in lines if line.startswith("function ") and line.split("(", 1)[0].split()[1] in HELPERS)
    tests = r"""
const assert = require('node:assert/strict');
assert.equal(monthLength(2024, 1), 29, 'leap February');
assert.equal(monthLength(2023, 1), 28, 'common February');
assert.equal(monthLength(2000, 1), 29, 'leap century');
assert.equal(monthLength(2100, 1), 28, 'non-leap century');
assert.equal(weekNumber(2027, 0, -3, 1), 1, 'Monday-first first displayed week');
assert.equal(weekNumber(2027, 0, -4, 0), 1, 'Sunday-first first displayed week');
const leap = parseEvents('02-29: Leap day\n02-30: Impossible\n1-1: New year', 2024);
assert.equal(leap.map['2-29'][0], 'Leap day');
assert.equal(leap.map['1-1'][0], 'New year');
assert.equal(leap.invalid, 1);
const common = parseEvents('02-29: Not this year', 2023);
assert.equal(common.invalid, 1, 'reject impossible date for selected year');
for (const c of ['#ffffff', '#f4d35e', '#436b5a', '#000000']) {
  const result = readableAccent(c);
  assert.ok(1.05 / (lum(result) + .05) >= 4.5, `${c} should yield readable text ${result}`);
}
console.log('PASS  calendar math, event validation, and accent contrast checks');
"""
    with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8") as temp:
        temp.write(source + "\n" + tests)
        temp.flush()
        result = subprocess.run([node, temp.name], text=True, capture_output=True)
    if result.returncode:
        print(result.stdout, end="")
        print(result.stderr, file=sys.stderr, end="")
        raise SystemExit(result.returncode)
    print(result.stdout.strip())


if __name__ == "__main__":
    main()
