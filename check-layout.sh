#!/bin/bash

set -x

[[ "$(pdfinfo $1 | grep Pages | awk '{print $2}')" == "$2" ]] || exit 1
