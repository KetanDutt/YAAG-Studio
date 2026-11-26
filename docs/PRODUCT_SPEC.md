# Product specification

## Purpose

Let people create a one-page, wall-oriented year overview with visible dates, weekdays, and usable handwritten space. The output is a printable page, not just a screen calendar.

## Primary user journey

1. Choose the year and calendar conventions.
2. Choose a visual arrangement and page format.
3. Adjust legibility, color, writing space, and personal annotations.
4. Check the live preview, then print or save as PDF.
5. Export/import settings when the configuration needs to move between browsers.

## Supported calendar formats

### Month grid

- 4×3, 3×4, 2×6, 6×2, 12×1, and 1×12 month-panel arrangements.
- Row-by-row or column-by-column placement.
- Seven-day week headers, six fixed week rows per month, optional week numbers and adjacent-month dates.

### Annual wall matrix

- Twelve rows, one per month; 31 possible date columns per row.
- Each valid date cell shows the local weekday abbreviation and date number; weekends may be tinted; events can be annotated.
- Invalid days at the end of short months remain empty. Week-start and month flow settings are hidden because they do not apply to this presentation.
- Intended for larger landscape paper (A2 recommended minimum for practical handwriting); smaller sheets remain selectable but become dense.

## Functional requirements

- Calendar year 1900–2100, bounded to a valid value.
- Month/day calculations respect leap years and locale month/weekday display.
- Paper options: A2, A3, A4, US Letter, Tabloid; auto, landscape, and portrait orientation.
- Theme, typography, paper tone, margin, line weight, writing-space and header/footer customization.
- Optional recurring `MM-DD: label` events, max 50 valid dates, 3,000 characters, 40 characters per label, up to 3 printed labels per date.
- Local browser settings persistence and portable JSON import/export.
- Live page preview; print-only stylesheet and dynamic `@page` dimensions.
- Manual dark mode for builder chrome; printable surface remains light and print-oriented.

## Non-goals

- Official holiday/observance data, religious calendar conversion, or holiday claims.
- Multi-year planning, event recurrence rules, data sync, collaboration, accounts, or server storage.
- Automated PDF engine, print-shop imposition, or guaranteed printer color management.
- Accessibility certification or guaranteed physical printer margins.
