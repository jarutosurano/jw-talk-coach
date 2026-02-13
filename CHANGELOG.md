# Changelog

All notable changes to this project will be documented in this file.

---

## [3.1.0] - 2026-02-13

### Standardize 10-minute talk format and reorganize nav

**Changed:**
- 10-min script format: removed "PUNTO" prefix, use `## 1 —` numbered format
- 10-min script format: removed "### Teksto:" subheadings
- 10-min script format: IMAGE header simplified to `## IMAGE` (no "pagkatapos ng Punto X")
- 10-min script format: title is plain text (no "Script:" prefix)
- 10-min script format: date added below frontmatter (`Mon DD, YYYY`)
- Updated both existing 10-min talks (0124, 0130) to new format
- Removed "Script:" prefix from 30-min talk title for consistency
- Updated `CLAUDE.md` with new 10-minute format standard
- Hid Field Ministry from navigation (files kept, not published)
- Created `docs/espirituwal-na-hiyas/` folder for Spiritual Gems section

---

## [3.0.0] - 2026-02-13

### Migrated from Astro Starlight to MkDocs Material

**Why:** Simpler Python-based toolchain, native Tagalog language support (`language: tl`), lighter dependency footprint, and better mobile reading experience.

**Added:**
- MkDocs Material configuration (`mkdocs.yml`, `requirements.txt`)
- Explicit navigation in `mkdocs.yml` with section labels
- Dark/light mode toggle (Material theme palette)
- Tagalog UI language (`language: tl`)
- New `docs/index.md` homepage with Material button styling

**Changed:**
- Content moved from `src/content/docs/` to `docs/` (MkDocs content root)
- GitHub Actions workflow now uses Python + `mkdocs gh-deploy`
- GitHub Pages source: "GitHub Actions" → "Deploy from a branch" (`gh-pages`)
- `push-to-notion.py` fallback path updated to `docs/`
- `.claude/skills/10minute.md` paths updated to `docs/`
- `CLAUDE.md` and `README.md` updated with new paths and commands
- Frontmatter simplified: removed `sidebar.label` (nav labels in `mkdocs.yml`)

**Removed:**
- Astro Starlight (`astro.config.mjs`, `package.json`, `package-lock.json`, `tsconfig.json`)
- Starlight content config (`src/content.config.ts`)
- Entire `src/` directory
- `public/` directory (favicon moved to `docs/assets/`)

---

## [2.0.1] - 2026-02-06

### Fix UI issues and content publishing

**Fixed:**
- Removed Tagalog locale config that caused raw translation keys (`tableOfContents.onThisPage`, etc.) to display instead of proper labels
- Fixed broken "Reference Materials" link on homepage (replaced with "30-Minute Talks")

**Changed:**
- Only scripts (`index.md`) are now published to GitHub Pages — outlines, summaries, and reference docs moved back to root-level folders outside `src/content/docs/`
- Updated `CLAUDE.md` with publishing rule: only `index.md` scripts go in `src/content/docs/`
- Sidebar now shows only published scripts (removed Reference section)

---

## [2.0.0] - 2026-02-06

### Migrated from Jekyll to Astro Starlight

**Why:** Better sidebar navigation, full-text search, dark/light mode, and mobile reading experience for speakers.

**Added:**
- Astro Starlight framework (`astro.config.mjs`, `package.json`, `tsconfig.json`)
- Sidebar navigation organized by talk type (10-min, 30-min, Field Ministry, Reference)
- Full-text search via Pagefind
- Dark/light mode toggle
- GitHub Actions deployment (`.github/workflows/deploy.yml`)
- YAML frontmatter on all content files for Starlight compatibility
- Splash homepage (`src/content/docs/index.mdx`)

**Changed:**
- Content moved from root to `src/content/docs/` (Starlight content collection)
  - `talks/` → `src/content/docs/talks/`
  - `field-ministry/` → `src/content/docs/field-ministry/`
  - `public-talk-aralin.md`, `guidelines.md`, `ministeryo-aralin.md` → `src/content/docs/reference/`
- `push-to-notion.py` now auto-resolves both old and new paths, strips YAML frontmatter
- `.claude/skills/10minute.md` updated to new content paths
- `CLAUDE.md` and `README.md` updated with new structure and workflows
- GitHub Pages source: "Deploy from a branch" → "GitHub Actions"

**Removed:**
- Jekyll configuration (`_config.yml`, `_layouts/default.html`)
- Root-level `index.md` navigation page (replaced by Starlight sidebar)
- Root-level reference docs (moved to `src/content/docs/reference/`)

---

## [1.0.0] - 2026-01-24

### Initial Release

- Jekyll-based site with `jekyll-theme-minimal`
- Talk scripts for 10-min and 30-min talks
- Field ministry Bible study scripts
- Push-to-Notion integration (`scripts/push-to-notion.py`)
- GitHub Pages deployment (branch-based)
- Claude AI coaching skills
