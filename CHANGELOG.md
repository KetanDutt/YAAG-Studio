# Changelog

## 1.1.0 — 2026-11-26

Premium visual refinement, responsive polish, and documented design direction.

- Replaced the decorative radial canvas with a quiet print-studio neutral and reduced sheet shadow; the paper remains the visual focal point.
- Added a restrained, translucent functional top bar with opaque, legible controls and fallback surfaces; no glass is applied to the printable content.
- Replaced Unicode action glyphs with consistent inline SVG icons and the generic monogram with a 12-cell calendar signature mark.
- Reduced tracked all-caps copy, systematized spacing/color/type/radius tokens, improved mobile toolbar wrapping and zoom, and added visible active/focus states.
- Added `prefers-reduced-motion` support and dark-mode semantic tokens.
- Added pre-change UI audit, design system, Unslop adaptation/attribution, and updated project docs.

## 1.0.0 — 2026-11-26

First reviewed YAAG Studio release.

- Added the reference-inspired 12-month-row × 31-date annual wall matrix.
- Added single-row/single-column month overviews, row/column flow for grid layouts, and a persistent builder dark mode.
- Hardened imported settings and calendar-year/event input handling; bounded event annotations and setup-file size, and report malformed/impossible dates.
- Fixed week-number calculations to use UTC arithmetic (avoids DST drift), removed duplicate custom-color render handlers, and made margin/date-size indicators reflect their current values.
- Added a color-contrast adjustment for accent-colored text on the printable page while preserving the selected accent for decorative fills.
- Corrected the editorial month-heading selector and ensured weekend shading respects its toggle in the annual matrix.
- Added project architecture/product/privacy/accessibility/limitations/release documentation, design summaries, QA guidance, and static + calendar-core checks.
