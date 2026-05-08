---
name: repository-governance
description: Establish durable AI-native repository governance by organizing agent documentation, preserving institutional memory, normalizing collaboration workflows, documenting decisions, improving safety guidance, and strengthening supply-chain practices.
---

# Repository Governance

This skill establishes durable repository governance for humans and AI coding agents.

It combines agent documentation, institutional memory, decision preservation, collaboration standards, validation workflows, safety guidance, repository archaeology, repository assessment, and supply-chain governance into one coherent repository-local system.

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
    DEFINITION_OF_DONE.md
    AUTORESEARCH.md
    ASSESSMENT.md
  developer/
    adr/
  user/
```

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
- memory and decision preservation quality.

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
- missing onboarding guidance.

## Recommended next steps

Prioritize improvements by:

1. safety/security impact;
2. operational risk reduction;
3. onboarding improvement;
4. contributor productivity;
5. AI-agent reliability.

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
