# Platform and Supply-Chain Governance

Use this reference when repository governance depends on GitHub settings, CI/CD settings, dependencies, external actions, registries, containers, packages, MCP servers, AI tooling, or other trust boundaries.

## Observable vs. unknown settings

Repository files are not the whole governance surface. Some controls live in repository, organization, CI, package-registry, cloud, or deployment-platform settings.

When tools allow access to repository or organization settings, include platform governance in the audit:

- branch protection or rulesets,
- required reviews and required status checks,
- CODEOWNERS review enforcement,
- deployment environments and approval gates,
- GitHub Actions permissions and default token permissions,
- secret scanning and push protection,
- dependency graph, dependency review, Dependabot alerts/updates,
- Dependabot update configuration in `.github/dependabot.yml` or Renovate configuration when dependency manifests are present,
- code scanning or CodeQL setup.

If settings are not observable, mark them as **unknown**, not missing. Do not claim that a repository lacks a protection unless the setting was actually inspected.

## Trust-boundary inventory

Treat these as trust boundaries:

- new runtime dependencies,
- package registries,
- GitHub Actions and reusable workflows,
- Docker images,
- build plugins,
- MCP servers,
- external APIs and SaaS services,
- cloud services,
- AI tools and model providers,
- deployment platforms,
- artifact stores,
- telemetry and analytics sinks.

For each trust boundary, document:

- what it is used for,
- what data it can access,
- what credentials or permissions it requires,
- how it is configured,
- how it is validated,
- how it can be disabled or replaced,
- what risks or assumptions exist.

## Supply-chain governance checks

During repository scans, inspect:

- dependency manifests and lockfiles,
- package-manager configuration,
- Dockerfiles and compose files,
- GitHub Actions workflows,
- reusable workflow references,
- action pinning style,
- container image pinning style,
- scripts that download or execute remote content,
- generated artifacts,
- SBOM/provenance/signing documentation,
- license or dependency-review configuration,
- dependency-age quarantine checks and allowlist files such as `.dependency-age-allowlist`,
- Dependabot or Renovate configuration.

When the repository has supported dependency manifests and no existing dependency-update bot configuration, propose or create the smallest useful `.github/dependabot.yml` (or Renovate equivalent) for the observed ecosystems. Keep update schedules conservative, group related updates where it reduces PR noise, and document that bot PRs still require human review for runtime, CI, Docker, security-sensitive, or trust-boundary changes.

If the repository has dependency-age quarantine controls, preserve them when handling bot PRs. Do not bypass age gates by default. If the repository uses an allowlist file such as `.dependency-age-allowlist`, only add entries for explicit security fixes or maintainer-approved exceptions, include the CVE or justification and expiry/removal condition, and remove exceptions once the package version ages past the quarantine window.

For GitHub repositories, distinguish file-based Dependabot update configuration from platform-only settings such as dependency graph, Dependabot alerts, Dependabot security updates, dependency review, and secret scanning. If those settings cannot be inspected or changed through available tools, mark them as **unknown** and recommend human verification rather than implying the config file enables alerts.

Classify supply-chain findings as:

- dependency governance gap,
- workflow trust-boundary gap,
- container trust-boundary gap,
- remote-execution risk,
- artifact provenance gap,
- license visibility gap,
- credential exposure risk,
- unobservable platform setting.

## CI and workflow governance

Workflow governance should make it clear:

- who may change workflows,
- when workflow changes require human review,
- what permissions workflows need,
- whether default tokens are least-privilege,
- how secrets are scoped,
- which checks are required before merge or release,
- which jobs publish artifacts,
- which jobs deploy or mutate external systems.

Agents should not broaden workflow permissions, add new network calls, add publish/deploy behavior, or change approval behavior without explicit scope and review.

## Provenance and signing direction

Security-sensitive repositories should eventually plan for:

- SBOM generation,
- artifact signing,
- container signing,
- signed SBOMs,
- provenance attestations,
- release traceability.

Do not require these controls for every repository. Treat them as maturity indicators whose priority depends on operational, security, distribution, and customer risk.

## Compliance boundary

Supply-chain governance is not the same as certification or regulatory compliance.

Use governance language such as:

- "missing documented control",
- "requires human compliance review",
- "evidence not found",
- "not observable from repository files".

Do not claim compliance with a law, regulation, standard, certification, or customer requirement unless the repository contains explicit evidence and the user asked for that assessment.
