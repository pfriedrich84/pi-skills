# Clawpatch

This skill wraps the `clawpatch` CLI for structured repository review and conservative one-finding-at-a-time remediation.

Use it for:

- repository reliability checks,
- pipeline and validation review,
- focused code-review findings,
- triage of persisted `.clawpatch/` findings,
- explicit fix loops for approved findings.

## What clawpatch does

`clawpatch` maps a repository into semantic feature slices, reviews those slices with a provider, persists findings, and can run an explicit fix loop for one finding at a time.

The fix loop changes the worktree but does not commit, push, open pull requests, merge, or land changes automatically.

## Recommended structure

```text
skills/clawpatch/
  SKILL.md
  README.md
```

## Typical workflow

```bash
git status --short
clawpatch doctor
clawpatch init
clawpatch map
clawpatch review --limit 3 --jobs 1
clawpatch report
clawpatch next
```

Inspect a finding:

```bash
clawpatch show --finding <id>
```

Fix only after explicit approval:

```bash
git status --short
clawpatch fix --finding <id>
clawpatch revalidate --finding <id>
git diff -- . ':!.clawpatch'
git status --short
```

## Safety posture

This skill is intentionally conservative:

- review before fix,
- one finding per fix loop,
- no automatic commits or PRs,
- no CI/workflow edits unless explicitly allowed,
- always show diff and validation after fixes.
