# Architecture

## Runtime shape

`index.html` is deliberately self-contained. Its markup, CSS, and application JavaScript are inline so a user can keep one file, open it offline, and retain a portable print workflow. There are no package installs, external fonts, CDN assets, APIs, or build steps.

## Main components

- **Settings sidebar:** native inputs, selects, checkboxes, radio cards with generated inline-SVG layout diagrams, palette controls, and event text area.
- **Preview page:** a page-sized semantic article containing title/year, month layout, and footer.
- **State:** one JavaScript `state` object. UI settings are read into state, normalized, then used to render and persist.
- **Persistence:** browser `localStorage`, guarded with `try/catch` for restricted/file contexts.
- **Portable setup:** JSON export via Blob/download; JSON import via `FileReader`, size-limited and normalized against allowlists.
- **Print:** CSS variables carry chosen physical dimensions. A dynamic `@page` rule, exact mm page box, and `@media print` hide the builder UI.

## Render paths

- **Month-grid path:** creates twelve mini-month panels; each has weekday labels and a fixed 6×7 date grid. Grid placement is row-first or column-first.
- **Annual-matrix path:** creates a 12-row CSS grid with a month-label column and 31 date columns. Every actual date is calculated from the selected year; short-month trailing cells remain blank.
- Shared settings (year, labels, palette, type, page dimensions, notes, events) are applied to both render paths where relevant.

## Input safety and resilience

- Imported keys/options are constrained to explicit allowed values; imported booleans must be true booleans.
- Titles and notes are assigned with `textContent`, not HTML interpolation.
- Color values are validated as six-digit hex before being applied.
- Event text is length-limited and parsed as bounded lines; impossible month/day combinations are ignored and reported.
- Local storage, export downloads, and file import fail gracefully where browser permissions are restricted.

## Performance notes

The entire year is a small bounded DOM (up to 504 date cells in the mini-month grid or 384 month/date cells in the annual matrix), rendered locally. There is no network or runtime dependency cost. Custom color input uses one render path, avoiding duplicate redraws.

## Trade-offs

The inline single-file model makes offline use and handoff simple, but makes automated unit-level testing and code navigation less modular than a bundled multi-file application. This project favors portability over a framework/build pipeline.