# QA and release checklist

## Automated static check

Run `python3 scripts/check_project.py` from the project root. If Node.js is installed, it also syntax-checks the extracted inline application script.

## Functional scenarios

- [ ] Fresh browser state starts on year 2027, A2 landscape, 4×3, Monday-first.
- [ ] Change year to a leap year (2024): February has 29 days; 2023 has 28.
- [ ] Change year to a common-year century (2100): February has 28 days; confirm upper/lower bounds are reflected back into the input.
- [ ] Toggle Monday/Sunday; verify mini-month positions and week-number labels.
- [ ] Switch month grid through all arrangements; confirm all twelve months appear once.
- [ ] Switch row-first/column-first on a multi-row month grid; check chronological reading order.
- [ ] Select 12×1 and 1×12; verify density hint and no overflow.
- [ ] Select Annual wall matrix: 12 month rows, day columns 1–31, correct weekday per real date, and blank dates after 28/29/30-day months.
- [ ] Check matrix weekend tint on/off; check events in valid matrix cells.
- [ ] Add valid events, malformed dates, impossible dates (for example 02-30), multiple labels for one date, and >50 lines; confirm accepted labels and warning status.
- [ ] Exercise palettes, custom hex/color picker, paper tones, line weights, date size, margin label, and all title/footer toggles.
- [ ] Toggle dark mode; reload; verify it persists and the printed calendar surface remains light.
- [ ] Export a setup, import it, and verify state. Try invalid/oversized JSON and confirm graceful handling.
- [ ] Reset defaults and confirm it returns to the initial configuration.

## Browser and accessibility smoke checks

- [ ] Test in current Chrome/Edge and Firefox; include Safari if available.
- [ ] Tab through controls; confirm focus is visible and radio/select actions are operable.
- [ ] Inspect labels with a screen reader or accessibility tree; confirm date cells have understandable names in matrix mode.
- [ ] Resize to a narrow viewport; confirm settings and preview remain reachable.
- [ ] Test high zoom and browser text zoom; check clipped controls and calendar title.
- [ ] Emulate `prefers-reduced-motion: reduce`; confirm smooth scrolling and transitions are suppressed.
- [ ] Check top-bar translucency with backdrop-filter supported and unsupported; text/action contrast must remain clear.
- [ ] Verify the opaque paper surface remains print-faithful in both builder light and dark modes.

## Print checks

- [ ] Print/save to PDF at A2 landscape in 100% scale; confirm one page, full year, no UI controls.
- [ ] Check A3 and A4 landscape and portrait; confirm the selected layout's proportions and legibility.
- [ ] Compare Annual wall matrix on A2 and A3; check label/date readability and open writing area.
- [ ] Confirm browser headers/footers are disabled and chosen paper is supported by the dialog/printer.
- [ ] Print one physical sample; evaluate faint lines, custom accent, and actual non-printable margins.

## Known test limitation

This project has no automated browser or visual-regression harness. The repository check validates structure and JavaScript syntax, not rendered layout, screen-reader behavior, browser-specific print engines, or physical output. Complete manual checks before a public production release.