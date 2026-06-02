# Repository Governance Audit Workflow

Use this reference for detailed repository scans, documentation topology reviews, and governance drift checks.

## Audit posture

Governance audits should be evidence-based and multi-pass:

1. scan broadly before proposing changes,
2. build an inventory of existing documents and settings,
3. identify the current documentation topology,
4. compare related documents for overlap, contradiction, drift, and missing links,
5. infer the intended structure from repository evidence,
6. propose the smallest safe restructuring path,
7. separate facts, inferences, risks, recommendations, and open questions.

Do not expose private chain-of-thought. Provide concise rationale, file paths, evidence, and reviewable decisions.

## Repository inventory

Look for:

- root `AGENTS.md`,
- nested `AGENTS.md` or `AGENTS.override.md` files,
- `README.md`,
- `TODO.md` or roadmap files,
- `CONTEXT.md` and `CONTEXT-MAP.md`,
- `docs/adr/`,
- `docs/architecture/`,
- `docs/security/`,
- `docs/integration/`,
- `docs/implementation/`,
- `docs/operations/`,
- `docs/agent/`,
- contribution, release, deployment, validation, or runbook docs,
- `.github/workflows/`,
- dependency manifests and lockfiles,
- Docker, compose, infrastructure, or deployment descriptors,
- configuration examples,
- scripts that define validation, release, or operational behavior.

For each relevant document, classify its role:

- canonical operating contract,
- project overview,
- architecture reference,
- decision record,
- implementation plan,
- security guidance,
- integration contract,
- operational runbook,
- validation/checklist,
- roadmap or TODO,
- archive, spike, or historical note,
- duplicate, stale, orphaned, or conflicting document.

## Documentation topology assessment

Identify:

- canonical entrypoints,
- intended reading order for agents,
- documents that should be linked from `AGENTS.md`,
- duplicated documents,
- documents that contradict accepted decisions or current code,
- stale or archival documents,
- missing governance topics,
- missing trust-boundary documentation,
- missing validation or definition-of-done guidance,
- unclear ownership between docs,
- places where docs should be merged, moved, renamed, archived, or cross-linked.

Prefer evidence-backed observations over generic templates.

## Governance drift checks

Compare these sources for contradictions:

- `AGENTS.md` vs. README setup instructions,
- validation docs vs. package scripts, Makefile, build files, and CI workflows,
- ADRs vs. current architecture docs and code structure,
- deployment docs vs. workflow files, environment descriptors, and runtime config,
- dependency guidance vs. manifests, lockfiles, Dependabot/Renovate config, and CI,
- security guidance vs. workflows, Dockerfiles, config examples, scripts, and runbooks,
- release docs vs. tags, branches, artifact workflows, changelog, and release notes.

Classify drift as:

- command drift,
- ownership drift,
- architecture drift,
- security drift,
- release drift,
- trust-boundary drift.

## Safe restructuring sequence

Do not reorganize documents aggressively just to match an ideal template.

Prefer this order:

1. add missing links and reading order,
2. clarify canonical ownership of topics,
3. mark stale or archival content clearly,
4. consolidate duplicated content only when the canonical destination is obvious,
5. move or rename files only when the user asked for restructuring or the benefit is clear,
6. preserve existing conventions unless they are actively harmful.

Before moving, deleting, or renaming many documents, propose the target structure and rationale first.

When restructuring, preserve history and reviewer confidence:

- keep changes small and reviewable,
- avoid mixing large rewrites with file moves,
- retain redirects or index links when useful,
- summarize what changed and why,
- document remaining open questions.

## Nested agent instructions

For monorepos or repositories with distinct subprojects, consider nested agent instructions when subdirectories have different build/test commands, security rules, deployment rules, or ownership.

When nested instructions exist:

- verify their precedence is intentional,
- check for contradictions with the root contract,
- ensure the root file explains or links the nested instruction model,
- avoid duplicating shared rules across every nested file,
- keep shared repository-wide constraints in the root file.
