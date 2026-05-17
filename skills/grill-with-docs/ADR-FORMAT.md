# ADR Format

ADRs live in `docs/adr/` by default and use sequential numbering: `0001-slug.md`, `0002-slug.md`, etc.

Create the `docs/adr/` directory lazily — only when the first ADR is needed.

If the repository already has a coherent ADR structure, follow it instead of forcing this layout.

## Template

```md
# {Short title of the decision}

{1-3 sentences: what's the context, what did we decide, and why.}
```

That's it. An ADR can be a single paragraph. The value is in recording *that* a decision was made and *why* — not in filling out sections.

## Optional sections

Only include these when they add genuine value. Most ADRs won't need them.

- **Status** frontmatter (`proposed | accepted | deprecated | superseded by ADR-NNNN`) — useful when decisions are revisited
- **Considered Options** — only when the rejected alternatives are worth remembering
- **Consequences** — only when non-obvious downstream effects need to be called out
- **Links** — only when the decision depends on durable docs, issues, or implementation plans

## Numbering

Scan `docs/adr/` for the highest existing number and increment by one.

If there are context-local ADR folders, number within the relevant folder according to the existing convention.

## When to offer an ADR

All three of these must be true:

1. **Hard to reverse** — the cost of changing your mind later is meaningful
2. **Surprising without context** — a future reader will look at the code or docs and wonder "why on earth did they do it this way?"
3. **The result of a real trade-off** — there were genuine alternatives and you picked one for specific reasons

If a decision is easy to reverse, skip it. If it is not surprising, nobody will wonder why. If there was no real alternative, there is nothing to record beyond "we did the obvious thing."

## Superseding decisions

Accepted ADRs must not be contradicted silently.

If a new direction conflicts with an accepted ADR, create a new ADR that explicitly supersedes or amends the older decision. Do not edit historical ADRs in a way that hides the original decision.

Use status metadata or a short note such as:

```md
Status: supersedes ADR-0007
```

or:

```md
Status: superseded by ADR-0012
```

depending on the repository's existing convention.

## What qualifies

- **Architectural shape.** "We're using a monorepo." "The write model is event-sourced, the read model is projected into Postgres."
- **Integration patterns between contexts.** "Ordering and Billing communicate via domain events, not synchronous HTTP."
- **Technology choices that carry lock-in.** Database, message bus, auth provider, deployment target. Not every library — just the ones that would take meaningful time to swap out.
- **Boundary and scope decisions.** "Customer data is owned by the Customer context; other contexts reference it by ID only." The explicit no-s are as valuable as the yes-s.
- **Deliberate deviations from the obvious path.** "We're using manual SQL instead of an ORM because X." Anything where a reasonable reader would assume the opposite. These stop the next engineer from "fixing" something that was deliberate.
- **Constraints not visible in the code.** "We can't use a specific cloud provider because of compliance requirements." "Response times must stay under a threshold because of a partner contract."
- **Repository governance decisions.** "CI workflow changes require explicit review." "Generated artifacts are not committed." "External tools are treated as trust boundaries."
- **Rejected alternatives when the rejection is non-obvious.** If you considered GraphQL and picked REST for subtle reasons, record it — otherwise someone will suggest GraphQL again in six months.

## What does not qualify

- ordinary TODOs
- transient preferences
- obvious implementation details
- small library choices with low switching cost
- decisions that belong in `CONTEXT.md` as terminology
- plans that are not yet decisions
