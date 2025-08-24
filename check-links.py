#!/usr/bin/env python
import sys

import pdfx


pdf = pdfx.PDFx(sys.argv[1])

refs = [ref for ref in pdf.get_references() if ref.reftype == 'url']

status_codes = [pdfx.downloader.get_status_code(ref.ref) for ref in refs]

broken_links = [(ref.ref, code) for ref, code in zip(refs, status_codes) if code != 200]
