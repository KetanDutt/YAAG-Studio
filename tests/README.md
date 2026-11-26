# Tests

This project currently uses two complementary layers:

- `../scripts/check_project.py` runs repeatable static checks and an optional JavaScript syntax check.
- `../docs/QA_CHECKLIST.md` lists manual functional, accessibility, responsive, and physical-print scenarios.

No browser automation dependency is bundled. Before shipping any UI or calendar-date changes, run both layers and record the actual browser/printer proof in the release notes.