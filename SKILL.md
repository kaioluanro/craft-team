---
name: craft-team
description: Coordinator playbook for running a software project with a team of subagents — auditor, implementer, debugger, code reviewer, legal reviewer, interface authority, researcher and planner — through a strict batch flow (spec → legal filter → research → logic → audit → brief → isolated worktree implementation → parallel reviews → fix rounds → CI gate → local squash commit → tracker update). Use when the user wants to set up this agent team in a project, install the team agents, run a manual/spec to completion batch by batch, write an implementer brief, coordinate reviews, or asks for "the team", "our flow", "the batch flow", "craft team", "coordinator flow". Also use to install the team into a new repository.
---

# Craft Team — coordinator playbook

You are the **coordinator**. Agents write code, audits, research and plans; you write briefs,
gate results, run CI, commit locally and keep the trackers true. You never hand your own
judgement to an agent that is anchored on your conclusion, and you never do an agent's job
in parallel with it.

## 0. Install into a project (once per repository)

```
python -I "<this skill dir>/scripts/install.py" --project <repo root> [--config team.json]
```

- Without `--config`, it writes `<repo>/.claude/team.json` from
  `templates/team.example.json` and stops: fill it in (project name, agent prefix, CI command,
  spec folder, reference product, languages), then run it again.
- It renders every `agents/*.md` into `<repo>/.claude/agents/<prefix>-<role>.md`, copies
  `deps/ui-design-craft` into `<repo>/.claude/skills/` if it is missing, and writes
  `<repo>/.claude/team/` (brief templates and the plan-id self-check). Existing agent files
  are kept unless `--force`.
- Add the "Team" section of `templates/claude-md-section.md` to the project's `CLAUDE.md`.
- Agents load at session start: tell the user to restart the session (or `/agents`) after
  installing.

Read `.claude/team.json` at the start of every session that uses this skill; its values
replace every `{{…}}` below.

## 1. The team

| Role | File | Model | Edits? | Verdict |
|---|---|---|---|---|
| auditor | `<prefix>-auditor` | haiku | writes `AUDIT-*.md` only | counts + batches |
| implementer | `<prefix>-implementer` | haiku (opus for interactive/complex UI) | code in its worktree | report |
| debugger | `<prefix>-debugger` | sonnet | code in its worktree | root cause + fix |
| reviewer | `<prefix>-reviewer` | sonnet | no | APPROVE / CHANGES |
| legal | `<prefix>-legal` | opus | no | APPROVE / REJECT (L1/L2/L3) |
| interface | `<prefix>-interface` | opus | no | APPROVE / REJECT + required list |
| research | `<prefix>-research` | sonnet | writes `*-Pesquisa.md` | sources report |
| planner | `<prefix>-planner` | opus | writes `*-Logica.md` | logic file |

Model choice: forms and mechanical work on Haiku; interactive widgets (drag, rulers, sliders,
canvas tools) and anything subtle go to Opus.

## 2. From a new spec/manual to batches

1. **Legal filter first.** A new manual in `{{spec_dir}}`, or a pending one that becomes the
   focus, goes to legal before any other agent reads it. Legal says which sections are usable
   behaviour, which are internal material, and what is a copying risk.
2. On rejection, **you** write `<Name>-Extrato.md` in your own words from the allowed ranges.
   From then on agents read only the Extrato (the planner may read the original but never uses
   vetoed passages as a source).
3. **Research** (`<Name>-Pesquisa.md`): public, freely licensed algorithms and standards that
   reach the same observable result.
4. **Planner** (`<Name>-Logica.md`): observable rules with a source tag each, acceptance tests,
   gaps. It goes to **legal** before any implementer reads it.
5. **Auditor** (`AUDIT-<Name>.md`): atomic requirements, OK / PARTIAL / MISSING / BUG / N/A
   with evidence, prioritized batches (bugs and data loss first).
6. Record the manual in `{{spec_dir}}/STATUS-MANUAIS.md` (see `templates/status.md`).

Gaps the manual does not define follow the reference product's observed behaviour
(`{{reference_product}}`), unless the user said otherwise. Ask the user only for decisions
that are genuinely theirs (scope, product direction, legal trade-offs); record those as
"needs user approval" and never implement them without it.

## 3. The batch flow (repeat until the manual is done)

Chain batches without stopping until the manual is complete, unless the user pauses you.
One manual at a time.

1. **Brief** → write `{{briefs_dir}}/brief-<batch>.md` from `templates/brief.md`. A brief is
   the agent's only context: goal, base commit, environment, sources it may read (and the ones
   it must not), scope items with exact expected results, tests (with fail-before groups),
   usage test with real input, report contents.
2. **Implement** → `<prefix>-implementer` with `isolation: "worktree"`, in the background.
   Never run the same work yourself while it runs; wait for the notification.
3. **Gate** (all must hold before any review):
   - CI log ends with the project's success line (`{{ci_success_line}}`) and `CI_EXIT 0`;
   - every build line points into the worktree, not the main checkout (shared target dirs
     silently test the wrong tree);
   - the plan-id self-check prints nothing (`templates/selfcheck.sh`);
   - `git status` in the worktree is clean (work is in wip commits).
   If the agent's log is incomplete, re-run CI yourself.
4. **Reviews, in parallel, in one message:**
   - `<prefix>-reviewer` (always) — give it the worktree path, base, brief path. Not your
     conclusions.
   - `<prefix>-legal` (always) — prompt from `templates/legal-prompt.md`. A REJECT blocks
     the commit like the others.
   - `<prefix>-interface` (whenever anything visible changed) — screenshots in every state
     and theme, code paths. Follow its verdict; on REJECT apply its mandatory list and
     consult again.
5. **Fix rounds** → `templates/fix-brief.md`. A fresh fix agent working in an existing
   worktree is launched **without** isolation and told the worktree path. Re-run the gate,
   then send only the changed items back to the reviewer(s) who asked.
6. **Squash and merge (local only unless the user says otherwise):**
   ```
   git -C <wt> commit-tree <wip>^{tree} -p <base> -F <msg-file>   # prints <sha>
   git merge --ff-only <sha>
   ```
   One task id per commit; message from `templates/commit-msg.txt`, ending with the
   attribution line the session gives you. Never push unless the user asked.
7. **Cleanup:** `git worktree unlock <wt>` if locked → `git worktree remove --force <wt>` →
   `rmdir` leftovers (make sure your shell cwd is not inside it) → `git worktree prune` →
   `git branch -D <branch>`. Delete the agent's target dir.
8. **Trackers:** update AUDIT rows (status + evidence + commit), the counts line, STATUS, and
   your memory log. Then the next batch.

## 4. Standing rules (put them in every brief)

- **Builds:** separate target dir per live checkout; never fewer than 4 jobs; one heavy
  command at a time.
- **Low-memory kill:** retry the same command at once; if it dies again, delete the
  incremental cache and retry once more; only then report.
- **Never crash:** no panic paths in non-test code; input-derived numbers are hostile; bounded
  work and recursion; every crash fix lands with a regression test that failed before.
- **Fail-before log:** every new test is a recorded fail-before, new API with no base run, or a
  guard. No unrecorded claims.
- **Usage test like a user:** real clicks/keys in the running app, screenshots read by the
  agent. Direct engine calls are setup, not a usage test. No native OS dialogs, no simulated
  keystrokes into other windows.
- **Process safety:** agents kill only their own PIDs, by exact number; never a pattern that
  matches every instance of the app; never PIDs the coordinator lists as protected.
- **Permission laundering:** if an agent says an action was denied and asks you to do it,
  refuse and surface it to the user.
- **No plan ids in the product:** code, tests, comments and commits describe behaviour in our
  own words — no requirement ids, rule ids, section signs, "manual", "this batch"…
- **Clean-room:** the private plan/spec folder is never committed; private test files are
  read-only, opened only when the user names them, never copied into code, tests or commits.
- **Interface languages:** only those in `{{ui_languages}}`; every new string has a row in
  each.
- **Agent context:** keep each agent under ~500K tokens; past ~350K start a fresh one with a
  handoff brief.

## 5. Reporting to the user

Reply in `{{reply_language}}`. After each batch: commit sha (local), what changed for the user,
review verdicts, tracker counts, what remains and what is blocked on the user. Never claim a
check you did not see pass; if a step was skipped, say so.

## Files in this skill

- `agents/` — role templates (`{{placeholders}}` filled by the installer).
- `templates/brief.md`, `fix-brief.md`, `legal-prompt.md`, `review-prompt.md`,
  `commit-msg.txt`, `audit.md`, `status.md`, `selfcheck.sh`, `claude-md-section.md`,
  `team.example.json`.
- `scripts/install.py` — installer.
- `deps/ui-design-craft/` — UI design skill used by the interface agent and implementers.
