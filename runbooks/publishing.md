# Publishing — Notion, GitHub Pages, navigation, MkDocs features

> Moved verbatim from `CLAUDE.md` on 2026-10-30 (instruction-budget fix). The hard rules (never/must) are also kept in `CLAUDE.md`; if the two ever differ, `CLAUDE.md` wins. Add new procedures, templates and lookup rows here, not in `CLAUDE.md`.

---

## Notion Integration

### /10minute Command
Push 10-minute talk scripts to Notion using the `/10minute` command (`.claude/commands/10minute.md`).

**Usage:**
| Command | What it does |
|---------|--------------|
| `/10minute` | Lists all talks, you pick one to push |
| `/10minute <folder-name>` | Push specific talk (e.g., `/10minute 0124-siya-ang-ating-diyos`) |
| `/10minute all` | Push all talks (with confirmation) |

**Requirements:**
- `scripts/config.json` must have valid Notion API key and parent page ID
- Talk folder must have `index.md` file

**Script Formatting for Notion:**
- Outline phrases (exact words from outline) should use **==highlight==** format: `**==outline phrase here==**`
- This renders as bold highlighted text in the published site
- Headings should NOT have bold markers (converter handles them)

---

## GitHub Pages

Scripts are published to GitHub Pages for easy sharing and reading on any device.

**URL Format:**
```
https://[username].github.io/jw-talk-coach/talks/10min/[folder-name]/
```

**Example:**
```
https://jarutosurano.github.io/jw-talk-coach/talks/10min/0130-parangalan-si-Jehova/
```

**Why `index.md` instead of `script.md`:**
- Using `index.md` creates clean URLs (folder path only, no filename needed)
- MkDocs renders `index.md` as the folder's default page

**Setup (one-time):**
1. Go to repo Settings → Pages
2. Source: **Deploy from a branch** (`gh-pages`, `/ (root)`)
3. The `.github/workflows/deploy.yml` handles `mkdocs gh-deploy` automatically

**Notes:**
- Repo must be **public** for free GitHub Pages
- Private repos require GitHub Pro ($4/mo) for Pages
- Navigation is defined in `mkdocs.yml` under the `nav:` section

**Tab Navigation Structure:**

The site uses MkDocs Material's header tabs (`navigation.tabs`) with 4 top-level tabs:

| Tab | Sidebar Content | Adding New Content |
|-----|----------------|-------------------|
| **Home** | Custom hero page (no sidebar) | Edit `overrides/home.html` |
| **Talks** | 5-Minute / 10-Minute / 30-Minute groups | Add under `Talks:` → `X-Minute:` in `mkdocs.yml` nav |
| **Espirituwal na Hiyas** | Weekly entries | Add under `Espirituwal na Hiyas:` in nav |
| **CBS** | Weekly entries | Add under `CBS:` in nav |
| **Watchtower** | Weekly answer scripts | Add under `Watchtower:` in nav |
| **Field Ministry** | Demo/arrangement scripts + guidelines | Add under `Field Ministry:` in nav |

Nav labels: talk = its title; Hiyas = the reading (`Jeremias 47-48`); CBS = week range (`Oct 26-Nov 1`); Watchtower = article title (quote it if it contains `:` or `"`). Latest first, except 30-min.

Features enabled:
- `navigation.tabs` — top-level nav items become header tabs
- Tabs hide on scroll down, reappear on scroll up (no `navigation.tabs.sticky`)
- `navigation.footer` — Previous/Next pagination in footer
- `navigation.sections` — sidebar section headings stay bold

**Adding a New Talk:**

When adding a new talk:
1. Create the folder and `index.md` under `docs/talks/`
2. Add the nav entry in `mkdocs.yml` under `Talks:` → the appropriate duration group

---

## MkDocs Material Features

These MkDocs Material features are available for use in scripts. Extensions are already configured in `mkdocs.yml`.

### Admonitions (Callout Boxes)

Useful for highlighting key points, tips, or notes in scripts.

```markdown
!!! quote "Isaias 33:6"
    "Siya ang magpapatatag sa iyo..."

!!! tip "Ikapit"
    Pag-aralan ang Bibliya araw-araw.

!!! example "Para Ilarawan"
    Isipin ang isang barko sa gitna ng bagyo...
```

**Collapsible version** (click to expand):
```markdown
??? note "Karagdagang Impormasyon"
    Expanded by clicking...

???+ note "Bukas by Default"
    Already expanded...
```

**Available types:** `note`, `abstract`, `info`, `tip`, `success`, `question`, `warning`, `failure`, `danger`, `bug`, `example`, `quote`

### Images with Captions

```markdown
<figure markdown="span">
  ![Alt text](picture.jpg){ width="100%" }
  <figcaption>Caption text here</figcaption>
</figure>
```

Alignment: `{ align=left }` or `{ align=right }`
Lazy loading: `{ loading=lazy }`

### Content Tabs

Organize content in tabbed sections:

```markdown
=== "Punto 1"
    Content for tab 1

=== "Punto 2"
    Content for tab 2
```

### When to Use These Features

| Feature | Good for | Example use in talks |
|---------|----------|---------------------|
| Admonitions | Highlighting key sections | Scripture quotes, application boxes, illustrations |
| Images | Rendering pictures with captions | Talk images with teaching captions |
| Content tabs | Organizing alternatives | REIA breakdown, multiple examples |
| Collapsible | Optional/extra content | Reference details, buod ng punto |
