#!/bin/bash
#
# Check that a given pdf has a certain number of pages.
# Usage:
#   check-num-pages.sh [pdffile] [num_pages]

set -x
# pdffile=$1
# num_pages=$1
[[ "$(pdfinfo $pdffile | grep Pages | awk '{print $2}')" == "$num_pages" ]] || exit 1
