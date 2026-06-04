# Repository Governance

This skill establishes durable repository governance for humans and AI coding agents.

It combines:

- active documentation scanning,
- documentation structure audits,
- agent documentation,
- root agent operating contracts,
- institutional memory,
- decision preservation,
- collaboration standards,
- validation workflows,
- code-quality and duplicate-prevention governance,
- agent execution readiness,
- safety guidance,
- trust-boundary awareness,
- and supply-chain governance

into one coherent repository-local system.

The skill helps repositories evolve from ad-hoc documentation into durable, AI-native operational knowledge systems.

The skill is intentionally domain-generic. It should preserve reusable governance patterns without copying product-specific business rules, implementation details, customer assumptions, or domain terminology between repositories.

## Governance areas

- Active Repository Scan
- Documentation Inventory
- Documentation Structure Audit
- Agent Docs
- Root Agent Operating Contract
- Repo Memory
- Decisions / ADRs
- Collaboration
- Code Quality
- Duplicate Prevention
- User Decision Gates
- Agent Execution Readiness
- Tool and Sandbox Boundaries
- Untrusted Content Handling
- Reproducible Setup and Validation
- Output / Evidence Contracts
- Handoff and Interruption Recovery
- Generated Artifact Rules
- Safety
- Trust Boundaries
- Supply Chain
- Validation
- Definition of Done
- Repo Archaeology
- Knowledge Preservation

## Recommended repository pattern

A strong repository should usually have a root `AGENTS.md` as the primary operating contract for AI agents.

Use modular `docs/agent/*` files only when the repository grows beyond what one root file can safely cover. Modular files should support the root contract rather than replace it.

Useful governance information can live in repository-appropriate locations such as:

```text
AGENTS.md
README.md
TODO.md
CONTEXT.md
CONTEXT-MAP.md
docs/adr/
docs/architecture/
docs/security/
docs/integration/
docs/implementation/
docs/operations/
docs/standards/
docs/agent/
.github/workflows/
.github/pull_request_template.md
```

The exact structure should follow the repository's existing documentation style.

## Reference topics

Detailed reusable guidance lives under `references/`:

- `activation-playbook.md` — repository governance activation workflow.
- `audit-workflow.md` — repository scan, topology review, drift checks, and safe restructuring.
- `output-templates.md` — audit output, finding, inventory, patch-plan, and evidence templates.
- `governance-scaffolding.md` — issue forms, PR templates, CODEOWNERS, labels, and lightweight GitHub scaffolding.
- `platform-and-supply-chain-governance.md` — platform settings, CI/CD, dependency, provenance, SBOM, and supply-chain guidance.
- `code-quality-and-duplicate-prevention.md` — coding standards topology, no-duplicates policy, search-before-create rules, review checklists, and user decision gates.
- `agent-execution-readiness.md` — instruction topology, context budget, tool/sandbox boundaries, untrusted content, reproducibility, handoff, generated artifacts, and evidence contracts.
- `maturity-model.md` — maturity criteria from bootstrap to enterprise-ready.

## Active scan workflow

Before creating or restructuring governance docs, the skill should actively scan existing files and classify them by role:

- canonical operating contract,
- project overview,
- architecture reference,
- decision record,
- implementation plan,
- security guidance,
- integration contract,
- operational runbook,
- validation checklist,
- coding standard,
- duplicate-prevention policy,
- execution-readiness guidance,
- roadmap or TODO,
- archive, spike, or historical note,
- duplicate, stale, orphaned, or conflicting document.

The skill should then propose the smallest safe restructuring path: link first, clarify ownership second, mark stale content third, consolidate only when the canonical destination is obvious, and move or rename files only when the benefit is clear.

## Reasoning posture

Governance work should use deliberate, evidence-based analysis.

When the runtime supports configurable reasoning effort, prefer high reasoning effort for governance audits, documentation restructuring, drift detection, and maturity assessments.

The skill should summarize evidence, file paths, rationale, assumptions, recommendations, and open questions instead of exposing private chain-of-thought.

## Recommended skill structure

```text
skills/repository-governance/
  SKILL.md
  README.md
  references/
    activation-playbook.md
    audit-workflow.md
    output-templates.md
    governance-scaffolding.md
    platform-and-supply-chain-governance.md
    code-quality-and-duplicate-prevention.md
    agent-execution-readiness.md
    maturity-model.md
```
