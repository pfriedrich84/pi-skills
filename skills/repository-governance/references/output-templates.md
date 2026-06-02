# Repository Governance Output Templates

Use these templates when the user asks for an audit, maturity assessment, governance patch plan, or reviewable finding list.

Keep outputs concise and evidence-backed. Prefer repository-specific findings over generic advice.

## Default audit output

Unless the user asks for another format, produce these sections:

1. **Governance inventory**
   - path
   - observed role
   - status: canonical | stale | duplicate | conflicting | unknown
   - evidence
   - recommended action

2. **Topology assessment**
   - canonical entrypoints
   - intended reading order
   - missing or unclear links
   - ownership gaps

3. **Prioritized findings**
   - P0: unsafe or production-impacting governance gap
   - P1: likely to cause agent or contributor errors
   - P2: maintainability or drift risk
   - P3: cleanup or clarity improvement

4. **Smallest safe patch plan**
   - files to edit
   - files not to move
   - review risks
   - validation steps

5. **Open questions**
   - only where repository evidence is insufficient

## Finding format

For each non-trivial finding, use:

- **Finding:** concise statement
- **Evidence:** file paths, commands, snippets, observed absence, or repository/platform setting inspected
- **Type:** fact | inference | risk | recommendation | open question
- **Severity:** P0 | P1 | P2 | P3
- **Confidence:** high | medium | low
- **Suggested action:** smallest safe next step

## Governance inventory row format

Use this compact row format when a table is useful:

| Path | Observed role | Status | Evidence | Recommended action |
| --- | --- | --- | --- | --- |
| `AGENTS.md` | Agent operating contract | canonical | Root-level instruction file links validation and ADR rules. | Keep as primary entrypoint. |

## Patch plan format

When proposing changes, use:

- **Goal:** what the patch makes safer or clearer
- **Files to edit:** exact paths
- **Files not to touch:** avoid accidental scope expansion
- **Expected effect:** how agents/contributors should behave differently
- **Validation:** markdown checks, link checks, tests, or manual review steps
- **Rollback:** how to revert if the structure is not accepted

## Evidence rules

Do not claim that a repository lacks a control unless it was actually inspected.

If repository files suggest a risk but settings or external systems cannot be observed, write:

- **Evidence found:** describe the observable repository evidence
- **Not observable:** describe the setting or platform state that could not be inspected
- **Inference:** clearly mark the risk as an inference, not a fact
