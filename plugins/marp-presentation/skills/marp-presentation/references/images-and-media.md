# Images, backgrounds, media

## Inline image

```markdown
![alt text](path/to/image.png)
```

For tighter control, MARP accepts size keywords inside the alt text:

```markdown
![width:400px](image.png)
![height:200px](image.png)
![w:400 h:200](image.png)
```

## Background image (full-bleed)

```markdown
![bg](image.jpg)
```

Variants:

```markdown
![bg fit](image.jpg)         <!-- contain, no crop -->
![bg cover](image.jpg)       <!-- fill, may crop (default) -->
![bg left](image.jpg)        <!-- left half of slide -->
![bg right:40%](image.jpg)   <!-- right 40% of slide -->
![bg blur](image.jpg)        <!-- blur for layering text on top -->
![bg opacity:.5](image.jpg)  <!-- transparency -->
```

Multiple backgrounds stack:

```markdown
![bg left](one.jpg)
![bg right](two.jpg)
```

## Local images and PDF export

When exporting to PDF with local image paths, you need:

```bash
npx @marp-team/marp-cli deck.md --pdf --allow-local-files
```

Without it, Chrome refuses to load `file://` images for security.

## Asset placement

Convention:
- User-deck assets next to the deck (`my-deck/images/foo.png`)
- Plugin-shipped assets under `assets/`

Reference with relative paths from the deck file:

```markdown
![logo](images/logo.png)
```

## Alt text

Always provide alt text for images. Accessibility win, and it shows up
in HTML exports for screen readers.

## SVG

SVG works as both inline and background. Useful for diagrams that need
to remain crisp at any zoom level.

```markdown
![](diagrams/architecture.svg)
```

## Video / audio

Not natively supported in MARP-rendered PDF. For HTML, embed via raw
HTML:

```markdown
<video src="clip.mp4" controls></video>
```

Won't render in PDF — only HTML.
