# Repository Governance Activation Playbook

Use this playbook when the user wants to activate repository governance in a target repository so humans and agents can reliably find the right instructions, docs, decisions, validation steps, and review boundaries.

Activation is not just an audit. The expected outcome is a repository structure where agents can answer:

1. Where do I start?
2. Which docs are canonical?
3. What must I not change without approval?
4. How do I validate changes?
5. What needs human review?
6. Which platform settings are required but not observable from files?

## Activation outcome

When activating this governance skill in a target repository, aim for:

- a clear root `AGENTS.md` or equivalent agent operating contract,
- a documented reading order for humans and agents,
- linked canonical docs for ADRs, validation, security, trust boundaries, release/runtime, and governance scaffolding,
- optional lightweight `.github/` scaffolding where useful,
- clear distinction between repository-file controls and platform settings,
- a smallest-safe-next-step plan for remaining governance gaps.

## Activation workflow

### 1. Inspect existing repository context

Scan before creating anything. Look for:

- root and nested `AGENTS.md` or `AGENTS.override.md`,
- README and docs indexes,
- ADRs or decision logs,
- validation and contribution docs,
- security, trust-boundary, release, runtime, deployment, and operations docs,
- `.github/` workflows, issue templates, PR templates, and CODEOWNERS,
- dependency manifests, lockfiles, Docker/compose files, infrastructure descriptors, scripts, and config examples.

Mark missing platform settings as **unknown** unless they were inspected.

### 2. Decide canonical entrypoints

Identify which files should be the first things humans and agents read.

A typical order is:

1. `README.md` for project purpose and setup,
2. `AGENTS.md` for agent operating rules,
3. docs index or architecture overview,
4. ADRs or decision logs,
5. validation, security, trust-boundary, runtime, and release docs as needed.

Do not force this exact order if the repository already has a coherent structure. Preserve existing conventions unless they are harmful.

### 3. Create or update `AGENTS.md`

The root `AGENTS.md` should be operational, concise, and link to durable docs instead of duplicating them.

It should normally include:

- repository purpose,
- read-first order,
- non-negotiable rules,
- validation commands,
- definition of done,
- ADR rules,
- security and secret-handling rules,
- CI/workflow change rules,
- trust-boundary rules,
- when human approval is required.

For monorepos, add nested instructions only where local rules differ by subproject.

### 4. Link canonical docs

Make the structure easy to navigate.

Prefer adding links and short indexes before moving files. Ensure agents can find:

- current architecture context,
- accepted decisions,
- validation commands,
- security and trust-boundary guidance,
- runtime and release expectations,
- contribution and review expectations,
- scaffolding or issue/PR intake rules.

### 5. Add lightweight GitHub scaffolding where useful

If missing and appropriate, propose or create the smallest useful set:

- `.github/ISSUE_TEMPLATE/config.yml`,
- `.github/ISSUE_TEMPLATE/bug_report.yml`,
- `.github/ISSUE_TEMPLATE/governance_change.yml`,
- `.github/pull_request_template.md`.

For production, security-sensitive, public, or multi-contributor repositories, consider also:

- `.github/ISSUE_TEMPLATE/feature_request.yml`,
- `.github/ISSUE_TEMPLATE/security_or_trust_boundary.yml`,
- `.github/ISSUE_TEMPLATE/documentation_drift.yml`,
- `.github/CODEOWNERS`,
- `CONTRIBUTING.md`,
- `SECURITY.md`,
- `SUPPORT.md`.

Do not overwrite existing scaffolding unless asked.

### 6. Separate file controls from platform settings

Some governance cannot be fully activated through files.

Document desired platform settings such as:

- branch protection or rulesets,
- required reviews and required status checks,
- required CODEOWNERS review,
- Actions default permissions,
- deployment environments and approval gates,
- secret scanning and push protection,
- dependency graph, dependency review, Dependabot, and CodeQL.

If these are not observable, mark them as **unknown** and recommend human verification.

### 7. Produce an activation report

After activation, produce a concise report:

- files created or changed,
- canonical reading order,
- what agents can now find,
- remaining unknowns,
- platform settings needing human verification,
- smallest safe next improvements.

## Activation report template

Use this structure:

```markdown
## Repository governance activation

### Files changed

- `AGENTS.md` — created/updated root agent operating contract.
- `...` — reason.

### Canonical reading order

1. `README.md`
2. `AGENTS.md`
3. `...`

### Agent findability check

Agents can now find:

- repository purpose: `...`
- operating rules: `...`
- validation: `...`
- decisions: `...`
- trust boundaries: `...`
- PR/issue intake: `...`

### Unknown or platform-only settings

- Branch protection/rulesets: unknown unless inspected.
- Required CODEOWNERS review: unknown unless inspected.

### Remaining improvements

- P1: ...
- P2: ...
```

## Activation caution

Keep activation patches small and reviewable. Do not combine major rewrites, large file moves, workflow changes, and governance scaffolding in one uncontrolled patch.

Prefer a clear first activation pass over an overbuilt governance system.
