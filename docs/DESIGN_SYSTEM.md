# YAAG Studio design system

## Product intent

A quiet print studio for a writable annual artifact. The calendar sheet—not the interface chrome—is the primary visual moment. Liquid Glass is interpreted as a light floating material for the top navigation/tool layer only; it is not used on the paper surface or on date cells.

## Tokens (screen UI)

| Role | Light | Dark | Use |
|---|---|---|---|
| Ink | `#1F2924` | `#E8EEE9` | Primary copy |
| Muted | `#68746D` | `#A8B3AC` | Helper copy/status |
| Canvas | `#EEEDE7` | `#111A16` | Work surface |
| Surface | `#FAFAF7` / translucent | `#19231D` / translucent | Sidebar and glass toolbar |
| Divider | `#D8DED8` | `#34443B` | Quiet structure |
| Brand | `#315D48` | `#80BD97` | Primary action and focus |
| Error | `#9B3638` | `#F08E89` | Invalid event feedback |

The annual paper keeps its selected accent and light print stock independent from builder dark mode. Accent-colored paper text is darkened as necessary against a white surface; decorative accent bars/tints retain the chosen color.

## Type scale

Use system sans for controls and UI, with a local stack only. Calendar output can choose Sans, Serif, Mono, or Rounded. UI scale: 10px microcopy (rare), 11–12px labels, 13–14px body, 16px brand, 22px page title. Avoid long tracked all-caps labels; use sentence case and reserve uppercase for small weekday abbreviations and metadata that genuinely benefits from it.

## Spacing and shape

UI rhythm: 4, 8, 12, 16, 24, 32px. Compact controls use 8–10px radii; larger sheet/panel shapes remain modest. Print layout uses mm because physical dimensions matter. Keep boundaries subtle and reduce repeated nested borders.

## Material and depth

- **Content layer:** opaque, paper-like and fully readable. No backdrop blur on printable page or calendar cells.
- **Primary chrome:** one translucent top bar with `backdrop-filter` where supported, high-opacity neutral fallback, subtle edge and low shadow.
- **Secondary surfaces:** opaque controls/cards to protect contrast and keyboard focus.
- No luminous blobs, gradients, or continuous animations. The paper sheet gets a restrained screen-only shadow and no shadow in print.

## Motion

Short feedback only (roughly 140–180ms); animate opacity/transform on hover/press, never calendar layout changes. `prefers-reduced-motion: reduce` disables nonessential transitions and smooth scrolling.

## Icon language

Inline, currentColor SVG line icons, a consistent 16px viewBox and stroke weight, decorative SVGs hidden from assistive technology when paired with text. No emoji or arbitrary Unicode button icons.

## Reference principles

- Unslop by Damir Sokolovsky: product-specific direction, quiet chrome, richness concentrated in real content; original: https://github.com/heydamir/unslop (CC BY 4.0, attribution in `UNSLOP_ADAPTATION.md`).
- Apple HIG materials: use material to differentiate functional controls/navigation from content, sparingly: https://developer.apple.com/design/human-interface-guidelines/materials
- W3C WCAG 2.2: https://www.w3.org/TR/WCAG22/
