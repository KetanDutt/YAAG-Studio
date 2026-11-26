# Skill 03 — Visual hierarchy and design systems

## Principles distilled from Apple HIG and Material 3

- Establish hierarchy with scale, weight, spacing, and alignment before adding decoration.
- Treat type, color, shape, and spacing as a coherent system rather than independent one-off choices.
- Use color intentionally: one principal accent, neutral surfaces, and quiet supporting tones.
- Keep the content primary; visual treatments should make information easier to scan.
- Make the interface consistent, then allow controlled personalization through tokens and presets.
- Support adaptive layouts rather than assuming one screen size or orientation.

## Applied to YAAG

- A clear title/year header, named month panels, weekday row, then date cells create repeatable scan order.
- Seven palettes share the same hierarchy; a custom accent derives related pale line/weekend tints.
- Month treatments (structured, soft card, editorial), type choices, and print line weight are separate controls.
- Shared CSS variables carry accent, surface, line, gap, and scale decisions across the page.
- No remote font is needed; built-in font stacks preserve offline behavior and avoid missing assets in print.

## Quick review questions

1. Is the year and the calendar's purpose obvious at a glance?
2. Do months and dates have a consistent reading order?
3. Does accent color identify hierarchy without overpowering writing space?
4. Do palette changes preserve the same component logic?

## Sources

- Apple Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
- Material 3: https://m3.material.io/get-started
- Material 3 typography: https://m3.material.io/styles/typography/applying-type