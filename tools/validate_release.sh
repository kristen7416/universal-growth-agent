#!/usr/bin/env bash

set -u

usage() {
  echo "Usage: $0 OUTPUT_DIR [EXPECTED_ARTICLE_COUNT] [REQUIRED_URL] [EXPECTED_IMAGE_SIZE]" >&2
  echo "Example: $0 ./release 18 https://github.com/example/repo 1024x572" >&2
}

if [ "$#" -lt 1 ]; then
  usage
  exit 2
fi

output_dir=$1
expected_count=${2:-}
required_url=${3:-}
expected_size=${4:-}
errors=0
warnings=0

error() {
  echo "ERROR: $*" >&2
  errors=$((errors + 1))
}

warn() {
  echo "WARN: $*" >&2
  warnings=$((warnings + 1))
}

if [ ! -d "$output_dir" ]; then
  error "output directory does not exist: $output_dir"
  echo "Validation failed with $errors error(s)." >&2
  exit 1
fi

article_list=$(find "$output_dir" -maxdepth 1 -type f -name '[0-9][0-9]-*.md' ! -name '00-*' ! -name '*-配图提示词.md' | sort)
article_count=$(printf '%s\n' "$article_list" | awk 'NF { count++ } END { print count + 0 }')

if [ -n "$expected_count" ] && [ "$article_count" -ne "$expected_count" ]; then
  error "expected $expected_count article(s), found $article_count"
fi

if [ "$article_count" -eq 0 ]; then
  error "no numbered article Markdown files found"
fi

while IFS= read -r article; do
  [ -n "$article" ] || continue

  title_count=$(grep -c '^# ' "$article" || true)
  if [ "$title_count" -ne 1 ]; then
    error "article must contain exactly one H1: $article"
  fi

  if grep -Eq 'TODO|TBD|XXX|待补充|待确认|占位' "$article"; then
    error "placeholder text found: $article"
  fi

  if [ -n "$required_url" ]; then
    last_line=$(awk 'NF { line=$0 } END { print line }' "$article")
    case "$last_line" in
      *"$required_url"*) ;;
      *) error "required URL is not in the last non-empty line: $article" ;;
    esac
  fi
done <<EOF
$article_list
EOF

manifest=$(find "$output_dir" -maxdepth 1 -type f -name '00-*.md' | head -n 1)
if [ -z "$manifest" ]; then
  error "missing 00 release manifest"
fi

prompt_file=$(find "$output_dir" -maxdepth 1 -type f -name '*-配图提示词.md' | head -n 1)
image_dir="$output_dir/配图"

if [ -n "$prompt_file" ]; then
  if [ ! -d "$image_dir" ]; then
    warn "prompt file exists but image directory is missing"
  else
    while IFS= read -r image_name; do
      [ -n "$image_name" ] || continue
      if [ ! -f "$image_dir/$image_name" ]; then
        error "referenced image is missing: $image_name"
      fi
    done <<EOF
$(awk -F'`' '/\*\*文件名\*\*/ { print $2 }' "$prompt_file")
EOF
  fi
else
  warn "image prompt file not found"
fi

image_count=0
if [ -d "$image_dir" ]; then
  image_list=$(find "$image_dir" -maxdepth 1 -type f ! -name '._*' \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' -o -iname '*.webp' \) | sort)
  image_count=$(printf '%s\n' "$image_list" | awk 'NF { count++ } END { print count + 0 }')

  if [ -n "$expected_count" ] && [ "$image_count" -gt 0 ] && [ "$image_count" -ne "$expected_count" ]; then
    error "expected $expected_count image(s), found $image_count"
  fi

  if [ -n "$expected_size" ] && [ "$image_count" -gt 0 ]; then
    expected_width=${expected_size%x*}
    expected_height=${expected_size#*x}
    if command -v sips >/dev/null 2>&1; then
      while IFS= read -r image; do
        [ -n "$image" ] || continue
        width=$(sips -g pixelWidth "$image" 2>/dev/null | awk '/pixelWidth/ { print $2 }')
        height=$(sips -g pixelHeight "$image" 2>/dev/null | awk '/pixelHeight/ { print $2 }')
        if [ "$width" != "$expected_width" ] || [ "$height" != "$expected_height" ]; then
          error "unexpected image size ${width}x${height}: $image"
        fi
      done <<EOF
$image_list
EOF
    else
      warn "sips is unavailable; skipped image dimension validation"
    fi
  fi
fi

temp_files=$(find "$output_dir" -type f \( -name '._*' -o -name '.viewport-*' -o -name '.figma-*' -o -name '.export-*' -o -name '*.tmp' \) | head -n 1)
if [ -n "$temp_files" ]; then
  warn "temporary or metadata files remain in the release package"
fi

if [ "$errors" -gt 0 ]; then
  echo "Validation failed: $errors error(s), $warnings warning(s)." >&2
  exit 1
fi

echo "Validation passed: $article_count article(s), $image_count image(s), $warnings warning(s)."
