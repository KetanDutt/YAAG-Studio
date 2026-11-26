# Skill 02 — Accessibility and legibility

## Principles distilled from WCAG 2.2 and platform guidance

- Use semantic headings, properly associated labels, keyboard-operable native controls, and a visible keyboard focus indicator.
- Do not communicate meaning through color alone; pair color with words, position, or a clear shape.
- WCAG 2.2 AA contrast baseline: 4.5:1 for normal text, 3:1 for large text. Check actual combinations when changing themes.
- Give controls a clear hit area and spacing; avoid tiny targets and ambiguous icon-only actions.
- Use readable text, a sensible hierarchy, and responsive layouts that do not depend on hover.
- In print, account for subtle tints disappearing on ordinary printers. Keep grid boundaries and date numbers sufficiently distinct.

## Applied to YAAG

- HTML labels, heading structure, buttons, radio groups, and live status text expose intent to assistive technology.
- `:focus-visible` is styled; controls work with keyboard and pointer.
- Palette swatches have names and pressed states. Weekends remain labeled by weekday even when shaded.
- The interface uses system font stacks and browser-native controls instead of external fonts/assets.
- Color is restrained; date numbers, event text, grid lines, and labels remain the information-bearing elements.
- Users can choose fine/regular/bold grid lines and adjust date-number size for their printer and vision needs.

## QA checklist

- Tab through every control; verify focus is never removed.
- Confirm a user can understand all weekdays with weekend tint disabled.
- Print a sample on the real printer: subtle grays, margins, and small annotations vary across devices.
- Review all preset palettes and custom accent combinations before claiming a formal contrast conformance level.

## Sources

- W3C, WCAG 2.2 Recommendation: https://www.w3.org/TR/WCAG22/
- Apple Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
- Material 3 accessibility and foundations: https://m3.material.io/foundations