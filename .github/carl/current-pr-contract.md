# Current PR contract: actions/checkout v7

## Goal and contract status

Active for PR #2. Upgrade the governance workflow's `actions/checkout` reference
from v4.4.0 to v7.0.1 using immutable commit
`3d3c42e5aac5ba805825da76410c181273ba90b1`. This contract becomes historical
when PR #2 is merged.

## Approved scope

- Update only the `actions/checkout` reference and version comment in
  `.github/workflows/governance.yml`.
- Reconcile this active contract with PR #2 and record the scoped owner
  authorization below.

## Non-goals and forbidden scope

- Do not change any other action, workflow behavior, dependency, runner,
  permission, secret, repository setting, or unrelated governance policy.
- Do not force-push, enable auto-merge, bypass branch protection, delete a
  branch, or merge any PR other than #2 under this contract.

## Constraints

- Keep `permissions: contents: read` and `persist-credentials: false`.
- Preserve `runs-on: ubuntu-24.04`, the 10-minute job timeout, the existing
  setup-python pin, and Python 3.12.
- The checkout action must be exactly
  `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1`.
- Do not weaken existing security, validation, or branch-protection controls.

## Contract assertions and validation

1. The complete diff changes only the intended checkout reference/comment and
   this PR-specific contract.
2. The action SHA is immutable and corresponds to v7.0.1; workflow permissions,
   runner, Python runtime, and credential persistence remain as specified.
3. The required `Governance validation` check succeeds on the final PR head,
   and the PR is mergeable under the live `main` protections.
4. After merge, the default-branch workflow succeeds for the resulting main
   merge SHA before PR #3 is considered.

## Risks, stop conditions, and escalation

Stop if the action SHA/version, workflow baseline, branch protection, required
check, or mergeability cannot be verified; if any check fails or times out; or
if an unexpected file or security-sensitive behavior changes. Leave the PR open
and stop this sequence. Never bypass or weaken a gate.

## Owner authorization amendment (2026-10-31)

The repository owner explicitly authorizes merging this specific PR #2, after
PR #5 has merged and its required default-branch workflow has succeeded. This
supersedes prior task-scoped instructions not to merge only for PR #2. It does
not authorize PR #3 or any other PR; the rest of the approved sequence remains
separately gated. Do not use auto-merge, force-push, or branch-protection
bypasses. If any gate is missing, fails, or times out, leave PR #2 open and stop.
