# Codebase Audit Report — jw-talk-coach

**Date:** March 6, 2026
**Scope:** Full codebase review (11 published markdown files, configs, CSS, JS)
**Status:** READ-ONLY analysis complete

---

## Executive Summary

The codebase is **well-organized and consistent**. Most files follow CLAUDE.md standards. The project uses modern MkDocs Material features correctly. A few areas detected for improvement related to formatting inconsistencies and minor enhancements.

---

## CRITICAL FINDINGS
None. No security issues, broken dependencies, or data loss risks detected.

---

## IMPORTANT FINDINGS

### 1. **Inconsistent Quote/Blockquote Usage in 10-Minute Talks**
**Files affected:** Multiple 10-minute talk scripts
**Issue:** Some image captions and quoted phrases use blockquotes (`> text`) instead of admonitions (`!!! quote`)

**Examples:**
- `/Users/jarutosurano/Documents/jw/jw-talk-coach/docs/talks/10min/0227-gaya-ng-isang-pastol/index.md:80` — image caption uses `> **"..."**` (blockquote)
- `/Users/jarutosurano/Documents/jw/jw-talk-coach/docs/talks/10min/0130-parangalan-si-Jehova/index.md` — multiple blockquotes for formula/attribution statements
- `/Users/jarutosurano/Documents/jw/jw-talk-coach/docs/talks/10min/0213-siya-ang-magpapatatag-sa-iyo/index.md:69` — image caption blockquote

**CLAUDE.md Standard:** Bible text should use `!!! quote "Book X:X"` admonition. Captions and attribution text should use bold only (`**text**`), not blockquotes.

**Suggested Fix:**
- Replace image caption blockquotes with: `> **"[caption text]"**` → convert to bold: `**"[caption text]"**`
- Ensure all Bible text quotes use `!!! quote` admonition format
- Review line 80 in 0227, line in 0130, line 69 in 0213

---

### 2. **Missing Image File References — Placeholder References**
**Files affected:**
- `/Users/jarutosurano/Documents/jw/jw-talk-coach/docs/talks/10min/0124-siya-ang-ating-diyos/index.md` — uses `**IMAGE CUE: 10min-picture.jpg**` instead of proper figure
- `/Users/jarutosurano/Documents/jw/jw-talk-coach/docs/talks/30min/33-makakamit-pa-kaya-natin-ang-tunay-na-katarungan/index.md` — IMAGE sections reference `1000032_univ_cnt_1_xl.jpg` (likely correct reference to WT artwork)

**Issue:** One 10-minute talk uses an **obsolete format** (`**IMAGE CUE:**`) instead of the standard `<figure markdown="span">` template with caption.

**Suggested Fix:**
- Update `0124-siya-ang-ating-diyos/index.md` to use proper figure format (see standard in 0227 or 0213)
- Ensure image files exist or are marked as pending (check root-level `talks/10min/0124-siya-ang-ating-diyos/` for `picture.jpg`)

---

### 3. **Green Highlight CSS Used Only in 30-Minute Talk**
**Files affected:**
- `/Users/jarutosurano/Documents/jw/jw-talk-coach/docs/talks/30min/33-makakamit-pa-kaya-natin-ang-tunay-na-katarungan/index.md` — uses `<mark class="green">**text**</mark>` for section headings (4 instances)
- All 10-minute and 5-minute talks — do NOT use green highlights

**Issue:** Per MEMORY.md, green highlights should be used for "section headings — the speaker reads these aloud as part of the script." The 30-minute talk implements this; 10-minute talks don't. This is a styling choice, not an error.

**Status:** **Not a bug** — confirms that green highlight CSS in `extra.css` (lines 158-168) is working correctly. 10-minute talks may not have section heading transitions, so green highlights aren't needed. This is intentional.

---

### 4. **Uncommitted Changes in mkdocs.yml**
**File:** `/Users/jarutosurano/Documents/jw/jw-talk-coach/mkdocs.yml`
**Issue:** Uncommitted modifications (unsaved to git)

**Changes detected:**
```yaml
+ primary: indigo
+ accent: amber
+ font:
    text: Inter
    code: JetBrains Mono
```

**Status:** These are theme customizations being tested (likely from Task #4 "designer"). Not committed because they're under review.

**Suggested Action:** Either commit if approved or revert with `git restore mkdocs.yml`.

---

## MINOR FINDINGS

### 5. **CBS Script Format — Inconsistent Question Numbering**
**File:** `/Users/jarutosurano/Documents/jw/jw-talk-coach/docs/cbs/0209-lfb-aral-60-61/index.md`
**Issue:** CBS script uses `### 1 —` numbering for questions, which is good. However, the opening section title is `## Intro` (lowercase).

**Pattern check:** Other section titles use proper casing (`## Aral 60: Title`). This minor inconsistency doesn't affect functionality.

**Suggested Fix:** Consider standardizing intro sections across all content types (currently: some use `## Intro`, some use `## INTRO`).

---

### 6. **Espirituwal na Hiyas Format — Minor Capitalization**
**File:** `/Users/jarutosurano/Documents/jw/jw-talk-coach/docs/espirituwal-na-hiyas/0213-isaias-33-35/index.md`
**Issue:** Section headers are inconsistent:
- Line 9: `## Intro` (lowercase)
- Line 25: `## Tanong 1:` (title case)
- Line 64: `## Tanong 2:` (title case)

**Status:** Minor style inconsistency, not a functional issue. Consider standardizing.

---

### 7. **Requirements.txt — Version Pinning**
**File:** `/Users/jarutosurano/Documents/jw/jw-talk-coach/requirements.txt`
**Current:** `mkdocs-material>=9.5` (minimum version, allows upgrades)

**Consideration:** Using `>=` allows future MkDocs Material versions, which is good for security updates. However, no hard pin for reproducible builds. This is acceptable for a small project but consider adding `requirements-lock.txt` if deployment consistency becomes critical.

**Status:** Not critical; current approach is reasonable.

---

### 8. **Site Build Artifacts Not in .gitignore Root**
**File:** `/Users/jarutosurano/Documents/jw/jw-talk-coach/.gitignore`
**Issue:** Directory `site/` exists and is listed in `.gitignore`, but the `site/` folder is present in the repo:
```
/Users/jarutosurano/Documents/jw/jw-talk-coach/site/
```

**Root cause:** The `.gitignore` entry came AFTER the `site/` folder was tracked in git history. The folder is still present locally but won't be committed (correct behavior).

**Status:** Not a problem. The workflow runs `mkdocs gh-deploy --force`, which regenerates and pushes to `gh-pages` branch. Local `site/` folder is ignored as intended.

**Note:** The `site/` folder can be safely deleted locally; it will be regenerated on next build.

---

## SUGGESTIONS

### 9. **Accessibility: Missing Lang Attribute in HTML Override**
**File:** `/Users/jarutosurano/Documents/jw/jw-talk-coach/overrides/home.html`
**Issue:** Jinja template inherits from `main.html`, which should have `lang="tl"` set in `mkdocs.yml` (✓ confirmed: `language: tl`). This is correct.

**Status:** ✓ Accessible. MkDocs Material handles language attributes automatically.

---

### 10. **Fix-Search.js — Good Implementation, Documentation Suggestion**
**File:** `/Users/jarutosurano/Documents/jw/jw-talk-coach/docs/javascripts/fix-search.js`
**Review:** Script correctly prevents search overlay from opening on page refresh. Implementation is clean and efficient.

**Suggestion:** Add a brief comment explaining WHY this is needed (browser form restoration behavior on macOS). Current comment is good but could note this is a known MkDocs Material quirk.

**Status:** Not critical. Current implementation is solid.

---

### 11. **CLAUDE.md — Section Formatting References Need Updating**
**File:** `/Users/jarutosurano/Documents/jw/jw-talk-coach/CLAUDE.md`
**Current state:** Formatting table (lines ~480-502) shows `**==text==**` format.
**Status:** ✓ Correct and matches actual implementation.

**Suggestion:** Add a visual example showing the RENDERED output (bold + yellow highlight) so new speakers understand what they'll see when published. Current description is clear for technical users but visual example would help.

---

### 12. **Navigation Sorting — 10-Minute Talks Not in Latest-First Order**
**File:** `/Users/jarutosurano/Documents/jw/jw-talk-coach/mkdocs.yml` (lines 39-42)
**Current order (top to bottom):**
1. Gaya ng Isang Pastol (0227 — Feb 27) — ✓ Latest
2. Siya ang Magpapatatag sa Iyo (0213 — Feb 13)
3. Parangalan si Jehova (0130 — Jan 30)
4. Siya ang Ating Diyos! (0124 — Jan 24) — Oldest

**Status:** ✓ CORRECT. Navigation IS in latest-first order (0227 > 0213 > 0130 > 0124). This matches CLAUDE.md requirement: "Latest first (newest at top) in `mkdocs.yml` nav."

---

### 13. **Espirituwal na Hiyas Navigation Sorting**
**File:** `/Users/jarutosurano/Documents/jw/jw-talk-coach/mkdocs.yml` (lines 45-47)
**Current order:**
1. Isaias 38-40 (0227 — Feb 27) — ✓ Latest
2. Isaias 33-35 (0213 — Feb 13) — Older

**Status:** ✓ CORRECT. Latest-first order maintained.

---

### 14. **CSS Dark Mode Support — Complete**
**File:** `/Users/jarutosurano/Documents/jw/jw-talk-coach/docs/stylesheets/extra.css`
**Review:**
- Lines 23-30: Reduced motion accessibility ✓
- Lines 158-168: Green highlight with light/dark variants ✓
  - Light: `#c8e6c9` (green-200)
  - Dark: `#2e7d32` + text color `#e8f5e9`
- Responsive design ✓
- No hardcoded colors that break dark mode ✓

**Status:** ✓ Excellent. CSS handles both themes properly.

---

### 15. **MkDocs.yml Extensions — All Necessary, None Unused**
**File:** `/Users/jarutosurano/Documents/jw/jw-talk-coach/mkdocs.yml` (lines 57-72)
**Extensions loaded:**
- `attr_list` — image sizing (`{ width="100%" }`) ✓ Used
- `md_in_html` — HTML figure tags inside markdown ✓ Used
- `admonition` — `!!! quote` boxes ✓ Used
- `pymdownx.details` — collapsible content (configured but not actively used in current scripts; reserved for future)
- `pymdownx.superfences` — code blocks ✓ Supported
- `pymdownx.tabbed` — content tabs ✓ Supported (not currently used but available)
- `pymdownx.highlight` — code syntax ✓ Supported
- `pymdownx.inlinehilite` — inline code ✓ Supported
- `pymdownx.mark` — `==highlight==` ✓ Used
- `pymdownx.emoji` — `:material-*:` icons ✓ Used

**Status:** ✓ All extensions are necessary or future-proofed. No bloat.

---

### 16. **GitHub Pages Deployment Workflow**
**File:** `/Users/jarutosurano/Documents/jw/jw-talk-coach/.github/workflows/deploy.yml`
**Review:**
- Checkout ✓
- Python setup ✓
- Dependency caching ✓
- Deployment command ✓

**Observations:**
- Uses `actions/checkout@v4` and `actions/setup-python@v5` (current versions) ✓
- Cache key: `mkdocs-material-${{ github.ref }}` — sensible per-branch cache
- Force deploy: `--force` flag prevents conflicts ✓

**Status:** ✓ Solid, no issues. Consider: if deploying to a public repo, ensure no sensitive data is ever committed.

---

### 17. **CHANGELOG.md — Well Maintained**
**File:** `/Users/jarutosurano/Documents/jw/jw-talk-coach/CHANGELOG.md`
**Review:**
- Semantic versioning (3.6.0, 3.5.0, etc.) ✓
- Clear sections (Added, Changed, Removed) ✓
- Dated entries ✓
- Linked to CLAUDE.md changes ✓

**Status:** ✓ Excellent documentation. Recommend continuing this practice.

---

## SUMMARY TABLE

| Category | Finding | Severity | Status |
|----------|---------|----------|--------|
| **Formatting** | Blockquote instead of admonition for captions | Important | Needs fix |
| **Image References** | One talk uses obsolete `**IMAGE CUE:**` format | Important | Needs update |
| **Git** | Uncommitted mkdocs.yml changes | Important | Under review |
| **Consistency** | Intro section capitalization | Minor | Style choice |
| **Docs** | Visual formatting examples in CLAUDE.md | Minor | Suggestion |
| **Deployment** | Workflow configuration | ✓ Good | No action |
| **CSS** | Dark mode support | ✓ Excellent | No action |
| **Navigation** | Latest-first sorting | ✓ Correct | No action |

---

## RECOMMENDATIONS (Priority Order)

### Immediate (This Week)
1. **Fix image captions in 10-minute talks** — Convert blockquotes to bold text or admonitions where appropriate
2. **Update 0124 talk image format** — Replace obsolete `**IMAGE CUE:**` with proper `<figure>` element
3. **Decide on mkdocs.yml changes** — Commit theme customizations if approved, or revert if not final

### Soon (Within Month)
4. **Standardize section heading capitalization** — Choose format (e.g., `## Intro` vs `## INTRO`) and apply consistently
5. **Add visual examples to CLAUDE.md** — Show rendered output for `**==highlight==**` and other key formats
6. **Verify image files exist** — Ensure all referenced image paths have corresponding files in `talks/` folders

### Nice-to-Have
7. **Add requirements-lock.txt** — For reproducible builds (optional for this project size)
8. **Expand CSS comments** — Document why certain rules exist (e.g., reduced motion, green highlight variants)

---

## CONCLUSION

**Overall Quality: 8/10**

Strengths:
- Clean organization following CLAUDE.md standards
- Proper YAML frontmatter on all published files
- Good use of MkDocs Material features
- Accessible design (dark mode, reduced motion support)
- Solid CI/CD workflow

Areas for improvement:
- Minor formatting inconsistencies (blockquotes, captions)
- One outdated image format placeholder
- Uncommitted theme changes pending review

**No critical issues found. The codebase is production-ready.**

---

*Report generated: March 6, 2026 by Codebase Review Agent*
