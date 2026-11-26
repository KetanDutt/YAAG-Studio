#!/usr/bin/env python3
"""Dependency-free sanity check for the YAAG Studio single-file app."""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "index.html"


class AuditParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.duplicate_ids: set[str] = set()
        self.external_assets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        props = dict(attrs)
        ident = props.get("id")
        if ident:
            if ident in self.ids:
                self.duplicate_ids.add(ident)
            self.ids.append(ident)
        if tag == "script" and props.get("src"):
            self.external_assets.append(f"script src={props['src']}")
        if tag == "link" and props.get("href", "").startswith(("http://", "https://")):
            self.external_assets.append(f"link href={props['href']}")
        if tag in {"img", "iframe", "audio", "video"} and (props.get("src") or "").startswith(("http://", "https://")):
            self.external_assets.append(f"{tag} src={props['src']}")


def fail(message: str) -> None:
    print(f"FAIL  {message}")
    raise SystemExit(1)


def main() -> None:
    if not APP.is_file():
        fail("index.html is missing")
    html = APP.read_text(encoding="utf-8")
    parser = AuditParser()
    parser.feed(html)
    parser.close()
    if parser.duplicate_ids:
        fail("duplicate HTML IDs: " + ", ".join(sorted(parser.duplicate_ids)))
    print(f"PASS  HTML parsed ({len(parser.ids)} unique IDs)")

    if parser.external_assets:
        fail("unexpected external runtime assets: " + ", ".join(parser.external_assets))
    if re.search(r"url\(\s*['\"]?https?://", html, flags=re.I):
        fail("external CSS URL found; app should work offline")
    print("PASS  no external runtime assets found")

    script_match = re.search(r"<script>(.*?)</script>", html, flags=re.S)
    if not script_match:
        fail("inline application script missing")
    script = script_match.group(1)
    ids = set(parser.ids)
    referenced = set(re.findall(r"\$\(['\"]([^'\"]+)['\"]\)", script))
    missing = referenced - ids
    if missing:
        fail("script references missing element IDs: " + ", ".join(sorted(missing)))
    print("PASS  direct DOM ID references resolve")

    required = [
        'id="darkModeBtn"', 'value="matrix"', 'id="eventStatus"',
        'data-layout="matrix"', 'id="dynamicPage"', '@media print',
        'localStorage', 'function weekNumber', 'function parseEvents',
        'function importSettings', 'function downloadSettings', 'function renderLayoutThumbs',
        'prefers-reduced-motion:reduce', 'backdrop-filter:blur(16px)', '--accent-ink',
    ]
    missing_features = [token for token in required if token not in html]
    if missing_features:
        fail("required feature/hooks missing: " + ", ".join(missing_features))
    print("PASS  expected builder, calendar, and print hooks present")

    node = shutil.which("node")
    if node:
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8") as temp:
            temp.write(script)
            temp.flush()
            result = subprocess.run([node, "--check", temp.name], text=True, capture_output=True)
        if result.returncode:
            fail("JavaScript syntax check failed:\n" + result.stderr.strip())
        print("PASS  JavaScript syntax (Node.js)")
    else:
        print("SKIP  Node.js not installed; JavaScript syntax was not checked")

    core_test = subprocess.run([sys.executable, str(ROOT / "tests" / "test_calendar_core.py")], text=True, capture_output=True)
    if core_test.returncode:
        fail("calendar core tests failed:\\n" + core_test.stdout + core_test.stderr)
    print(core_test.stdout.strip() or "PASS  calendar core tests")

    required_docs = [
        "README.md", "VERSION", "CHANGELOG.md", "docs/PRODUCT_SPEC.md",
        "docs/ARCHITECTURE.md", "docs/QA_CHECKLIST.md", "docs/ACCESSIBILITY.md",
        "docs/PRIVACY_SECURITY.md", "docs/KNOWN_LIMITATIONS.md", "docs/RELEASE.md",
        "docs/UI_AUDIT.md", "docs/DESIGN_SYSTEM.md", "docs/UNSLOP_ADAPTATION.md",
        "docs/design-skills/README.md", "tests/README.md", "tests/test_calendar_core.py",
    ]
    absent = [path for path in required_docs if not (ROOT / path).is_file()]
    if absent:
        fail("project documentation missing: " + ", ".join(absent))
    print("PASS  project documentation present")
    print("NOTE  static checks do not replace browser, accessibility, or print proofing")


if __name__ == "__main__":
    main()
