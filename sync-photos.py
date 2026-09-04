#!/usr/bin/env python3
"""
=============================================================
  Meraki Ascent · Photography Page Sync
=============================================================

  Reads every photo in the category subfolders under
  Website/assets/Top photos/{landscapes,portraits,animals,food}/
  and syncs them to the live photography page.

  USAGE (in Terminal):
    cd "/Users/hannahweymuller/Desktop/Meraki Ascent LLC"
    python3 sync-photos.py

  TO ADD A PHOTO:
    Drag it into the right subfolder
    (Top photos/landscapes/, Top photos/portraits/,
     Top photos/animals/, or Top photos/food/)
    then re-run this script.

  TO REMOVE A PHOTO:
    Delete it from its subfolder.
    Re-run this script.

  TO RECATEGORIZE A PHOTO:
    Move it from one subfolder to another.
    Re-run this script.

  AFTER THE SCRIPT RUNS:
    cd Website
    git add .
    git commit -m "Photography update"
    git push

=============================================================
"""
from PIL import Image, ImageOps
import os, glob, re, sys, time, hashlib

# ---------- CONFIG ----------
# Script lives inside the Website/ folder now (moved from project root).
# WEBSITE is therefore the script's own directory.
WEBSITE      = os.path.dirname(os.path.abspath(__file__))
SRC_ROOT     = os.path.join(WEBSITE, "assets", "Top photos")
DST          = os.path.join(WEBSITE, "assets")
PAGE         = os.path.join(WEBSITE, "portfolio-photography.html")

CATEGORIES = ["landscapes", "portraits", "animals", "food"]
MAX_LONG_SIDE = 1200
QUALITY = 82

# ---------- COLOR OUTPUT (optional, terminal-friendly) ----------
def c(s, code):
    return f"\033[{code}m{s}\033[0m" if sys.stdout.isatty() else s
def bold(s):   return c(s, "1")
def green(s):  return c(s, "32")
def red(s):    return c(s, "31")
def yellow(s): return c(s, "33")
def dim(s):    return c(s, "2")

print()
print(bold("=" * 60))
print(bold("  Meraki Ascent · Photography Sync"))
print(bold("=" * 60))
print()

# ---------- SANITY CHECKS ----------
if not os.path.isdir(WEBSITE):
    print(red(f"ERROR: Can't find Website folder at {WEBSITE}"))
    print("       Run this script from the project root folder.")
    sys.exit(1)

missing_cat_dirs = [c for c in CATEGORIES if not os.path.isdir(os.path.join(SRC_ROOT, c))]
if missing_cat_dirs:
    print(red(f"ERROR: Missing category subfolders: {missing_cat_dirs}"))
    print(f"       Expected: {SRC_ROOT}/{{landscapes,portraits,animals,food}}/")
    sys.exit(1)

# ---------- COLLECT PHOTOS FROM SUBFOLDERS ----------
photos = []   # list of (full_path, category, basename)
for cat in CATEGORIES:
    cat_dir = os.path.join(SRC_ROOT, cat)
    for f in sorted(glob.glob(f"{cat_dir}/*.jpg") + glob.glob(f"{cat_dir}/*.JPG")
                  + glob.glob(f"{cat_dir}/*.jpeg") + glob.glob(f"{cat_dir}/*.JPEG")):
        photos.append((f, cat, os.path.basename(f)))

# Warn about loose photos at top level (not in any subfolder)
loose = [f for f in glob.glob(f"{SRC_ROOT}/*.jpg") + glob.glob(f"{SRC_ROOT}/*.JPG")
              + glob.glob(f"{SRC_ROOT}/*.jpeg") + glob.glob(f"{SRC_ROOT}/*.JPEG")
              if os.path.isfile(f)]
if loose:
    print(yellow(f"WARNING: {len(loose)} photo(s) at top of Top photos/ are NOT in any category subfolder."))
    print(yellow("         These will be IGNORED. Move them into a category subfolder first:\n"))
    for f in loose[:10]:
        print(f"           {os.path.basename(f)}")
    if len(loose) > 10:
        print(f"           ... and {len(loose) - 10} more")
    print()

if not photos:
    print(red("No photos found in any category subfolder. Nothing to sync."))
    sys.exit(0)

# Sort by MD5 hash of the basename — gives a stable but visually random
# order so new photos intermix with existing ones (instead of clumping at
# the end when new files sort alphabetically after old ones).
photos.sort(key=lambda p: hashlib.md5(p[2].encode()).hexdigest())

# ---------- PER-CATEGORY COUNTS ----------
counts = {c: 0 for c in CATEGORIES}
for _, cat, _ in photos:
    counts[cat] += 1

print(bold(f"Found {len(photos)} photos:"))
for cat in CATEGORIES:
    print(f"  {cat:12s} {counts[cat]:3d}")
print()

# ---------- WIPE OLD GALLERY FILES ----------
old = glob.glob(f"{DST}/gallery-*.jpg")
for f in old:
    os.remove(f)
print(dim(f"Wiped {len(old)} old gallery-*.jpg files"))

# ---------- PROCESS PHOTOS ----------
print(dim(f"Processing {len(photos)} photos (resize, compress, save)..."))
manifest = []
total_kb = 0
t0 = time.time()

for idx, (src_path, cat, basename) in enumerate(photos, start=1):
    dst_name = f"gallery-{idx:03d}.jpg"
    dst_path = f"{DST}/{dst_name}"

    try:
        img = Image.open(src_path)
        img = ImageOps.exif_transpose(img)
        if img.mode != "RGB":
            img = img.convert("RGB")
        w, h = img.size
        if max(w, h) > MAX_LONG_SIDE:
            if w >= h:
                new_w, new_h = MAX_LONG_SIDE, int(round(h * MAX_LONG_SIDE / w))
            else:
                new_h, new_w = MAX_LONG_SIDE, int(round(w * MAX_LONG_SIDE / h))
            img = img.resize((new_w, new_h), Image.LANCZOS)
        img.save(dst_path, "JPEG", quality=QUALITY, optimize=True, progressive=True)

        kb = os.path.getsize(dst_path) // 1024
        total_kb += kb
        manifest.append({
            "idx": idx, "src": basename, "dst": dst_name,
            "category": cat, "width": img.width, "height": img.height,
        })
    except Exception as e:
        print(red(f"  FAILED: {basename} -> {e}"))

elapsed = time.time() - t0
print(dim(f"Done in {elapsed:.1f}s · {total_kb/1024:.1f} MB total"))

# ---------- REGENERATE MASONRY HTML ----------
CAT_ALT = {
    "landscapes": "Landscape photograph",
    "portraits":  "Portrait photograph",
    "animals":    "Animal photograph",
    "food":       "Food photograph",
}

def cell(m):
    alt = f"{CAT_ALT[m['category']]} {m['idx']:03d}"
    return (f'    <div class="masonry-cell" data-category="{m["category"]}">\n'
            f'      <button class="masonry-item" data-category="{m["category"]}">\n'
            f'        <img src="assets/{m["dst"]}" alt="{alt}" loading="lazy" '
            f'width="{m["width"]}" height="{m["height"]}"/>\n'
            f'      </button>\n'
            f'    </div>')

new_inner = "\n\n".join(cell(m) for m in manifest)

with open(PAGE) as f:
    src = f.read()

new_src, n = re.subn(
    r'(<div class="masonry-grid">)\s*\n.*?\n(\s*</div>\s*\n\s*</div>\s*\n\s*<!-- ========== CLOSER)',
    rf'\1\n{new_inner}\n\2',
    src, count=1, flags=re.DOTALL)

if n != 1:
    print(red(f"WARN: Couldn't update masonry block in HTML (matched {n} times)."))
    print(red("      You may need to inspect portfolio-photography.html manually."))
else:
    with open(PAGE, 'w') as f:
        f.write(new_src)

# ---------- SUMMARY ----------
print()
print(green(bold("✓ Sync complete")))
print()
print(f"  Photos on site:  {bold(str(len(manifest)))}")
print(f"  Total weight:    {bold(f'{total_kb/1024:.1f} MB')}  ({total_kb} KB)")
print(f"  By category:")
for cat in CATEGORIES:
    print(f"    {cat:12s} {counts[cat]:3d}")
print()
print(bold("Next: commit and push the changes:"))
print(dim('  cd "Website"'))
print(dim('  git add .'))
print(dim('  git commit -m "Photography update"'))
print(dim('  git push'))
print()
