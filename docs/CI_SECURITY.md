# Least-privilege CI and supply-chain guidance

These requirements do not install workflows in other repositories. Each repository
must implement checks appropriate to its actual stack.

## Untrusted contributions

Test contributor code with `pull_request`, not privileged `pull_request_target` or
`workflow_run` contexts. Default tokens to `contents: read`; elevate individual
jobs only when explicitly justified. Do not expose secrets, cloud identities,
write tokens, or persistent privileged runners to untrusted PRs. Do not retain
checkout credentials. Treat caches and artifacts as untrusted input.

Pin actions to reviewed full SHAs and downloaded tooling to a version with a
committed digest. Set timeouts. Never interpolate issue/PR text or branch names
directly into shell source; pass validated data through structured inputs instead.

## Required checks

Use stable unique job names. Required jobs must run for every PR without path
filters that leave checks pending. Create and successfully run the initial job
before requiring its exact context in branch protection.

Implementation CI needs build, formatting/lint, unit/integration/adversarial tests,
static analysis, dependency checks, secret scanning, and cARL validation.
Documentation CI must validate its actual configuration and document contracts.
A governance check verifies artifact health and effective packs, not model adherence.
Missing tools and failed checks must fail explicitly.

This repository runs `Governance validation` with a read-only token, YAML/document
validation, exact pack assertions, cARL health, trace, and harness diagnostics.
It installs a pinned cARL archive only after verifying its committed SHA-256.
The checksum binds bytes, not a publisher signing trust root.

## Dependencies and distribution

Dependabot configuration covers real GitHub Actions and CI Python dependencies.
Alerts and security-update settings are separate controls and require read-back.
An alert is not a fix; update PRs need review.

No production publishing is authorised. Before distribution, agree licence,
signing trust root, trusted build environment, immutable artifact digests, SBOM,
provenance, and verification instructions. Separate future narrowly privileged
publishing jobs from untrusted tests and prefer short-lived identity where justified.
