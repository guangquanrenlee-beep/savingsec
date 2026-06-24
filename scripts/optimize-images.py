#!/usr/bin/env python3
"""
Image Optimizer for SavingSec
================================
Converts all images in static/images/ to 800×450 JPG, ≤500KB.
Usage: python scripts/optimize-images.py [--dir static/images]
"""

import os
import sys
from PIL import Image

TARGET_W = 800
TARGET_H = 450      # 16:9
MAX_BYTES = 500 * 1024  # 500KB


def optimize_image(path, dry_run=False):
    ext = os.path.splitext(path)[1].lower()
    if ext not in ('.jpg', '.jpeg', '.png', '.webp'):
        return None

    im = Image.open(path)
    orig_size = os.path.getsize(path)

    # Check if already compliant
    if im.width <= TARGET_W + 20 and orig_size <= MAX_BYTES:
        return None  # skip, no change needed

    resized = im.resize((TARGET_W, TARGET_H), Image.LANCZOS)
    base = os.path.splitext(path)[0]
    out_path = f"{base}.jpg"

    if dry_run:
        return {
            'file': os.path.basename(path),
            'from': f"{im.width}x{im.height} {orig_size/1024:.1f}KB",
            'to': f"{TARGET_W}x{TARGET_H} <={MAX_BYTES/1024:.0f}KB",
        }

    quality = 85
    rgb = resized.convert('RGB')
    rgb.save(out_path, 'JPEG', quality=quality, optimize=True)
    new_size = os.path.getsize(out_path)

    while new_size > MAX_BYTES and quality > 30:
        quality -= 5
        rgb.save(out_path, 'JPEG', quality=quality, optimize=True)
        new_size = os.path.getsize(out_path)

    # Remove old file if different format
    if out_path != path:
        os.remove(path)

    return {
        'file': os.path.basename(path),
        'from': f"{im.width}x{im.height} {orig_size/1024:.1f}KB",
        'to': f"{TARGET_W}x{TARGET_H} {new_size/1024:.1f}KB (q={quality})",
    }


def main():
    target_dir = r'D:\site\chanpintuijian\static\images'
    dry_run = '--dry-run' in sys.argv

    if '--dir' in sys.argv:
        idx = sys.argv.index('--dir') + 1
        if idx < len(sys.argv):
            target_dir = sys.argv[idx]

    if not os.path.isdir(target_dir):
        print(f"❌ Directory not found: {target_dir}")
        sys.exit(1)

    results = []
    for fname in sorted(os.listdir(target_dir)):
        fpath = os.path.join(target_dir, fname)
        if not os.path.isfile(fpath):
            continue
        result = optimize_image(fpath, dry_run=dry_run)
        if result:
            results.append(result)

    if not results:
        print("✅ All images already comply with the standard.")
        return

    verb = "Would optimize" if dry_run else "Optimized"
    print(f"\n{verb} {len(results)} image(s):\n")
    for r in results:
        print(f"  {r['file']}")
        print(f"    From: {r['from']}")
        print(f"    To:   {r['to']}")
        print()

    print("📐 Standard: 800×450 (16:9) JPG, ≤500KB")


if __name__ == '__main__':
    main()
