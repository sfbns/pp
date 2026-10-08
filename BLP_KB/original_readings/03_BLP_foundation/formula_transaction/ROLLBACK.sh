#!/bin/sh
set -eu
[ "$#" -eq 1 ] || { printf "%s\n" "Usage: ROLLBACK.sh TARGET_COPY" >&2; exit 64; }
here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cp -- "$here/ORIGINAL_BASELINE.md" "$1"
printf "%s\n" "ROLLBACK restored pristine baseline bytes"
