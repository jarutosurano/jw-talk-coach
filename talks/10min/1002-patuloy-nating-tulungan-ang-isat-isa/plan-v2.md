# v2 Script — "Patuloy Nating Tulungan ang Isa't Isa" — Design + Plan

> **For agentic workers:** Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** A from-scratch v2 script (8 minuto, ≈1,050–1,100 words incl. Bible reading) that delivers the 3 workbook points + "Tanungin ang Sarili" with room for pauses and gestures.

**Architecture:** New skeleton — not v1's. The whole talk hangs on one observation from the account: **in all three examples, the help was given through words.** Each point = one "voice":

| Punto | Outline wording (exact) | Ang "boses" | Sino → kanino |
|---|---|---|---|
| 1 | Ipagtanggol ang iba gaya ng ginawa ni Ebed-melec | Magsalita **para sa** kapatid | Ebed-melec → hari |
| 2 | Patibayin ang iba gaya ng ginawa ni Jeremias | Magsalita **sa** kapatid | Jeremias → Ebed-melec |
| 3 | Pasiglahin ang iba na sundin si Jehova gaya ng ginawa ni Jeremias | Magsalita **nang may "pakisuyo"** | Jeremias → Zedekias |

Refrain per section: *"Ano ang sinabi niya?"* → then *"Ano po ang matututuhan natin dito, mga kapatid?"*
New-learning beat (Aralin 18/19): w26.07 ¶7 question **"Ano ang itinuturo nito sa akin tungkol kay Jehova?"** applied to Jer 39:15-18 — and repeated in the conclusion so it isn't forgotten.

**Files:**
- Create: `docs/talks/10min/1002-patuloy-nating-tulungan-ang-isat-isa/v2.md` (published — v1 `index.md` untouched)
- Modify: `mkdocs.yml` nav — add `Patuloy Nating Tulungan ang Isa't Isa (v2)` above v1
- Modify: `CHANGELOG.md` — new `4.34.0` entry

## Global Constraints

- Exact outline wording in headers and once as `**==highlight==**` per section intro; bold-only elsewhere.
- Read ONLY outline texts: Jer 38:7-9, Jer 39:15-18, Jer 38:20 (current NWT, verified p. 1247/1249). Background (38:4-6, 10-13, 19) = explanation only, never read.
- No off-outline scriptures read (memory: outline-scriptures-only).
- "ngayong gabi"; no formal greeting; open with a hook, theme revealed after (memory: intro-and-acronyms).
- Normal spoken prose, < 10 `{pause}`, no manufactured emotion (memory: no-storytelling-mode).
- Every text: "Buksan po natin…" + what to look for → read → repeat key words (guidelines #13, Aralin 4/6).
- Image pattern: call attention → figure → rhetorical question → describe → caption → apply → `*Salamat po sa picture.*`
- Green `<mark class="green">` for spoken section headings in transitions.
- "Base sa referensya natin" — no publication names spoken.

## Timing budget (8:00)

| Section | Time | Words | Aralin featured |
|---|---|---|---|
| INTRO | 0:45 | ~110 | 1, 3, 14 |
| 1 — Ipagtanggol + Picture 1 | 2:30 | ~330 | 4, 7, 9, 13 |
| 2 — Patibayin + Jehova lens + Picture 2 | 2:30 | ~340 | 18, 19, 9, 8 |
| 3 — Pasiglahin | 1:00 | ~140 | 3, 19 |
| TANUNGIN ANG SARILI + CONCLUSION | 1:15 | ~170 | 13, 14, 20 |

## Review Focus (accuracy traps — Aralin 7)

1. Ebed-melec = "banyaga, pero tunay na lingkod at kaibigan ni Jehova." Never "proselita"/"tuli"; skip "bating" (Aralin 17).
2. Jehova's traits (mapagpahalaga, makatarungan, hindi nagtatangi) are FROM w26.07 ¶13; any verse-to-trait link is framed as our reasoning ("Pansinin…"), not "sabi ng artikulo."
3. The king *ordered* the 30 men (38:10); the officials *asked* for death (38:4); Zedekias said "Kayo na ang bahala sa kaniya" (38:5). No "in public" embellishment.
4. Use current-NWT wording of 38:20 ("Pakisuyo, makinig ka sa tinig ni Jehova"), not jr's old "Sundin mo, pakisuyo."
5. w20.09 ¶17 scenario: "ginagawa naman ng sister ang buong makakaya niya… hindi siya ang nasusunod" — don't exaggerate.

---

### Task 1: Draft v2 script

**Files:** Create `docs/talks/10min/1002-patuloy-nating-tulungan-ang-isat-isa/v2.md`

- [ ] Frontmatter `title: 'Patuloy Nating Tulungan ang Isa''t Isa (v2)'`, date `Oct 2, 2026`, `---` between all sections.
- [ ] INTRO hook: "Naranasan mo na bang pag-usapan nang mali… at may isang nagsabi, 'Hindi po ganoon. Kilala ko siya'?" → theme → preview the three "voices."
- [ ] Punto 1: brief background (38:4-6 as explanation) → read 38:7-9 → key words "napakasama ng ginawa" → reasoning questions → Picture 1 → application from w20.09 ¶17.
- [ ] Punto 2: Ebed-melec afraid (w19.11 ¶17, jr kab. 7 ¶19) → read 39:15-18 → "Ano ang itinuturo nito sa akin tungkol kay Jehova?" → Picture 2 → "simpleng mga salita na mula sa puso."
- [ ] Punto 3: Zedekias afraid (38:19 explanation) → read 38:20 → "Pakisuyo" → application.
- [ ] TANUNGIN ANG SARILI (exact wording) + CONCLUSION recap of three voices + Jehova-lens + call to action.
- [ ] Bottom: `## CHECKLIST NG ARALIN` (all 12 requested Aralin → where applied) + optional extra (karanasan ng sulat) for if time remains.

### Task 2: Verify

- [ ] Word count of spoken text 1,000–1,150: `sed '/^## CHECKLIST/,$d' v2.md | wc -w`
- [ ] Bible quotes diff against outline.md Bible Texts (exact match).
- [ ] Grep for Review Focus traps: `grep -n -i -E "proselita|tuli|bating|Sundin mo, pakisuyo|ayon sa Bantayan" v2.md` → expect no hits.
- [ ] `mkdocs build --strict` passes (or no new warnings).

### Task 3: Publish

- [ ] Add nav entry in `mkdocs.yml`; add CHANGELOG `4.34.0`.
- [ ] Commit (plan + outline notes + v2 + nav + changelog) and `git push` to `main` → GitHub Pages deploys.
