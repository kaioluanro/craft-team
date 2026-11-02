## Team (craft-team)
- **Dev team** (`.claude/agents/`): `{{prefix}}-auditor` (spec → `AUDIT-*.md`), `{{prefix}}-implementer`
  (one batch in a worktree: code + tests + usage test + green CI, never commits to the main
  branch), `{{prefix}}-debugger` (failing test → root cause → fix), `{{prefix}}-reviewer`
  (read-only diff review, APPROVE/CHANGES), `{{prefix}}-interface` (UI verdict), `{{prefix}}-legal`
  (legal verdict APPROVE/REJECT with same-behaviour alternatives), `{{prefix}}-research` (public
  sources), `{{prefix}}-planner` (observable logic). The coordinator splits work, writes briefs,
  reviews, runs CI and commits.
- **Flow per batch:** brief → implement (worktree) → gate (CI line, build paths, self-check,
  clean status) → reviewer + legal (+ interface if UI changed), in parallel → fix rounds →
  squash → commit locally → trackers. A REJECT/CHANGES from any of them blocks the commit.
- **Specs** live in `{{spec_dir}}` (not committed if private). New or newly focused specs pass
  legal before any agent reads them; on rejection agents read only the coordinator's Extrato.
- **Interface authority:** every UI decision or change goes to `{{prefix}}-interface` with
  screenshots and code paths; follow its verdict.
- **Interface languages:** {{ui_languages}} only; every new string in each.
- **Quality gate before every commit:** `{{ci_command}}` must end with `{{ci_success_line}}`.
