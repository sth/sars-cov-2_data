#!/usr/bin/env python3

import sys, os, subprocess

failed = False
for sub in os.listdir('.'):
    if not os.path.exists(os.path.join(sub, 'fetch.py')):
        continue
    print("processing:", sub, flush=True)
    cp = subprocess.run(['./fetch.py'] + sys.argv[1:], cwd=sub)
    if cp.returncode != 0:
        print("failed:", sub, file=sys.stderr)
    failed = failed or (cp.returncode != 0)

if failed:
    sys.exit(1)
