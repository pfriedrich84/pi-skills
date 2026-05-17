# Repository Governance

This skill establishes durable repository governance for humans and AI coding agents.

It combines:

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
docs/adr/
docs/architecture/
docs/security/
docs/integration/
docs/implementation/
docs/operations/
docs/agent/
```

The exact structure should follow the repository's existing documentation style.

## Recommended skill structure

```text
skills/repository-governance/
  SKILL.md
  README.md
```
