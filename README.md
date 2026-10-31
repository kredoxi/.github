# Kredoxi community and governance

This repository contains the organisation profile and default community health
files. Repository-local files take precedence over shared defaults. The profile
uses `profile/README.md` from the default branch; an unmerged PR is not yet live.

- [Contributing](CONTRIBUTING.md)
- [Code of conduct](CODE_OF_CONDUCT.md)
- [Security and coordinated disclosure](SECURITY.md)
- [Support](SUPPORT.md)
- [Governance controls and verification](docs/GOVERNANCE.md)
- [Least-privilege CI and supply-chain guidance](docs/CI_SECURITY.md)

For local validation, install CI-only dependencies with
`python -m pip install -r requirements-ci.txt`, then run
`python scripts/validate_governance.py`. Use the installed cARL v1.0.2 CLI for
`carl status`, `carl pack effective --json`, `carl trace`, and `carl harness status`.

No project licence has been selected. Do not add a licence or publishing workflow
without an explicit owner decision.
