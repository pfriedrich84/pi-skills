---
name: repository-governance
description: Establish durable AI-native repository governance by organizing agent documentation, preserving institutional memory, normalizing collaboration workflows, documenting decisions, improving safety guidance, assessing repository maturity, detecting governance drift, and strengthening supply-chain practices.
---

# Repository Governance

This skill establishes durable AI-native repository governance.

## Durable governance patterns

High-quality repositories increasingly use:

- modular `docs/agent/*` systems
- durable repository memory
- lightweight decision logs
- anti-pattern documentation
- definition-of-done docs
- governance maturity assessments
- CODEOWNERS
- markdown drift detection
- SBOM generation
- explicit trust-boundary documentation
- runtime security guidance
- release governance
- architecture fitness functions
- policy-as-code planning
- architecture compliance guidance
- provenance and signing roadmaps
- incident-response readiness

## Valuable docs/agent files

Strong governance repositories often include:

- `RULES.md`
- `CONSTRAINTS.md`
- `CHECKS.md`
- `MEMORY.md`
- `DECISIONS.md`
- `ANTI_PATTERNS.md`
- `DEFINITION_OF_DONE.md`
- `ASSESSMENT.md`

These files help future agents preserve durable context and reduce governance drift.

## Policy-as-code guidance

Repositories benefit from identifying governance rules that should eventually become machine-enforced.

Examples:

- least-privilege CI
- dependency governance
- secret-handling rules
- workflow restrictions
- approval invariants
- container restrictions

## Runtime governance guidance

Repositories with operational or production impact should document:

- runtime trust boundaries
- monitoring expectations
- security event expectations
- deployment assumptions
- runtime secret-handling expectations
- operational security constraints

## Release governance guidance

Useful release-governance topics include:

- trusted release branches/tags
- review expectations
- required CI checks
- artifact traceability
- provenance goals
- deployment approvals
- rollback awareness

## Provenance & signing guidance

Security-sensitive repositories should eventually plan for:

- artifact signing
- container signing
- signed SBOMs
- provenance attestations
- release traceability

## Architecture fitness functions

Repositories benefit from documenting architectural invariants that should eventually become automatically testable.

Examples:

- transport isolation
- approval invariants
- secret logging restrictions
- least-privilege CI
- dependency governance
- governance consistency

## Architecture compliance guidance

Repositories should explicitly document important architecture invariants.

Examples:

- approval enforcement
- payload separation
- configuration isolation
- transport abstraction boundaries
- secret safety expectations

## Incident readiness

Operational repositories should eventually document:

- incident categories
- containment expectations
- audit preservation expectations
- rollback approaches
- credential rotation procedures

## Repository memory guidance

Useful durable memory includes:

- architectural preferences
- operational assumptions
- preferred implementation patterns
- intentionally avoided approaches
- security expectations
- repository direction

Do not store:

- secrets
- temporary debugging notes
- guesses
- private data

## Governance maturity progression

Typical maturity progression:

1. bootstrap
2. structured
3. operational
4. hardened
5. enterprise-ready

Indicators of maturity include:

- explicit security invariants
- AI-agent safety rules
- dependency governance
- CODEOWNERS
- SBOM generation
- validation automation
- governance drift awareness
- supply-chain documentation
- durable memory and decision tracking
- runtime governance
- release governance
- architecture fitness guidance
- policy-as-code direction
- provenance planning
- operational incident readiness

## Drift prevention

Common governance drift:

- stale links
- outdated workflow docs
- contradictory security guidance
- undocumented constraints
- duplicated rules
- unclear ownership

Useful mitigations:

- markdown link checking
- modular governance docs
- CODEOWNERS
- governance assessments
- decision logs
- durable repo memory

## Security-sensitive repository guidance

Repositories handling:

- payments
- credentials
- infrastructure
- CI/CD
- deployment automation
- customer payloads
- banking workflows

should explicitly document:

- trust boundaries
- workflow invariants
- approval invariants
- logging restrictions
- transport isolation
- secret-handling rules
- dependency review expectations
- AI-agent safety constraints
