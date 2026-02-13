# Changelog

All notable changes to this project will be documented in this file.

---

## [3.5.0] - 2026-02-13

### Header tab navigation + Previous/Next footer

**Added:**
- Header tab navigation (`navigation.tabs`) — 4 tabs: Home, Talks, Espirituwal na Hiyas, CBS
- Tabs hide on scroll down, reappear on scroll up (like squidfunk.github.io/mkdocs-material)
- Previous/Next footer pagination (`navigation.footer`)
- Tab navigation documentation in CLAUDE.md

**Added:**
- CBS conductor script: Aral 60-61 (Isang Kaharian na Mananatili Magpakailanman + Hindi Sila Yumukod)

**Changed:**
- Restructured `mkdocs.yml` nav: Talks now groups 5-Minute, 10-Minute, 30-Minute under one tab
- Removed `navigation.expand` (conflicts with tab navigation)
- CBS questions split into numbered format (1 — question, answer below)

---

## [3.4.0] - 2026-02-13

### Creative homepage redesign, 5-min talk folder, dual-reference rule

**Added:**
- Animated homepage: floating icon, staggered fade-in for title/tagline/buttons
- Feature cards section: 3 clickable cards (10-Min, 30-Min, Hiyas) with hover lift effect
- Gradient accent line separating hero from cards
- `prefers-reduced-motion` support (disables all animations)
- 5-minute talk folder: `talks/5min/0213-kung-paano-mananalangin/outline.md`
- MANDATORY dual-reference rule in CLAUDE.md: check both `guidelines.md` AND `public-talk-aralin.md` for talks

**Changed:**
- Homepage redesigned with CSS animations (no JS, pure CSS)
- `extra.css` restructured: animations, hero, cards, responsive sections
- Step 7 in CLAUDE.md now references both documents with expanded checklist
- Removed leftover `node_modules/` (213MB Astro/Starlight dependencies)

---

## [3.3.1] - 2026-02-13

### Refine highlight rules and script polish

**Changed:**
- Highlight (`==`) now ONLY used at section intro when explicitly stating the outline point
- All other uses of outline words (application, conclusion, summary) use bold only
- Bible text phrases, formula, and talk title = bold only (not highlight)
- Smoother intro transition (bridge from hook to theme, removed "mula sa Isaias 33:6")
- Ana's experience now attributed to reference ("makikita natin sa ating referensya")
- Fixed scripture transition for Isa 33:6a (was incorrectly described as "pangako")
- Conclusion now uses bullet points
- Summary now uses bullet points with outline text in bold (removed "Punto X —" prefix)
- Removed `*[Ipakita ang larawan]*` stage cue from IMAGE section

**Updated:**
- `CLAUDE.md` with nuanced highlight vs bold rules and updated image template

---

## [3.3.0] - 2026-02-13

### Improve 10-min talk formatting: highlights, admonitions, transitions

**Changed:**
- Outline phrases now use `**==highlight==**` format (bold + highlight via `pymdownx.mark`) instead of `**{curly braces}**`
- Bible text quotes now use `!!! quote "Book X:X"` admonition format with book icon instead of blockquotes
- Added talk title mention in INTRO section
- Added scripture transitions before every Bible reading ("Buksan po natin ang...")
- Added image transitions with rhetorical questions and caption reading
- Updated IMAGE section: speech transitions first, then figure with caption

**Added:**
- `pymdownx.mark` extension in `mkdocs.yml` for `==highlight==` syntax
- `theme.icon.admonition.quote` set to `material/book-open-page-variant` (book icon for Bible quotes)
- Content-to-footer spacing in `extra.css` (`padding-bottom: 3rem`)
- MANDATORY rules in `CLAUDE.md`: scripture transitions (#13), image transitions (#8), Bible text admonition format, talk title in intro

**Updated:**
- `CLAUDE.md` formatting table, template, and Notion section to reflect new `**==highlight==**` and `!!! quote` patterns
- 10-min talk script "Siya ang Magpapatatag sa Iyo" fully revised with all new formatting

---

## [3.2.0] - 2026-02-13

### Add MkDocs Material features, REIA pattern, and talk rules

**Added:**
- MkDocs Material features documentation in CLAUDE.md (admonitions, images with captions, content tabs)
- `pymdownx.tabbed` extension in mkdocs.yml for content tabs
- REIA pattern requirement for 10-min talk scripts (Read → Explain → Ilarawan → Ikapit)
- Talks vs Hiyas distinction rule (MANDATORY: no audience interaction in talks)
- Exact outline wording rule (MANDATORY: use outline's own words in script sentences)

---

## [3.1.1] - 2026-02-13

### Fix Bible text accuracy and enhance Hiyas script

**Fixed:**
- All 10 Bible text quotes in Espirituwal na Hiyas gems now use EXACT wording from outline.md (NWT Tagalog) — previously some were truncated or paraphrased
- Isaias 33:2 was missing "At kaligtasan namin sa panahon ng paghihirap"
- Isaias 33:22 was missing "Dahil" and "Siya ang magliligtas sa atin"
- Isaias 33:24, 34:16, 35:1, 35:3-4, 35:5-6, 35:10 all restored to full verse text

**Added:**
- "Espirituwal na paraiso" explanation in simplified answer (what it means in simple terms)
- "Para ilarawan" illustration section in Tanong 1 (kagubatan analogy)
- MANDATORY Bible text accuracy rule in CLAUDE.md (Hiyas section + Key Guidelines)
- "Para ilarawan" template section in CLAUDE.md Hiyas script format

**Changed:**
- Personal reflections updated to reference newly included full Bible text portions
- CLAUDE.md Tanong 1 body workflow updated to include illustration step

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
