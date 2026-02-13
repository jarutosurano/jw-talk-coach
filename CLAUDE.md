# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## 🚀 New Session? Start Here!

1. **Check `README.md`** for quick start guide
2. **Check `docs/talks/` folder** for existing and new talks
3. **Ask user:** "Anong talk po ang gagawin natin ngayon?"

---

## Project Overview

This is a JW Public Talk Coaching System—a Tagalog-language knowledge base for helping speakers prepare and deliver effective public talks (pahayag pangmadla). Built with MkDocs Material. Run `mkdocs serve` for local development, `mkdocs build` to build.

## File Structure

**IMPORTANT — Publishing Rule:**
Only `index.md` scripts go in `docs/` (published to GitHub Pages). All other files (outlines, summaries, reference docs) stay in root-level folders and are NOT placed in `docs/`.

**Published content (GitHub Pages):**
- **docs/talks/10min/*/index.md** — 10-minute talk scripts
- **docs/talks/30min/*/index.md** — 30-minute talk scripts
- **docs/talks/5min/*/index.md** — 5-minute talk scripts
- **docs/field-ministry/*/index.md** — Bible study demonstration scripts
- **docs/index.md** — Homepage

**Non-published content (root-level, repo only):**
- **talks/10min/*/outline.md, summary.md** — Talk outlines and summaries
- **talks/30min/*/outline.md, summary.md** — Talk outlines and summaries
- **field-ministry/*/outline.md** — Field ministry outlines
- **reference/public-talk-aralin.md** — Training curriculum with 15 lessons
- **reference/guidelines.md** — Official speaker guidelines (S-141-TG)
- **reference/ministeryo-aralin.md** — Counsel points for field ministry
- **.claude/skills/jw-pagbabasa-at-pagtuturo.md** — Claude AI skill definition

**IMPORTANT: All published markdown files (in `docs/`) need YAML frontmatter:**
```yaml
---
title: 'Your Title Here'
---
```
Navigation labels are defined in `mkdocs.yml` under the `nav:` section.

## Claude Skill Behavior

The skill in `.claude/skills/jw-pagbabasa-at-pagtuturo.md` activates when users say: "public talk", "pahayag pangmadla", "coach me", "improve intro/ending", or "fix outline/script".

### Quick Intake Flow
1. Ask for tema/title and time limit
2. Request existing outline if available
3. Identify audience (kapatid / bisita / mixed)
4. Determine main struggle area
5. Get 1-2 goals

### Diagnostic Mapping (struggle → recommended Aralin)
- Weak intro → Aralin 1
- Engagement issues → Aralin 3, 8
- Texts feel "inserted" → Aralin 4, 6
- Accuracy/credibility issues → Aralin 7
- Need visuals → Aralin 9
- Lacks application → Aralin 13
- Poor structure → Aralin 14, 17
- Too negative → Aralin 16
- No new learnings → Aralin 18
- Doesn't touch hearts → Aralin 19
- Weak ending → Aralin 20

### Default Outputs
1. One-sentence theme + goal
2. 3-4 main points with transition lines
3. Text handling (intro-before-read + "so what?" after)
4. Application scenarios (2-3 realistic)
5. Practice plan (10 minutes)
6. Mini rubric (1-5): Clarity, Structure, Scripture-use, Warmth, Ending

## Talk Preparation Workflow

### Talk Types
| Type | Duration | Schedule | Time of Day | Use in Script |
|------|----------|----------|-------------|---------------|
| 5 min | 5 minutes | Friday (OCLM) | Gabi | "ngayong gabi" |
| 10 min | 10 minutes | Friday (OCLM) | Gabi | "ngayong gabi" |
| 30 min | 30 minutes | Sunday (Public Talk) | Umaga | "ngayong umaga" |

### Recommended File Structure

**Published scripts** (in `docs/`):
```
docs/talks/
  5min/MMDD-title/index.md
  10min/MMDD-title/index.md
  30min/[outline-number]-title/index.md

docs/field-ministry/
  MMDD-title-Xmin/index.md

docs/espirituwal-na-hiyas/
  MMDD-title/index.md
```

**Non-published support files** (root-level):
```
talks/
  5min/MMDD-title/outline.md
  10min/MMDD-title/outline.md, summary.md, picture.jpg
  30min/[outline-number]-title/outline.md, summary.md, references.md

field-ministry/
  MMDD-title-Xmin/outline.md

espirituwal-na-hiyas/
  MMDD-title/outline.md

reference/
  public-talk-aralin.md
  guidelines.md
  ministeryo-aralin.md
```

**Naming Convention:**
- **5min/10min/espirituwal-na-hiyas folders:** `MMDD-short-title` (e.g., `0124-siya-ang-ating-diyos`)
- **30min folders:** `[outline-number]-title` (e.g., `33-makakamit-pa-kaya-natin-ang-tunay-na-katarungan`) — uses outline number since speakers may have few talks per year
- Files inside: simple names (`outline.md`, `index.md`, `summary.md`)
- Images: `picture.jpg` or `picture-1.jpg`, `picture-2.jpg` (if multiple)
- Use lowercase and hyphens for folder names

**Navigation Sorting:**
- **10-Minute Talks:** Latest first (newest at top) in `mkdocs.yml` nav
- **30-Minute Talks:** Leave as is (few per year)

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

**==Key phrase from outline==** — [explanation]

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

**IMAGE CUE: picture.jpg**

Ngayon naman po, tingnan natin ang larawan.

*[Ipakita ang larawan]*

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
- The exact words from the outline's main points MUST appear in the script sentences (wrapped in `**==highlight==**` — bold + highlight using `pymdownx.mark`)
- Don't paraphrase or rephrase the outline — use the outline's own words
- These phrases should be woven naturally into the flow, not just in headings

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
2. Show: `*[Ipakita ang larawan]*`
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
- Match struggles to relevant Aralin (see diagnostic mapping)
- Incorporate specific techniques from chosen Aralin

**Step 6: Time Check**
- 5 min: ~750 words
- 10 min: ~1,500 words
- 30 min: ~4,500 words
- Adjust content to fit, prioritize susing teksto

**Step 7: Review Against Guidelines**
- Positive tone? (Aralin 16)
- Clear structure? (Aralin 14, 17)
- Practical application? (Aralin 13)
- Heart-reaching? (Aralin 19)

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

---

## Field Ministry Scripts

For Bible study demonstrations and other field ministry assignments.

### Folder Structure

**Published script** (in `docs/`):
```
docs/field-ministry/
  MMDD-title-Xmin/index.md          # script (published)
```

**Non-published outline** (root-level):
```
field-ministry/
  MMDD-title-Xmin/outline.md        # reference content + notes
```

### Script Creation Workflow

**Step 1: Intake**
- Collect: reference (lff aralin, etc.), time limit, counsel point (lmd aralin)
- Ask for: actual Bible verse text, character names

**Step 2: Create outline.md**
- Copy full reference content from publication
- Include all questions from the book
- Add actual Bible verse text (ask user to provide)
- Note if there are pictures with captions
- Add notes section (time constraints, setting, what to skip)

**Step 3: Draft Script**
- Use JW/HH format with character names in header
- Mostly Tagalog, basic English lang (okay, sure, exactly, video, picture)
- Explicitly say "Panoorin natin yung video" then "nakita natin yung video" (skip watching)
- Use questions directly from the publication
- Include picture discussion with caption if applicable
- Address householder by name for natural flow
- Follow counsel point guidelines (e.g., aralin 11 #3 = short explanations)

**Step 4: Review**
- Check Bible verses match actual NWT Tagalog text
- Verify questions align with publication
- Ensure timing fits (4 min = skip prayer, skip video watching)

### Script Format

```markdown
---
title: Title (X min)
---

**Setting:** Bible Study (ongoing)
**Reference:** lff aralin X: #X-X
**Counsel point:** lmd aralin X: #X
**Characters:** JW = [Name], HH = [Name]

---

## Script

**JW:** [dialogue]

**HH:** [dialogue]

---

## Notes

- [Key reminders]
```

### Reference Files

- **reference/ministeryo-aralin.md** — Counsel points from "Maging Mahusay sa Ministeryo at sa Pagtuturo" (lmd)

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
3. Claude reads `outline.md` and creates `docs/espirituwal-na-hiyas/MMDD-title/index.md`

### MANDATORY — Bible Text Accuracy

- **NEVER** paraphrase, assume, or search for Bible text
- **ALWAYS** use the EXACT words from the user's `outline.md` (which contains NWT Tagalog text copied from their Bible)
- Strip footnote markers (single lowercase letters appearing as superscripts after words: e.g., `bisiga` → `bisig`, `kami.c` → `kami.`) but keep every word exact
- If Bible text is not in the outline, **ASK the user** to provide it — do not guess
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
- Closing: always ends with the standard closing script (salamat, huling komento, paumanhin, balik sa chairman)
- References from `outline.md` are NEVER published — only the highlights/summaries appear in the script
- No timing markers in the script (conductor uses phone timer)

### Navigation Sorting

Latest first (newest at top) in `mkdocs.yml` nav — same as 10-Minute Talks.

---

## Notion Integration

### /10minute Command
Push 10-minute talk scripts to Notion using the `/10minute` skill.

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

**Adding a New Talk:**

When adding a new talk:
1. Create the folder and `index.md` under `docs/talks/`
2. Add the nav entry in `mkdocs.yml` under the appropriate section

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

---

## Pre-Commit Workflow

**Before committing/pushing to git, always:**

1. **Update `CHANGELOG.md` (REQUIRED):**
   - Add entry under the current version or create a new version section
   - Describe what changed and why
   - Use format: `## [X.X.X] - YYYY-MM-DD` with `Added`, `Changed`, `Removed` subsections

2. **Update documentation if needed:**
   - `CLAUDE.md` — Update if workflow or skills changed
   - `README.md` — Update if user-facing instructions changed
   - `.claude/skills/*.md` — Update if skill behavior changed

3. **Review changes:**
   - Check modified files make sense
   - Ensure no secrets (API keys) are being committed
   - Verify `config.json` is in `.gitignore`

4. **Commit with clear message:**
   - Describe what changed and why
   - Use conventional format if applicable

---

## Key Guidelines to Remember

- **Public talk scope only** — not for Bible reading assignments
- **Visual aids**: Pictures only, no videos unless instructed by org; use for teaching, not decoration
- **Text handling**: Explain → Illustrate → Apply (ipaliwanag → ilarawan → ipakita kung paano isasabuhay)
- **Scripture intro**: Prep the mind before reading (tanong or what to look for)
- **Tone**: Positive and upbuilding; avoid insults or harmful jokes
- **Delivery**: Speak from heart, not read; practice aloud
- **Audience adaptation**: Adjust wording based on bisita vs kapatid ratio
- **Natural Taglish**: Use common English words naturally mixed with Tagalog (e.g., "lip service," "shortcut," "proud") — this reflects how Filipinos actually speak and makes the talk more conversational
- **No formal greetings**: Skip "Mga kapatid at mga kaibigan, magandang gabi po sa inyong lahat" — jump straight into the hook
- **Generic reference citations**: Use "Base sa referensya natin" instead of specific publication names (e.g., "Ayon sa Bantayan") — sounds more natural and less like reading from a script
- **Memorable formula (optional)**: When possible, create a simple equation or phrase that captures the main point (e.g., "Labi + Puso = Tunay na Pagsamba"). Introduce it in the intro, reinforce at key moments, and drive it home in the conclusion. This helps the message stick.
- **MANDATORY — Bible text accuracy**: NEVER paraphrase, assume, or search for Bible text. ALWAYS use the EXACT words from the user's `outline.md` (NWT Tagalog). Strip footnote markers only. If Bible text is unavailable, ASK the user — do not guess.

