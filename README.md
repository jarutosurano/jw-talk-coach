# JW Public Talk Coaching System

> Quick reference guide para sa talk preparation.

---

## 📂 Saan Ako Dapat Pumunta?

| Kung gusto mo... | Pumunta sa... |
|------------------|---------------|
| Gumawa ng bagong talk | `talks/5min/`, `talks/10min/`, or `talks/30min/` |
| Tingnan ang workflow | `CLAUDE.md` |
| Aralin reference | `public-talk-aralin.md` |
| Speaker guidelines | `guidelines.md` |

---

## 🚀 Quick Start: Bagong Talk

### Step 1: Gumawa ng folder
```
talks/10min/MMDD-short-title/
```
Example: `talks/10min/0131-bagong-paksa/`

### Step 2: Gumawa ng `outline.md`
Paste ang outline + references dito.

### Step 3: Sabihin kay Claude
> "May bagong 10min talk ako sa folder 0131-bagong-paksa. Gawan mo ng script."

### Step 4: Claude will create
- `summary.md` — simplified overview ng topic
- `script.md` — full script with timing

---

## 📁 Folder Structure

```
/talks/
  /5min/                    ← Student talks (Friday gabi)
  /10min/                   ← Assigned talks (Friday gabi)
    /0124-siya-ang-ating-diyos/
      outline.md
      script.md
      summary.md
      picture.jpg
  /30min/                   ← Public talks (Sunday umaga)

/CLAUDE.md                  ← Full workflow guide
/public-talk-aralin.md      ← 15 teaching lessons
/guidelines.md              ← Official speaker guidelines (S-141-TG)
```

---

## 📋 Talk Types Quick Reference

| Type | Day | Time | Script phrase |
|------|-----|------|---------------|
| 5 min | Friday | Gabi | "ngayong gabi" |
| 10 min | Friday | Gabi | "ngayong gabi" |
| 30 min | Sunday | Umaga | "ngayong umaga" |

---

## 💡 Reminders for Claude

When starting a new session, tell Claude:

1. **"Basahin mo ang CLAUDE.md para sa workflow"**
2. **"May talk ako sa [folder path]"**
3. **"[Your specific request]"**

Example:
> "Basahin mo ang CLAUDE.md. May bagong 10min talk ako sa talks/10min/0131-paksa. Gawan mo ng script."

---

## 📚 Key Files Explained

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Complete workflow, diagnostic mapping, script creation steps |
| `public-talk-aralin.md` | 15 lessons for improving talks (intro, structure, texts, etc.) |
| `guidelines.md` | Official S-141-TG speaker guidelines |
| `outline.md` | Your assigned outline + references |
| `script.md` | Full talk script with timing markers |
| `summary.md` | Simplified overview of the topic |

---

## ✅ Before Your Talk Checklist

- [ ] Script is final
- [ ] Timing is within limit
- [ ] All outline phrases are included (check 【brackets】 in script)
- [ ] Images are ready (if applicable)
- [ ] Practiced aloud at least once
- [ ] Eye contact practiced (hindi binabasa ang script)
- [ ] (Optional) Pushed to Notion

---

## 🚀 Push to Notion

After your script is ready, push it to Notion:

```bash
cd scripts
python push-to-notion.py ../talks/10min/0124-siya-ang-ating-diyos
```

First time? See `scripts/README.md` for setup instructions.

---

*Last updated: January 2025*
