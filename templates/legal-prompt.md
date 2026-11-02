Review batch <BATCH-ID> before commit.

- Worktree: <path>. Diff: `git -C <path> diff <base>` plus untracked files.
- Brief: <brief path> (what the batch was asked to do). Sources the implementer used: <list>.
- Reference text to compare against, if any: <original manual path / ranges>.
- New user-facing strings (en + other languages): see the report excerpt below, but read the
  diff yourself — do not rely on the list.
- Screenshots (if UI changed): <paths>.

Names already changed and committed, or kept by the user's decision, are settled. Do not raise
them again. Review only what this batch's diff adds or changes.
<Project-specific settled decisions, one line each, e.g. "the <x> licence note is settled and
never blocks a batch".>

Return the verdict in the agent's required format.
