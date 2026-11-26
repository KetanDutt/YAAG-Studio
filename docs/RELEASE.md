# Release process

The app intentionally has no dependency installation or compilation step.

1. Update `VERSION` and `CHANGELOG.md`.
2. Run `python3 scripts/check_project.py`.
3. Complete relevant browser, accessibility, and print scenarios in `QA_CHECKLIST.md`.
4. Review `README.md`, `PRODUCT_SPEC.md`, and `KNOWN_LIMITATIONS.md` against actual behavior.
5. Create a clean archive that includes `index.html`, `README.md`, `VERSION`, `CHANGELOG.md`, `docs/`, `scripts/`, and `tests/`. Include the reference image only when sharing the documented design context; do not include user event data or exported settings.
6. Test opening the archived `index.html` offline and run a sample print/save-as-PDF.
7. Record browser versions and printer/paper details for any release-specific visual sign-off.

Do not describe the app as WCAG certified or guarantee print dimensions/colors without completed independent audits and physical proofs.

## No-CI Policy

**Never add GitHub Actions workflows (`.github/workflows/`) or CI pipelines to this project in the future.** All verification is run locally via `python scripts/check_project.py` and `python tests/test_calendar_core.py`.
