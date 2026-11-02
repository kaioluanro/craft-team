# <BATCH-ID> fix round <n>

**Worktree:** <path>, HEAD <sha> (wip). Work directly in it and do not create a worktree. Read
<original brief path> first; its environment, low-memory, process-safety, sources and self-check
rules still apply. Finish with a wip commit, made only after a green CI; never push and never
squash.

Logs: CI <path>; fail-before <path>; shots <dir>, prefix fix<n>-.

Every new sentence goes back to legal, so list them in the report.

## Required (code review), in order
1. **<Finding as a fix>.** <What is wrong, where (file/function), the exact behaviour required,
   the tests to add and which need a recorded fail-before.>

## Required (legal)
2. <Exact wording/name change, plus a grep that must print nothing afterwards.>

## Required (interface review), in order
3. <Mandatory change with values; shots to take, in which theme and language.>

## Optional, do it
4. <...>

## CI and report
Format, touch the entry files, run the CI once in the foreground after your last edit. It must end
with "<success line>" and CI_EXIT 0, and every build line must point to this worktree.

Report: each item done with file:line, its tests and fail-before group; contrast pairs with
theme; shots; new strings; CI line, path check, empty self-check; retries; what was not verified.
