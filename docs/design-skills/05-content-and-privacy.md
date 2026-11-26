# Skill 05 — Content clarity and local-first behavior

## Principles

- Use concrete labels and short instructions next to the decision they support.
- Show examples in the format users need to enter; explain print units and page terminology.
- Keep personal information private by default and explain what is saved.
- Make customization portable and let users retain control of their settings.
- Errors should point to a repair, not simply say something failed.

## Applied to YAAG

- Event entry accepts one `MM-DD: label` per line and shows examples in the placeholder and help copy.
- Calendar settings are saved in browser local storage; JSON export/import makes them portable. No calendar content is sent to a server.
- `Print / PDF` invokes the browser's own print/save-as-PDF flow.
- Errors in imported configuration are explained in plain language; reset asks for confirmation.
- Page size and layout names include common aliases, such as Tabloid / Ledger.

## Notes

- Local storage is browser/device-specific. Export a setup JSON when moving browsers or devices.
- Personal event labels are annotations only; they are not connected to holiday calendars or shared calendars.

## Source context

- NN/g usability heuristics: https://www.nngroup.com/articles/ten-usability-heuristics/
- W3C WCAG 2.2: https://www.w3.org/TR/WCAG22/