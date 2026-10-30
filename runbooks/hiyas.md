# Espirituwal na Hiyas — conductor script

> Moved verbatim from `CLAUDE.md` on 2026-10-30 (instruction-budget fix). The hard rules (never/must) are also kept in `CLAUDE.md`; if the two ever differ, `CLAUDE.md` wins. Add new procedures, templates and lookup rows here, not in `CLAUDE.md`.

---

## Espirituwal na Hiyas (Spiritual Gems)

Conductor-led 10-minute discussion segment from the midweek meeting (OCLM). The user is the conductor — asks questions, audience answers. This is NOT a talk; it's a facilitated discussion.

### How It Works

1. **Timing:** 10 minutes total (no need to show timing per section in the script — conductor uses phone timer)
2. **Two standard questions:**
   - **Tanong 1:** Based on the Bible reading for that week. Comes with a specific scripture text and a Watchtower/workbook reference. The audience answers, and the conductor may ask guided follow-up questions if the answer needs to go deeper.
   - **Tanong 2:** Always the same — "Sa pagbabasa ng Bibliya para sa linggong ito, anong espirituwal na hiyas ang nagustuhan mo?" Audience shares personal gems from their reading.

### Folder Structure

**Published script** (in `docs/`):
```
docs/espirituwal-na-hiyas/
  MMDD-bible-reading/index.md     # conductor script (published)
```

**Non-published reference** (root-level):
```
espirituwal-na-hiyas/
  MMDD-bible-reading/outline.md   # bible text, reference paragraphs, notes
```

**Naming:** `MMDD-bible-reading` (e.g., `0213-isaias-33-35`)

### User Workflow

1. User creates `espirituwal-na-hiyas/MMDD-title/outline.md` with:
   - Bible reading range (e.g., Isaias 33-35)
   - Tanong 1 text + scripture + reference paragraph
   - Any notes
2. User tells Claude: "May bagong hiyas ako sa folder MMDD-title. Gawan mo ng script."
   - If `outline.md` doesn't exist, build it from that week's `reference/books/mwb-rtf/txt/mwb_TG_YYYYMM_NN.txt` (Tanong 1 question + reference) and fetch the reference from wol.jw.org (memory `reference_wol-research-shortcuts`). Full article text goes to `reference/articles/` (git-ignored).
3. Claude reads `outline.md` and creates `docs/espirituwal-na-hiyas/MMDD-title/index.md`

### MANDATORY — Bible Text Accuracy

- **NEVER** paraphrase, assume, or search for Bible text
- **ALWAYS** use the EXACT words from the user's `outline.md` (which contains NWT Tagalog text copied from their Bible)
- Strip footnote markers (single lowercase letters appearing as superscripts after words: e.g., `bisiga` → `bisig`, `kami.c` → `kami.`) but keep every word exact
- If Bible text is not in the outline, **read it from `reference/books/nwt-bagong-sanlibutang-salin.pdf`** — see "Reading Exact Bible Text" in `runbooks/reference-library.md` for the required column-crop commands. Only ask the user if that fails; never guess.
- All publications and references should use jw.org data
- This applies to ALL Bible quotes: Intro scripture, Tanong 1 scripture, and Tanong 2 personal gems

### Script Creation Workflow

**Step 1:** Read `outline.md` — get bible reading, tanong 1, scripture text, reference

**Step 2:** Draft script with this format:

```markdown
---
title: Espirituwal na Hiyas — [Bible Reading]
---

Mon DD, YYYY

---

## Intro

Magandang gabi po sa inyong lahat — mga kapatid at mga bisita.

Dumako na po tayo sa ating bahagi na "Espirituwal na Hiyas" mula sa pagbabasa ng Bibliya sa aklat ng [Book] kabanata [X-X].

Pero bago po natin sagutin ang unang tanong, sino po dito ang gustong bumasa sa [Scripture]?

*[Basahin ang Scripture]*

> "Scripture text here..."

Salamat po.

---

## Tanong 1: [Exact workbook question with reference] (e.g., Isa 35:8 — Saan tumutukoy ang "Daan ng Kabanalan" ngayon? (w23.05 15 ¶8))

**Simplified na sagot:**

[1-2 sentence plain answer — the core idea]

**Mga highlight ng sagot:**

- [Key point 1 from reference]
- [Key point 2 from reference]
- [Key point 3 from reference]

**Para ilarawan:**

[Simple illustration or analogy to help explain the concept — practical, relatable, easy to understand. Think of a real-life scenario that makes the spiritual point click.]

**Guided follow-up (kung kailangan):**

- **[Follow-up question]**
  Sagot: [Answer to the follow-up]

- **[Another follow-up question]**
  Sagot: [Answer]

---

**Buod ng reference:**

- [Summary bullet 1 from the reference material]
- [Summary bullet 2]
- [Summary bullet 3]

---

## Tanong 2: Sa pagbabasa ng Bibliya para sa linggong ito, anong espirituwal na hiyas ang nagustuhan mo?

**[Book X:X]** — "[Scripture text]"

- [Personal gem — short, direct, uses "ako/ko", within 30 seconds]

**[Book X:X]** — "[Scripture text]"

- [Another personal gem]

(Provide top 10 gems from the Bible reading — personal, concise, practical)

---

### Mga handang sagot (kung ako ang sasagot)

!!! success "Sagot kapag binasa nang malakas — [Book X:X]"
    Sa [Book X:X], [key phrase only, exact NWT]. [What I learned, plainly.] Kaya [ako/ko application].

(At least 2 blocks, each under 1 minute)

---

## Maraming salamat po.

Para sa huling komento po.. si sister..

Maraming salamat po, mga kapatid, sa inyong pakikibahagi at sa inyong paghahanda.

At paumanhin po sa di natawag.

Balik po tayo sa chairman.
```

**Key rules:**
- Intro: improve/vary wording each time — use engaging synonyms, align with the Bible reading theme
- Tanong 1 heading: use the EXACT workbook question word-for-word including scripture reference and publication reference
- Tanong 1 body: simplified answer first (explain "espirituwal na paraiso" or any unfamiliar terms in simple language), then highlights, then "Para ilarawan" illustration, then guided follow-ups WITH answers
- Buod ng reference: bullet-point summary of the reference material (placed before Tanong 2)
- Tanong 2 heading: always the exact same question text
- Tanong 2 body: provide top 10 gems from the Bible reading — each with scripture text + personal answer (short, uses "ako/ko", within 30 seconds, practical application)
- Tanong 2 handang sagot (from Oct 23, 2026): below the 10 gems, at least 2 spoken answers as if Jayr is the audience member answering — CBS style `!!! success` block. Open with the reference + key phrase only (exact NWT, not the whole verse), then what I learned and how I apply it ("ako/ko"). Real talk, straight to the point: no forced analogies, nothing OA (analogy only if it comes naturally). ~45-60 words, well under 1 minute. Avoid verses the same week's talk uses.
- Closing: always ends with the standard closing script (salamat, huling komento, paumanhin, balik sa chairman)
- References from `outline.md` are NEVER published — only the highlights/summaries appear in the script
- No timing markers in the script (conductor uses phone timer)

### Navigation Sorting

Latest first (newest at top) in `mkdocs.yml` nav — same as 10-Minute Talks.
