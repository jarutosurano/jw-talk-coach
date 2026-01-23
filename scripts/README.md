# Scripts

Automation scripts for talk management.

---

## push-to-notion.py

Push your talk script to Notion as a new subpage.

### Setup (One-time)

#### 1. Install Python dependency
```bash
pip install notion-client
```

#### 2. Create Notion Integration
1. Go to [notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Click **"+ New integration"**
3. Name: `Talk Script Uploader`
4. Submit and copy the **Secret Key** (starts with `secret_...`)

#### 3. Create Parent Page in Notion
1. Create a page called **"Talks"** in Notion
2. This is where all your talk scripts will be saved as subpages

#### 4. Connect Integration to Page
1. Open your "Talks" page
2. Click **"..."** → **"Connections"** → **"Connect to"**
3. Select **"Talk Script Uploader"**

#### 5. Get Parent Page ID
1. Open your "Talks" page in Notion
2. Copy the ID from the URL:
   ```
   https://www.notion.so/Talks-abc123def456...
                              └─────────────┘
                              This is the Page ID
   ```
   (32 characters, may have dashes)

#### 6. Create config.json
```bash
cp config.example.json config.json
```

Edit `config.json`:
```json
{
  "notion_api_key": "secret_abc123...",
  "parent_page_id": "abc123def456..."
}
```

---

### Usage

```bash
# From the scripts folder
cd scripts

# Push a talk script to Notion
python push-to-notion.py ../talks/10min/0124-siya-ang-ating-diyos
```

### What It Does

1. Reads `script.md` from the talk folder
2. Extracts the title from the script
3. Converts markdown to Notion blocks
4. Creates a new subpage under your "Talks" page
5. Returns the Notion page URL

---

### Example Output

```
📂 Reading from: ../talks/10min/0124-siya-ang-ating-diyos
📝 Title: "Siya ang Ating Diyos!" (10 min)
🚀 Creating Notion page...
✅ Done!
🔗 View your page: https://notion.so/Siya-ang-Ating-Diyos-abc123...
```

---

### Troubleshooting

| Error | Solution |
|-------|----------|
| `notion-client not installed` | Run `pip install notion-client` |
| `config.json not found` | Copy `config.example.json` to `config.json` and fill in credentials |
| `script.md not found` | Make sure the talk folder has a `script.md` file |
| `401 Unauthorized` | Check your API key in config.json |
| `404 Not Found` | Make sure the integration is connected to your Talks page |

---

### Security Note

⚠️ **Never commit `config.json` to git!** It contains your secret API key.

The `.gitignore` should already exclude it, but double-check.
