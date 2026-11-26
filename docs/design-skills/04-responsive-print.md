# Skill 04 — Responsive and print-first layout

## Principles

- Treat the printable page as a real output format, not a screenshot of the screen UI.
- Make page dimensions, orientation, and scale explicit; use physical units for print.
- Preserve calendar reading order when the arrangement changes.
- Allocate useful writing area to each date cell; avoid letting controls or decoration consume the page.
- Keep builder chrome out of print and specify backgrounds/ink behavior for print.
- Offer a practical default before exposing alternative densities.

## Applied to YAAG

- Month grids: 4×3, 3×4, 2×6, 6×2, 12×1, and 1×12; row-first or column-first flow.
- Annual wall matrix: twelve month rows by up to 31 daily columns, based on the user's reference image. A2 landscape or larger is recommended for writing.
- A2, A3, A4, US Letter, and Tabloid sizes are included; orientation can auto-match or be overridden.
- Print CSS uses exact millimetre dimensions and a dynamic `@page` rule; settings sidebar and toolbar are hidden in print.
- The preview reorganizes for narrow screens while retaining the selected paper's proportions.
- Month panels use stable six-week rows, keeping month geometry aligned and preserving space for handwritten plans.
- Date text size, grid weight, margins, event annotations, and notes line are configurable.

## Print check

1. Choose page size and orientation in YAAG and again in the browser/printer dialog.
2. Set scale to 100% / actual size; disable browser headers and footers.
3. Check printer non-printable margins, especially on A4/Letter.
4. Print one test sheet before using a large-format or specialty stock.

## Source context

- Apple HIG layout guidance: https://developer.apple.com/design/human-interface-guidelines/layout
- Material 3 adaptive layout guidance: https://m3.material.io/foundations/layout/layout-overview/adaptive-design