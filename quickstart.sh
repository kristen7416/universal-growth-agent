#!/usr/bin/env bash
# Universal Growth Agent - Quickstart & Skill Installer
# Compatible with Google Antigravity, Claude Code, and Codex environments.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$SCRIPT_DIR/skills"

echo "=========================================================="
echo "🚀 Universal Growth Agent - Setup & Skill Installer"
echo "=========================================================="

show_usage() {
  echo "Usage: $0 [command]"
  echo ""
  echo "Commands:"
  echo "  install        Install all growth skills into local AI agent environments"
  echo "  init <name>    Initialize a new product marketing workspace"
  echo "  matrix <name>  Generate the 12-channel lifecycle growth matrix"
  echo "  help           Show this help message"
  echo ""
}

install_skills() {
  echo "📦 Installing skills into local environments..."

  # 1. Antigravity (~/.gemini/config/skills)
  GEMINI_SKILLS_DIR="$HOME/.gemini/config/skills"
  if [ -d "$HOME/.gemini" ]; then
    mkdir -p "$GEMINI_SKILLS_DIR"
    for skill_path in "$SKILLS_DIR"/*; do
      if [ -d "$skill_path" ]; then
        skill_name="$(basename "$skill_path")"
        rm -rf "$GEMINI_SKILLS_DIR/$skill_name"
        cp -R "$skill_path" "$GEMINI_SKILLS_DIR/$skill_name"
        echo "  ✓ Installed $skill_name -> Antigravity ($GEMINI_SKILLS_DIR/$skill_name)"
      fi
    done
  fi

  # 2. Claude Code (~/.claude/skills)
  CLAUDE_SKILLS_DIR="$HOME/.claude/skills"
  if [ -d "$HOME/.claude" ]; then
    mkdir -p "$CLAUDE_SKILLS_DIR"
    for skill_path in "$SKILLS_DIR"/*; do
      if [ -d "$skill_path" ]; then
        skill_name="$(basename "$skill_path")"
        rm -rf "$CLAUDE_SKILLS_DIR/$skill_name"
        cp -R "$skill_path" "$CLAUDE_SKILLS_DIR/$skill_name"
        echo "  ✓ Installed $skill_name -> Claude Code ($CLAUDE_SKILLS_DIR/$skill_name)"
      fi
    done
  fi

  # 3. Codex (~/.codex/skills)
  CODEX_SKILLS_DIR="$HOME/.codex/skills"
  if [ -d "$HOME/.codex" ]; then
    mkdir -p "$CODEX_SKILLS_DIR"
    for skill_path in "$SKILLS_DIR"/*; do
      if [ -d "$skill_path" ]; then
        skill_name="$(basename "$skill_path")"
        rm -rf "$CODEX_SKILLS_DIR/$skill_name"
        cp -R "$skill_path" "$CODEX_SKILLS_DIR/$skill_name"
        echo "  ✓ Installed $skill_name -> Codex ($CODEX_SKILLS_DIR/$skill_name)"
      fi
    done
  fi

  echo ""
  echo "🎉 All skills successfully installed and ready to be invoked!"
}

init_product() {
  PRODUCT_NAME="${1:-MyProduct}"
  TARGET_DIR="$PWD/$PRODUCT_NAME-growth"
  mkdir -p "$TARGET_DIR"

  echo "📁 Initializing growth workspace in: $TARGET_DIR"
  cp "$SCRIPT_DIR/templates/product-fact-sheet.md" "$TARGET_DIR/product-fact-sheet.md"
  cp "$SCRIPT_DIR/templates/campaign-brief.template.md" "$TARGET_DIR/campaign-brief.md"
  cp "$SCRIPT_DIR/templates/operations-memory.template.json" "$TARGET_DIR/operations-memory.json"

  python3 "$SCRIPT_DIR/tools/generate_growth_matrix.py" --product "$PRODUCT_NAME" --output "$TARGET_DIR/growth-matrix.md"

  echo "  ✓ Created product-fact-sheet.md"
  echo "  ✓ Created campaign-brief.md"
  echo "  ✓ Created operations-memory.json"
  echo "  ✓ Generated growth-matrix.md"
  echo ""
  echo "👉 Next step: Open $TARGET_DIR/product-fact-sheet.md and fill in your product details!"
}

case "${1:-install}" in
  install)
    install_skills
    ;;
  init)
    init_product "${2:-MyProduct}"
    ;;
  matrix)
    python3 "$SCRIPT_DIR/tools/generate_growth_matrix.py" --product "${2:-MyProduct}"
    ;;
  help|--help|-h)
    show_usage
    ;;
  *)
    echo "Unknown command: $1"
    show_usage
    exit 1
    ;;
esac
