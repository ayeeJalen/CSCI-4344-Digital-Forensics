#!/usr/bin/env bash
# Usage: bash hash_manifest.sh /path/to/evidence-dir
set -euo pipefail
dir="${1:?Provide evidence directory}"
find "$dir" -type f -print0 | sort -z | xargs -0 -r sha256sum
