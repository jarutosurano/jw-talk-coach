# Reference Library — books, exact NWT text, stored articles

> Moved verbatim from `CLAUDE.md` on 2026-10-30 (instruction-budget fix). The hard rules (never/must) are also kept in `CLAUDE.md`; if the two ever differ, `CLAUDE.md` wins. Add new procedures, templates and lookup rows here, not in `CLAUDE.md`.

---

### Reference Books (`reference/books/`)

Full copyrighted JW publication PDFs are stored here for research/citation. This folder is **git-ignored** (`.gitignore`: `reference/books/`) so the PDFs stay local and are **never committed or published**. When the user downloads a publication PDF and asks to store it, copy it here.

**Naming convention:** `[publication-symbol]-[title-slug].pdf` (e.g., `lmd-mahalin-ang-mga-tao-gumawa-ng-mga-alagad.pdf`, `jr-mensahe-ng-diyos-sa-pamamagitan-ni-jeremias.pdf`). Periodicals keep the jw.org filename: `w_TG_YYYYMM.pdf`, `mwb_TG_YYYYMM.pdf`. A study-edition issue is studied ~2 months later (Hunyo → Ago 10–Set 6); put the study-week range in the row. Download: `https://b.jw-cdn.org/apis/pub-media/GETPUBMEDIALINKS?pub=w&issue=YYYYMM&fileformat=PDF&langwritten=TG&output=json` → the `w_TG_YYYYMM.pdf` URL.

**Currently stored:**
| Symbol | Title | File |
|--------|-------|------|
| lmd | Mahalin ang mga Tao—Gumawa ng mga Alagad (Love People, Make Disciples) | `lmd-mahalin-ang-mga-tao-gumawa-ng-mga-alagad.pdf` |
| jr | Mensahe ng Diyos sa Pamamagitan ni Jeremias | `jr-mensahe-ng-diyos-sa-pamamagitan-ni-jeremias.pdf` |
| w | Ang Bantayan (Pag-aaral) Enero 2026 | `w_TG_202601.pdf` |
| w | Ang Bantayan (Pag-aaral) Hunyo 2026 | `w_TG_202606.pdf` |
| w | Ang Bantayan (Pag-aaral) Hulyo 2026 — study articles Setyembre 7–Oktubre 4, 2026 | `w_TG_202607.pdf` |
| w | Ang Bantayan (Pag-aaral) Agosto 2026 — study articles Oktubre 5–Nobyembre 1, 2026 (downloaded Oct 30 via jw.org pub-media API) | `w_TG_202608.pdf` |
| w | Ang Bantayan (Pag-aaral) Setyembre 2026 — study articles Nobyembre 2–Disyembre 6, 2026 (downloaded Nov 6 via jw.org pub-media API) | `w_TG_202609.pdf` |
| w | Ang Bantayan (Pag-aaral) Agosto 2020 — Araling Artikulo 33 "Pagkabuhay-Muli—Patunay ng Pag-ibig, Karunungan, at Pagtitiis ng Diyos" (Blg. 184 research) | `w_TG_202008.pdf` |
| wcg | Lakas-Loob na Lumakad Kasama ng Diyos (Walk Courageously With God) — **current CBS book**, 54 kabanata | `wcg-lakas-loob-na-lumakad-kasama-ng-diyos.pdf` |
| nwt | Bagong Sanlibutang Salin ng Banal na Kasulatan (makabagong-wika) — source for exact NWT Tagalog Bible text | `nwt-bagong-sanlibutang-salin.pdf` |
| mwb | Workbook Para sa Pulong — Setyembre-Oktubre 2026 (Sep 7–Nov 1; Jeremias 32-48) | `mwb_TG_202609.pdf` + `mwb-rtf/202609/*.rtf` |
| mwb | Workbook Para sa Pulong — Nobyembre-Disyembre 2026 (Nov 2–Ene 3; Jeremias 49–Ezekiel 10) | `mwb_TG_202611.pdf` + `mwb-rtf/202611/*.rtf` |
| S-34 | Public talk outline Blg. 21 "Pahalagahan ang Papel Mo Bilang Sakop ng Kaharian" (30 min, 4/18). Speaker outline, not on jw.org; stored Nov 2, 2026. Its first point uses the same Dan 2:44 + Mat 6:9, 10 as lmd apendise A #21 | `s34/S-34_TG_021.docx` + `.txt` |

**Workbook (mwb) tip:** `_00` is the first week, not a cover file (`202609_00` = Sep 7-13, `202611_00` = Nov 2-8).
Read text from the RTF conversions in `reference/books/mwb-rtf/txt/`
(one file per week, e.g. `mwb_TG_202609_04.txt` = Okt 5-11). They include every quoted Bible
text and reference paragraph verbatim. To regenerate:
`textutil -convert txt -output txt/NAME.txt 202609/NAME.rtf`. Use the PDF only to pull
pictures (`pdfimages -j -f PAGE -l PAGE`). The PDF pictures are small (~356 px wide); for a talk picture,
take the 1200 px copy from wol instead: find the week's page by phrase search (Nov 2-8, 2026 = doc `202026401`; the docids run in week order, so Nov 9-15 = `202026402`),
grep its HTML for `/tl/wol/mp/r27/lp-tg/mwb26/2026/NNN` links, and download them (the larger file is the picture).

### Reading Exact Bible Text (`nwt-bagong-sanlibutang-salin.pdf`)

**The full NWT Tagalog Bible is stored locally, so exact Bible text can be READ directly —
no need to ask the user for it, and never paraphrase from memory.**

File: `reference/books/nwt-bagong-sanlibutang-salin.pdf` (git-ignored, local only).
Edition: **makabagong-wika** — the same edition the wcg book and current publications quote.
Verified: Gen. 22:2 matches the wcg book word-for-word.

**IMPORTANT — this PDF needs column-cropped extraction.** The page layout is three columns
(text | cross-references | text). A plain `pdftotext` or `pdftotext -layout` interleaves the
verse text with cross-reference fragments and produces unusable output. Crop by column
geometry instead:

```bash
# Left text column
pdftotext -f PAGE -l PAGE -x 8   -y 0 -W 128 -H 520 reference/books/nwt-bagong-sanlibutang-salin.pdf -
# Right text column
pdftotext -f PAGE -l PAGE -x 164 -y 0 -W 145 -H 520 reference/books/nwt-bagong-sanlibutang-salin.pdf -
```

Read the left column first, then the right, then concatenate. Printed page number == PDF page
number, so to find a passage: `pdftotext -layout` the whole file once, grep for a distinctive
phrase, then locate the page via its running header (e.g. `GENESIS 21:32-22:14`).

**Known page locations** (add to this as they are found):

| Passage | Page(s) |
|---------|---------|
| Genesis 22:1-19 | 71-72 |
| Exodo 1:1-16 | 125 |
| Exodo 1:17–2:11 | 126 |
| Exodo 15:16–16:3 | 148 |
| Gawa 7:5-24 | 1677 |
| Mikas 6:3-14 | 1441 |
| Hebreo 11 (v. 8-25) | 1847 |
| Jeremias 39:10–41:18 | 1249-1251 |
| Jeremias 23:25–24:1 | 1221 |
| Deuteronomio 8:1-18 | 325 |
| Exodo 3:6–4:16 | 128-129 |
| Exodo 7:10–8:2 (7:6, 7 sa p. 133) | 133-134 |
| Hebreo 11:26–12:1 | 1848 |
| Mateo 4:10 / 11:19 | 1488 / 1500-1501 |
| Juan 10:29 / 15:13 | 1645 / 1654 |
| Awit 118:2-22 | 966 |
| Kawikaan 4 / 13:20 / 19:3 | 1001 / 1015 / 1023 |
| Isaias 5:20 | 1080 |
| 1 Tesalonica 5:5-28 | 1813 |
| Santiago 4:8 | 1856 |
| 1 Hari 15:10-26 | 576 |
| Jeremias 42:1–44:30 | 1252-1256 |
| Bilang 13:23–14:31 | 269-271 |
| Exodo 23:2 | 159 |
| Josue 14:7-15 | 389 |
| Josue 6:10 | 375 |
| Jeremias 46:14-28 | 1258-1259 |
| Jeremias 46:27–49:7 (Jer 47-48) / 16:16–17:18 | 1259-1263 / 1209-1210 |
| Josue 1:17–3:9 / 4:10–5:4 / 6:6–7:6 | 370-371 / 373 / 375-376 |
| Daniel 2:41–3:3 / 6:28–7:20 | 1375 / 1384-1385 |
| Mateo 6:8-25 / Lucas 1:54-79 (1:79 sa 1573) | 1492 / 1572 |
| Isaias 60:21–61:9 / Apocalipsis 10:11–11:15 | 1165 / 1893 |
| Santiago 2:21–3:12 / Kawikaan 11:5-20 / Eclesiastes 3:4-22 / Efeso 4:24–5:12 | 1855 / 1011 / 1049 / 1794 |
| Jeremias 48:45–50:40 (Jer 49-50) / Lucas 21:34–22:19 | 1263-1269 / 1616 |
| Ruth 1:1–4:22 / Levitico 19:3-19 / Deuteronomio 24:13–25:6 | 444-449 / 225 / 348 |
| Awit 91:1–92:3 / Mateo 4:1-23 / Mateo 5:20-36 | 941 / 1488 / 1490 |
| Jeremias 50:41–52:34 (Jer 51-52) | 1270-1277 |
| Hukom 3:25–6:11 (Huk 4-5) | 411-415 |
| Awit 106:1-7 / Jeremias 23:1-13 / 2 Cronica 19:3–20:20 / 1 Hari 3:2-17 | 954 / 1219 / 710-711 / 550 |

**Always still strip footnote markers** — single lowercase letters trailing a word
(`bisiga` → `bisig`, `kami.c` → `kami.`) — and drop any stray cross-reference digits that
leak into the crop. Keep every actual word exact.

### Article Texts (`reference/articles/`)

Full text of individual articles the speaker supplies (pasted from JW Library, typed up, or
copied from a publication). This folder is **git-ignored** (`.gitignore`: `reference/articles/`)
for the same reason as `reference/books/` — the repo is public, so full copyrighted article
text stays local. Only short cited excerpts go into committed research/outline files.

**Naming:** `[publication-symbol][year]-[title-slug].md` (e.g. `w91-kayoy-binili-sa-halaga.md`).

**Currently stored:**
| Symbol | Title | Why |
|--------|-------|-----|
| w91 | Isang Katumbas na Pantubos Para sa Lahat | Blg. 184 Sek. 3 — "bakit hindi anghel," katumbas na pantubos, ilustrasyon ng pabrika |
| w91 | "Kayo'y Binili sa Halaga" | Blg. 184 Sek. 3 — **the verbatim "legal na karapatan sa buhay"**, and why the value had to be presented in heaven |
| w90 | Ano ba ang Kabuluhan sa Iyo ng Kamatayan ni Jesus? | Blg. 184 Sek. 3 — the rights attached to the life Adam lost; why "binuhay bilang espiritu" matters |
| wcg09 | wcg Kabanata 9 (Sipra, Pua, Amram, Jokebed, Miriam) — "Alamin" references (g04 4/8, it "Komadrona", w03 11/1, ijwia artikulo 7) | CBS Sep 21-27, 2026 — fetched from wol.jw.org Tagalog |
| wcg05 | wcg Kabanata 5 (Abraham) — "Alamin" references (g 5/12, it "Abraham", ia 26, rr 20, g88 4/8) | CBS Aug 24-30, 2026 — the four Alamin research answers |
| cl07 | cl kab. 7 "Pagbibigay ng Proteksiyon" (¶13-20) | 10-min talk Oct 9 — "Lagi Ba Tayong Pinoprotektahan ni Jehova sa Pisikal?" |
| jr | jr kab. 15 "Hindi Magawang Manahimik ni Jeremias" (¶16) | 10-min talk Oct 9 |
| w06 | "'Alagaan Mo ang Punong Ubas na Ito'!" (w06 6/15) | Hiyas Oct 9 Tanong 1 (Jer 40:12) |
| w26.08 | "Labanan si Satanas—Magtiwala kay Jehova at kay Jesus" | Watchtower Oct 5–11 |
| wcg11 | wcg Kabanata 11 (Moises) — Alamin + Tingnan Din references + chapter text | CBS Oct 5-11 |
| w25.07 | Araling Artikulo 28 "Bakit Kailangan Nating Humingi ng Payo?" | 10-min talk Oct 16 — "Humingi Sila ng Payo, Pero Hindi Sila Sumunod" (¶14 + context) |
| wcg12 | wcg Kabanata 12 (Caleb) — Alamin + Tingnan Din references | CBS Oct 12-18 |
| w25.07 | "Natutuhan Mo Na Ba ang 'Sekreto Kung Paano Maging Kontento'?" (p. 20-25) | 10-min talk Oct 23 — "Tinutulungan Tayo ng Pag-asa Natin Para Maging Kontento" (¶2, 8-9, 13-14) |
| wcg13 | wcg Kabanata 13 (Josue) — Alamin + Tingnan Din references | CBS Oct 19-25 |
| it / w24.05 | it "Moab, Mga Moabita" (full) + "Patuloy Tayong Nangangaral Dahil sa Pag-ibig!" | 10-min talk Oct 30 "Matuwid at Maawaing Hukom si Jehova" |
| wcg14 | wcg Kabanata 14 (Rahab) — Alamin + Tingnan Din references | CBS Oct 26–Nov 1 |
| w26.08 | "Pahalagahan ang 'Pribilehiyong Gumawa ng Sagradong Paglilingkod'" (p. 20-25) | Watchtower Oct 26–Nov 1 |
| lff/wp20/bhs | lff aralin 31, wp20 Blg. 1 p. 12-13, bhs kab. 8 — "Ano ang Kaharian ng Diyos?" | Pahayag Nov 13 (apendise A #21) |
| it / w08 | it "Kapangahasan" (full) + w08 6/15 p. 7-11 "Mga Bagay na Dapat Nating Takasan" | 10-min talk Nov 6 "Tulungan ang Iba na Makinabang sa Awa ni Jehova" |
| it | it "Bitag" (full) | Hiyas Nov 6 Tanong 1 (Jer 50:24) |
| wcg15 | wcg Kabanata 15 (Noemi at Ruth) — Alamin + Tingnan Din references (ia 39 ¶23 tlb., ia 47 ¶17-18, w16.11 3, w23.03 14, w21.11 8-13, ijwis artikulo 12) | CBS Nov 2-8 |
| w26.09 | "Magtiwalang Poprotektahan Ka ni Jehova" (p. 2-7) | Watchtower Nov 2-8 |
| wcg16 | wcg Kabanata 16 (Barak at Debora) — Alamin + Tingnan Din references (w15 8/1 12-13, w86 6/1 31, w05 1/15 25, w17.04 28-32, w03 11/15 28-31) | CBS Nov 9-15 |
| w26.09 | "Kung Paano Magkakaroon ng 'Masunuring Puso'" (p. 8-13) | Watchtower Nov 9-15 |

**Note:** `lmd apendise A` (used for 5/10-min talk assignments) is the sample-presentation topic list in the lmd book — each numbered item is a one-line theme + cited scriptures (not a paragraph). E.g., `#18. Inihula ni Jesus ang mga pangyayaring nakikita natin ngayon.—Mat. 24:3, 7, 8, 14; Luc. 21:10, 11.`
