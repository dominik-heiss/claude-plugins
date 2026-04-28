# Theme customization

Two themes ship with the plugin:

- `assets/themes/editorial.css` (default) — magazine aesthetic,
  Fraunces + Inter, terracotta accent on warm paper.
- `assets/themes/soft-tech.css` — Linear/Vercel-style, all-Inter +
  JetBrains Mono micro labels, indigo accent on near-white.

Both implement the same pattern set and the same markdown contract
(`.brand`, `.source`, frontmatter `footer:` + `paginate: true`), so
swapping themes is a one-line change in frontmatter.

CSS variables at the top of either file let you re-skin without
touching layout rules.

## Re-skin: edit CSS variables

```css
:root {
  --c-ink:        #111111;       /* primary ink — headings, hero */
  --c-ink-soft:   #2C2A28;       /* body copy, subheads */
  --c-paper:      #F4EFE6;       /* slide background — warm off-white */
  --c-paper-2:    #E8E1D3;       /* card / soft surface */
  --c-accent:     #C2410C;       /* terracotta — bullets, page nr, eyebrow */
  --c-rule:       rgba(17,17,17,0.18);
  --c-rule-soft:  rgba(17,17,17,0.10);
  --c-muted:      #6B645A;       /* meta text, footer, source line */

  --font-display: "Fraunces", "Source Serif 4", Georgia, serif;
  --font-sans:    "Inter", -apple-system, BlinkMacSystemFont, sans-serif;

  --pad-x: 80px;
  --top-chrome: 64px;     /* brand zone height */
  --bottom-chrome: 72px;  /* footer / source / pagination zone */
  --gap-top: 14px;        /* top-chrome → headings */
  --gap-bottom: 36px;     /* content → bottom-chrome */
}
```

Change values, re-export — every pattern picks up the new palette /
spacing.

## Common re-skins

**Cooler palette:** swap `--c-paper` to `#FFFFFF`, `--c-paper-2` to
`#F4F4F2`, `--c-accent` to a different brand color (e.g. `#1E40AF`
royal blue). Keep `--c-ink` dark for contrast.

**Different display serif:** replace `Fraunces` in `--font-display`.
Drop-in candidates: Source Serif 4, Recoleta, Playfair Display, Spectral.
The theme uses optical sizing variants (`font-variation-settings: "opsz"`) —
those only apply to true variable fonts. Static fallbacks still render
fine.

**Tighter rhythm:** reduce `--pad-x` to 64px and `--gap-top` to 10px for
denser slides.

## Add a new pattern

1. Add a section in `editorial.css`:

   ```css
   section.your-class {
     /* layout overrides */
   }
   section.your-class h1 {
     /* heading override if needed */
   }
   ```

2. Use it in markdown:

   ```markdown
   <!-- _class: your-class -->
   ```

Conventions to follow:
- **Reserve top/bottom chrome zones.** The base `section` already
  reserves them via `padding-top` / `padding-bottom` calculations from
  `--top-chrome` / `--bottom-chrome`. Don't override these unless the
  pattern explicitly needs full-bleed (e.g. `section-divider`).
- **Use the existing variables.** Don't hard-code colors or fonts.
- **For grid / flex children that fill the slide,** set `flex: 1;
  min-height: 0;` so they expand and respect the chrome reservations.

## Fork the theme

If you need a different brand entirely, copy `editorial.css` to a new
file:

```
assets/themes/your-theme.css
```

Change the `@theme` declaration:

```css
/* @theme your-theme */
```

Reference it from the deck:

```yaml
---
marp: true
theme: your-theme
---
```

Or pass the path on the CLI:

```bash
npx @marp-team/marp-cli deck.md \
  --theme assets/themes/your-theme.css \
  --pdf
```

## Inline per-slide CSS

For one-off tweaks without changing the theme, use `<style scoped>`:

```markdown
<style scoped>
section h1 { color: red; }
</style>

# This title is red, only on this slide
```

## Web fonts

The theme imports Fraunces and Inter from Google Fonts:

```css
@import url('https://fonts.googleapis.com/css2?family=Fraunces:...&family=Inter:...');
```

This requires internet access at render time. For offline / air-gapped
exports, either:
- Self-host the fonts and update the `@import` URL
- Use `@font-face` with local paths
- Drop the import and let the OS-installed fallbacks (Source Serif,
  Georgia, Inter, system sans) take over
