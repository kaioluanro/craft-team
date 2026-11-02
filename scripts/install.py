"""Install the craft-team agents and templates into a project.

Usage:
    python -I install.py --project <repo root> [--config <team.json>] [--force]

Without a config (and with no <repo>/.claude/team.json yet) it writes the example config there
and stops, so the coordinator can fill it in first.
"""

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
ROLES = ["auditor", "implementer", "debugger", "reviewer", "legal", "interface", "research", "planner"]
REQUIRED = [
    "project_name", "project_desc", "prefix", "reference_product", "rules_file", "spec_dir",
    "briefs_dir", "ci_command", "ci_success_line", "usage_test_hint", "ui_theme_hint",
    "ui_languages", "reply_language",
]
PLACEHOLDER = re.compile(r"\{\{([a-z_]+)\}\}")


def render(text, cfg):
    missing = set()

    def sub(m):
        key = m.group(1)
        if key in cfg:
            return str(cfg[key])
        missing.add(key)
        return m.group(0)

    out = PLACEHOLDER.sub(sub, text)
    return out, missing


def set_model(text, model):
    return re.sub(r"(?m)^model: .*$", f"model: {model}", text, count=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--config")
    ap.add_argument("--force", action="store_true", help="overwrite existing agent files")
    args = ap.parse_args()

    repo = Path(args.project).resolve()
    if not repo.is_dir():
        sys.exit(f"not a directory: {repo}")
    claude = repo / ".claude"
    cfg_path = Path(args.config).resolve() if args.config else claude / "team.json"

    if not cfg_path.exists():
        claude.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SKILL / "templates" / "team.example.json", cfg_path)
        print(f"wrote {cfg_path}: fill it in, then run the installer again")
        return 1

    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    absent = [k for k in REQUIRED if not str(cfg.get(k, "")).strip()]
    if absent:
        sys.exit(f"{cfg_path} is missing: {', '.join(absent)}")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", cfg["prefix"]):
        sys.exit("prefix must be lowercase letters, digits and dashes")
    models = cfg.get("models", {})

    agents_dir = claude / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    for role in ROLES:
        text, missing = render((SKILL / "agents" / f"{role}.md").read_text(encoding="utf-8"), cfg)
        if missing:
            sys.exit(f"agents/{role}.md needs config keys: {', '.join(sorted(missing))}")
        if role in models:
            text = set_model(text, models[role])
        dest = agents_dir / f"{cfg['prefix']}-{role}.md"
        if dest.exists() and not args.force:
            print(f"kept   {dest} (use --force to overwrite)")
            continue
        dest.write_text(text, encoding="utf-8", newline="\n")
        print(f"agent  {dest}")

    ui_skill = claude / "skills" / "ui-design-craft"
    if not ui_skill.exists():
        shutil.copytree(SKILL / "deps" / "ui-design-craft", ui_skill)
        print(f"skill  {ui_skill}")

    team = claude / "team"
    team.mkdir(parents=True, exist_ok=True)
    for name in ["brief.md", "fix-brief.md", "legal-prompt.md", "review-prompt.md",
                 "commit-msg.txt", "audit.md", "status.md", "selfcheck.sh"]:
        shutil.copyfile(SKILL / "templates" / name, team / name)
    section, _ = render((SKILL / "templates" / "claude-md-section.md").read_text(encoding="utf-8"), cfg)
    (team / "claude-md-section.md").write_text(section, encoding="utf-8", newline="\n")
    print(f"tmpl   {team}")

    rules = repo / cfg["rules_file"]
    if rules.exists() and "## Team (craft-team)" in rules.read_text(encoding="utf-8"):
        print(f"{rules.name} already has the Team section")
    else:
        print(f"next: paste {team / 'claude-md-section.md'} into {rules}")
    print("restart the Claude Code session (or open /agents) so the new agents load")
    return 0


if __name__ == "__main__":
    sys.exit(main())
