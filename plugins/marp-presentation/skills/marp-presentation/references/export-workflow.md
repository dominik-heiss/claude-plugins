# Export workflow

All exports go through `marp-cli`, invoked via `npx` — no global install.

## PDF — client-ready

```bash
npx @marp-team/marp-cli your-deck.md \
  --theme assets/themes/editorial.css \
  --pdf \
  --allow-local-files \
  -o exports/your-deck.pdf
```

`--allow-local-files` is needed if the deck references local images.

## HTML — fast preview / sharing

```bash
npx @marp-team/marp-cli your-deck.md \
  --theme assets/themes/editorial.css \
  --html \
  -o exports/your-deck.html
```

Open the file in any browser. No server required.

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
