---
description: Export a MARP deck to PDF or HTML using the bundled editorial theme
argument-hint: <deck-path> [--pdf|--html]
---

Export the MARP deck at the path the user provides.

Workflow:

1. **Resolve the deck path.** If no argument is given, default to the
   most recently edited `.md` file in the current working directory.
2. **Pick the format.** Default is PDF unless the user passes `--html`.
3. **Pick the theme.** Default is `assets/themes/editorial.css` (relative
   to the plugin root) unless the deck's frontmatter already declares a
   different theme.
4. **Resolve the output path.** Default to `exports/<deck-stem>.<ext>`.
   Create `exports/` if it doesn't exist.
5. **Run the export:**

   ```bash
   npx @marp-team/marp-cli <deck-path> \
     --theme <theme-path> \
     --pdf \
     --allow-local-files \
     -o exports/<deck-stem>.pdf
   ```

   For HTML, swap `--pdf` for `--html` and drop `--allow-local-files`.

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
