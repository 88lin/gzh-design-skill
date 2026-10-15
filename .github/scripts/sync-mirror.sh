#!/usr/bin/env bash
set -euo pipefail

source_dir="$(realpath "$1")"
target_repo="$(realpath "$2")"
# Keep the checkout and the mirror disjoint, including symlink-resolved paths.
case "$target_repo/" in "$source_dir/"*) echo "Target must be outside source" >&2; exit 1;; esac
case "$source_dir/" in "$target_repo/"*) echo "Source must be outside target" >&2; exit 1;; esac
test -d "$source_dir"
test -d "$target_repo"

mirror_dir="$target_repo/gzh-skill-kit"
rm -rf -- "$mirror_dir"
mkdir -p "$mirror_dir"
rsync -a --exclude='.git' --exclude='.github' "$source_dir/" "$mirror_dir/"
test ! -d "$mirror_dir/dst"
