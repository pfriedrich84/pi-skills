# Governance Scaffolding

Use this reference when a repository needs lightweight GitHub/community scaffolding to make governance, triage, issue intake, PR review, ownership, validation, and agent safety more repeatable.

Scaffolding is not bureaucracy. Create or propose only the smallest useful set for the repository's risk, maturity, and contribution model.

## Scope

This skill may inspect, propose, or create governance scaffolding such as:

- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/governance_change.yml`
- `.github/ISSUE_TEMPLATE/security_or_trust_boundary.yml`
- `.github/ISSUE_TEMPLATE/documentation_drift.yml`
- `.github/pull_request_template.md`
- `.github/CODEOWNERS`
- `.github/dependabot.yml`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `SUPPORT.md`

Do not overwrite existing templates, CODEOWNERS, or community-health files unless the user explicitly asks for replacement. Prefer additive or minimally invasive changes.

## Before creating scaffolding

Before proposing or creating scaffolding:

1. inspect existing `.github/` files and community-health files,
2. preserve the repository's current naming and style where it is coherent,
3. identify whether the repository is private/internal, public/open-source, product-facing, security-sensitive, or operational,
4. choose the smallest useful set,
5. prefer issue forms for governance-sensitive input,
6. mark platform-only settings as recommendations when they cannot be changed through files,
7. separate files that can be committed from GitHub state such as labels, branch protection, rulesets, and repository settings.

## Minimal default scaffold

For small, private, or early-stage repositories, prefer this minimal set:

- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/governance_change.yml`
- `.github/pull_request_template.md`

Use this set when the main goal is better issue quality, safer agent changes, and more consistent PR review without adding heavy process.

## Expanded production scaffold

For repositories with operational, security, customer, release, or multi-contributor impact, consider adding:

- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/security_or_trust_boundary.yml`
- `.github/ISSUE_TEMPLATE/documentation_drift.yml`
- `.github/CODEOWNERS`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `SUPPORT.md`

Use these when the repository needs clearer intake, ownership, disclosure, contribution, or support expectations.

## Issue form: bug report

Create `.github/ISSUE_TEMPLATE/bug_report.yml` when the repository needs structured defect reports.

Useful fields:

- summary,
- expected behavior,
- actual behavior,
- steps to reproduce,
- environment,
- logs or screenshots,
- regression status,
- validation already tried.

Keep the form focused on reproducibility. Do not ask for secrets, tokens, customer data, or sensitive logs.

## Issue form: feature request

Create `.github/ISSUE_TEMPLATE/feature_request.yml` when new functionality needs consistent triage.

Useful fields:

- problem,
- proposed solution,
- alternatives considered,
- user impact,
- scope boundaries,
- validation idea,
- documentation impact.

Prefer problem-first feature requests. Avoid encouraging broad implementation proposals without scope boundaries.

## Issue form: governance change

Create `.github/ISSUE_TEMPLATE/governance_change.yml` when changes to repository governance should be reviewed deliberately.

Use this for proposed changes to:

- `AGENTS.md`, nested agent instructions, or skill-related guidance,
- ADR rules,
- validation commands,
- CI/workflows,
- release process,
- CODEOWNERS,
- issue/PR templates,
- dependency policy,
- security or trust-boundary documentation,
- runtime or deployment governance.

Useful fields:

- governance area,
- current problem,
- proposed change,
- files likely affected,
- risk if wrong,
- whether the change affects agent behavior,
- whether the change affects CI, release, runtime, security, or dependencies,
- required validation,
- required owner decision.

## Issue form: security or trust boundary

Create `.github/ISSUE_TEMPLATE/security_or_trust_boundary.yml` when the repository needs structured review for new or changed trust boundaries.

Use this for:

- dependencies,
- GitHub Actions,
- Docker images,
- MCP servers,
- external APIs or SaaS services,
- package registries,
- CI permissions,
- secrets or credentials,
- telemetry or outbound network calls,
- deployment platforms.

Useful fields:

- trust-boundary type,
- what is being added or changed,
- data or credentials exposed,
- permissions required,
- validation plan,
- fallback or removal plan,
- human approval needed,
- related files or workflows.

This template is not a replacement for private vulnerability reporting. If the repository is public or handles security-sensitive code, also consider `SECURITY.md` and private disclosure guidance.

## Issue form: documentation drift

Create `.github/ISSUE_TEMPLATE/documentation_drift.yml` when the repository has multiple docs that may contradict each other.

Useful fields:

- conflicting documents,
- observed contradiction,
- source that appears canonical,
- risk for agents or contributors,
- suggested correction,
- validation or link-check impact.

This form is especially useful for AI-agentic repositories because stale docs can directly cause unsafe or incorrect agent behavior.

## Pull request template

Create `.github/pull_request_template.md` when PRs need consistent review information.

A useful PR template should include:

```markdown
## Summary

## Scope

## Governance impact

- [ ] No `AGENTS.md` or agent-instruction impact
- [ ] No ADR or decision-record impact
- [ ] No CI/workflow impact
- [ ] No dependency or trust-boundary impact
- [ ] No release/runtime impact
- [ ] No secrets or credential-handling impact

## Validation

## Documentation updated

## Open questions / risks
```

Adapt the checklist to the repository. Do not add checkboxes that create fake assurance or require irrelevant process.

## CODEOWNERS

Create or propose `.github/CODEOWNERS` when ownership should be reviewable or enforceable.

Good candidates for ownership rules:

- `AGENTS.md`,
- nested agent instruction files,
- `.github/workflows/`,
- `.github/ISSUE_TEMPLATE/`,
- `.github/pull_request_template.md`,
- security docs,
- ADRs,
- deployment docs,
- release docs,
- dependency manifests and lockfiles.

CODEOWNERS only becomes enforceable when repository platform settings require code-owner review. If that setting cannot be inspected, mark enforcement as **unknown** and recommend verification.

## Dependabot configuration

Create or propose `.github/dependabot.yml` when dependency manifests are present and no dependency-update bot configuration exists. Include only ecosystems that are actually present in the repository, use a conservative schedule, group related updates when appropriate, and keep PR limits low enough for maintainers to review. Document that Dependabot update configuration is separate from platform settings such as Dependabot alerts, security updates, dependency graph, and dependency review; mark those settings as **unknown** when they cannot be inspected.

## Community-health files

Consider root-level community-health files when relevant:

- `CONTRIBUTING.md` for contribution and validation expectations,
- `SECURITY.md` for vulnerability reporting and disclosure expectations,
- `SUPPORT.md` for support boundaries and contact expectations.

Do not create public-support promises that the maintainer cannot meet. For private repositories, keep these files internal and practical.

## Labels

Labels are GitHub state, not usually repository files. When tool access allows label management, the skill may propose or create labels. Otherwise, output a recommended label taxonomy.

Useful governance label families:

- `type: bug`
- `type: feature`
- `type: docs`
- `type: governance`
- `type: security`
- `type: trust-boundary`
- `type: adr`
- `type: ci`
- `type: release`
- `type: runtime`
- `priority: p0`
- `priority: p1`
- `priority: p2`
- `priority: p3`
- `status: needs-triage`
- `status: blocked`
- `status: needs-owner-decision`

Avoid excessive label taxonomies. Start small and expand only when labels improve triage or reporting.

## Branch protection and rulesets

Branch protection, rulesets, required checks, and required CODEOWNERS review are platform settings. They may not be visible or editable from repository files.

When scaffolding depends on these settings:

- document the desired setting,
- mark current state as **unknown** if not inspected,
- avoid claiming enforcement from file presence alone,
- recommend human verification in repository settings.

## Scaffold output

When proposing scaffolding, include:

- files to add,
- files intentionally not added,
- reason for each file,
- expected governance effect,
- risks or maintenance burden,
- platform settings that still need human verification.

When creating scaffolding, keep each file small, reviewable, and repository-neutral unless the repository evidence supports more specific wording.
