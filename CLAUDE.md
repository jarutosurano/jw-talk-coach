# CLAUDE.md

Guidance for Claude Code in this repo. This file holds only the hard rules and a routing table. Procedures,
templates and lookup tables live in `runbooks/` (see "Which runbook to read first").

## New session? Start here

1. **Check `README.md`** for the quick start guide.
2. **Check `docs/talks/`** for existing and new talks.
3. **Ask the user:** "Anong talk po ang gagawin natin ngayon?"

## Project

JW Public Talk Coaching System: a Tagalog-language knowledge base for preparing and delivering talks (pahayag
pangmadla), Espirituwal na Hiyas, CBS, Watchtower answers and field-ministry demos. Built with MkDocs Material
(`mkdocs serve` for local preview, `mkdocs build` to build); published to GitHub Pages from `docs/`. The repo is public.

## Which runbook to read first (MUST)

Before you draft, edit, review or red-team anything in this table (even a one-line change), Read the whole runbook for
that task, then open the latest published file of the same type (`ls docs/<type>/ | sort | tail -1`) and match its
structure; if the two differ, follow the file and fix the runbook. When you hand work to a subagent or reviewer, name the
runbook it must read. If this file and a runbook disagree, this file wins.

| Task | Read first |
|---|---|
| 5, 10 or 30-minute talk (outline, script, summary.md, picture) | `runbooks/talks.md` |
| Espirituwal na Hiyas | `runbooks/hiyas.md` |
| CBS (Congregational Bible Study) | `runbooks/cbs.md` |
| Watchtower answer script | `runbooks/watchtower.md` |
| Field ministry demonstration or arrangement | `runbooks/field-ministry.md` |
| Coaching request ("public talk", "pahayag pangmadla", "coach me", "improve intro/ending", "fix outline/script") | `runbooks/coaching.md` |
| Stored books/PDFs, NWT page numbers, workbook weeks, stored articles (and adding new ones) | `runbooks/reference-library.md` |
| Nav entries, GitHub Pages, MkDocs features, Notion `/10minute` | `runbooks/publishing.md` |

## Where files go (publishing rule)

- **Only `index.md` scripts go in `docs/`** (published). Outlines, summaries and reference files stay in
  root-level folders and are NEVER placed in `docs/`.
- Published: `docs/talks/{5min,10min,30min}/*/index.md`, `docs/espirituwal-na-hiyas/*/index.md`, `docs/cbs/*/index.md`,
  `docs/watchtower/*/index.md`, `docs/field-ministry/*/index.md`, `docs/index.md` (homepage). Pictures sit next to
  their `index.md` (`picture.jpg`, `picture-1.jpg`, …).
- Not published (root level, same folder name): `talks/…/outline.md, summary.md`, `espirituwal-na-hiyas/…/outline.md`,
  `cbs/…/outline.md`, `watchtower/…/outline.md`, `field-ministry/…/outline.md`, `runbooks/`, and `reference/`:
  `public-talk-aralin.md` (teaching Aralin), `guidelines.md` (S-141-TG), `ministeryo-aralin.md` (lmd counsel points),
  `mahalin-ang-mga-tao.md` (lmd notes), `jr-overview.md` (check first for any Jeremiah talk). The coaching skill is
  `.claude/skills/jw-pagbabasa-at-pagtuturo/SKILL.md`; the Notion push command is `.claude/commands/10minute.md`.
- Folder names: talks/Hiyas/CBS/field ministry `MMDD-short-title` (MMDD = meeting date; lowercase, hyphens);
  30-min `[outline-number]-title`; Watchtower a short title slug (per-type examples in the runbooks). Files inside: `outline.md`, `index.md`, `summary.md`.
- **Every published `.md` needs YAML frontmatter** (`title: 'Your Title Here'`), and every new page needs a nav entry
  in `mkdocs.yml` (`nav:` defines the labels). 10-min, 5-min, Hiyas, CBS and Watchtower: latest first. 30-min: leave as is.

## Copyrighted material and secrets: NEVER commit or publish

- `reference/books/` (full publication PDFs, workbook RTF/TXT) and `reference/articles/` (full article texts) are
  git-ignored and local-only. Never commit or publish them, and never paste their full text into tracked files: the repo
  is public. Only short cited excerpts go into committed outlines.
- When the user downloads a publication PDF and asks to store it, copy it to `reference/books/` (full article texts go to
  `reference/articles/`) and add a row to `runbooks/reference-library.md`.
- Never commit secrets or API keys; `scripts/config.json` (Notion key) must stay git-ignored.

## Bible text: MANDATORY

- **NEVER paraphrase, assume, or search for Bible text.** Use the EXACT NWT Tagalog (makabagong-wika) from the user's
  `outline.md`. If it isn't there, read it from `reference/books/nwt-bagong-sanlibutang-salin.pdf`. Ask the user only
  if reading the PDF fails; never guess.
- That PDF needs column-cropped extraction (plain `pdftotext` interleaves cross-references and is unusable). Read the left
  column, then the right; printed page = PDF page; known pages are in `runbooks/reference-library.md`;
  for an unknown page, grep the running header (e.g. `JEREMIAS 50:`) in `pdftotext -layout` output.
  - Left: `pdftotext -f PAGE -l PAGE -x 8 -y 0 -W 128 -H 520 reference/books/nwt-bagong-sanlibutang-salin.pdf -`
  - Right: `pdftotext -f PAGE -l PAGE -x 164 -y 0 -W 145 -H 520 reference/books/nwt-bagong-sanlibutang-salin.pdf -`
- Strip footnote markers (`bisiga` → `bisig`, `kami.c` → `kami.`) and stray cross-reference digits; keep every word exact.
- Verses quoted inside it/w/wcg often use an older edition or a paraphrase: attribute that wording to its source, or
  use the exact NWT crop.
- All publications and references come from jw.org data.

## Talk scripts: MANDATORY (5, 10, 30 min; full format in `runbooks/talks.md`)

- **Exact outline wording:** the outline's main-point words must appear word for word (don't paraphrase; elders may
  follow along), woven into the spoken flow, not just the headings. `**==highlight==**` them once,
  when the point is introduced; reuse them elsewhere (application, conclusion, summary) as **bold only**. Bible-text
  phrases, the formula and the talk title are also bold only.
- **Mention the talk title in the intro.** Open with a hook (question, story or analogy); no formal greeting.
- **Scripture transitions:** before every reading, "Buksan po natin ang [Book] kabanata X, bersikulo Y." plus what to
  look for; returning to a text: "Balikan po natin ang [Book] X:X, pansinin naman ang…". Each point follows REIA (Read,
  Explain, Ilarawan, Apply).
- **Bible text format:** `!!! quote "Book X:X"` admonition for every scripture reading in talks (not blockquotes).
- **Image transitions:** "Ngayon naman po, tingnan natin ang larawan." → `<figure markdown="span">` with caption →
  "Ano po ba ang nakikita natin dito, mga kapatid at mga kaibigan?" → describe and connect → read the caption → apply.
- **Talks vs Hiyas:** in talks (5, 10, 15, 30 min) WE are the speaker: no audience interaction, and we read every
  scripture ourselves; never "sino po ang gustong bumasa?" (Hiyas only, where we conduct).
- **10-min format (must):** follow Step 4a in `runbooks/talks.md` exactly: `## INTRO [1 minuto]`, `## N — full outline
  text [X minuto]` (no "PUNTO"), `---` between every section, `## IMAGE` + `**IMAGE CUE: picture.jpg**` only if the
  outline has an image, `## CONCLUSION [1 minuto]`.
- **Dual reference:** prepare every talk with BOTH `reference/guidelines.md` (S-141-TG: how to deliver) AND
  `reference/public-talk-aralin.md` (Pagtuturo: what to focus on). Never rely on just one.
- **Outline template:** every new `outline.md` (any talk type) has HTML comment guides in `## Outline`, `## References`,
  `## Bible Texts`, `## Image`, `## Notes` (see `runbooks/talks.md`).
- Friday OCLM = "ngayong gabi"; Sunday public talk = "ngayong umaga". Date line `Mon DD, YYYY`. Word targets: `runbooks/talks.md`
  Step 6 (Jayr's pace, not the generic rate: a 10-min script is ~1,165 spoken words).

## Other deliverables: MANDATORY (details in the runbooks)

- **Hiyas:** Tanong 1 heading = the exact workbook question with its scripture and publication reference; Tanong 2
  heading = always the exact same question; Bible text never paraphrased (intro, Tanong 1, gems); top 10 gems; standard
  closing; no timing markers; the outline's references are never published.
- **Hiyas handang sagot (from Oct 23, 2026):** at least 2 `!!! success` spoken answers below the gems: reference + key
  phrase only (exact NWT, not the whole verse), then what I learned and how I apply it (ako/ko). Real talk, no forced
  analogy, nothing OA; ~45-60 words; avoid verses the same week's talk uses.
- **CBS:** exact workbook questions word for word; no timing markers; no "Para ilarawan" section.
- **Watchtower (since Aug 23, 2026):** the full answer format in `runbooks/watchtower.md` is mandatory; the user is an
  audience member, not the conductor; no timing markers; Bible quotes: only quote text that appears verbatim in the
  article, the outline, or an NWT column crop; never paraphrase NWT text from memory.

## Key guidelines for talks (5, 10, 30 min)

- **Coaching scope:** talks only; not for Bible reading (pagbabasa) assignments.
- **Visual aids:** pictures only, no videos unless instructed by the org; use them for teaching, not decoration.
- **Text handling:** Explain → Illustrate → Apply (ipaliwanag → ilarawan → ipakita kung paano isasabuhay).
- **Scripture intro:** prep the mind before reading (a tanong, or what to look for).
- **Tone:** positive and upbuilding; avoid insults or harmful jokes. **Delivery:** speak from the heart, not read; practise aloud.
- **Audience adaptation:** adjust wording to the bisita vs kapatid ratio.
- **Natural Taglish:** common English words mixed naturally into Tagalog (e.g. "lip service", "shortcut", "proud").
- **No formal greetings:** skip "Mga kapatid at mga kaibigan, magandang gabi po sa inyong lahat"; jump straight into the hook. (Hiyas and CBS keep their conductor greeting.)
- **Generic reference citations:** "Base sa referensya natin", not publication names such as "Ayon sa Bantayan".
- **Formula or acronym: rare, never the default** (Jayr 2026-11-01: talks became a pattern, "no longer unique"). Use one
  only when the outline's points genuinely suggest it. Before drafting, check the last 3 published talks and never reuse
  their device (formula, acronym, hook type, "unang punto" framing).

## Pre-commit workflow

**Before committing/pushing to git, always:**

1. **Update `CHANGELOG.md` (REQUIRED):** add an entry under the current version or a new `## [X.X.X] - YYYY-MM-DD`
   section with `Added` / `Changed` / `Removed`, saying what changed and why.
2. **Update documentation if needed:** this file or `runbooks/*.md` (workflow or rules), `README.md` (user-facing
   instructions), `.claude/skills/*/SKILL.md` and `.claude/commands/*.md` (skill/command behavior). If a commit
   changes a deliverable's structure, update that runbook's template in the same commit.
3. **Review changes:** files make sense; no secrets (API keys); `config.json` still in `.gitignore`.
4. **Commit with a clear message** saying what changed and why (conventional format if applicable).

## Keeping this file small

- Budget: ≤200 lines and ≤20 KB, checked by `~/.claude/scripts/claude-budget.sh`. Run it after editing this file.
- Only never/must rules and rules born from an incident belong here, one or two lines each. Everything else (new
  procedures, templates, NWT page rows, stored-book and article rows) goes into the matching runbook.
- The pre-split version is kept locally as `CLAUDE.md.bak-2026-10-30` (git-ignored), and in git history.
