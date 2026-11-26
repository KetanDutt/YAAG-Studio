# Privacy and security

## Data flow

- The app has no server, analytics, remote fonts, CDN requests, or external API calls.
- Calendar year, appearance, and event annotations stay in the browser's `localStorage` until the user exports a JSON setup file.
- Printing/PDF output is handled by the browser/operating system print dialog.
- The uploaded visual reference in `docs/reference/` is a local project file, not transmitted by the app.

## Input handling

- Imported setup JSON is limited to 100 KB and treated as untrusted configuration, not executable content.
- Option values are normalized against allowlists; title, subtitle, footer, and event text have length bounds.
- Calendar text is rendered as text nodes (`textContent`); imported strings are not inserted as markup.
- Custom colors must be valid six-digit hex values before assignment to design variables.
- Event entries are limited to 3,000 characters and 50 valid date entries; invalid dates are skipped with feedback.

## User guidance

JSON setup exports may contain personal event labels. Store/share those files accordingly. Browser local storage is device/profile-specific; clear browser site/file data if settings should be removed. Some browsers restrict localStorage on `file://` pages; export settings before switching browsers or use a local static server.
