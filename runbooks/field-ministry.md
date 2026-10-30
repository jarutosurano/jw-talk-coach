# Field Ministry Scripts

> Moved verbatim from `CLAUDE.md` on 2026-10-30 (instruction-budget fix). The hard rules (never/must) are also kept in `CLAUDE.md`; if the two ever differ, `CLAUDE.md` wins. Add new procedures, templates and lookup rows here, not in `CLAUDE.md`.

---

## Field Ministry Scripts

For Bible study demonstrations and other field ministry assignments.

### Folder Structure

**Published script** (in `docs/`):
```
docs/field-ministry/
  MMDD-short-title/index.md         # script (published)
```

**Non-published outline** (root-level):
```
field-ministry/
  MMDD-short-title/outline.md       # questions, short excerpts, notes
```

### Script Creation Workflow

**Step 1: Intake**
- Collect: reference (lff aralin, etc.), time limit, counsel point (lmd aralin)
- Ask for: character names (Bible verse text: read it from the NWT PDF — see `runbooks/reference-library.md`)

**Step 2: Create outline.md**
- Save the full lesson text to `reference/articles/lff-aralin-NN.md` (git-ignored); put only the questions and short cited excerpts in `outline.md` (the repo is public)
- Include all questions from the book
- Add the exact NWT text for each cited verse (column crop; see CLAUDE.md "Bible text")
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
