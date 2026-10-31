#!/usr/bin/env python3
import sys, yaml
images = set()

def scan(x):
    if isinstance(x, dict):
        if isinstance(x.get('image'), str) and x['image'].strip():
            images.add(x['image'])
        for v in x.values(): scan(v)
    elif isinstance(x, list):
        for v in x: scan(v)

with open(sys.argv[1], encoding='utf-8') as f:
    for doc in yaml.safe_load_all(f): scan(doc)
if not images: raise SystemExit('ERROR: No images found in rendered manifests')
print('\n'.join(sorted(images)))
