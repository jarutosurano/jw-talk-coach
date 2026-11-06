# Watchtower Study — answer script

> Moved verbatim from `CLAUDE.md` on 2026-10-30 (instruction-budget fix). The hard rules (never/must) are also kept in `CLAUDE.md`; if the two ever differ, `CLAUDE.md` wins. Add new procedures, templates and lookup rows here, not in `CLAUDE.md`.

---

## Watchtower Study (Pag-aaral sa Bantayan)

Personal answer-preparation script for the Sunday Watchtower study. The user is an audience member preparing comments — NOT the conductor.

### Folder Structure

**Published script** (in `docs/`):
```
docs/watchtower/
  [short-title-slug]/index.md      # answer script (published)
```

**Non-published reference** (root-level):
```
watchtower/
  [short-title-slug]/outline.md    # article summary, paragraph notes
```

**Source material:** Watchtower issue PDFs go in `reference/books/` (git-ignored, local only, NEVER committed). Naming: keep original filename (e.g., `w_TG_202606.pdf`). The June issue covers study articles ~2 months later (e.g., Hunyo 2026 issue = Agosto 10–Setyembre 6, 2026 study weeks). The study week ends on Sunday (study day).

**Naming:** short title slug (e.g., `iingatan-ang-pakikipagkaibigan`)
**Nav:** `Watchtower` section in `mkdocs.yml`, latest first.

### MANDATORY — Answer Format (effective Aug 23, 2026)

Script header (top of file, in order):
1. YAML frontmatter `title:` (exact article title)
2. `Pag-aaral sa Bantayan — [study week dates]`
3. `!!! quote` admonition with the theme scripture
4. `**MATUTUTUHAN:**` line from the article
5. **No FORMULA box** (removed Nov 6, 2026, Jayr; formula is rare, never the default). Articles up to Oct 26–Nov 1 still have one; leave those as they are.

Per question (use `### N — [exact question text] (Scripture ref if any)`):
1. **Mahahalagang punto:** — unordered list of the paragraph's main points only (not full paragraph), with scripture refs inline
2. **Direktang sagot:** — 1-2 sentence GENERALIZED answer (no "ako"/"tayo" — user personalizes later); short, concise, direct
3. `!!! success "Sagot kapag binasa nang malakas"` — the answer as spoken aloud, built from the bullets, using the Bible as much as possible (cite/weave scriptures). Most answers stay short; mark deeper ones `"Sagot kapag binasa nang malakas (mas malalim)"` — use the deep version for "Basahin" texts and key paragraphs
4. **Tanong para ikapit:** — 1 application question (question form, not statement)

Review questions ("ANO ANG SAGOT MO?" / end-of-article box):
- Heading `## MGA ARAL NA NATUTUHAN`
- Each review question becomes a **lesson learned** in an `!!! abstract "Aral"` box — state the key quality/principle ("[Katangian] ang susi"), then the compressed takeaway with scriptures

Key rules:
- Use the Bible as much as possible in every answer — weave the cited texts into the spoken answers
- `*[Basahin ang ...]*` cue before each "Basahin" text's question body
- Section headings from the article as `## ALL CAPS` (matching article subheadings)
- No timing markers
- Bible quotes: only quote text that appears verbatim in the article/outline — never paraphrase NWT text from memory
