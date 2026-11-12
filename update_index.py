#!/usr/bin/env python3
"""bulten/ klasöründeki sayılardan index.json üretir (en yeni başta, son 60 sayı).
Kullanım: python3 update_index.py"""
import glob, hashlib, json, os, datetime
items = []
for f in sorted(glob.glob('bulten/*.json'), reverse=True)[:60]:
    raw = open(f, 'rb').read()
    d = json.loads(raw)
    assert d['date'] == os.path.basename(f)[:-5], f
    items.append({'date': d['date'], 'file': f, 'sha': hashlib.sha1(raw).hexdigest()[:16]})
json.dump({'updated': datetime.datetime.now().astimezone().isoformat(timespec='seconds'), 'items': items},
          open('index.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), 'sayı;', items[0]['date'] if items else '-')
