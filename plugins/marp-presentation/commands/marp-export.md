---
description: Export a MARP deck to HTML (default) or PDF using a bundled theme
argument-hint: <deck-path> [--pdf|--html]
---

Export the MARP deck at the path the user provides.

Workflow:

1. **Resolve the deck path.** If no argument is given, default to the
   most recently edited `.md` file in the current working directory.
2. **Pick the format.** **Default is HTML.** Render PDF only when the
   user explicitly passes `--pdf` or asks for it. PDF needs Chromium
   and is slower, so don't render it speculatively.
3. **Pick the theme.** Read `theme:` from the deck's frontmatter. If
   it's `editorial` (default) or `soft-tech`, resolve to the matching
   bundled CSS at `assets/themes/<theme>.css`. If the user supplied a
   custom path, pass that through. If frontmatter says nothing, default
   to `editorial`.
4. **Resolve the output path.** Default to `exports/<deck-stem>.<ext>`.
   **Add a `-<theme>` suffix only if a same-stem export from a
   different theme already exists** in `exports/` (e.g., if
   `exports/foo.html` was rendered from editorial and the user is now
   exporting under soft-tech, write `exports/foo-soft-tech.html`). For
   the first / only render of a deck, the filename stays plain.
   Create `exports/` if it doesn't exist.
5. **Run the export:**

   ```bash
   npx @marp-team/marp-cli <deck-path> \
     --theme <theme-path> \
     --html \
     -o exports/<deck-stem>.html
   ```

   For PDF, swap `--html` for `--pdf` and add `--allow-local-files`.

6. **Report the result.** Show the output path. If the command failed,
   surface the stderr and point the user at
   `skills/marp-presentation/references/pitfalls.md`.

Prerequisites:
- Node.js 18+ (for `npx`)
- Chrome / Chromium (for PDF only)
- Internet access for first run (Google Fonts) — see pitfalls for
  offline workflow

If either prerequisite is missing, refer the user to `README.md` rather
than trying to install them automatically.
