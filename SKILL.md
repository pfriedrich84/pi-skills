---
name: tune-repo
description: Tune a repository for AI coding agents by consolidating tool-specific instructions into a short tool-neutral AGENTS.md, making CLAUDE.md point to it, and reorganizing Markdown docs into docs/agent, docs/developer, and docs/user. Use when the user asks to tune, standardize, or clean up repo agent documentation.
---

# Tune Repo

Turn a repository into an agent-friendly, tool-neutral documentation structure.

The goal is **not** to dump everything into one prompt file. The goal is a small `AGENTS.md` entry point with durable documentation split into `docs/agent/`, `docs/developer/`, and `docs/user/`.

## Desired end state

```text
AGENTS.md                 # short, tool-neutral entry point for all coding agents
CLAUDE.md                 # tiny Claude-specific shim pointing to AGENTS.md
docs/
  README.md               # optional docs index
  agent/
    RULES.md              # non-negotiable project/domain rules
    PROJECT.md            # concise project brief for agents
    CHECKS.md             # validation commands and when to run them
    WORKFLOWS.md          # repeatable maintenance/change workflows
    SAFETY.md             # safe/ask-first/never guidance
    AUTORESEARCH.md       # optional metric-driven experiment guidance, if useful
  developer/              # architecture, CLI/API, contributing, internals, ADR links
  user/                   # installation, configuration, deployment, workflow/how-to docs
```

Use [references/AGENT-DOCS-PATTERN.md](references/AGENT-DOCS-PATTERN.md) as the pattern and [references/TEMPLATES.md](references/TEMPLATES.md) for starter text.

## Before editing: clarify scope

If the user did not explicitly say to implement immediately, ask concise scope questions first. Recommended questions:

1. Should I **only reorganize docs and agent instructions**, or also update links in README/code comments?
2. Should existing docs be **moved with minimal rewriting** or **rewritten into the standard agent-friendly structure**?
3. Should I create all standard agent files (`RULES`, `PROJECT`, `CHECKS`, `WORKFLOWS`, `SAFETY`, `AUTORESEARCH`) even if some are initially short?
4. Should obsolete tool-specific files besides `CLAUDE.md` (for example `.cursor/rules`, `GEMINI.md`, `copilot-instructions.md`) be converted, kept as shims, or left untouched?
5. Should I run validation and commit, or leave changes staged/uncommitted?
6. Should I add useful optional docs suggested by the repository shape, such as ADRs, testing docs, troubleshooting docs, configuration docs, or ecosystem-specific validation examples?
7. If I notice additional improvements while inspecting the repo, should I suggest them and ask before implementing, or include clearly safe documentation-only improvements in this pass?

If the user asks for the default/best-practice scope, use:

- implement the full standard structure;
- always create/normalize all standard agent files: `RULES.md`, `PROJECT.md`, `CHECKS.md`, `WORKFLOWS.md`, `SAFETY.md`, `AUTORESEARCH.md`;
- keep `AGENTS.md` short;
- make `CLAUDE.md` a shim;
- convert other tool-specific instruction files such as `GEMINI.md`, `.cursor/rules`, `.github/copilot-instructions.md`, Windsurf/Cline/Codex files into shims that point to `AGENTS.md`, unless preserving tool-specific content is explicitly required;
- move relevant Markdown into `docs/agent`, `docs/developer`, `docs/user`;
- update README links, docs indexes, and internal Markdown links that break because of moves;
- add a lightweight Markdown local-link checker script when the repository does not already have one;
- add useful optional docs only when the repository shape supports them, such as ADRs, testing docs, troubleshooting docs, configuration docs, or ecosystem-specific validation examples;
- suggest additional improvements discovered during inspection, ask before implementing anything outside the agreed scope, and include only clearly safe documentation-only improvements by default;
- do not commit unless explicitly asked; if asked, commit after validation with a concise message;
- when finishing with uncommitted changes, actively ask whether the user wants the changes committed, and whether they should also be pushed.

## Process

### 1. Inspect repository

Read first, do not edit yet:

- root listing and Git status;
- existing `AGENTS.md`, `CLAUDE.md`, `README.md`, `.github/copilot-instructions.md`, `GEMINI.md`, Cursor/Windsurf rule files, if present;
- existing `docs/` tree;
- package/build files that reveal validation commands (`pyproject.toml`, `package.json`, `composer.json`, `Makefile`, `justfile`, CI workflows, Docker files).

Look for common ecosystem signals and use them to suggest checks without inventing commands:

- Python: `pyproject.toml`, `requirements*.txt`, `tox.ini`, `noxfile.py`, `pytest.ini`, Ruff/Mypy/Pyright config.
- Node/TypeScript: `package.json`, lockfiles, `tsconfig.json`, ESLint/Prettier/Vitest/Jest/Playwright config.
- Home Assistant: `custom_components/`, `hacs.json`, `manifest.json`, Hassfest/HACS workflows, Home Assistant test helpers.
- Docker/containers: `Dockerfile`, `docker-compose*.yml`, `.devcontainer/`, container build/test scripts.
- CI/release: `.github/workflows/`, release scripts, changelog/versioning files.

Identify:

- project purpose and deployment/runtime shape;
- user docs versus developer docs versus agent-only instructions;
- non-negotiable domain/product invariants;
- relevant checks/lints/tests;
- safe/unsafe operations for agents.

### 2. Classify Markdown files

Use these placement rules:

- `docs/agent/`: instructions for coding agents, repo rules, safety, workflows, checks, autoresearch, project brief.
- `docs/developer/`: architecture, APIs, CLI, internal implementation, contributing, testing, ADRs, release engineering.
- `docs/user/`: installation, configuration, deployment, user workflows, operations, troubleshooting.
- Root `README.md`: keep as human entry point; link to docs index.
- Root `AGENTS.md`: keep short; link to `docs/agent/*`.
- Root `CLAUDE.md`: should only point to `AGENTS.md` unless the user explicitly needs Claude-specific differences.

Prefer `git mv`/filesystem moves over copy/delete when preserving history matters.

### 3. Create or normalize agent docs

Create the standard files if missing. Keep them concise and project-specific.

Minimum content expectations:

- `AGENTS.md`: read-first list, project docs list, quick summary, check reminder.
- `CLAUDE.md`: `This repository uses tool-neutral agent instructions. Read [AGENTS.md](AGENTS.md) first.`
- `docs/agent/RULES.md`: hard project/domain invariants and change discipline.
- `docs/agent/PROJECT.md`: purpose, architecture, important paths, canonical docs.
- `docs/agent/CHECKS.md`: commands and when to run them.
- `docs/agent/WORKFLOWS.md`: standard change workflow, local CI simulation, dependency workflow if relevant.
- `docs/agent/SAFETY.md`: allowed, ask-first, never, before finishing.
- `docs/agent/AUTORESEARCH.md`: only if useful; otherwise a short optional workflow note is fine.

Avoid hallucinating commands. If a check is not discoverable, write a placeholder like `TODO: confirm <subsystem> validation command` and mention it in the final summary.

### 4. Update links, indexes, and tool shims

After moving files:

- update Markdown links affected by path changes;
- update README documentation tables/lists so moved docs are discoverable;
- create or refresh `docs/README.md` as a docs index when useful;
- update references to old agent files;
- ensure `AGENTS.md` links are valid;
- ensure docs index links are valid if `docs/README.md` exists;
- convert tool-specific instruction files to shims pointing at `AGENTS.md`:
  - `CLAUDE.md`
  - `GEMINI.md`
  - `.github/copilot-instructions.md`
  - `.cursor/rules/*` or `.cursor/rules.md`
  - `.windsurf/rules/*`
  - `.clinerules`, `.codex/*`, or equivalent when present;
- preserve any truly tool-specific, non-duplicative command syntax only if needed, but keep the canonical repo rules in `AGENTS.md` + `docs/agent/`;
- search for stale paths.

### 4a. Add Markdown local-link checker and optional docs

If the repository does not already have a Markdown link checker, add a lightweight script, preferably under `scripts/check_markdown_links.py` or equivalent. The script should:

- scan `*.md` files while ignoring `.git`, dependencies, virtualenvs, build outputs, and caches;
- validate local relative links and anchors enough to catch moved-file regressions;
- skip external URLs and `mailto:` links;
- exit non-zero on broken local links;
- be documented in `docs/agent/CHECKS.md` as the docs-only validation command.

Keep the script dependency-free unless the repository already has a docs tooling stack. Prefer copying/adapting [`references/LINK-CHECKER-TEMPLATE.py`](references/LINK-CHECKER-TEMPLATE.py), which validates local files and simple Markdown anchors.

Add optional docs only when they are clearly useful:

- `docs/developer/adr/` for significant architectural decisions.
- `docs/developer/testing.md` when tests require setup, fixtures, services, or hardware.
- `docs/user/troubleshooting.md` when user-facing failure modes are discoverable.
- `docs/user/configuration.md` when runtime configuration is non-trivial.
- Ecosystem-specific check examples in `docs/agent/CHECKS.md`, clearly marked by prerequisite tools.

Use small, targeted edits. Do not broadly rewrite prose unless the user requested a rewrite.

### 5. Validate

Always run lightweight validation for docs-only changes:

- `git status --short`
- search for old paths and stale tool-specific instruction references;
- run the repository Markdown local-link checker; if you just added one, run it before finishing.

Run code tests/lints only if code, build files, executable docs, or validation scripts changed, or if the user requested full validation.

### 6. Commit only on request

Do not commit by default. Before finishing with uncommitted changes, actively ask whether the user wants the changes committed, and whether they should also be pushed.

If the user explicitly asks to commit:

1. run the documented docs validation and any relevant checks;
2. inspect `git status --short`;
3. commit all intended documentation/tuning changes with a concise message such as `Tune repository agent documentation`;
4. push only if the user explicitly asks to push.

### 7. Final response

Summarize:

- files created/moved/updated;
- key structure now in place;
- validation run and results;
- open questions/TODOs;
- suggested follow-up improvements that were not implemented;
- whether changes are committed/pushed, or explicitly ask whether uncommitted changes should be committed/pushed.

## Quality bar

- Tool-neutral: `AGENTS.md` is canonical; tool-specific files are shims.
- Concise: agent entry points should be scannable.
- Durable: domain rules and checks live in `docs/agent`, not in chat-only notes.
- Discoverable: user and developer docs are clearly separated.
- Safe: do not expose secrets, do not rewrite history, do not commit unless asked.
