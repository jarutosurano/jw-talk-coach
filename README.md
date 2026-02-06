# JW Public Talk Coaching System

> Quick reference guide para sa talk preparation. Powered by Astro Starlight.

---

## Quick Start

```bash
npm install        # Install dependencies (first time only)
npm run dev        # Start dev server at localhost:4321
npm run build      # Build for production
```

---

## Saan Ako Dapat Pumunta?

| Kung gusto mo... | Pumunta sa... |
|------------------|---------------|
| Gumawa ng bagong talk | `src/content/docs/talks/5min/`, `10min/`, or `30min/` |
| Gumawa ng field ministry script | `src/content/docs/field-ministry/` |
| Tingnan ang workflow | `CLAUDE.md` |
| Aralin reference | `src/content/docs/reference/public-talk-aralin.md` |
| Ministeryo aralin reference | `src/content/docs/reference/ministeryo-aralin.md` |
| Speaker guidelines | `src/content/docs/reference/guidelines.md` |

---

## Bagong Talk Quick Start

### Step 1: Gumawa ng folder
```
src/content/docs/talks/10min/MMDD-short-title/
```
Example: `src/content/docs/talks/10min/0131-bagong-paksa/`

### Step 2: Gumawa ng `outline.md`
Paste ang outline + references dito. Add YAML frontmatter:
```yaml
---
title: 'Outline: Talk Title Here'
sidebar:
  label: Outline
---
```

### Step 3: Sabihin kay Claude
> "May bagong 10min talk ako sa folder 0131-bagong-paksa. Gawan mo ng script."

### Step 4: Claude will create
- `summary.md` — simplified overview ng topic
- `index.md` — full script with timing (main page)

All new files need YAML frontmatter with `title` and `sidebar.label`.

---

## Folder Structure

```
src/content/docs/
  talks/
    5min/                     # Student talks (Friday gabi)
    10min/                    # Assigned talks (Friday gabi)
      0124-siya-ang-ating-diyos/
        outline.md
        index.md              # main script
        summary.md
    30min/                    # Public talks (Sunday umaga)
  field-ministry/             # Bible study demonstrations
  reference/                  # Aralin, guidelines, ministeryo

scripts/                      # Notion integration
  push-to-notion.py
  config.json                 # (gitignored)

.github/workflows/deploy.yml  # Auto-deploy to GitHub Pages
```

---

## GitHub Pages

Site is deployed via GitHub Actions (Astro build).

URL format:
```
https://jarutosurano.github.io/jw-talk-coach/talks/10min/[folder-name]/
```

---

## Talk Types Quick Reference

| Type | Day | Time | Script phrase |
|------|-----|------|---------------|
| 5 min | Friday | Gabi | "ngayong gabi" |
| 10 min | Friday | Gabi | "ngayong gabi" |
| 30 min | Sunday | Umaga | "ngayong umaga" |

---

## Push to Notion

After your script is ready, push it to Notion:

```bash
cd scripts
python push-to-notion.py talks/10min/0124-siya-ang-ating-diyos
```

The script auto-resolves paths from both `talks/` and `src/content/docs/talks/`.

First time? See `scripts/README.md` for setup instructions.

---

## Before Your Talk Checklist

- [ ] Script is final
- [ ] Timing is within limit
- [ ] All outline phrases are included (check **{braces}** in script)
- [ ] Images are ready (if applicable)
- [ ] Practiced aloud at least once
- [ ] Eye contact practiced (hindi binabasa ang script)
- [ ] (Optional) Pushed to Notion

---

*Last updated: February 2026*
