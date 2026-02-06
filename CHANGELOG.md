# Changelog

All notable changes to this project will be documented in this file.

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
