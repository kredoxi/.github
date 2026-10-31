# Current PR contract: actions/setup-python v7

## Goal and contract status

Active for PR #3. Upgrade the governance workflow's `actions/setup-python`
reference from v5.6.0 to v7.1.0 using immutable commit
`6d4fd22b20465ccc0f7354476588e8df7c9ca0e0`. This contract becomes historical
when PR #3 is merged.

## Approved scope

- Update only the `actions/setup-python` reference and version comment in
  `.github/workflows/governance.yml`.
- Reconcile this active contract with PR #3 and record the scoped owner
authorization below.

## Non-goals and forbidden scope

- Do not change any other action, workflow behavior, dependency, runner,
  permission, secret, repository setting, or unrelated governance policy.
- Do not force-push, enable auto-merge, bypass branch protection, delete a
  branch, or merge any PR other than #3 under this contract.

## Constraints

- Keep `permissions: contents: read` and `persist-credentials: false`.
- Preserve the `actions/checkout` v7.0.1 immutable pin
  `3d3c42e5aac5ba805825da76410c181273ba90b1`, `runs-on: ubuntu-24.04`, and the
  10-minute job timeout.
- Keep Python 3.12, CI dependency installation, governance validation, unit
  tests, and pinned cARL validation unchanged.
- The setup-python action must be exactly
  `actions/setup-python@6d4fd22b20465ccc0f7354476588e8df7c9ca0e0 # v7.1.0`.
- Do not weaken existing security, validation, or branch-protection controls.

## Contract assertions and validation

1. The complete diff changes only the intended setup-python reference/comment
   and this PR-specific contract.
2. The action SHA is immutable and corresponds to v7.1.0; checkout remains
   pinned to v7.0.1; permissions, runner, credential persistence, Python 3.12,
   dependency installation, and governance checks remain unchanged.
3. The required `Governance validation` check succeeds on the final PR head,
   and the PR is mergeable under the live `main` protections.
4. After merge, the default-branch workflow succeeds for the resulting main
   merge SHA and verifies both action upgrades before completion.

## Risks, stop conditions, and escalation

Stop if either action SHA/version, workflow baseline, branch protection,
required check, or mergeability cannot be verified; if any check fails or times
out; or if an unexpected file or security-sensitive behavior changes. Leave
the PR open and stop this sequence. Never bypass or weaken a gate.

## Owner authorization amendment (2026-10-31)

The repository owner explicitly authorizes merging this specific PR #3 only
after PR #5 and PR #2 have merged and each required default-branch workflow has
succeeded. This supersedes prior task-scoped instructions not to merge only
for PR #3. It does not authorize any other PR. Do not use auto-merge,
force-push, or branch-protection bypasses. If any gate is missing, fails, or
times out, leave PR #3 open and stop.
