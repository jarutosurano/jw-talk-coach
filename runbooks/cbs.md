# CBS — Congregational Bible Study conductor script

> Moved verbatim from `CLAUDE.md` on 2026-10-30 (instruction-budget fix). The hard rules (never/must) are also kept in `CLAUDE.md`; if the two ever differ, `CLAUDE.md` wins. Add new procedures, templates and lookup rows here, not in `CLAUDE.md`.

---

## CBS (Congregational Bible Study)

Conductor-led 30-minute book study from the midweek meeting (OCLM). The user is the conductor — introduces the material, assigns a reader, asks workbook questions, and facilitates discussion. This is NOT a talk; it's a facilitated study.

### How It Works

1. **Timing:** 30 minutes total (covers 2 aralins, sometimes with an introduction)
2. **Flow per aralin:**
   - Conductor gives brief intro on what we'll cover
   - Reader reads the paragraphs: "Para simulan, makikisuyo tayo ni brother [name] para basahin ang mga talata"
   - Conductor asks workbook questions after reading
   - Audience answers, conductor may ask guided follow-ups
   - Transition to next aralin
3. **Current book:** wcg (Lakas-Loob na Lumakad Kasama ng Diyos) — earlier: lfb (Mga Aral Mula sa Bibliya)

### Folder Structure

**Published script** (in `docs/`):
```
docs/cbs/
  MMDD-wcg-kabanata-NN/index.md     # conductor script (published)
```

**Non-published reference** (root-level):
```
cbs/
  MMDD-wcg-kabanata-NN/outline.md   # questions, short excerpts, notes
```

**Naming:** `MMDD-wcg-kabanata-NN` (e.g., `1030-wcg-kabanata-14`); old lfb weeks used `MMDD-lfb-aral-XX-XX`
**Nav label:** `CBS` → `Feb 9-15` (week date range)

### Script Creation Workflow

**Step 1:** Read `outline.md` — get aralin text, questions, quoted texts, bible references

> **Current format (wcg, since Aug 2026); the lfb "Aral XX / Q-A / SUMMARY" template below is obsolete.** Copy the structure of the latest `docs/cbs/*-wcg-kabanata-*/index.md`: theme `!!! quote`, MATUTUTUHAN, BASAHIN SA BIBLIYA, `!!! tip "FORMULA"` with table, `## INTRO` (green-highlight chapter title, hook, reader line), then the chapter's sections (`## TALAKAYIN`, `## ALAMIN`, `## GAWIN ANG MGA NATUTUHAN MO`, `## MAHALAGANG PAG-ISIPAN`, `## TINGNAN DIN (kung may oras)`). Each question: `### N — [exact question] (ref) — Larawan X`, Mahahalagang punto, Direktang sagot, `!!! success "Sagot kapag binasa nang malakas"` (add `(mas malalim)` for key ones), Tanong para ikapit. End with `## MGA ARAL NA NATUTUHAN` (`!!! abstract "Aral"` boxes), `!!! tip "Tandaan ang FORMULA"`, `## SUMMARY`. Describe pictures only as visible.

**Step 2 (old lfb format, kept for reference):** Draft script with this format:

```markdown
---
title: CBS — [Date Range]
---

[Date Range], 2026

---

## Intro

[Brief introduction on what we'll cover — 2 aralins overview]

Para simulan, makikisuyo tayo ni brother [name] para basahin ang mga talata.

---

## Aral XX: [Title]

### Tanong: [Exact workbook question]

**Simplified na sagot:**

[1-2 sentence plain answer — the core idea]

**Mga highlight ng aralin:**

- [Key point 1 from the aralin]
- [Key point 2]
- [Key point 3]

### Mga Guided Questions

**Q: [Basic question from intro/early part]**
A: [30-second personalized answer — simple words, uses "ako/ko"]

**Q: [Deeper question from middle]**
A: [30-second personalized answer]

**Q: [Application question from end]**
A: [30-second personalized answer]

---

[Transition script to next aralin]

---

## Aral XX: [Title]

[Same format as above]

---

## SUMMARY

### Aral XX: [Title]
- [Summary point 1]
- [Summary point 2]

### Aral XX: [Title]
- [Summary point 1]
- [Summary point 2]
```

**Key rules:**
- Intro: brief overview of both aralins, assign reader
- Questions: use EXACT workbook questions word-for-word
- Simplified answers: plain, simple Tagalog — the core idea in 1-2 sentences
- Highlights: bullet points from the aralin content
- Guided questions: personal use — structured from basic (intro) to deep (end of aralin), 30-second answers, personalized ("ako/ko"), simple words
- Transition: natural bridge between aralins
- Summary: at the bottom, one summary per aralin
- No "Para ilarawan" section (unlike Hiyas)
- No timing markers in the script (conductor manages time)

### Navigation

Nav label format: `CBS` section → `[Date Range]` (e.g., `Feb 9-15`)
Latest first in `mkdocs.yml` nav.
