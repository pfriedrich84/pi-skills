# Tune Repo Templates

Replace placeholders with project-specific facts discovered from the repository. Do not invent commands or invariants.

## `docs/agent/RULES.md`

```markdown
# Agent Rules

Core rules for coding agents working on <Project>.

## Product / domain safety

- Keep <primary deployment/runtime invariant>.
- Do not <unsafe domain action>.
- Preserve <important user data/invariant>.

## Change discipline

- Prefer small, reviewable changes.
- Update docs when behavior changes.
- Run relevant checks before finishing code changes; see [`CHECKS.md`](CHECKS.md).
- Do not expose or modify secrets from `.env` or runtime data.

## Domain invariants

- <Invariant 1>.
- <Invariant 2>.
- <Invariant 3>.
```

## `docs/agent/PROJECT.md`

```markdown
# Agent Project Brief — <Project>

Concise project context for coding agents. Prefer canonical docs linked below instead of duplicating them here.

## Purpose

<Project purpose in one paragraph.>

## Core architecture

- **<Subsystem>** owns <responsibility>.
- **<Subsystem>** owns <responsibility>.
- **<Storage/runtime>** provides <responsibility>.

## Important paths

```text
<path>/        <purpose>
<path>/        <purpose>
docs/          User/developer documentation
docs/agent/    Tool-neutral agent instructions
```

## Canonical docs

- [`../developer/architecture.md`](../developer/architecture.md) — architecture and data flow.
- [`../user/installation.md`](../user/installation.md) — installation and local development.
- [`../user/configuration.md`](../user/configuration.md) — runtime configuration.

## Agent docs

- [`RULES.md`](RULES.md) — non-negotiable project rules.
- [`CHECKS.md`](CHECKS.md) — validation commands.
- [`WORKFLOWS.md`](WORKFLOWS.md) — reusable maintenance workflows.
- [`SAFETY.md`](SAFETY.md) — safe/unsafe operations.
- [`AUTORESEARCH.md`](AUTORESEARCH.md) — optional metric-driven experiment workflow.
```

## `docs/agent/CHECKS.md`

Use exact commands discovered from the repository or CI. Do not invent commands. Mark commands that require optional tools or dependencies.

```markdown
# Agent Checks

Validation commands for agents. Run the smallest relevant set before finishing code changes, and report what passed or failed.

## <Subsystem>

From <directory>:

```bash
<command>
<command>
```

Use when changing <paths or file types>.

## Documentation-only changes

```bash
python scripts/check_markdown_links.py
```

Use when changing Markdown files, docs indexes, or agent instruction shims. Also verify that command examples and referenced paths are correct.
```

## `docs/agent/WORKFLOWS.md`

```markdown
# Agent Workflows

Reusable, tool-neutral workflows for common repository tasks.

## Standard change workflow

1. Read [`RULES.md`](RULES.md) and relevant project docs.
2. Keep the change small and reviewable.
3. Update tests and docs when behavior changes.
4. Run relevant checks from [`CHECKS.md`](CHECKS.md).
5. Summarize changed files, validation results, and follow-up work.

## Local CI simulation

Use this when a change touches multiple subsystems or CI configuration.

1. `<command>`
2. `<command>`

If one check fails, continue with independent checks where practical so the final report is complete.
```

## `docs/agent/SAFETY.md`

```markdown
# Agent Safety

Tool-neutral safety guidance for coding agents.

## Allowed by default

- Read, search, and make targeted edits to repository files.
- Run validation commands listed in [`CHECKS.md`](CHECKS.md).
- Use read-only Git commands for orientation: `git status`, `git diff`, `git log`, `git branch`.

## Ask first / avoid unless explicitly requested

- Destructive filesystem operations, especially recursive deletes.
- History rewriting or destructive Git operations such as force-push or hard reset.
- Broad formatting or large refactors unrelated to the task.

## Never do

- Do not print, copy, or modify secrets from `.env` or runtime data directories.
- Do not weaken authentication, authorization, review gates, or audit logging without an explicit security-driven task.

## Before finishing

Run the relevant checks from [`CHECKS.md`](CHECKS.md), or state clearly why checks were not run.
```

## Optional ecosystem check examples

Add only the sections that match the repository.

```markdown
## Python

```bash
python3 -m compileall <paths>
python3 -m pytest
ruff check .
```

Use when changing Python code. Run commands only when the required tools/dependencies are installed.

## Node / TypeScript

```bash
npm test
npm run lint
npm run typecheck
npm run build
```

Use the package manager implied by the lockfile and scripts.

## Home Assistant custom integration

```bash
python3 -m compileall custom_components tests scripts
python3 -m pytest
```

Also review `custom_components/<domain>/manifest.json`, `hacs.json`, and HACS/Hassfest workflows when changing integration metadata.

## Docker / containers

```bash
docker compose config
docker build .
```

Use only when container files changed and the commands are practical in the local environment.
```

## Optional documentation files

Create only when useful.

```markdown
# docs/developer/testing.md

Describe test setup, fixtures, services, hardware requirements, and how to run focused tests.

# docs/user/configuration.md

Describe user-facing configuration fields, defaults, examples, and migration notes.

# docs/user/troubleshooting.md

Describe symptoms, likely causes, diagnostic commands/logs, and safe recovery steps.

# docs/developer/adr/0001-example.md

Record significant architectural decisions with context, decision, consequences, and alternatives considered.
```

## Tool-specific shims

Use for `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, and similar files. Adjust heading to the filename/tool.

```markdown
# <TOOL>.md

This repository uses tool-neutral agent instructions.

Read [`AGENTS.md`](AGENTS.md) first.
```

For nested files such as `.github/copilot-instructions.md`, adjust the relative link:

```markdown
# Copilot Instructions

This repository uses tool-neutral agent instructions.

Read [`../AGENTS.md`](../AGENTS.md) first.
```

## `docs/agent/AUTORESEARCH.md`

```markdown
# Agent Autoresearch

Optional workflow for autonomous, metric-driven experiment loops. Use it only when the task has a measurable target and repeated iterations are useful.

## Good fits

- Performance optimization.
- Quality/accuracy experiments on fixtures.
- UI improvements with measurable checks.
- Best-practice hardening with a stable metric.

## Poor fits

- Documentation-only cleanup.
- Broad subjective refactors without a primary metric.
- Security-sensitive behavior changes without explicit review.

## Required setup

Before starting an experiment loop, define:

1. Primary metric.
2. Benchmark command.
3. Safety checks.
4. Rollback rule.
5. Data boundary.

## Experiment rules

- Keep each iteration small and reviewable.
- Run relevant checks after each kept result.
- Record failed ideas and why they failed.
- Do not keep a change solely because a secondary metric improved.
```
