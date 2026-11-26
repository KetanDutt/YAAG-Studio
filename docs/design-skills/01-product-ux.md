# Skill 01 — Product UX for a focused builder

## Principles distilled from NN/g

- Keep system state visible and respond promptly to a user's action.
- Use familiar language and recognizable patterns; avoid making people learn a bespoke control system.
- Give users control, an easy path out of mistakes, and reversible settings where possible.
- Prevent avoidable errors with bounds, defaults, constraints, and useful examples.
- Prefer recognition over recall: show options and labels in context.
- Keep the main task visually central; avoid decorative UI that competes with the work.
- Provide just-in-time help, not a long manual users must memorize.

## Applied to YAAG

- Grouped settings follow the work: basics → layout/content → visual finish → personal dates.
- A live preview is the main feedback loop; the page size and arrangement remain visible beside it.
- Calendar year is bounded to 1900–2100; event lines show an example format before entry.
- Controls use common radio groups, selects, checkboxes, and labeled fields.
- Import/export is explicit; reset has a confirmation. The current preview remains the source of truth.
- Expert options are present but visually grouped below the basic calendar choices.

## Quick review questions

1. Can someone tell what changed after touching a control?
2. Can they change their mind without rebuilding the calendar?
3. Are units and the expected event format stated next to the input?
4. Is the calendar itself still the visual focus?

## Source

Nielsen Norman Group, “10 Usability Heuristics for User Interface Design”: https://www.nngroup.com/articles/ten-usability-heuristics/