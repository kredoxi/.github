<!-- version: 1.0.0 -->
# Kredoxi project governance

Apply these additional constraints alongside the selected core and CI packs.

- Work only in the repository assigned by the user; no unrelated repository is
  a project authority.
- Use synthetic credentials only. Never inspect personal credential stores,
  disable host security software, or run privileged invasive tests outside an
  explicitly authorised disposable environment.
- References are not secrets, identity, or authorisation. Do not claim automatic
  substitution, transparent interception, or tamper prevention without executable
  evidence for the exact boundary.
- An authorised compromised process may expose received credentials; privileged
  host compromise and memory scraping remain explicit limitations.
- Never add a project licence, production publishing workflow, release, or
  automatic merge without the corresponding explicit owner decision.
- Preserve least-privilege CI. Untrusted PR code receives no production secrets,
  elevated tokens, or persistent privileged runner access.
- Verify saved GitHub control values before claiming enablement. Document exact
  permission/plan blockers and manual actions; do not silently relax controls.
- Require demonstrated checks and prevent force pushes/deletion. While there is
  only one maintainer, do not require approvals an author cannot supply.
- Keep private vulnerability disclosure and public support procedures distinct.
- Shared community files do not establish effective governance or security
  configuration in other repositories; verify each separately.
