# Accessibility notes

## Implemented

- Semantic page regions, headings, form labels, native inputs, and useful accessible names for actions and controls.
- Visible `:focus-visible` treatment and keyboard-operable native controls/radio cards.
- Palette swatches include labels and pressed state. Weekend status is conveyed by weekday text, not color alone.
- Matrix date cells expose a localized full-date accessible name; invalid trailing cells are hidden from assistive tech.
- Event-format guidance and validation feedback use a live region.
- System-font stacks, responsive controls, adjustable date size, and grid line-weight options.

## Important caveats

- Accent-colored text is automatically darkened as needed to meet a 4.5:1 contrast ratio against white, while the chosen accent remains on decorative marks and tints. This calculation does not constitute a complete WCAG audit, and contrast can still vary with paper tone and print media.
- Paper/date cell size is physical, not responsive in the same way as a web form. Ultra-dense arrangements and small paper sizes may be difficult to use.
- Screen-reader and keyboard testing remains a manual release step; see the checklist.
- Browser print dialogs and printer drivers are outside the app's control.

## Reference baseline

WCAG 2.2: https://www.w3.org/TR/WCAG22/
Apple HIG accessibility: https://developer.apple.com/design/human-interface-guidelines/accessibility/
