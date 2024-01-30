#!/usr/bin/env python

import os
import subprocess
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).parent

if os.environ.get('GITHUB_ACTIONS', '') == '':
    print('Not running when not in GitHub Actions.')
    sys.exit()
summary_file = os.environ.get('GITHUB_STEP_SUMMARY')
if summary_file is None:
    sys.exit('$GITHUB_STEP_SUMMARY is not set')

gh_pages = ROOT_DIR.parent / 'pages'
subprocess.run(['git', 'fetch', 'https://github.com/matplotlib/cheatsheets.git',
                'gh-pages:upstream-gh-pages'], check=True)
subprocess.run(['git', 'worktree', 'add', gh_pages, 'upstream-gh-pages'],
               check=True)

diff_dir = ROOT_DIR / 'diffs'
diff_dir.mkdir(exist_ok=True)

hashes = {}
for original in gh_pages.glob('*.png'):
    result = subprocess.run(
        ['compare', '-metric', 'PHASH',
         original,
         ROOT_DIR / 'docs/_build/html' / original.name,
         diff_dir / f'{original.stem}-diff.png'],
        text=True, stderr=subprocess.PIPE)
    if result.returncode == 2:  # Some kind of IO or similar error.
        hashes[original] = (float('nan'), result.stderr)
    elif result.stderr:  # Images were different.
        hashes[original] = (float(result.stderr), '')
    else:  # No differences.
        hashes[original] = (0.0, '')

with open(summary_file, 'w+') as summary:
    print('# Cheatsheet image comparison', file=summary)
    print('| Filename | Perceptual Hash Difference | Error message |', file=summary)
    print('| -------- | -------------------------- | ------------- |', file=summary)
    for filename, (hash, message) in sorted(hashes.items()):
        message = message.replace('\n', ' ').replace('|', '\\|')
        print(f'| {filename.name} | {hash:.05f} | {message}', file=summary)
    print(file=summary)

subprocess.run(['git', 'worktree', 'remove', gh_pages])
