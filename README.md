# JW Public Talk Coaching System

> Quick reference guide para sa talk preparation. Powered by MkDocs Material.

---

## Quick Start

```bash
pip install -r requirements.txt   # Install dependencies (first time only)
mkdocs serve                      # Start dev server at localhost:8000
mkdocs build                      # Build for production
```

---

## Saan Ako Dapat Pumunta?

| Kung gusto mo... | Pumunta sa... |
|------------------|---------------|
| Gumawa ng bagong talk | `docs/talks/5min/`, `10min/`, or `30min/` |
| Gumawa ng field ministry script | `docs/field-ministry/` |
| Tingnan ang workflow | `CLAUDE.md` |
| Aralin reference | `reference/public-talk-aralin.md` |
| Ministeryo aralin reference | `reference/ministeryo-aralin.md` |
| Speaker guidelines | `reference/guidelines.md` |

---

## Bagong Talk Quick Start

### Step 1: Gumawa ng folder
```
docs/talks/10min/MMDD-short-title/
```
Example: `docs/talks/10min/0131-bagong-paksa/`

### Step 2: Gumawa ng `outline.md`
Paste ang outline + references dito (sa root-level `talks/` folder).

### Step 3: Sabihin kay Claude
> "May bagong 10min talk ako sa folder 0131-bagong-paksa. Gawan mo ng script."

### Step 4: Claude will create
- `summary.md` — simplified overview ng topic (sa root-level `talks/` folder)
- `index.md` — full script with timing (sa `docs/talks/` — published)

New script files need YAML frontmatter with `title`. Navigation labels are in `mkdocs.yml`.

---

## Folder Structure

```
docs/                             # Published content (GitHub Pages)
  talks/
    5min/                         # Student talks (Friday gabi)
    10min/                        # Assigned talks (Friday gabi)
      0124-siya-ang-ating-diyos/
        index.md                  # main script
    30min/                        # Public talks (Sunday umaga)
  field-ministry/                 # Bible study demonstrations

talks/                            # Non-published (outlines, summaries)
  10min/
    0124-siya-ang-ating-diyos/
      outline.md
      summary.md

reference/                        # Aralin, guidelines, ministeryo

scripts/                          # Notion integration
  push-to-notion.py
  config.json                     # (gitignored)

mkdocs.yml                        # Site configuration & navigation
.github/workflows/deploy.yml      # Auto-deploy to GitHub Pages
```

---

## GitHub Pages

Site is deployed via GitHub Actions (`mkdocs gh-deploy`).

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

The script auto-resolves paths from both `talks/` and `docs/talks/`.

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
