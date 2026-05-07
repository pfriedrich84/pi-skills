# Agent Documentation Pattern

Use this as the default structure for making a repository easy for coding agents to understand, change, and validate.

## Default policy

When the user asks for best-practice defaults:

- always create or normalize the full `docs/agent/` set: `RULES.md`, `PROJECT.md`, `CHECKS.md`, `WORKFLOWS.md`, `SAFETY.md`, `AUTORESEARCH.md`;
- keep `AGENTS.md` short and tool-neutral;
- make tool-specific instruction files shims that point to `AGENTS.md`;
- update README and docs indexes so moved docs stay discoverable;
- move user/operator docs into `docs/user/` and maintainer/developer docs into `docs/developer/`;
- add a dependency-free Markdown local-link checker when none exists;
- add optional docs only when the repository shape supports them, such as ADRs, testing docs, troubleshooting docs, configuration docs, or ecosystem-specific validation examples;
- commit only when the user asks; push only when explicitly asked.

## Root files

### `AGENTS.md`

Characteristics:

- Tool-neutral title.
- Very short.
- Ordered "Read first" list into `docs/agent/`.
- Separate "Project docs" list into `docs/developer/` and `docs/user/`.
- One quick summary of what the project is.
- Final reminder to run relevant checks.

Example shape:

```markdown
# AGENTS.md — <Project> Agent Instructions

Tool-neutral entry point for coding agents working in this repository. Keep this file short; put durable details in `docs/agent/`.

## Read first

1. [`docs/agent/RULES.md`](docs/agent/RULES.md) — non-negotiable project rules and domain invariants.
2. [`docs/agent/PROJECT.md`](docs/agent/PROJECT.md) — project context, architecture notes, and important implementation details.
3. [`docs/agent/CHECKS.md`](docs/agent/CHECKS.md) — validation commands to run before finishing code changes.
4. [`docs/agent/WORKFLOWS.md`](docs/agent/WORKFLOWS.md) — reusable maintenance workflows.
5. [`docs/agent/SAFETY.md`](docs/agent/SAFETY.md) — safe/unsafe operations for agents.
6. [`docs/agent/AUTORESEARCH.md`](docs/agent/AUTORESEARCH.md) — optional metric-driven experiment workflow.

## Project docs

- [`docs/developer/architecture.md`](docs/developer/architecture.md) — architecture and data flow.
- [`docs/user/installation.md`](docs/user/installation.md) — installation and local development.
- [`docs/user/configuration.md`](docs/user/configuration.md) — runtime configuration.

## Quick summary

<Project summary in 2-4 sentences.>

Before finishing code changes, run the relevant checks from [`docs/agent/CHECKS.md`](docs/agent/CHECKS.md).
```

### Tool-specific shim files

Keep `CLAUDE.md` tiny:

```markdown
# CLAUDE.md

This repository uses tool-neutral agent instructions.

Read [`AGENTS.md`](AGENTS.md) first.
```

Use the same principle for `GEMINI.md`, `.github/copilot-instructions.md`, Cursor, Windsurf, Cline, Codex, or similar files. They should point to `AGENTS.md` and avoid duplicating canonical rules.

## Agent docs

### `docs/agent/PROJECT.md`

Include:

- Purpose.
- Core architecture.
- Domain model or safety boundaries.
- Important paths.
- Canonical docs.
- Agent docs.

Keep the project brief concise. Link to canonical docs rather than duplicating full manuals.

### `docs/agent/RULES.md`

Use sections like:

- Product/domain safety.
- Change discipline.
- Domain invariants.

Rules should be phrased as commands: "Do not...", "Keep...", "Prefer...".

### `docs/agent/CHECKS.md`

Group checks by subsystem and say when to run each group. Include exact commands from the repo's actual toolchain. Do not invent commands; use TODO placeholders when a validation command cannot be discovered.

### `docs/agent/WORKFLOWS.md`

Include repeatable workflows when relevant:

- standard change workflow;
- local CI simulation;
- dependency update workflow;
- docs workflow;
- release/deploy workflow.

### `docs/agent/SAFETY.md`

Use three buckets:

- Allowed by default;
- Ask first / avoid unless explicitly requested;
- Never do.

Finish with "Before finishing" check guidance.

### `docs/agent/AUTORESEARCH.md`

Optional but standardized. Useful when the repo has measurable optimization targets. Include:

- good fits;
- poor fits;
- required setup;
- suggested metrics;
- experiment rules.

If metric-driven experimentation is not currently useful, keep the file short and say when it would become useful.

## User/developer split

Use `docs/user/` for docs a deployer/operator/user needs:

- installation;
- configuration;
- deployment;
- user workflows;
- troubleshooting;
- operations and backup/restore.

Use `docs/developer/` for docs a contributor/maintainer needs:

- architecture;
- APIs, CLI, SDK, or internal protocols;
- contributing;
- tests and validation;
- CI/release internals;
- ADRs and design notes.

## Optional additions

Add these only when useful for the repository:

- `docs/developer/adr/` for architecture decision records.
- `docs/developer/testing.md` when tests need setup or fixtures.
- `docs/user/troubleshooting.md` when users have operational failure modes.
- `docs/user/configuration.md` when runtime config is non-trivial.
- Subdirectory `AGENTS.md` files only for large monorepos with different local rules; keep the root `AGENTS.md` canonical.

## Ecosystem-specific validation examples

Use these as discovery prompts, not as commands to invent. Only document commands that are present in the repository, documented by CI, or clearly supported by project configuration.

### Python

Common signals:

- `pyproject.toml`, `setup.cfg`, `setup.py`
- `requirements*.txt`, `uv.lock`, `poetry.lock`, `Pipfile.lock`
- `pytest.ini`, `tox.ini`, `noxfile.py`
- Ruff, Mypy, Pyright, Coverage config

Typical docs/check entries when supported:

```bash
python3 -m compileall <paths>
python3 -m pytest
ruff check .
mypy <package>
```

### Node / TypeScript

Common signals:

- `package.json`
- `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`, `bun.lockb`
- `tsconfig.json`
- ESLint, Prettier, Vitest, Jest, Playwright config

Typical docs/check entries when supported:

```bash
npm test
npm run lint
npm run typecheck
npm run build
```

Use the package manager implied by the lockfile or scripts.

### Home Assistant custom integrations

Common signals:

- `custom_components/<domain>/`
- `hacs.json`
- `custom_components/<domain>/manifest.json`
- Hassfest or HACS GitHub workflows
- Home Assistant test helper dependencies

Typical docs/check entries when supported:

```bash
python3 -m compileall custom_components tests scripts
python3 -m pytest
hassfest
```

Also document HACS layout review for metadata changes.

### Docker / containers

Common signals:

- `Dockerfile`
- `docker-compose.yml` or `compose.yml`
- `.devcontainer/`
- container build/test scripts in Makefile, justfile, or package scripts

Typical docs/check entries when supported:

```bash
docker build .
docker compose config
```

Avoid running long builds unless requested or clearly required.

### Make / Just / CI-driven repos

Common signals:

- `Makefile`
- `justfile`
- `.github/workflows/*.yml`

Prefer documented aggregate targets when available:

```bash
make test
make lint
just test
just lint
```

When CI is the only source of truth, mirror the lightweight jobs locally where practical and note anything that could not be run.
