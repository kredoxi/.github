# Contributing to Kredoxi

Discuss substantial scope or architecture changes before implementation. Use the
Kredoxi organisation repositories as project authorities.

1. Work on a scoped branch and preserve existing work.
2. Read requirements, threat model, decisions, and the effective cARL contract.
   Discover supported CLI commands rather than copying obsolete configurations.
3. Make the smallest complete change, with synthetic credentials only, explicit
   failures, authenticated identity, and least-privilege execution boundaries.
4. Update directly related documentation and reproducible regression tests.
5. Run documented build, formatting, tests, and governance checks. Report exact
   commands and results, including anything not executed.
6. Open a PR using the shared template. Never merge automatically or bypass checks.

Do not treat client-controlled process names, PIDs, or credential references as
authentication. Distinguish monitoring from prevention and explicit resolution
from transparent interception. Document supported platforms and known bypasses.
Privileged/host-disruptive testing needs an explicitly authorised disposable
environment. Never disable host security software or inspect real credential stores.

## Dependencies, CI, and review

Justify dependencies and their licence implications; keep real lockfiles current.
Pin external actions to reviewed full SHAs. PR code must not receive elevated
tokens or production secrets. See [CI guidance](docs/CI_SECURITY.md).

Require passing checks and seek independent review when available. Do not require
approvals that deadlock a sole maintainer: an author cannot approve their own PR.
Zero mandatory approvals does not waive documented review or security requirements.

## Licensing

No project licence has been selected. Do not add one or assume public source
grants redistribution rights. Selection requires an explicit owner decision.
