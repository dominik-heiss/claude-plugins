# Export workflow

All exports go through `marp-cli`, invoked via `npx` — no global install.

**Default to HTML.** Render PDF only when the user explicitly asks for
it. PDF needs Chromium and is slower; HTML opens in any browser.

## HTML — default, fast preview / sharing

```bash
npx @marp-team/marp-cli your-deck.md \
  --theme assets/themes/editorial.css \
  --html \
  -o exports/your-deck.html
```

Open the file in any browser. No server required.

Substitute `assets/themes/soft-tech.css` if the deck's frontmatter has
`theme: soft-tech`.

## PDF — only on explicit request

```bash
npx @marp-team/marp-cli your-deck.md \
  --theme assets/themes/editorial.css \
  --pdf \
  --allow-local-files \
  -o exports/your-deck.pdf
```

`--allow-local-files` is needed if the deck references local images.

## Output filename — theme suffix only on conflict

Default output filename is `exports/<deck-stem>.<ext>`. Add a
`-<theme>` suffix **only when a previous export of the same deck used
a different theme** and would otherwise be overwritten — e.g., the
deck was first rendered under `editorial` (`exports/foo.html`) and is
now being re-rendered under `soft-tech`. In that case write
`exports/foo-soft-tech.html` so both renderings coexist.

For a fresh deck or a same-theme re-export, keep the filename plain.

## Watch mode

Re-render on every save — useful while iterating:

```bash
npx @marp-team/marp-cli your-deck.md \
  --theme assets/themes/editorial.css \
  --html --watch \
  -o exports/your-deck.html
```

## PNG per slide

```bash
npx @marp-team/marp-cli your-deck.md \
  --theme assets/themes/editorial.css \
  --images png \
  -o exports/slide.png
```

Produces `slide.001.png`, `slide.002.png`, etc.

## PPTX (bitmap, NOT editable)

```bash
npx @marp-team/marp-cli your-deck.md --pptx -o exports/your-deck.pptx
```

Each slide becomes a single bitmap embedded in PPTX — **not editable in
PowerPoint**. Use only as a last-resort handoff to clients who insist on
a `.pptx` file but won't edit it. For real editable PPTX, this plugin is
the wrong tool.

## Theme by frontmatter vs CLI

If the deck's frontmatter has `theme: editorial` and MARP can resolve
the theme by name (registered via `--theme-set`), you can drop the
`--theme` flag:

```bash
npx @marp-team/marp-cli your-deck.md \
  --theme-set assets/themes/editorial.css \
  --pdf -o exports/your-deck.pdf
```

`--theme` (path) works as a one-shot override. `--theme-set` registers
the file so it can be referenced by name.

## Output folder

Convention: `exports/` at the project root, gitignored. The `/marp-export`
command will create it on first use.

## Exit codes

`marp-cli` exits non-zero on render error. Useful in scripts and CI.
