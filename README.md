# YAAG Studio

A self-contained, offline-first **Year-at-a-Glance calendar builder**. Customize a printable year calendar, preview it on screen, then print it or save it as PDF through your browser. No installation, account, network connection, or third-party libraries are required.

## Quick start

### GitHub Pages / Web
YAAG Studio is a pure static web application (`index.html`) with zero backend dependencies, ready to be served directly via **GitHub Pages** (Settings → Pages → Deploy from `main` branch, `/ (root)`).

### Local / Offline
1. Open `index.html` in a current desktop browser (Chrome, Edge, Firefox, or Safari).
2. Choose the year, language, paper, layout, and styling in the left panel.
3. Review the live preview. Add optional recurring personal dates with `MM-DD: label` lines.
4. Select **Print / PDF**. In the browser print dialog, match the paper size, choose **100% / actual size**, and disable browser headers and footers.
5. For a large wall print, check the printer's non-printable margins and print a test page first.

For easier sharing, the print preview also works when the single HTML file is opened directly from disk. Some browser security settings restrict local-storage or downloads for `file://` pages; if that happens, run `python3 -m http.server 8000` from this directory and open `http://localhost:8000`, or use **Export setup** as a fallback.

## Layouts

- **4 × 3** — balanced mini-month grid and recommended starting point.
- **3 × 4**, **2 × 6**, **6 × 2** — alternate month-grid proportions.
- **12 × 1** and **1 × 12** — ultra-compact single-row or single-column month overviews.
- **Annual wall matrix** — reference-inspired calendar: 12 month rows, dates 1–31 across, weekday abbreviations in each valid date cell, and open space for notes. A2 landscape or larger is recommended for legibility.
- For month-grid layouts, choose **row-by-row** or **column-by-column** reading order.

## Design direction

YAAG Studio is styled as a quiet print studio with a restrained Liquid Glass material system: warm neutral work surface, ink-like type, botanical green accents, and a calendar-grid brand mark. Translucent blur and soft edge highlights are applied to the topbar, sidebar, floating preview toolbar, and toast notifications, while the paper preview and date cells stay opaque and print-faithful. The builder supports dark mode, live zoom percentage readout, compact responsive controls, visible keyboard focus, and reduced-motion preferences. See `docs/UI_AUDIT.md`, `docs/DESIGN_SYSTEM.md`, and `docs/UNSLOP_ADAPTATION.md` for the audit, tokens, and attribution.

## Customization

Calendar year (1900–2100), language, week start, paper size (A2/A3/A4/Letter/Tabloid), orientation, month style, typeface, palette and custom accent, paper tone, page margins, grid weight, date-number size, title/subtitle/footer, weekend tint, week numbers, neighboring dates, notes line, and event annotations. A dark-mode toggle changes the builder interface, not the printable page.

Settings auto-save in the current browser. **Export setup** and **Import** create portable JSON settings files. Import files are limited to 100 KB. Event annotations are limited to 3,000 characters and 50 valid dates; only the first three labels for a given day are shown.

## Project map

```text
YAAG_Studio/
├── index.html                     # App; inline CSS and JS, no runtime dependencies
├── README.md                      # This guide
├── VERSION                        # Current release identifier
├── CHANGELOG.md                   # Release notes
├── examples_2027_A2_printable.pdf # Earlier A2 printable from the first project iteration
├── docs/
│   ├── PRODUCT_SPEC.md
│   ├── ARCHITECTURE.md
│   ├── QA_CHECKLIST.md
│   ├── ACCESSIBILITY.md
│   ├── PRIVACY_SECURITY.md
│   ├── KNOWN_LIMITATIONS.md
│   ├── RELEASE.md
│   ├── UI_AUDIT.md                # Specific pre-change findings and design direction
│   ├── DESIGN_SYSTEM.md           # Tokens, materials, type, spacing, and motion
│   ├── UNSLOP_ADAPTATION.md       # CC BY 4.0 attribution and adaptation note
│   ├── design-skills/             # Curated, original design-principle summaries
│   └── reference/                 # User-provided visual reference for the matrix layout
├── scripts/check_project.py       # Dependency-free static checks (+ Node syntax check if present)
└── tests/                          # Test notes and manual scenarios
```

## Quality checks

Run from this directory:

```sh
python3 scripts/check_project.py
```

The checker validates HTML parsing, duplicate IDs, required controls/features, external runtime dependencies, DOM ID references, and JavaScript syntax when Node.js is available. See `docs/QA_CHECKLIST.md` for browser and print checks that static analysis cannot replace.

## Privacy and limitations

- No analytics, external fonts, CDNs, APIs, or calendar sync. Settings stay in local browser storage unless you export them.
- Event labels are annual month/day annotations; they are not year-specific. The builder does not fetch public holidays.
- PDF creation uses the browser's print-to-PDF flow; the app does not bundle a PDF engine. Paper size and margins depend on browser and printer support.
- One-page formats with 12 months across or down are intentionally dense. Choose the annual wall matrix or the 4 × 3 grid when writing space matters.
- Accent text is darkened as needed for contrast, but custom palette fills and actual printer output are not a formal accessibility certification; proof the chosen palette on your stock.

See `docs/KNOWN_LIMITATIONS.md` for the full list and `docs/RELEASE.md` for release guidance.