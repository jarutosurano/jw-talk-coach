# Talks (5, 10, 30 min) — workflow, script format, templates

> Moved verbatim from `CLAUDE.md` on 2026-10-30 (instruction-budget fix). The hard rules (never/must) are also kept in `CLAUDE.md`; if the two ever differ, `CLAUDE.md` wins. Add new procedures, templates and lookup rows here, not in `CLAUDE.md`.

---

## Talk Preparation Workflow

### Talk Types
| Type | Duration | Schedule | Time of Day | Use in Script |
|------|----------|----------|-------------|---------------|
| 5 min | 5 minutes | Friday (OCLM) | Gabi | "ngayong gabi" |
| 10 min | 10 minutes | Friday (OCLM) | Gabi | "ngayong gabi" |
| 30 min | 30 minutes | Sunday (Public Talk) | Umaga | "ngayong umaga" |

### Recommended File Structure

File locations and folder naming: see CLAUDE.md "Where files go" (pictures sit next to `index.md` in `docs/`). The per-type examples that used to be here are superseded.

### MANDATORY — Outline Template with Guided Comments

When creating a new `outline.md` file for any talk type (5, 10, 30 min), ALWAYS include HTML comment guides (`<!-- -->`) in each section so the user knows exactly what to paste and how to format it. Every outline.md must have these sections with comments:

- `## Outline` — what to paste (workbook text, main points, scriptures)
- `## References` — format for each reference (publication code + full paragraph text)
- `## Bible Texts` — reminder to paste EXACT NWT Tagalog text (never paraphrase). If left blank, Claude reads it from `reference/books/nwt-bagong-sanlibutang-salin.pdf`.
- `## Image` — what to include (URL, description, caption) or note if none
- `## Notes` — suggestions for what to write (struggles, goals, audience type)

This ensures the user is guided on where to put each piece of information without needing to ask. See existing outlines in `talks/10min/` for the standard template.

### Script Creation Workflow

**Step 1: Intake**
- Collect: outline, references, time limit, audience type
- Ask: What's your main struggle? Any specific goals?

**Step 2: Analyze Outline**
- Identify tema (theme) and layunin (goal)
- Map pangunahing punto (main points)
- Note susing teksto (key texts marked "Basahin")

**Step 3: Research References**
- Read provided references
- Extract key quotes, illustrations, experiences
- Note which reference supports which point

**Step 4: Draft Script**
- Write intro (hook + tema + why it matters) — ~10% of time
- Develop each main point with: explain → illustrate → apply
- Handle each text: intro-before-read → read → "so what?" after
- Write conclusion (recap + call to action) — ~10% of time
- **IMPORTANT:** Use exact words/phrases from the outline — elders may follow along

**Step 4a: Script Formatting Standards (10-Minute Talks)**

This is the standard format. All 10-minute talks must follow this pattern:

```markdown
---
title: Talk Title Here
---

Mon DD, YYYY

---

## INTRO [1 minuto]

[Content here...]

---

## 1 — Full outline text here [X minuto]

[Intro before reading...]

*[Basahin ang Book X:X]*

!!! quote "Book X:X"
    "Scripture quote here..."

**==Key phrase from outline==** — only at section intro

**Key phrase from Bible text** — [explanation] (bold only, not highlight)

---

## 2 — Full outline text here [X minuto]

[Content here...]

---

## IMAGE

**IMAGE CUE: picture.jpg**

[Image discussion...]

---

## CONCLUSION [1 minuto]

[Content here...]
```

| Element | Format | Example |
|---------|--------|---------|
| Title | YAML frontmatter `title:` (plain, no "Script:" prefix) | `title: Siya ang Ating Diyos!` |
| Date | Below frontmatter, before first `---` | `Jan 24, 2026` |
| Section headers | `## SECTION [X minuto]` | `## INTRO [1 minuto]` |
| Point headers | `## N — Full outline text [X minuto]` (no "PUNTO") | `## 1 — Nagalit si Isaias... [2.5 minuto]` |
| Read cues | Italic with brackets | `*[Basahin ang Isaias 29:13]*` |
| Scripture quotes | Admonition (quote) | `!!! quote "Isaias 33:6"` |
| Outline phrases | Bold + highlight | `**==masunurin mula sa puso==**` |
| Image section | `## IMAGE` (no "pagkatapos ng Punto X") | `## IMAGE` |
| Image cue | Bold | `**IMAGE CUE: picture.jpg**` |
| Horizontal lines | Between every section | `---` |

**Key rules:**
- IMAGE is optional — not all 10-minute talks have images
- IMAGE can be placed between any points (not fixed to after last point)
- Always use `---` horizontal lines between sections
- Date format: `Mon DD, YYYY` (e.g., `Jan 30, 2026`)

**Step 4b: Handle Visual Aids (Images)**
- **10-min talks:** Images are optional — include only if the outline has one
- **30-min talks:** Images optional — include if specified in outline
- Script template for introducing image:

```markdown
## IMAGE

Ngayon naman po, tingnan natin ang larawan.

<figure markdown="span">
  ![Alt text](picture.jpg){ width="100%" }
  <figcaption>Exact caption text from workbook</figcaption>
</figure>

Ano po ba ang nakikita natin dito, mga kapatid at mga kaibigan?

[Describe what's in the image — connect to the point]

At napansin n'yo po ba ang caption? Sabi po dito:

> **"[exact caption text]"**

[Application from the image]
```

- Place image cue AFTER explaining the point (image supports the teaching, not replaces it)
- Call attention to image → Describe → Connect to point → Read caption (if any)
- See Aralin 9 and guidelines.md #8-9 for visual aid rules

**IMPORTANT — Talks vs Hiyas Distinction:**
- **Talks (5, 10, 15, 30 min):** WE are the speaker. No audience interaction. We read all scriptures ourselves. Never say "sino po ang gustong bumasa?" — that's Hiyas only.
- **Hiyas (Espirituwal na Hiyas):** We are the CONDUCTOR. We ask the audience to read, answer, and share. "Sino po ang gustong bumasa?" is correct here.

**MANDATORY — Use Exact Outline Wording:**
- The exact words from the outline's main points MUST appear in the script
- Don't paraphrase or rephrase the outline — use the outline's own words
- These phrases should be woven naturally into the flow, not just in headings

**Highlight vs Bold Rules:**
- `**==highlight==**` (bold + yellow highlight) = ONLY when explicitly introducing/stating the outline point at the START of each section (once per point). This is the visual indicator that "these are the exact words from the outline."
- `**bold only**` = for the SAME outline words when used in other contexts: application ("Kaya paano natin ito ikakapit?"), conclusion, summary, Bible text phrases, formula, and talk title
- Bible text key phrases (derived from scripture, not from the outline) = **bold only**
- Formula = **bold only** (not from the outline)
- Talk title in intro = **bold only**

**REIA Pattern (for each scripture/point):**
Each main point should follow this flow:
1. **R — Read** the scripture text
2. **E — Explain** what it means
3. **I — Ilarawan** (Illustrate) with a practical analogy or example
4. **A — Ikapit** (Apply) to the audience's daily life

**MANDATORY — Scripture Transitions (from guidelines.md #13):**
Before reading any scripture, ALWAYS add a transition that:
1. Tells the audience to open their Bible: "Buksan po natin ang [Book] kabanata X, bersikulo Y."
2. Prepares their mind — tell them what to look for or ask a question: "Dito, makikita natin ang..."
3. If returning to a previously opened text: "Balikan po natin ang [Book] X:X, pansinin naman ang..."

Example:
```
Buksan po natin ang Isaias kabanata 33, bersikulo 6.
Dito, makikita natin ang pangako ni Jehova sa atin.

*[Basahin ang Isaias 33:6a]*
```

**MANDATORY — Image Transitions (from guidelines.md #8):**
When presenting an image, ALWAYS follow this pattern:
1. Call attention: "Ngayon naman po, tingnan natin ang larawan."
2. Render image: `<figure markdown="span">` with caption
3. Ask rhetorical question: "Ano po ba ang nakikita natin dito, mga kapatid at mga kaibigan?"
4. Describe and connect to the point
5. Read caption: "At napansin n'yo po ba ang caption? Sabi po dito: ..."
6. Apply from the image

**MANDATORY — Bible Text Format:**
Use `!!! quote "Book X:X"` admonition format (with book icon) instead of blockquotes for ALL scripture readings in talks. The quote admonition icon is configured as `material/book-open-page-variant` in `mkdocs.yml`.

Example:
```markdown
!!! quote "Isaias 33:6"
    "Siya ang magpapatatag sa iyo..."
```

**MANDATORY — Talk Title in Intro:**
Always mention the talk title in the introduction. Example: "Ang tema po natin ngayong gabi: **Siya ang Magpapatatag sa Iyo** — mula sa Isaias 33:6."

**Step 5: Apply Aralin Principles**
- Match struggles to relevant Aralin (see the diagnostic mapping in `runbooks/coaching.md`)
- Incorporate specific techniques from chosen Aralin

**Step 6: Time Check**
- 5 min: ~750 words generic; a 4-minute student pahayag at Jayr's pace is ~490 spoken words incl. readings
- 10 min: ~1,165 words at Jayr's pace (≈9:50; hard max ~1,250). 1,500 is the generic rate; don't use it
- 30 min: ~4,500 words
- Adjust content to fit, prioritize susing teksto

**Step 7: Review Against Both Reference Documents**

MANDATORY: Check BOTH documents when preparing any talk (5, 10, 30 min):

- `reference/guidelines.md` — S-141-TG: HOW to deliver (eye contact, scripture transitions, visual aids, positive tone)
- `reference/public-talk-aralin.md` — Pagtuturo book: WHAT to focus on (structure, application, illustrations, main points)

Review checklist:
- Positive tone? (guidelines.md #14 + Aralin 16)
- Clear structure / main points stand out? (guidelines.md #4 + Aralin 14, 17)
- Practical application? (guidelines.md #5 + Aralin 13)
- Heart-reaching? (Aralin 19)
- Scripture transitions? (guidelines.md #13)
- Visual aids used correctly? (guidelines.md #8-9)

**Step 8: Practice Plan**
- 2 min warm-up (read intro aloud)
- 6 min run-through (focus on 1 skill)
- 2 min review (self-evaluate)

**Step 9: Create Summary (10-min talks)**
- Create `summary.md` with the following sections:
  - **Tema** — one-sentence theme
  - **Ang 3 Pangunahing Punto** — each with teksto and simpleng ideya
  - **Bakit Mahalaga Ito?** — table with tanong/sagot
  - **Mga Realistic na Application** — table with sitwasyon/lip service/heart service (if applicable)
  - **Visual na Structure ng Talk** — ASCII tree showing timing breakdown
  - **Mga Reference na Ginamit** — list of publications cited
- This helps the speaker review key points quickly before delivery
