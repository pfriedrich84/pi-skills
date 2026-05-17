---
name: clawpatch
description: Use the clawpatch CLI to map a repository into semantic feature slices, run structured code reviews, report findings, triage issues, and fix one explicitly approved finding at a time. Use for repository reliability checks, pipeline reviews, focused code review, and conservative finding/fix loops.
---

# Clawpatch

Use this skill when the user wants a structured repository review with `clawpatch`, especially for pipeline reliability, code quality, architecture-adjacent findings, or one-finding-at-a-time remediation.

`clawpatch` is a CLI review tool. It maps a repository into feature records, reviews those features with a provider, persists findings under `.clawpatch/`, and can run an explicit patch loop for a selected finding.

## Preconditions

Before using this skill, verify the CLI and provider are available:

```bash
clawpatch --version || true
codex --version || true
clawpatch doctor
```

If `clawpatch` is missing, install it with:

```bash
pnpm add -g clawpatch
```

## Safety rules

- Always inspect the repository state first with `git status --short`.
- Prefer read-only commands first: `doctor`, `init`, `map`, `status`, `review`, `report`, `next`, and `show`.
- Do not run `clawpatch fix` unless the user explicitly approves fixing a specific finding ID.
- Fix only one finding at a time.
- Do not commit, push, open a pull request, merge, release, deploy, or land changes unless the user explicitly asks for that separate action.
- Do not edit CI/workflow files unless the current task explicitly allows CI/workflow changes.
- Treat `.clawpatch/` as review state and audit metadata. Summarize changes there instead of deleting them blindly.
- After any fix attempt, show the diff, validation result, and remaining git status.
- If the worktree is dirty before a fix, stop and explain what is already modified.

## Standard read-only review workflow

Run this workflow first unless the user asked for a narrower command:

```bash
git status --short
clawpatch doctor
clawpatch init
clawpatch map
clawpatch review --limit 3 --jobs 1
clawpatch report
clawpatch next
```

Use `--jobs 1` by default for conservative, easier-to-debug runs. Increase only when the repository and provider are stable.

## Inspect a finding

```bash
clawpatch show --finding <id>
```

Summarize:

- finding ID
- severity
- affected feature or files
- evidence
- suggested validation
- whether the finding is actionable

## Triage a finding

Use triage only when the evidence clearly supports the decision.

```bash
clawpatch triage --finding <id> --status false-positive --note "covered by tests"
```

Prefer explicit notes. Do not mass-triage findings without user approval.

## Fix loop

Only after explicit user approval for a specific finding ID:

```bash
git status --short
clawpatch fix --finding <id>
clawpatch revalidate --finding <id>
git diff -- . ':!.clawpatch'
git status --short
```

Then report:

- what changed
- whether revalidation passed
- which validation commands ran
- any residual risk
- whether `.clawpatch/` recorded a patch attempt

## Revalidate open findings

For follow-up checks:

```bash
clawpatch revalidate --all --status open
clawpatch report
```

## Provider notes

The default provider is usually the local Codex CLI. `clawpatch` can also be used with supported provider flags such as:

```bash
clawpatch review --provider codex --limit 3 --jobs 1
clawpatch review --provider acpx --limit 3 --jobs 1
```

Use the provider already configured in the repository or environment unless the user asks to switch.

## Recommended use for Coresia / Payments repos

For Coresia payment or banking repositories, use `clawpatch` mainly as a conservative review and reliability checker:

- pipeline reliability findings
- flaky validation paths
- missing or weak test coverage around payment status handling
- risky workflow or approval assumptions
- brittle integration boundaries
- documentation drift that affects agent execution

Keep fixes small, reviewable, and scoped to one finding.
