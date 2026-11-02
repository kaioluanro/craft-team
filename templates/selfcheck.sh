#!/usr/bin/env sh
# Plan-id self-check: prints every added line that leaks plan ids or plan talk into the product.
# Usage: selfcheck.sh <base-sha> [paths...]   (default paths: src crates apps docs)
# Must print nothing. Extend PATTERN with the project's own id prefixes.
base="$1"; shift
[ -z "$base" ] && { echo "usage: selfcheck.sh <base-sha> [paths...]" >&2; exit 2; }
[ "$#" -eq 0 ] && set -- src crates apps docs
PATTERN='\b[A-Z]{2,4}-[AB][0-9]|\bR[0-9]+\.[0-9]|\bT[0-9]+\.[0-9]|_t[0-9]+_[0-9]|_r[0-9]+_[0-9]|§|Logica|Extrato|Pesquisa|carry-over|before the fix|see the report|manual|next batch|this batch'
git diff "$base" -- "$@" 2>/dev/null | grep '^+' | grep -niE "$PATTERN"
# untracked files too
git ls-files --others --exclude-standard -- "$@" 2>/dev/null | while read -r f; do
  grep -niHE "$PATTERN" "$f"
done
exit 0
