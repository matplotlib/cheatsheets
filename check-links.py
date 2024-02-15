#!/usr/bin/env python
import sys

import pdfx


pdf = pdfx.PDFx(sys.argv[1])

refs = [ref for ref in pdf.get_references() if ref.reftype == 'url']

status_codes = [pdfx.downloader.get_status_code(ref.ref) for ref in refs]

broken_links = [(ref.ref, code) for ref, code in zip(refs, status_codes) if code != 200]

# it seems that Twitter does not respond well to the link checker and throws a 400
if all(['twitter.com' in url for url, _ in broken_links]):
    sys.exit(0)
else:
    print('Broken links:', broken_links)
    sys.exit(1)
