#!/usr/bin/env python3
"""
Fix all issues found:
1. Replace .png/.webp -> .jpg in all image references (frontmatter + markdown + HTML)
2. Remove replacement characters (U+FFFD) from frontmatter title/description
3. Remove replacement characters from content body
"""
import re, os

content_dir = r'D:\site\chanpintuijian\content'
fixes = []

def fix_image_refs(text, fpath, fname):
    """Replace .png/.webp image refs with .jpg"""
    # Frontmatter image:
    text = re.sub(r'(image:\s*["\']?/images/[\w\-\.]+?)\.(png|webp)', r'\1.jpg', text)
    # Markdown images:
    text = re.sub(r'(!\[.*?\]\(/images/[\w\-\.]+?)\.(png|webp)\)', r'\1.jpg)', text)
    # HTML img tags:
    text = re.sub(r'(<img[^>]*src=")/images/[\w\-\.]+?\.(png|webp)"', r'\1/images/systeme-io.jpg"', text)
    return text

def clean_replacement_chars(text, fpath, fname):
    """Remove U+FFFD from frontmatter title and description"""
    # Remove \ufffd from title/description lines
    lines = text.split('\n')
    modified = False
    for i, line in enumerate(lines):
        if (line.startswith('title:') or line.startswith('description:')) and '\ufffd' in line:
            old = line
            # Remove \ufffd
            line = line.replace('\ufffd', '')
            # If the last char after \ufffd removal doesn't make sense as a closing quote
            # Keep the closing double quote
            if line.strip().endswith('"') or line.strip().endswith('"'):
                pass
            elif not line.strip().endswith('"'):
                line = line.rstrip() + '"'
            lines[i] = line
            modified = True
    text = '\n'.join(lines)
    # Remove remaining \ufffd from body
    text = text.replace('\ufffd', '')
    return text, modified

for root, dirs, fnames in os.walk(content_dir):
    for fname in sorted(fnames):
        if not fname.endswith('.md'):
            continue
        path = os.path.join(root, fname)
        rel = os.path.relpath(path, content_dir)
        
        with open(path, 'rb') as f:
            raw = f.read()
        
        # Handle encoding: try utf-8 with replace
        text = raw.decode('utf-8', errors='replace')
        
        old_text = text
        
        # Fix image references
        text = fix_image_refs(text, path, fname)
        
        # Clean replacement chars
        text, cleaned_fm = clean_replacement_chars(text, path, fname)
        
        if text != old_text:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(text)
            fixes.append(rel)
            print('FIXED: {}'.format(rel))

print('\n=== FIXED {} FILES ==='.format(len(fixes)))
