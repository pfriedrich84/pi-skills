---
name: tune-repo
description: Tune a repository for AI coding agents by consolidating tool-specific instructions into a short tool-neutral AGENTS.md, making CLAUDE.md point to it, and reorganizing Markdown docs into docs/agent, docs/developer, and docs/user. Use when the user asks to tune, standardize, or clean up repo agent documentation.
---

# Tune Repo

Turn a repository into an agent-friendly, tool-neutral documentation structure.

The goal is **not** to dump everything into one prompt file. The goal is a small `AGENTS.md` entry point that remains stable over time while detailed guidance lives in modular Markdown documents split into `docs/agent/`, `docs/developer/`, and `docs/user/`.

## Desired end state

```text
AGENTS.md                 # short, tool-neutral entry point for all coding agents
CLAUDE.md                 # tiny Claude-specific shim pointing to AGENTS.md
.github/
  ISSUE_TEMPLATE/
    bug_report.md
    feature_request.md
    task.md
    config.yml
  PULL_REQUEST_TEMPLATE.md
docs/
  README.md
  agent/
    RULES.md
    PROJECT.md
    CODING.md
    REVIEW.md
    CHECKS.md
    WORKFLOWS.md
    SAFETY.md
    DEFINITION_OF_DONE.md
    AUTORESEARCH.md
  developer/
  user/
```

Use [references/AGENT-DOCS-PATTERN.md](references/AGENT-DOCS-PATTERN.md) as the pattern and [references/TEMPLATES.md](references/TEMPLATES.md) for starter text.

## Before editing: clarify scope

### Question strategy

Do not ask all questions mechanically. First infer likely intent from the user's wording.

Use one of three modes:

#### Mode A — Implement now

Use when the user says things like:

- "mach"
- "setz um"
- "go ahead"
- "best practice"
- "update repo"
- "tune repo"
- "fix structure"
- "standardize docs"

In this mode:

- do not ask the full question list;
- use the default/best-practice scope below;
- ask at most one blocking question only if implementation would risk destructive Git actions, data loss, or the target repository is unclear;
- proceed directly with inspection and implementation.

#### Mode B — Guided setup

Use when the user asks for:

- a proposal,
- recommendations,
- a structure idea,
- a review before implementation,
- or seems undecided.

Ask only these concise questions:

1. Target repo/path?
2. Implement directly or only propose changes?
3. Leave changes uncommitted or commit after validation?

If the user says "best practice", "default", or equivalent, switch to Mode A.

#### Mode C — Review only

Use when the user asks to:

- audit,
- review,
- assess,
- analyze,
- or suggest improvements only.

In this mode:

- inspect the repository;
- provide a concrete patch plan;
- do not edit files unless explicitly requested.

### Blocking questions only

Only stop for clarification when:

- the target repository/path is unknown;
- the user requests commit/push behavior that is unclear;
- existing instruction files contain conflicting safety/security guidance;
- moving/removing files could destroy meaningful content;
- validation depends on unavailable secrets, hardware, or external services.

Otherwise make conservative best-effort decisions and document them in the final summary.

If the user asks for the default/best-practice scope, use:

- implement the full standard structure;
- always create/normalize all standard agent files: `RULES.md`, `PROJECT.md`, `CODING.md`, `REVIEW.md`, `CHECKS.md`, `WORKFLOWS.md`, `SAFETY.md`, `DEFINITION_OF_DONE.md`, `AUTORESEARCH.md`;
- keep `AGENTS.md` short;
- make `CLAUDE.md` a shim;
- convert other tool-specific instruction files such as `GEMINI.md`, `.cursor/rules`, `.github/copilot-instructions.md`, Windsurf/Cline/Codex files into shims that point to `AGENTS.md`, unless preserving tool-specific content is explicitly required;
- move relevant Markdown into `docs/agent`, `docs/developer`, `docs/user`;
- update README links, docs indexes, and internal Markdown links that break because of moves;
- add GitHub issue and pull request templates unless equivalent templates already exist;
- add a lightweight Markdown local-link checker script when the repository does not already have one;
- add useful optional docs only when the repository shape supports them, such as ADRs, testing docs, troubleshooting docs, configuration docs, or ecosystem-specific validation examples;
- implement clearly safe documentation-only improvements that are necessary to complete the agreed structure;
- collect unrelated or larger improvements in a "Suggested follow-ups" section instead of interrupting the run;
- ask before implementing anything that changes code behavior, CI behavior, dependencies, repository policy, or Git history;
- do not commit unless explicitly asked; if asked, commit after validation with a concise message;
- when finishing with uncommitted changes, actively ask whether the user wants the changes committed, and whether they should also be pushed.

## Process

### 1. Inspect repository

Read first, do not edit yet:

- root listing and Git status;
- existing `AGENTS.md`, `CLAUDE.md`, `README.md`, `.github/copilot-instructions.md`, `GEMINI.md`, Cursor/Windsurf rule files, if present;
- existing `docs/` tree;
- package/build files that reveal validation commands.

After inspection, create a short implementation plan before editing:

- files to create;
- files to move;
- files to convert into shims;
- links/indexes to update;
- validation commands to run.

Then execute the plan unless the current mode is Review only.

### 2. Create or normalize agent docs

Create concise project-specific agent docs.

Minimum content expectations:

- `AGENTS.md`: read-first list, project docs list, quick summary, check reminder.
- `docs/agent/CODING.md`: coding conventions, implementation patterns, testing discipline, refactor expectations, and preferred coding workflows.
- `docs/agent/REVIEW.md`: PR review expectations and review focus areas.
- `docs/agent/DEFINITION_OF_DONE.md`: completion criteria for implementation tasks.
- `docs/agent/CHECKS.md`: validation commands and when to run them.
- `docs/agent/SAFETY.md`: safe/ask-first/never guidance.

Avoid hallucinating commands.

### 3. Normalize GitHub collaboration templates

If the repository uses GitHub and does not already contain equivalent templates:

Create:

- `.github/ISSUE_TEMPLATE/bug_report.md`
- `.github/ISSUE_TEMPLATE/feature_request.md`
- `.github/ISSUE_TEMPLATE/task.md`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`

Keep templates:

- concise;
- implementation-oriented;
- compatible with coding agents;
- focused on reproducibility and acceptance criteria.

Avoid excessive process bureaucracy.

## Agent ergonomics

Prefer:

- short entry points;
- modular linked documents;
- deterministic validation commands;
- stable filenames;
- repo-local instructions over chat-only instructions.

Avoid:

- giant monolithic prompt files;
- duplicated rules across tools;
- embedding large architecture explanations directly in `AGENTS.md`.

## Quality bar

- Tool-neutral: `AGENTS.md` is canonical; tool-specific files are shims.
- Concise: agent entry points should be scannable.
- Durable: domain rules and checks live in `docs/agent`, not in chat-only notes.
- Discoverable: user and developer docs are clearly separated.
- Safe: do not expose secrets, do not rewrite history, do not commit unless asked.
