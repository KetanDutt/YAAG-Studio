# Known limitations and proposed next steps

## Current limitations

1. **Print engine is the browser.** Print-to-PDF layout, physical margins, paper availability, and color reproduction vary by browser and printer. No bundled PDF library guarantees identical output.
2. **Single-page output.** 12×1, 1×12, and matrix layouts are intentionally dense; only larger landscape stock keeps the annual matrix comfortable for handwriting.
3. **No public holiday feed.** No country/religion-specific holidays are included, avoiding stale or misleading dates. Users can enter their own annual `MM-DD: label` annotations.
4. **Annual event recurrence only.** Entries repeat by month/day; no year-specific dates, recurring rules, multiple calendars, or event import.
5. **Week numbering conventions.** The mini-month week-number option uses calendar rows from the selected week start; it is not a configurable ISO/locale week-number standard.
6. **Custom-color contrast.** Accent text is darkened as needed to reach a 4.5:1 ratio against white, but decorative accents/tints and printer output are not automatically certified for every paper tone.
7. **Storage scope.** Local settings belong to the current browser profile; users need JSON export to move them.
8. **Localization scope.** Month and weekday names are localized for the listed locales; builder controls, print metadata, and event date-entry syntax remain English/Western numeric format.
9. **No automated browser/print visual tests.** Static checks and a manual QA matrix are provided, but cross-browser print rendering and physical proofing remain necessary.
10. **Layout density.** On screen and small paper, some formats are previews rather than comfortable handwriting layouts. A2/A3 wall matrix should be proofed before print.

## Suggested improvements (not silently enabled)

- Add optional country holiday packs from maintained, attributable sources with an update policy and a clear on/off switch.
- Provide explicit ISO / locale week-number convention selection.
- Add a separate page-per-month or multi-page export mode for users who want larger event areas.
- Add automatic contrast warnings and print-friendly palette presets with a contrast preview.
- Add browser automation (Playwright) and image-based print regression tests when CI/build infrastructure is acceptable.
- Consider a locale-aware event editor and import/export format with version migrations.
