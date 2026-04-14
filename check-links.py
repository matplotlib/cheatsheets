#!/usr/bin/env python
import sys

import pdfx


pdf = pdfx.PDFx(sys.argv[1])

refs = [ref for ref in pdf.get_references() if ref.reftype == 'url']

status_codes = [pdfx.downloader.get_status_code(ref.ref) for ref in refs]

broken_links = [(ref.ref, code) for ref, code in zip(refs, status_codes) if code != 200]
# It seems that stackoverflow does not respond well to the link checker and throws a 400
broken_links = [b for b in broken_links if not ('stackoverflow.com' in b[0])]

if len(broken_links) == 0:
    sys.exit(0)
else:
    print('Broken links:', broken_links)
    sys.exit(1)
