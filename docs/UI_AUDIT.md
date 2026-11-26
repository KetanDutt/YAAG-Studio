# UI audit (pre-refinement)

**Scope inspected:** the one-page `index.html` application and its inline CSS/JavaScript, plus product/architecture/QA docs and the user-provided wall-matrix reference. The app is a dependency-free static HTML/CSS/JS print-design tool; it has no framework, API, backend, or route layer. Primary journey: set calendar conventions → choose layout and styling → optionally annotate dates → preview → print/save as PDF. Data is browser-local with JSON import/export.

## What already works and stays

- A large live paper preview is the product's primary content, not an unrelated dashboard.
- Print CSS sets actual page dimensions and hides builder chrome.
- The month grid and image-inspired annual matrix serve distinct planning needs.
- Local-first settings, valid-date feedback, dark builder mode, and export/import keep the tool useful offline.
- The design remains customizable without relying on remote assets.

## Findings prioritized by impact

| Priority | Location | Finding | Impact / refinement |
|---|---|---|---|
| High | `.stage` light/dark background | A prominent radial gradient and very broad sheet shadow read as generic mockup chrome rather than a calm print studio. | Replace with a quiet warm-neutral desk surface; reserve the one rich moment for the printed page itself. Keep a restrained sheet shadow only on screen. |
| High | Mobile `.topbar` / `.top-actions` | Header actions have fixed desktop assumptions and can become crowded at phone widths. | Let the toolbar wrap deliberately, keep the print action visible, and give controls a coherent order and touch space. |
| Medium | `.side-kicker`, `.paper-kicker`, footer metadata | Small all-caps/letter-spaced labels create noisy hierarchy and feel template-like. | Use short sentence/title case; keep uppercase only for compact essential abbreviations such as weekdays. |
| Medium | Header Unicode action marks and `YA` square | Text glyph arrows/print mark and a generic monogram do little to identify a calendar product. | Replace action marks with small inline SVGs; use a custom 3×4 date-grid signature mark, with one date accented. |
| Medium | `.topbar`, `.preview-toolbar` | Functional chrome is visually flat while the stage supplies decorative gradient. | Move subtle translucent material to only the primary top bar (with solid fallback); keep controls opaque/readable and the print surface unglazed. |
| Medium | `.radio-cards`, repeated field outlines | Every setting group uses similarly framed choices, so the sidebar feels like a long wall of boxes. | Preserve choice affordances but reduce decoration, use consistent spacing, and distinguish selected/focused states cleanly. |
| Medium | Type stacks and controls | `Inter` is named but not shipped, causing a silent fallback; control/body typography has little token structure. | Use an explicit local system stack and document a small type/space/radius/color token set. |
| Medium | Motion/keyboard preferences | Existing transitions do not honor reduced-motion preferences, and active/pressed feedback is minimal. | Add brief pressed/focus feedback and a reduced-motion override. Avoid continuous or decorative animation. |
| Low | Preview stage | The reference calendar page already provides visual richness and meaning; adding glass to the page content would reduce print realism. | Keep page surfaces opaque, only tint controls/navigation; the content/page is the focal moment. |

## Visual direction

- **Product:** an offline planner builder for turning a whole year into a writable wall artifact.
- **Character:** editorial, composed, quietly tactile.
- **World:** a printmaker's desk—warm stock, graphite/ink, precise rules, one botanical green.
- **Moments:** the actual year sheet is the rich focal surface; the annual date matrix is the signature content view.
- **Signature:** a small 12-cell calendar mark in the brand and a restrained floating glass toolbar over the studio canvas.

## Unslop / Liquid Glass interpretation

Use the Unslop audit-and-refine mindset: retain working flows, remove decorative competition, let this product's real calendar carry the visual interest, and keep interface chrome quiet. Apply the Apple material concept selectively to navigation/tool chrome only; no glass over date cells or printed content. Keep readable, high-contrast text opaque. The direction intentionally rejects colorful ambient blobs, glass cards everywhere, heavy glow, and gratuitous transitions.

## Validation status

Static project checks, Node syntax, date/event helpers, and contrast helper tests pass. A screenshot-capable browser/physical printer QA run is not available in this workspace; follow `QA_CHECKLIST.md` before treating any specific browser/printer output as signed off.
## Changes applied in the 1.1.0 refinement

- Consolidated screen colors, spacing, radii, motion, focus, and semantic status colors into a small token layer; kept the page's print-specific tokens separate.
- Replaced the radial background with a calm studio surface; softened the paper shadow and preserved an opaque print preview.
- Added a restrained, fallback-safe glass top bar only. Controls and page content remain high-opacity/readable.
- Added small generated SVG layout maps beside each month arrangement, including a mini 12-row/31-column matrix, so layout choices are previewable before selection.
- Replaced header action glyphs with consistent inline SVGs and the plain YA tile with a small 12-cell calendar mark.
- Reduced tracked uppercase copy in print metadata, aligned the font stack to actual locally available system fonts, and tightened the label/heading hierarchy.
- Wrapped mobile actions deliberately; the page preview now follows available width and zoom range is larger on narrow screens.
- Added clear pressed/focus states and `prefers-reduced-motion` handling.
- Preserved existing calendar calculations, matrix/grid modes, settings, palette choices, dark mode, import/export, and print flow.
