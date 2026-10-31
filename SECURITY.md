# Security policy

## Project status and supported versions

Kredoxi is under development. There are no supported production releases or
guaranteed security-update timelines. Development-only providers are not
production credential stores. Reports and tests must use synthetic credentials.

References are not secrets or proof of identity. Protection against authorised
application compromise, memory disclosure, or privileged host compromise must
not be claimed without demonstrated enforcement at the exact boundary.

## Reporting a vulnerability

Do not disclose exploitable details or credential values in public issues.
On the affected repository, use **Security > Advisories > Report a vulnerability**.
If that option is unavailable there, use the
[organisation governance repository's private reporting page](https://github.com/kredoxi/.github/security/advisories/new)
and clearly identify the affected repository. The current verified configuration
is recorded in [governance evidence](docs/GOVERNANCE.md).

If neither route is available, open a public issue titled "Private security
contact requested" with no vulnerability details, sensitive references, logs, or
attachments. Wait for a maintainer to establish a private route. No dedicated
project security mailbox has been established.

In a private report include the affected repository and commit, synthetic
reproduction, prerequisites, attacker capabilities, observed impact, and suggested
mitigations. Redact credentials, tokens, environment dumps, and personal data.
Do not test third-party deployments or access real credential stores.

## Coordinated disclosure

A maintainer will triage reports and agree a disclosure plan with the reporter.
Use private advisories and temporary private forks where available. Fixes need
reproducible tests and bounded claims. Publish an advisory and remediation guidance
after coordination. Best-effort handling has no guaranteed response or fix deadline.

If a credential was exposed, rotate or revoke it through its issuer. Deleting a
message or commit is not sufficient remediation.
