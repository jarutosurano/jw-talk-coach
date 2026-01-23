#!/usr/bin/env python3
"""
Push Talk Script to Notion
Creates a new subpage under your Talks parent page with the script content.

Usage:
    python push-to-notion.py ../talks/10min/0124-siya-ang-ating-diyos

Requirements:
    pip install notion-client
"""

import os
import sys
import json
from pathlib import Path

try:
    from notion_client import Client
except ImportError:
    print("❌ notion-client not installed!")
    print("Run: pip install notion-client")
    sys.exit(1)


def load_config():
    """Load configuration from config.json"""
    config_path = Path(__file__).parent / "config.json"

    if not config_path.exists():
        print("❌ config.json not found!")
        print("Copy config.example.json to config.json and add your credentials.")
        sys.exit(1)

    with open(config_path) as f:
        return json.load(f)


def read_script(talk_folder):
    """Read the script.md file from the talk folder"""
    script_path = Path(talk_folder) / "script.md"

    if not script_path.exists():
        print(f"❌ script.md not found in {talk_folder}")
        sys.exit(1)

    with open(script_path, encoding='utf-8') as f:
        return f.read()


def extract_title(script_content):
    """Extract title from script (first # heading)"""
    for line in script_content.split('\n'):
        if line.startswith('# '):
            # Remove "Script: " prefix if present
            title = line[2:].strip()
            if title.startswith('Script: '):
                title = title[8:]
            return title
    return "Untitled Talk"


def parse_inline_formatting(text):
    """Parse bold (**text**) and italic (*text*) into Notion rich_text array"""
    import re
    rich_text = []

    # Pattern to match **bold**, *italic*, or plain text
    # Order matters: check ** before * to handle bold correctly
    pattern = r'(\*\*[^*]+\*\*|\*[^*]+\*|[^*]+)'

    parts = re.findall(pattern, text)

    for part in parts:
        if not part:
            continue

        if part.startswith('**') and part.endswith('**'):
            # Bold text
            content = part[2:-2]
            rich_text.append({
                "type": "text",
                "text": {"content": content},
                "annotations": {"bold": True}
            })
        elif part.startswith('*') and part.endswith('*'):
            # Italic text
            content = part[1:-1]
            rich_text.append({
                "type": "text",
                "text": {"content": content},
                "annotations": {"italic": True}
            })
        else:
            # Plain text
            rich_text.append({
                "type": "text",
                "text": {"content": part}
            })

    return rich_text if rich_text else [{"type": "text", "text": {"content": text}}]


def markdown_to_notion_blocks(markdown_text):
    """Convert markdown to Notion blocks (simplified)"""
    blocks = []
    lines = markdown_text.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Skip empty lines
        if not line.strip():
            i += 1
            continue

        # Headings
        if line.startswith('### '):
            blocks.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {
                    "rich_text": parse_inline_formatting(line[4:].strip())
                }
            })
        elif line.startswith('## '):
            blocks.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": parse_inline_formatting(line[3:].strip())
                }
            })
        elif line.startswith('# '):
            blocks.append({
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": parse_inline_formatting(line[2:].strip())
                }
            })
        # Blockquotes
        elif line.startswith('> '):
            blocks.append({
                "object": "block",
                "type": "quote",
                "quote": {
                    "rich_text": parse_inline_formatting(line[2:].strip())
                }
            })
        # Horizontal rule
        elif line.strip() == '---':
            blocks.append({
                "object": "block",
                "type": "divider",
                "divider": {}
            })
        # Checklist
        elif line.strip().startswith('- [ ]'):
            blocks.append({
                "object": "block",
                "type": "to_do",
                "to_do": {
                    "rich_text": [{"type": "text", "text": {"content": line.strip()[6:].strip()}}],
                    "checked": False
                }
            })
        elif line.strip().startswith('- [x]'):
            blocks.append({
                "object": "block",
                "type": "to_do",
                "to_do": {
                    "rich_text": [{"type": "text", "text": {"content": line.strip()[6:].strip()}}],
                    "checked": True
                }
            })
        # Bullet list
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": parse_inline_formatting(line.strip()[2:].strip())
                }
            })
        # Table rows (simplified - just show as text)
        elif line.strip().startswith('|'):
            # Skip table formatting
            pass
        # Regular paragraph
        else:
            content = line.strip()
            if content:
                blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": parse_inline_formatting(content)
                    }
                })

        i += 1

    return blocks


def create_notion_page(notion, parent_id, title, script_content):
    """Create a new page in Notion with the script content"""

    # Convert markdown to Notion blocks
    blocks = markdown_to_notion_blocks(script_content)

    # Notion API has a limit of 100 blocks per request
    # We'll add blocks in chunks if needed
    initial_blocks = blocks[:100]
    remaining_blocks = blocks[100:]

    # Create the page
    new_page = notion.pages.create(
        parent={"page_id": parent_id},
        properties={
            "title": {
                "title": [{"type": "text", "text": {"content": title}}]
            }
        },
        children=initial_blocks
    )

    # Add remaining blocks if any
    if remaining_blocks:
        page_id = new_page["id"]
        for i in range(0, len(remaining_blocks), 100):
            chunk = remaining_blocks[i:i+100]
            notion.blocks.children.append(block_id=page_id, children=chunk)

    return new_page


def main():
    if len(sys.argv) < 2:
        print("Usage: python push-to-notion.py <talk-folder>")
        print("Example: python push-to-notion.py ../talks/10min/0124-siya-ang-ating-diyos")
        sys.exit(1)

    talk_folder = sys.argv[1]

    print(f"📂 Reading from: {talk_folder}")

    # Load config
    config = load_config()

    # Initialize Notion client
    notion = Client(auth=config["notion_api_key"])

    # Read script
    script_content = read_script(talk_folder)

    # Extract title
    title = extract_title(script_content)
    print(f"📝 Title: {title}")

    # Create page
    print(f"🚀 Creating Notion page...")
    new_page = create_notion_page(
        notion,
        config["parent_page_id"],
        title,
        script_content
    )

    # Get the URL
    page_url = new_page.get("url", "")

    print(f"✅ Done!")
    print(f"🔗 View your page: {page_url}")


if __name__ == "__main__":
    main()
