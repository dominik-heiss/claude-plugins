# Common pitfalls

## "Chrome not found" on PDF export

`marp-cli` needs a Chromium binary to render PDF.

- macOS / Windows: install Chrome
- Linux: `apt install chromium-browser` or install `google-chrome-stable`
- WSL: same as Linux. Make sure the binary is on `PATH`

Override the binary path:

```bash
CHROME_PATH=/path/to/chrome npx @marp-team/marp-cli deck.md --pdf
```

## Local images not appearing in PDF

Add `--allow-local-files`. Chrome blocks `file://` access by default for
security.

## Custom font not rendering

The editorial theme imports Fraunces and Inter from Google Fonts via
`@import url(...)` at the top of the CSS. Web fonts must load before
render. Either:
- Use a font installed system-wide (e.g., Inter via `apt install fonts-inter`)
- Self-host: download the WOFF2 files, drop them in `assets/fonts/`, and
  replace the `@import` with `@font-face` declarations
- Drop the import entirely — the theme falls back to Source Serif 4 /
  Georgia (display) and system sans (body). Metrics shift slightly but
  the deck still renders coherently

If the font fallback chain kicks in unintentionally, the deck still
renders — but metrics shift and slides may overflow.

## Offline / air-gapped PDF export

`@import url(https://fonts.googleapis.com/...)` in the editorial theme
needs internet at first render. Chrome caches the response, so
subsequent exports work offline once the cache is warm. For fully
air-gapped environments, self-host the fonts (see above).

## Slide overflows the page

MARP doesn't auto-shrink. If a slide overflows:
- Cut content (preferred — usually too much on one slide)
- Reduce font size for that slide via `<style scoped>` or a custom `_class`
- Split into two slides

## Wrong theme applied

Two ways MARP picks a theme:
1. `theme:` in frontmatter — must match the `@theme NAME` declaration
   inside the CSS file (or be registered via `--theme-set`)
2. `--theme path/to/file.css` on the CLI — explicit path, one-shot

If neither matches, MARP silently falls back to its built-in `default`.

## VS Code preview differs from PDF

Chrome (PDF) and the VS Code preview (Electron) can render slightly
differently — fonts, line wrapping, image dimensions. Always validate
the final PDF before sending to anyone.

## Page breaks don't flow

MARP is one-slide-per-`---`, not a paginated document tool. Long content
gets clipped, not flowed. Split deliberately.

## Pagination shows on title / section / back slides

Add per-slide overrides:

```markdown
<!-- _paginate: false -->
<!-- _footer: '' -->
```

The bundled `title` pattern already includes these overrides in the
example deck and starter template — copy from there.

## Background image overpowers the title

Use `![bg blur]` or `![bg opacity:.4]` to dim the image, or use a
half-slide background:

```markdown
![bg right:50%](image.jpg)

# Title only on the left half
```

## Theme variable changes don't show up

Browsers and `marp-cli` cache aggressively. Force re-render:
- Delete the output file before re-exporting
- Hard-reload the HTML preview (Ctrl+Shift+R)
- Restart `--watch` mode after CSS changes

## Markdown inside `<div class="col">` not rendering

MARP needs **blank lines** around the markdown content inside HTML
blocks:

```markdown
<div class="col">

**Header**

- Bullet

</div>
```

Without the blank lines, the inner content is treated as raw HTML and
markdown features (bold, lists) don't render.
