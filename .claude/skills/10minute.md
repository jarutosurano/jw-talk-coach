# /10minute — Push 10-Minute Talks to Notion

## Activation
- User types `/10minute` (no args) → List & choose mode
- User types `/10minute <folder-name>` → Push specific talk
- User types `/10minute all` → Push all talks

## Behavior

### Mode 1: List & Choose (no arguments)
1. Scan `/talks/10min/` for all talk folders
2. Display numbered list:
   ```
   Available 10-minute talks:
   1. 0124-siya-ang-ating-diyos
   2. 0207-another-talk
   ...
   ```
3. Ask user: "Alin ang i-push sa Notion? (Enter number or 'all')"
4. Run script for selected talk

### Mode 2: Push Specific (with folder name)
Example: `/10minute 0124-siya-ang-ating-diyos`

1. Verify folder exists in `/talks/10min/`
2. Verify `script.md` exists in that folder
3. Run: `python scripts/push-to-notion.py talks/10min/<folder-name>`
4. Display result with Notion link

### Mode 3: Push All (argument = "all")
Example: `/10minute all`

1. Scan `/talks/10min/` for all folders with `script.md`
2. Confirm with user: "Push X talks to Notion? (y/n)"
3. Run script for each talk sequentially
4. Display summary:
   ```
   Pushed 3 talks:
   ✅ 0124-siya-ang-ating-diyos → [link]
   ✅ 0207-another-talk → [link]
   ❌ 0214-incomplete (no script.md)
   ```

## Script Location
```
/Users/jarutosurano/Documents/jw/jw-talk-coach/scripts/push-to-notion.py
```

## Prerequisites Check
Before running, verify:
1. `scripts/config.json` exists with valid API key
2. Talk folder has `script.md` file
3. Python and notion-client installed

## Error Handling
- No talks found → "Walang talks sa /talks/10min/. Gumawa muna ng talk folder."
- Folder not found → "Hindi mahanap ang folder: <name>. Check spelling."
- No script.md → "Walang script.md sa folder na ito. Gumawa muna ng script."
- API error → Show error message from script

## Example Outputs

### List mode:
```
📂 Available 10-minute talks:

1. 0124-siya-ang-ating-diyos
2. 0207-pag-ibig-ng-diyos

Alin ang i-push sa Notion? (number, folder name, or 'all')
```

### Success:
```
🚀 Pushing to Notion...
✅ Done!
🔗 https://notion.so/Siya-ang-Ating-Diyos-abc123...
```

### Batch success:
```
📤 Pushing 2 talks to Notion...

✅ 0124-siya-ang-ating-diyos → https://notion.so/...
✅ 0207-pag-ibig-ng-diyos → https://notion.so/...

Done! 2/2 talks pushed.
```
