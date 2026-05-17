# Repository Governance

This skill establishes durable repository governance for humans and AI coding agents.

It combines:

- active documentation scanning,
- documentation structure audits,
- agent documentation,
- institutional memory,
- decision preservation,
- collaboration standards,
- validation workflows,
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
docs/agent/
.github/workflows/
```

The exact structure should follow the repository's existing documentation style.

## Active scan workflow

Before creating or restructuring governance docs, the skill should actively scan existing files and classify them by role:

- canonical operating contract
- project overview
- architecture reference
- decision record
- implementation plan
- security guidance
- integration contract
- operational runbook
- validation checklist
- roadmap or TODO
- archive, spike, or historical note
- duplicate, stale, orphaned, or conflicting document

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
```
