# Grill With Docs

This skill interviews the user to clarify durable repository knowledge and captures the result in the right project documents.

It is the interactive companion to `repository-governance`:

- `repository-governance` defines the governance pattern.
- `grill-with-docs` discovers missing knowledge through focused questioning and writes it down.

The skill is intentionally domain-generic. It should preserve reusable governance practices without copying product-specific rules, terminology, customer assumptions, integration details, regulatory assumptions, or implementation plans between repositories.

## Use it for

- stress-testing a plan against existing repository language and decisions
- creating or sharpening a root `AGENTS.md`
- clarifying repository purpose and non-purpose
- extracting agent rules and non-negotiable constraints
- documenting validation commands and definition of done
- identifying trust boundaries
- recording ADR-worthy decisions
- clarifying project-specific language in `CONTEXT.md`
- resolving stale, duplicated, or conflicting docs

## Session behavior

The skill should:

- ask one load-bearing question at a time
- provide a recommended answer for each question
- inspect code and existing docs instead of asking when the answer is discoverable
- challenge terms that conflict with `CONTEXT.md`
- sharpen vague or overloaded language into canonical terms
- use concrete scenarios to test boundaries and edge cases
- cross-check user claims against code, docs, and accepted ADRs
- update durable docs inline as decisions crystallize

## Documentation routing

```text
AGENTS.md              agent operating contract and reading order
CONTEXT.md             project-specific language and resolved ambiguities
CONTEXT-MAP.md         map of multiple contexts when needed
docs/adr/              hard-to-reverse decisions and trade-offs
docs/architecture/     structural explanations and invariants
docs/security/         secret handling, trust boundaries, security assumptions
docs/integration/      external systems, interfaces, permissions, failure modes
docs/implementation/   plans, sequencing, non-final proposals
TODO.md / roadmap      open work and prioritization
```

Follow the repository's existing documentation style when it is coherent.

## Recommended skill structure

```text
skills/grill-with-docs/
  SKILL.md
  README.md
  CONTEXT-FORMAT.md
  ADR-FORMAT.md
```
