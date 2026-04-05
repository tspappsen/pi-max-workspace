#!/usr/bin/env python3
"""
Ingest script: /home/pi/study/affaan-m/everything-claude-code → raw/entries/
Obsidian vault (folder of .md files): each note becomes one raw entry.
Idempotent: re-running produces the same output files.
"""

import os
import re
import hashlib
import datetime
from pathlib import Path

SOURCE_DIR = Path("/home/pi/study/affaan-m/everything-claude-code")
ENTRIES_DIR = Path("/home/pi/.max/brain/raw/entries")
SOURCE_TYPE = "obsidian"


def wikilinks_to_text(content: str) -> str:
    """Convert [[wikilinks]] and [[wikilinks|alias]] to plain text."""
    # [[link|alias]] → alias
    content = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', content)
    # [[link]] → link
    content = re.sub(r'\[\[([^\]]+)\]\]', r'\1', content)
    return content


def stable_id(rel_path: str) -> str:
    """Generate a stable, filesystem-safe ID from the relative path."""
    # Use hash prefix + sanitized name for uniqueness + readability
    h = hashlib.md5(rel_path.encode()).hexdigest()[:8]
    safe = re.sub(r'[^a-z0-9]+', '-', rel_path.lower().rstrip('.md'))
    safe = safe.strip('-')[:60]
    return f"{safe}-{h}"


def extract_description(content: str, max_len: int = 150) -> str:
    """Extract a ~150 char description from the content."""
    # Strip frontmatter if present
    body = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL).strip()
    # Strip markdown headings and code blocks
    body = re.sub(r'```.*?```', '', body, flags=re.DOTALL)
    body = re.sub(r'^#{1,6}\s+', '', body, flags=re.MULTILINE)
    # Collapse whitespace
    body = re.sub(r'\s+', ' ', body).strip()
    if len(body) <= max_len:
        return body
    # Truncate at word boundary
    truncated = body[:max_len]
    last_space = truncated.rfind(' ')
    if last_space > max_len * 0.7:
        truncated = truncated[:last_space]
    return truncated + '…'


def extract_existing_frontmatter(content: str):
    """Return (frontmatter_dict, body) from a file that may have YAML frontmatter."""
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if match:
        fm_text, body = match.group(1), match.group(2)
        return fm_text, body.strip()
    return None, content.strip()


def infer_date(filepath: Path) -> tuple[str, str]:
    """Return (date_str, time_str) from filename or mtime."""
    name = filepath.stem
    # Try YYYY-MM-DD in filename
    m = re.search(r'(\d{4}-\d{2}-\d{2})', name)
    if m:
        return m.group(1), "00:00:00"
    # Fall back to file mtime
    mtime = datetime.datetime.fromtimestamp(filepath.stat().st_mtime)
    return mtime.strftime('%Y-%m-%d'), mtime.strftime('%H:%M:%S')


def infer_tags(rel_path: str, content: str) -> list[str]:
    """Derive tags from path and content."""
    tags = ["raw-entry", "obsidian"]
    parts = Path(rel_path).parts
    if len(parts) > 1:
        tags.append(parts[0])  # top-level folder as tag
    # Content-based tags
    lower = content.lower()
    if 'agent' in lower or 'orchestrat' in lower:
        tags.append("ai-agents")
    if 'security' in lower or 'cve' in lower:
        tags.append("security")
    if 'hook' in lower:
        tags.append("hooks")
    if 'skill' in lower:
        tags.append("skills")
    if 'claude' in lower:
        tags.append("claude-code")
    return list(dict.fromkeys(tags))  # deduplicate, preserve order


def build_entry(filepath: Path) -> tuple[str, str]:
    """Return (output_filename, output_content) for a given .md file."""
    rel = str(filepath.relative_to(SOURCE_DIR))
    raw = filepath.read_text(encoding='utf-8')

    existing_fm, body = extract_existing_frontmatter(raw)
    body_clean = wikilinks_to_text(body)

    date_str, time_str = infer_date(filepath)
    entry_id = stable_id(rel)
    description = extract_description(body_clean)
    tags = infer_tags(rel, body_clean)

    # Merge any existing frontmatter fields we want to preserve
    extra_fm = ""
    if existing_fm:
        # Preserve original frontmatter as a comment block
        extra_fm = f"\n# original_frontmatter: |\n"
        for line in existing_fm.splitlines():
            extra_fm += f"#   {line}\n"

    tag_lines = "\n".join(f"  - {t}" for t in tags)
    frontmatter = f"""---
id: {entry_id}
date: {date_str}
time: "{time_str}"
source_type: {SOURCE_TYPE}
source_file: {rel}
description: "{description}"
tags:
{tag_lines}
---"""

    output = f"{frontmatter}\n\n{body_clean}"
    filename = f"{date_str}_{entry_id}.md"
    return filename, output


def ingest():
    ENTRIES_DIR.mkdir(parents=True, exist_ok=True)

    md_files = sorted(SOURCE_DIR.rglob("*.md"))
    created = 0
    skipped = 0

    for filepath in md_files:
        filename, content = build_entry(filepath)
        out_path = ENTRIES_DIR / filename
        # Idempotent: only write if content changed
        if out_path.exists() and out_path.read_text(encoding='utf-8') == content:
            skipped += 1
            print(f"  [skip]    {filename}")
        else:
            out_path.write_text(content, encoding='utf-8')
            created += 1
            print(f"  [written] {filename}")

    print(f"\nDone. {created} written, {skipped} unchanged.")
    print(f"Total .md files processed: {len(md_files)}")


if __name__ == "__main__":
    ingest()
