# Plugin development brief — marp-presentation

You are working on `marp-presentation`, a standalone Claude Code plugin
that lets users author and export MARP markdown presentations using the
bundled **editorial** theme.

## What this plugin is — and isn't

- **Is**: a self-contained MARP plugin. Skill + command + theme +
  templates + examples, all built around a single design language.
- **Isn't**: tied to any specific domain, project, customer, or other
  plugin. Examples and templates stay abstract / Lorem-ipsum so the
  patterns travel anywhere.

## Repo layout

```
marp-presentation/
  README.md                          public-facing overview
  CLAUDE.md                          this file
  .claude-plugin/plugin.json         Claude Code plugin manifest
  skills/marp-presentation/
    SKILL.md
    references/
      slide-patterns.md
      theme-customization.md
      frontmatter.md
      images-and-media.md
      export-workflow.md
      pitfalls.md
  commands/
    marp-export.md
  assets/themes/
    editorial.css
  templates/
    starter-deck.md
  examples/
    reference-deck.md
  exports/                           gitignored
```

## Design decisions (settled — do not redebate)

- **Format:** 16:9 (1280×720)
- **Aesthetic:** magazine / editorial — display serif headings + sans body,
  generous whitespace, asymmetric composition
- **Palette:** ink `#111111` on paper `#F4EFE6`, terracotta accent `#C2410C`,
  card surface `#E8E1D3`, muted `#6B645A`
- **Typography:** Fraunces (display) + Inter (sans), Google-Fonts imported
- **Chrome zones:**
  - Top-left: `<span class="brand">SECTION · NN</span>` — uppercase sans
  - Bottom-left: `<p class="source">Source: ...</p>` — italic muted
  - Bottom-right: footer (italic muted) + page number (italic terracotta)
- **Patterns:** title, agenda, default content, two-col, cards,
  section-divider, statement

## Working principles

- Senior-to-senior tone with the user. No filler, no trailing summaries,
  no "let me know if that works".
- Iterate **one pattern at a time** when working on the CSS. Show
  before/after, get feedback, then move on.
- Keep all examples abstract. No domain content (no fictional
  industries, no made-up companies, no scenario-based KPIs).
- Lorem ipsum is fine for placeholder copy — it preserves the design
  intent without committing to a domain.

## Common dev loop

1. Edit `assets/themes/editorial.css` or `examples/reference-deck.md`
2. Re-render the example:
   ```bash
   npx @marp-team/marp-cli examples/reference-deck.md \
     --theme assets/themes/editorial.css \
     --html -o exports/reference.html
   ```
3. Visual check in browser
4. Validate PDF once HTML looks right:
   ```bash
   npx @marp-team/marp-cli examples/reference-deck.md \
     --theme assets/themes/editorial.css \
     --pdf --allow-local-files -o exports/reference.pdf
   ```
5. Iterate

## What NOT to do

- Don't install `marp` globally — always `npx @marp-team/marp-cli`
- Don't add editable-PPTX paths here — that's deliberately out of scope
- Don't introduce framework dependencies. The plugin is markdown + CSS
  + a thin CLI wrapper, nothing more.
- Don't create git commits unless explicitly asked
- Don't add domain-specific examples back in (no industries, no
  fictional companies, no scenario-based content)

## Communication

- User speaks German and English — answer in whichever he uses
- Senior consulting principal background — expects senior-to-senior tone
- Lean, incremental work; one change at a time when iterating
