# Repository Governance Maturity Model

Use this model to make governance maturity assessments repeatable and reviewable.

Assign the lowest maturity level whose criteria are substantially met. Do not promote a repository based on intent alone; require observable evidence in files, workflows, platform settings, or documented process.

## Levels

### 1. Bootstrap

The repository has basic orientation but limited durable governance.

Typical evidence:

- README explains the project purpose.
- Basic setup or validation commands are discoverable.
- Main language, package manager, and test entrypoints are identifiable.

Common gaps:

- No explicit agent operating contract.
- Validation expectations are incomplete or implicit.
- Architecture and decision context are hard to find.

Smallest safe next improvement:

- Add or improve root `AGENTS.md` with reading order, validation commands, safety rules, and definition-of-done basics.

### 2. Structured

The repository has clear documentation topology and agent/contributor entrypoints.

Typical evidence:

- Root `AGENTS.md` or equivalent exists.
- Canonical docs and reading order are clear.
- Ownership between README, AGENTS, ADRs, architecture docs, and roadmap docs is understandable.
- Stale or archival docs are marked or isolated.

Common gaps:

- ADR and validation expectations may still be incomplete.
- Trust boundaries may not be documented.
- Governance drift may not be checked.

Smallest safe next improvement:

- Add ADR rules, validation requirements, and trust-boundary documentation guidance.

### 3. Operational

The repository governance is usable during normal PR work.

Typical evidence:

- Validation commands are documented and correspond to scripts or CI.
- ADR or decision-log rules exist and are followed for durable decisions.
- Security, secret-handling, and trust-boundary rules are actionable.
- Definition of done covers code, tests, docs, security implications, and operational impact where relevant.
- Agents have clear stop/ask/escalate rules.

Common gaps:

- CODEOWNERS, platform settings, supply-chain governance, and drift checks may be incomplete.
- Runtime/release governance may be partial.

Smallest safe next improvement:

- Add CODEOWNERS/review expectations, dependency governance, and drift-check guidance.

### 4. Hardened

The repository combines documented governance with enforceable or semi-enforceable controls.

Typical evidence:

- CODEOWNERS or review ownership exists.
- Branch protection, rulesets, required checks, or equivalent settings are documented or observable.
- Dependency governance is documented and supported by tools such as dependency review, Dependabot/Renovate, lockfile policy, or license checks.
- Supply-chain expectations include SBOM/provenance direction.
- Workflow restrictions and least-privilege expectations are documented.
- Governance drift checks are planned or partially automated.

Common gaps:

- Policy-as-code may still be aspirational.
- Runtime, incident, and release governance may not be consistently measured.

Smallest safe next improvement:

- Turn the highest-risk documented governance rules into automated checks or platform-enforced rules.

### 5. Enterprise-ready

The repository has governance that is durable, partly automated, measurable, and suitable for high-trust collaboration.

Typical evidence:

- Governance controls are documented and partly automated.
- Policy-as-code direction is clear.
- Runtime, release, incident, and supply-chain governance are connected.
- Provenance, signing, or SBOM practices are documented and validated where relevant.
- Governance metrics are reviewable.
- Platform settings and repository docs are intentionally aligned.

Common gaps:

- Evidence may still depend on external systems that are not visible from the repository.
- Certification or regulatory assurance still requires human review and explicit evidence.

Smallest safe next improvement:

- Improve measurement, evidence collection, and cross-system traceability.

## Assessment output

Always include:

- assigned level,
- evidence for the assigned level,
- missing criteria for the next level,
- platform or external settings marked as unknown if not observable,
- smallest safe next improvement.

## Scoring caution

Do not over-score repositories because they have many documents. Maturity depends on whether governance is discoverable, accurate, current, enforceable where needed, and useful for real contributor and agent workflows.
