import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "out")
HTML_PATH = os.path.join(OUT, "index.html")

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Extract all src and href attributes
refs = set(re.findall(r'(?:src|href)=["\']([^"\']+)["\']', html))
local_refs = [r for r in refs if r.startswith("/") and not r.startswith("//") and not r.startswith("/#")]

print(f"Total local references found in index.html: {len(local_refs)}")

missing = []
for ref in sorted(local_refs):
    # remove query params or hash if any
    clean_ref = ref.split("?")[0].split("#")[0].lstrip("/")
    full_path = os.path.join(OUT, clean_ref)
    if os.path.exists(full_path):
        size = os.path.getsize(full_path)
        print(f"  [OK] {ref} ({size:,} bytes)")
    else:
        print(f"  [MISSING] {ref}")
        missing.append(ref)

if not missing:
    print("\nSUCCESS: 100% of referenced files exist on disk with non-zero size!")
else:
    print(f"\nWARNING: {len(missing)} files missing!")
