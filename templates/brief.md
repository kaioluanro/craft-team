# <BATCH-ID>: <one-line goal in user terms>

Work in an isolated worktree based on <branch>. Run `git merge --ff-only <branch>` first, so you
sit on <base sha> (<previous batch>). Make wip commits; never push and never squash.

## Environment
- **Build settings:** target dir <path>, <N ≥ 4> jobs. One heavy command at a time.
- **Before the first build,** touch <entry files> so every build line points to your worktree.
- **Low memory:** if the system stops a build for low memory (<project-specific signs>), retry
  that command once, right away. If the retry dies too, delete <incremental cache> and retry once
  more. Only then stop and report. Never clean the whole target.
- **CI:** after your last edit, run `<ci command> > <log> 2>&1; echo CI_EXIT $? >> <log>` once, in
  the foreground. It must end with "<success line>" and CI_EXIT 0. Never make a wip commit after a
  red CI.
- **Fail-before log:** <path>, with real runs and their output. Sort every new test into: recorded
  fail-before, new API with no base run, or guard.
- **Outputs:** <out dir>. Shots: <shots dir>, prefix NN-; read each one.
- **App** (only if a UI path is involved): <how to start it, port, data dir, how to check the
  port belongs to you, language/theme switches, how to save/open without native dialogs>.

## Code navigation
<graph/index tool command, if any>. Confirm each hit in your worktree, then read only the located
lines. Start from:
- <file/symbol>: <why>

## Process safety
- Kill only your own PIDs, by exact number. Never kill <protected PIDs>. Never run a command that
  matches every instance of the app.
- If a kill or any other action is denied, stop and report it; never ask anyone else to do it.
- Leave no app running.

## Sources (only these)
- <Extrato §…>
- <Logica rules/tests …> (approved by legal), and its legal notes.
- <AUDIT rows …>
- Never open <original manual, research, private files>.

## Plan-id rules
- Code comments are behaviour in our own words. No plan references anywhere: no requirement or
  rule ids, no section signs, nor their snake-case forms in test names; no plan words; no batch
  talk.
- **Self-check, must print nothing:** `<.claude/team/selfcheck.sh with base sha>`. Run it on new
  untracked files too.

## Scope
First write down, in the report, what the app does today for <feature>.

1. **<Item>.** <Exact expected result, with concrete inputs and outputs.>
2. ...

## Rules
- **Tests:** <named acceptance tests with inputs and expected results; which need a recorded
  fail-before>.
- **Never crash:** no panic paths or unchecked indexing on input; checked arithmetic; bounded work
  (<the specific bound>).
- **Strings:** every new user-facing string in <languages>, in our own words; list them all.

## UI review (if UI changes)
Load `ui-design-craft`. Measure every new text/background pair with `contrast.py` in every theme;
name the theme. No state by colour alone.

## Usage test (real input)
1. <Steps a user takes, via the app's real input channel, with what to shoot.>

## Report
- What the app did before.
- Each scope item: done, its tests and their fail-before groups.
- <Design notes the reviewer needs.>
- The CI line, the path check and the empty self-check.
- Contrast pairs, shots with what each shows, new strings.
- Proposed audit rows: <ids>.
- What was not verified.
