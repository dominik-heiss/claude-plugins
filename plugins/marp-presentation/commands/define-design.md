---
description: Pick the design (theme) for future MARP decks, or list available designs and propose a custom one
argument-hint: [editorial | soft-tech | <custom-css-path>]
---

Set or inspect the active design for MARP decks generated in this
working directory. The choice is persisted to a project-local file
(`.marp-design`) at the repo root, so subsequent `/marp-export` runs
and any deck-generation work the skill does will pick it up
automatically.

## Behaviour

### Called with **no argument** — list & propose

1. List the bundled designs with their intended use cases.
2. If `.marp-design` already exists in the cwd, show the currently
   active selection at the top.
3. Offer the user three follow-ups:
   - Pick one of the bundled designs (`editorial` or `soft-tech`)
   - Modify a bundled design (re-skin via CSS variables — point at
     `skills/marp-presentation/references/theme-customization.md`)
   - Define a brand-new design (fork a bundled CSS, change
     `@theme <name>`, save under `assets/themes/<name>.css`, then run
     `/define-design <name>` again to activate it)

Reply template (keep it concise — adapt phrasing as needed):

> **Available designs**
>
> - **editorial** — magazine / editorial. Fraunces display serif +
>   Inter, terracotta accent on warm off-white paper. Use for
>   strategy decks, board memos, op-eds, brand-forward storytelling.
> - **soft-tech** — Linear / Vercel / Stripe-doc. All-Inter + JetBrains
>   Mono micro labels, indigo accent on near-white. Use for product
>   updates, technical reviews, internal eng / data narratives.
>
> Active: `<value from .marp-design or "editorial (default — no .marp-design set)">`
>
> Want me to (a) switch to one of these, (b) re-skin a bundled design
> via the CSS variables, or (c) fork one into a new design under
> `assets/themes/`?

### Called with an **argument** — activate

The argument is either a bundled design name (`editorial`,
`soft-tech`) or a path to a custom CSS file relative to the project
root (e.g. `assets/themes/my-brand.css`).

1. **Resolve the value:**
   - `editorial` or `soft-tech` → keep as-is (the skill / export
     command map these to `assets/themes/<name>.css`)
   - Anything else → treat as a custom CSS path. Verify the file
     exists. If it doesn't, stop and tell the user — don't write
     `.marp-design` for a missing file.
2. **Write `.marp-design`** at the cwd root. The file holds the design
   identifier on a single line, no frontmatter, no extra whitespace:

   ```
   soft-tech
   ```

   Overwrite any previous content.
3. **Confirm to the user**: state the new active design and remind
   them that future deck generation in this directory will use it
   unless overridden by a deck's own `theme:` frontmatter or a
   one-off `/marp-export <deck> --theme <other>`.

## Precedence rules

When the skill or `/marp-export` decides which CSS to apply:

1. Per-deck frontmatter `theme:` wins (deck author's intent is
   strongest).
2. Otherwise, fall back to `.marp-design` in the cwd.
3. Otherwise, fall back to `editorial` (the plugin's default).

The PDF / HTML choice is independent of the design and stays HTML-by-
default unless the user explicitly asks for PDF.

## Notes

- `.marp-design` is per-project state. It belongs in the consumer's
  repo, not the plugin repo. The plugin's own `examples/` decks
  override via frontmatter.
- The file is intentionally plain text (not JSON / YAML) so the user
  can edit it by hand without ceremony.
- If the user wants a custom design they haven't built yet, walk them
  through forking a bundled CSS — see
  `skills/marp-presentation/references/theme-customization.md` ("Fork
  the theme"). Don't generate a new theme from scratch unless they
  ask explicitly.
