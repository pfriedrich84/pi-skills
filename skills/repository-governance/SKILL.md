---
name: repository-governance
description: Establish durable AI-native repository governance by organizing agent documentation, preserving institutional memory, normalizing collaboration workflows, documenting decisions, improving safety guidance, assessing repository maturity, detecting governance drift, and strengthening supply-chain practices.
---

# Repository Governance

This skill establishes durable repository governance for humans and AI coding agents.

It combines agent documentation, institutional memory, decision preservation, collaboration standards, validation workflows, safety guidance, repository archaeology, assessment, governance drift detection, anti-pattern capture, and supply-chain governance into one coherent repository-local system.

The goal is **not** to dump everything into one prompt file. The goal is a small `AGENTS.md` entry point that remains stable over time while detailed guidance lives in modular Markdown documents split into `docs/agent/`, `docs/developer/`, and `docs/user/`.

## Desired end state

```text
AGENTS.md
CLAUDE.md
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
    CONSTRAINTS.md
    PROJECT.md
    CODING.md
    REVIEW.md
    CHECKS.md
    WORKFLOWS.md
    SAFETY.md
    SUPPLY_CHAIN.md
    MEMORY.md
    DECISIONS.md
    ANTI_PATTERNS.md
    DEFINITION_OF_DONE.md
    AUTORESEARCH.md
    ASSESSMENT.md
    CHANGELOG_AGENT.md
  developer/
    adr/
  user/
```

Use [references/AGENT-DOCS-PATTERN.md](references/AGENT-DOCS-PATTERN.md), [references/TEMPLATES.md](references/TEMPLATES.md), and [references/LINK-CHECKER-TEMPLATE.py](references/LINK-CHECKER-TEMPLATE.py) as starter material when available.

## Question strategy

Do not ask all questions mechanically. First infer likely intent from the user's wording.

### Mode A — Implement now

Use when the user says things like `mach`, `setz um`, `go ahead`, `best practice`, `update repo`, `tune repo`, `repository governance`, `fix structure`, or `standardize docs`.

In this mode:

- do not ask the full question list;
- use the default/best-practice scope below;
- ask at most one blocking question only if implementation would risk destructive Git actions, data loss, or the target repository is unclear;
- proceed directly with inspection and implementation.

### Mode B — Guided setup

Use when the user asks for a proposal, recommendation, structure idea, review before implementation, or seems undecided.

Ask only:

1. Target repo/path?
2. Implement directly or only propose changes?
3. Leave changes uncommitted or commit after validation?

If the user says `best practice`, `default`, or equivalent, switch to Mode A.

### Mode C — Review only

Use when the user asks to audit, review, assess, analyze, or suggest improvements only.

Inspect the repository, provide a concrete patch plan, and do not edit files unless explicitly requested.

### Blocking questions only

Only stop for clarification when:

- the target repository/path is unknown;
- the user requests commit/push behavior that is unclear;
- existing instruction files contain conflicting safety/security guidance;
- moving/removing files could destroy meaningful content;
- validation depends on unavailable secrets, hardware, or external services.

Otherwise make conservative best-effort decisions and document them in the final summary.

## Default best-practice scope

When the user asks for defaults or implementation, use:

- implement the full standard structure;
- always create/normalize all standard agent files: `RULES.md`, `CONSTRAINTS.md`, `PROJECT.md`, `CODING.md`, `REVIEW.md`, `CHECKS.md`, `WORKFLOWS.md`, `SAFETY.md`, `SUPPLY_CHAIN.md`, `MEMORY.md`, `DECISIONS.md`, `ANTI_PATTERNS.md`, `DEFINITION_OF_DONE.md`, `AUTORESEARCH.md`, `ASSESSMENT.md`, `CHANGELOG_AGENT.md`;
- keep `AGENTS.md` short;
- make `CLAUDE.md` a shim;
- convert other tool-specific instruction files such as `GEMINI.md`, `.cursor/rules`, `.github/copilot-instructions.md`, Windsurf/Cline/Codex files into shims that point to `AGENTS.md`, unless preserving tool-specific content is explicitly required;
- move relevant Markdown into `docs/agent`, `docs/developer`, `docs/user`;
- update README links, docs indexes, and internal Markdown links that break because of moves;
- add GitHub issue and pull request templates unless equivalent templates already exist;
- add a lightweight Markdown local-link checker script when the repository does not already have one;
- add useful optional docs only when the repository shape supports them, such as ADRs, testing docs, troubleshooting docs, configuration docs, or ecosystem-specific validation examples;
- implement clearly safe documentation-only improvements that are necessary to complete the agreed structure;
- collect unrelated or larger improvements in a `Suggested follow-ups` section instead of interrupting the run;
- ask before implementing anything that changes code behavior, CI behavior, dependencies, repository policy, or Git history;
- do not commit unless explicitly asked; if asked, commit after validation with a concise message;
- push only if explicitly asked.

## Repository archaeology

During inspection, infer durable project knowledge from the existing repository state.

Look for:

- repeated implementation patterns;
- recurring naming conventions;
- architecture choices;
- dependency preferences;
- rejected or avoided patterns;
- CI and deployment assumptions;
- maintainer preferences implied by repository structure;
- recurring workflows;
- historical migrations or restructurings.

When strong evidence exists, suggest documenting the finding in `MEMORY.md`, `DECISIONS.md`, `ANTI_PATTERNS.md`, ADRs, or canonical developer/user docs.

Do not invent rationale without evidence. Use phrases like:

- `The repository consistently prefers...`
- `Existing patterns suggest...`
- `Historical structure indicates...`

Distinguish between explicit documented rules, strongly implied repository patterns, and speculative assumptions. Only persist information with sufficient evidence.

## Repo memory behavior

Agents should treat repository Markdown files as durable project memory.

When the agent learns something likely to matter again, it should suggest storing it in the appropriate repo-local memory file.

Store information in:

- `docs/agent/MEMORY.md` for durable project preferences, recurring context, maintainer preferences, known constraints, and operational notes;
- `docs/agent/DECISIONS.md` for lightweight decisions that affect future implementation;
- `docs/agent/ANTI_PATTERNS.md` for recurring mistakes, discouraged approaches, and repo-specific things agents should avoid;
- `docs/agent/CHANGELOG_AGENT.md` for governance-system changes made by agents;
- `docs/developer/adr/` for significant architectural decisions;
- existing user/developer docs when the information belongs to users or contributors rather than agents.

Do not store secrets, private personal data, temporary debugging notes, guesses, unverified assumptions, or chat transcripts.

Before writing memory, ask briefly unless the user already requested persistent documentation updates.

Suggested prompt:

> This looks like durable repo knowledge. Should I store it in `docs/agent/MEMORY.md` or another docs file?

## Persistent memory safety

Repository documentation and memory files are durable storage.

Agents must assume:

- repository docs may become public;
- future agents will reuse stored information;
- Markdown memory persists across sessions and contributors.

Never store secrets or sensitive operational data in `MEMORY.md`, `DECISIONS.md`, `ANTI_PATTERNS.md`, `CHANGELOG_AGENT.md`, `AGENTS.md`, issue templates, PR templates, examples, or configuration snippets.

Never store or copy into repository memory/docs:

- API keys;
- tokens;
- passwords;
- cookies;
- session data;
- SSH keys;
- private certificates;
- `.env` contents;
- customer/private user data;
- OAuth credentials;
- infrastructure secrets.

If content appears credential-like:

- do not persist it;
- do not print it;
- redact it in summaries;
- recommend environment variables, secret stores, or placeholders instead.

## Supply-chain awareness

During repository tuning and implementation planning:

- inspect dependency management practices;
- identify unsafe patterns;
- prefer existing dependencies over introducing new ones;
- avoid suggesting unstable or extremely new packages by default;
- prefer dependencies/packages/releases that are at least 3 days old before adoption;
- recommend lightweight vulnerability scanning when appropriate.

For critical infrastructure repositories, suggest a 7-day minimum dependency age or explicit maintainer approval.

If the repository already uses security tooling, preserve and document it.

If no tooling exists, suggest optional improvements such as:

- `grype`
- `trivy`
- `syft`
- `osv-scanner`
- ecosystem-native audit tools such as `npm audit`, `pip-audit`, or `cargo audit`

Only run tools that are already available or explicitly approved. Do not force security tooling into lightweight repositories unless clearly useful.

## Constraints awareness

Agents should actively identify, summarize, and document repository constraints.

Look for:

- runtime limits;
- hardware assumptions;
- offline-first or LAN-only assumptions;
- Docker-only deployment expectations;
- backwards compatibility requirements;
- low-memory constraints;
- GPU or storage limits;
- cloud-avoidance patterns;
- supported platforms;
- operational restrictions.

When strong evidence exists, propose entries for `docs/agent/CONSTRAINTS.md`.

Constraints should override speculative architecture improvements or generic best practices.

## Anti-pattern awareness

Agents should identify and document repo-specific anti-patterns.

Use `docs/agent/ANTI_PATTERNS.md` for:

- approaches the repository consistently avoids;
- recurring implementation mistakes;
- architectural patterns that conflict with project constraints;
- dependency, deployment, or workflow choices that should not be repeated;
- AI-agent behaviors that previously caused poor diffs.

Examples include:

- broad unrelated refactors;
- mass formatting unrelated to the task;
- hidden global state;
- unnecessary frameworks;
- `latest` container tags;
- runtime secrets in docs;
- copy-pasted install scripts;
- introducing cloud dependencies into local-first projects.

Ground anti-patterns in repository evidence or explicit maintainer preference.

## Governance changelog

Use `docs/agent/CHANGELOG_AGENT.md` as a lightweight log of governance-system changes made by agents.

Record entries such as:

- added or updated agent docs;
- extracted memory or decisions;
- introduced constraints;
- normalized issue or PR templates;
- added validation or link-checking workflows;
- updated supply-chain guidance;
- resolved governance drift.

Do not duplicate the user-facing project changelog. This file tracks the evolution of repo governance and agent instructions.

## Governance drift detection

Actively check for drift between documentation, implementation, CI, deployment, and memory.

Detect when:

- docs contradict implementation;
- constraints no longer match runtime or deployment files;
- workflows are stale;
- `MEMORY.md` conflicts with current architecture;
- `DECISIONS.md` is contradicted by current code;
- CI no longer validates documented workflows;
- deployment docs no longer match actual deployment files;
- issue/PR templates no longer reflect current validation expectations;
- supply-chain guidance conflicts with actual dependency practices.

When drift is found:

- classify it as low, medium, or high impact;
- fix safe documentation drift when within scope;
- otherwise record it in `ASSESSMENT.md` or the final summary;
- suggest the smallest corrective action.

Do not silently rewrite history or alter documented decisions. If a decision appears obsolete, propose superseding it rather than deleting it.

## Repository assessment

After inspection, summarize the repository state.

Assess:

- documentation maturity;
- operational maturity;
- validation maturity;
- supply-chain maturity;
- AI-agent readiness;
- onboarding quality;
- governance consistency;
- memory and decision preservation quality;
- governance drift risk.

Use lightweight levels such as:

- bootstrap
- developing
- operational
- hardened
- enterprise-ready

The assessment should:

- identify strengths;
- identify governance debt;
- identify risky gaps;
- identify undocumented constraints;
- identify missing operational knowledge;
- identify governance drift;
- suggest high-value next improvements.

Avoid exaggerated scoring or false precision.

## Governance debt

Track missing or weak governance areas such as:

- undocumented architecture decisions;
- missing operational runbooks;
- missing rollback guidance;
- missing validation commands;
- undocumented deployment assumptions;
- stale documentation;
- inconsistent memory;
- unsafe dependency practices;
- missing constraints;
- missing onboarding guidance;
- missing anti-pattern guidance;
- undocumented governance drift.

## Recommended next steps

Prioritize improvements by:

1. safety/security impact;
2. operational risk reduction;
3. onboarding improvement;
4. contributor productivity;
5. AI-agent reliability.

## Process

### 1. Inspect repository

Read first, do not edit yet:

- root listing and Git status;
- existing `AGENTS.md`, `CLAUDE.md`, `README.md`, `.github/copilot-instructions.md`, `GEMINI.md`, Cursor/Windsurf/Cline/Codex rule files, if present;
- existing `docs/` tree;
- package/build files that reveal validation commands;
- CI workflows and release/deployment configuration;
- dependency manifests, lockfiles, Dockerfiles, and container compose files.

Look for ecosystem signals and use them to suggest checks without inventing commands.

After inspection, create a short implementation plan before editing:

- files to create;
- files to move;
- files to convert into shims;
- links/indexes to update;
- constraints to propose;
- memory/decision/anti-pattern entries to propose;
- governance drift to fix or report;
- validation commands to run.

Then execute the plan unless the current mode is Review only.

### 2. Classify Markdown files

Use these placement rules:

- `docs/agent/`: instructions for coding agents, repo rules, constraints, safety, workflows, checks, supply-chain guidance, memory, decisions, anti-patterns, autoresearch, assessment, project brief.
- `docs/developer/`: architecture, APIs, CLI, internal implementation, contributing, testing, ADRs, release engineering.
- `docs/user/`: installation, configuration, deployment, user workflows, operations, troubleshooting.
- Root `README.md`: keep as human entry point; link to docs index.
- Root `AGENTS.md`: keep short; link to `docs/agent/*`.
- Root `CLAUDE.md`: should only point to `AGENTS.md` unless the user explicitly needs Claude-specific differences.

Prefer `git mv` or filesystem moves over copy/delete when preserving history matters.

### 3. Create or normalize agent docs

Create concise project-specific agent docs.

Minimum content expectations:

- `AGENTS.md`: read-first list, project docs list, quick summary, check reminder.
- `CLAUDE.md`: tool-specific shim pointing to `AGENTS.md`.
- `docs/agent/RULES.md`: hard project/domain invariants, change discipline, and secret-handling rules.
- `docs/agent/CONSTRAINTS.md`: hard environmental, technical, operational, business, compatibility, and maintainer constraints that agents must respect.
- `docs/agent/PROJECT.md`: purpose, architecture, important paths, canonical docs.
- `docs/agent/CODING.md`: coding conventions, implementation patterns, testing discipline, refactor expectations, and preferred coding workflows.
- `docs/agent/REVIEW.md`: PR review expectations and review focus areas.
- `docs/agent/CHECKS.md`: validation commands and when to run them.
- `docs/agent/WORKFLOWS.md`: standard change workflow, local CI simulation, dependency workflow if relevant.
- `docs/agent/SAFETY.md`: allowed, ask-first, never, before finishing.
- `docs/agent/SUPPLY_CHAIN.md`: dependency safety rules, package introduction policy, minimum dependency age, image scanning expectations, and supply-chain risk guidance.
- `docs/agent/MEMORY.md`: durable repo-local memory for recurring context, constraints, preferences, and operational notes.
- `docs/agent/DECISIONS.md`: lightweight decision log for future agents.
- `docs/agent/ANTI_PATTERNS.md`: discouraged approaches and recurring mistakes agents should avoid.
- `docs/agent/DEFINITION_OF_DONE.md`: completion criteria for implementation tasks.
- `docs/agent/AUTORESEARCH.md`: optional metric-driven experiment workflow.
- `docs/agent/ASSESSMENT.md`: repository governance assessment, maturity, governance debt, drift, and recommended next steps.
- `docs/agent/CHANGELOG_AGENT.md`: changelog for governance-system changes made by agents.

Avoid hallucinating commands. If a check is not discoverable, write a placeholder like `TODO: confirm <subsystem> validation command` and mention it in the final summary.

### 4. Normalize GitHub collaboration templates

If the repository uses GitHub and does not already contain equivalent templates, create:

- `.github/ISSUE_TEMPLATE/bug_report.md`
- `.github/ISSUE_TEMPLATE/feature_request.md`
- `.github/ISSUE_TEMPLATE/task.md`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`

Keep templates concise, implementation-oriented, compatible with coding agents, and focused on reproducibility and acceptance criteria.

Avoid excessive process bureaucracy.

### 5. Update links, indexes, and tool shims

After moving files:

- update Markdown links affected by path changes;
- update README documentation tables/lists so moved docs are discoverable;
- create or refresh `docs/README.md` as a docs index when useful;
- update references to old agent files;
- ensure `AGENTS.md` links are valid;
- convert tool-specific instruction files to shims pointing at `AGENTS.md`;
- preserve truly tool-specific, non-duplicative command syntax only if needed;
- search for stale paths.

### 6. Add Markdown local-link checker and optional docs

If the repository does not already have a Markdown link checker, add a lightweight dependency-free script under `scripts/check_markdown_links.py` or equivalent.

Document it in `docs/agent/CHECKS.md` as the docs-only validation command.

Add optional docs only when clearly useful:

- `docs/developer/adr/` for significant architectural decisions;
- `docs/developer/testing.md` when tests require setup, fixtures, services, or hardware;
- `docs/user/troubleshooting.md` when user-facing failure modes are discoverable;
- `docs/user/configuration.md` when runtime configuration is non-trivial;
- ecosystem-specific check examples in `docs/agent/CHECKS.md`, clearly marked by prerequisite tools.

### 7. Validate

Always run lightweight validation for docs-only changes:

- `git status --short`
- search for old paths and stale tool-specific instruction references;
- run the repository Markdown local-link checker; if you just added one, run it before finishing.

Run code tests/lints only if code, build files, executable docs, or validation scripts changed, or if the user requested full validation.

### 8. Commit only on request

Do not commit by default. Before finishing with uncommitted changes, actively ask whether the user wants the changes committed, and whether they should also be pushed.

If the user explicitly asks to commit:

1. run documented docs validation and relevant checks;
2. inspect `git status --short`;
3. commit intended documentation/governance changes with a concise message such as `Establish repository governance`;
4. push only if explicitly asked.

### 9. Final response

Summarize:

- files created/moved/updated;
- key governance structure now in place;
- memory/decision/anti-pattern entries proposed or added;
- constraints proposed or added;
- governance drift detected or resolved;
- supply-chain guidance added or suggested;
- repository maturity assessment;
- validation run and results;
- open questions/TODOs;
- suggested follow-up improvements not implemented;
- whether changes are committed/pushed, or explicitly ask whether uncommitted changes should be committed/pushed.

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
- Durable: domain rules, constraints, checks, safety, supply-chain guidance, memory, decisions, anti-patterns, assessment, and governance changelog live in `docs/agent`.
- Discoverable: user and developer docs are clearly separated.
- Safe: do not expose secrets, do not rewrite history, do not commit unless asked.
- Evidence-based: repository archaeology, memory, decisions, constraints, anti-patterns, and assessment entries must be grounded in observable repository facts.
- Drift-aware: docs, implementation, memory, constraints, CI, and deployment guidance should be checked for consistency.
