# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## 🚀 New Session? Start Here!

1. **Check `README.md`** for quick start guide
2. **Check `talks/` folder** for existing and new talks
3. **Ask user:** "Anong talk po ang gagawin natin ngayon?"

---

## Project Overview

This is a JW Public Talk Coaching System—a Tagalog-language knowledge base for helping speakers prepare and deliver effective public talks (pahayag pangmadla). It is a documentation-based project with no build/test infrastructure.

## File Structure

- **public-talk-aralin.md** — Training curriculum with 15 lessons (Aralin 1, 3, 4, 6-9, 13-14, 16-20) for public talk development. Aralins 2, 5, 10, 11, 12, 15 are intentionally excluded—they cover Bible reading or other assignments not relevant to public talks.
- **guidelines.md** — Official speaker guidelines (S-141-TG) covering outline usage, visual aids, and delivery techniques.
- **.claude/skills/jw-pagbabasa-at-pagtuturo.md** — Claude AI skill definition for coaching public talks.

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

```
/talks/
  /5min/
    /MMDD-title/                    # e.g., 0131-paano-maging-masaya
      outline.md
      index.md

  /10min/
    /MMDD-title/                    # e.g., 0124-siya-ang-ating-diyos
      outline.md
      index.md
      summary.md
      picture.jpg                   # if applicable

  /30min/
    /MMDD-title/                    # e.g., 0202-pag-ibig-ni-jehova
      outline.md
      references.md                 # separate (can be lengthy)
      index.md
      picture-1.jpg                 # optional
      picture-2.jpg
```

**Naming Convention:**
- Talk folders: `MMDD-short-title` (e.g., `0124-siya-ang-ating-diyos`)
- Files inside: simple names (`outline.md`, `index.md`, `summary.md`)
- Images: `picture.jpg` or `picture-1.jpg`, `picture-2.jpg` (if multiple)
- Use lowercase and hyphens for folder names

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

**Step 4a: Script Formatting Standards (for Notion)**
Follow this format for consistency and proper Notion conversion:

```markdown
# Script: "Talk Title Here"

---

## INTRO [1 minuto]

[Content here...]

---

## PUNTO 1: Full outline text here [2 minuto]

### Teksto: Book X:X

[Intro before reading...]

*[Basahin ang Book X:X]*

> "Scripture quote here..."

**{Key phrase from outline}** — [explanation]

---

## IMAGE [pagkatapos ng Punto X]

**IMAGE CUE: picture.jpg**

[Image discussion...]

---

## CONCLUSION [1 minuto]

[Content here...]
```

| Element | Format | Example |
|---------|--------|---------|
| Title | `# Script: "Title"` | `# Script: "Siya ang Ating Diyos!"` |
| Section headers | `## SECTION [X minuto]` | `## INTRO [1 minuto]` |
| Punto headers | Full outline text | `## PUNTO 1: Nagalit si Isaias... [2.5 minuto]` |
| Read cues | Italic with brackets | `*[Basahin ang Isaias 29:13]*` |
| Scripture quotes | Blockquote | `> "Scripture text..."` |
| Outline phrases | Bold with curly braces | `**{masunurin mula sa puso}**` |
| Image cue | Bold | `**IMAGE CUE: picture.jpg**` |

**Step 4b: Handle Visual Aids (Images)**
- **10-min talks:** Images required — must include in script
- **30-min talks:** Images optional — include if specified in outline
- Script template for introducing image:

```markdown
## IMAGE [pagkatapos ng Punto X]

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

```
/field-ministry/
  /MMDD-title-Xmin/                 # e.g., 0130-paggawa-ng-mga-alagad-4min
    outline.md                       # reference content + notes
    index.md                         # script
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
# Title (X min)

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

- **ministeryo-aralin.md** — Counsel points from "Maging Mahusay sa Ministeryo at sa Pagtuturo" (lmd)

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
- Outline phrases (exact words from outline) should use **{curly braces}** format: `**{outline phrase here}**`
- This renders as bold text with braces in Notion, so you know it's from the outline
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
- GitHub Pages automatically serves `index.md` as the default page for a folder

**Setup (one-time):**
1. Go to repo Settings → Pages
2. Source: Deploy from a branch
3. Branch: `main`, folder: `/ (root)`
4. Save — site will be live in a few minutes

**Notes:**
- Repo must be **public** for free GitHub Pages
- Private repos require GitHub Pro ($4/mo) for Pages

**Updating Homepage Navigation:**

When adding a new talk, update `/index.md` to add it to the navigation table:

1. Open `/index.md`
2. Find the appropriate section (30-Minute or 10-Minute Talks)
3. Add a new row at the TOP of the table (latest first, oldest last)
4. Format: `| Mon DD | Talk Title | [View Script](./talks/XXmin/MMDD-folder-name/) |`

Example:
```markdown
## 10-Minute Talks

| Date | Title | Link |
|------|-------|------|
| Feb 06 | New Talk Title | [View Script](./talks/10min/0206-new-talk/) |  ← ADD NEW TALKS HERE
| Jan 30 | Parangalan si Jehova... | [View Script](./talks/10min/0130-parangalan-si-Jehova/) |
| Jan 24 | Siya ang Ating Diyos! | [View Script](./talks/10min/0124-siya-ang-ating-diyos/) |
```

**Order:** Latest to oldest (newest talks at the top)

---

## Pre-Commit Workflow

**Before committing/pushing to git, always:**

1. **Update documentation if needed:**
   - `CLAUDE.md` — Update if workflow or skills changed
   - `README.md` — Update if user-facing instructions changed
   - `.claude/skills/*.md` — Update if skill behavior changed

2. **Review changes:**
   - Check modified files make sense
   - Ensure no secrets (API keys) are being committed
   - Verify `config.json` is in `.gitignore`

3. **Commit with clear message:**
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
- **Always ask for actual Bible text**: Never assume or use memorized scripture wording. Always ask the user to provide the exact Bible verse from their copy (NWT Tagalog). Scripture wording must be accurate.

