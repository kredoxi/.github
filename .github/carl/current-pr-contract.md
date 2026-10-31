# Current PR contract: Kredoxi governance bootstrap

## Goal and contract status

Closed after bootstrap delivery; the feature PR remains open and unmerged.
Assisted implementation was approved by the user's execution brief and retry.
Establish the `.github` organisation profile, community standards, effective cARL
governance, least-privilege CI, and verifiable GitHub repository controls.

## Approved scope and plan

1. Install cARL v1.0.2 using the discovered CLI, retain canonical bundled assets,
   select relevant packs, sync Copilot, and replace upstream project memory with
   Kredoxi repository truth.
2. Add public community documents, issue forms, PR template, CI validation,
   GitHub Actions dependency updates, and shared security guidance.
3. Enable and read back supported security controls in `kredoxi/.github`, plus
   the requested organisation profile/member/new-repository security defaults.
   Document organisation Actions controls blocked by insufficient token scope.
4. Validate locally, commit, push, open a PR, confirm its CI, then require the
   demonstrated check on the protected default branch. Never merge.

## Non-goals and forbidden scope

No work in other repositories, runtime MVP, interception implementation, production
credentials, licence selection, releases, automatic merging, force pushes, broad
permission grants, disruptive 2FA enforcement, or weakening existing protections.

## Architectural and security constraints

Canonical cARL assets remain authoritative; loaders remain generated adapters.
No embedded source changes are needed in this consumer repository. Repository
memory is project-owned and must not describe the upstream cARL implementation
as Kredoxi. Custom project guidance is additive, not an override.

CI uses read-only tokens and reviewed pinned actions/tooling. Governance health
and pack diagnostics do not prove model adherence. Vulnerability reporting must
have a verified private route; avoid publishing exploit details.

## Expected files

`profile/`, root community documents, `.github/ISSUE_TEMPLATE/`,
`.github/PULL_REQUEST_TEMPLATE.md`, `.github/workflows/`, `.github/dependabot.yml`,
`scripts/`, `.gitignore`, `.gitattributes`, `requirements-ci.txt`, `docs/`, generated cARL assets and adapters,
project pack, selection state, current contract, memory, and generated repo map.

## Contract assertions and validation

1. Public files exist, local documentation links resolve, issue forms have
   required fields, and no licence is added: `python scripts/validate_governance.py`.
2. Workflow triggers cover every PR and default-branch push, tokens are read-only,
   checkout does not retain credentials, action pins are full SHAs, and downloads
   have committed integrity checks: same validator and GitHub CI.
3. cARL reports healthy assets and exactly the intended effective packs:
   `carl status`, `carl pack effective --json`, `carl trace`, `carl harness status`.
4. GitHub security controls are read back; required checks have a real successful
   run, and branch protection prevents force pushes/deletion without a sole-owner
   approval deadlock: REST API inspection.
5. PR stays open and unmerged: live PR state inspection.

## Risks, stop conditions, and escalation

Stop writes on permission denial, unexpected existing work, new dependency trust
concerns, conflicting governance, or any requirement for destructive operations.
Record unsupported API controls rather than claiming enablement. Python/PyYAML
is a narrowly scoped CI-only dependency for parsing real YAML, not product runtime.
The cARL release checksum establishes pinned integrity, not a signing trust root.

## Reconciliation and context reset

Project memory and governance documentation were updated for durable truth.
The demonstrated CI check is required on protected `main`, with no force pushes,
deletion, or sole-owner approval deadlock. Profile/community files remain proposed
until owner merge. This completed contract is historical scope, not an invariant
for unrelated future work; create a fresh active contract before future changes.
