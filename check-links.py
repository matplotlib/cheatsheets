#!/usr/bin/env python
import sys

import pdfx


pdf = pdfx.PDFx(sys.argv[1])

refs = [ref for ref in pdf.get_references() if ref.reftype == 'url']

status_codes = list(map(lambda ref: pdfx.downloader.get_status_code(ref.ref), refs))

broken_links = [refs[idx].ref for idx in range(len(refs)) if status_codes[idx] != 200]

# it seems that Twitter does not respond well to the link checker and throws a 400
if all(['twitter.com' in url for url in broken_links]):
    sys.exit(0)
else:
    print('Broken links:', broken_links)
    sys.exit(1)
