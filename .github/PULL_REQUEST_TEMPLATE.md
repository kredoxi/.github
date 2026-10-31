## Summary

Describe the change and link its issue, requirement, or decision.

## Security and trust boundaries

Explain identity, authorisation, credential handling, telemetry, dependency, and
workflow-permission changes. State limitations and known bypasses.
If not applicable, explain why.

## Verification

List exact commands and observed results. Identify checks not run and why.
Use synthetic credentials only.

## Contributor checklist

- [ ] The change follows the effective cARL contract.
- [ ] Directly related documentation and regression tests are updated.
- [ ] No real credentials, sensitive logs, or personal data are included.
- [ ] Dependency and action-pin changes have been reviewed.
- [ ] Security claims are bounded by demonstrated behaviour.
- [ ] No unapproved licence, release, or automatic merge is added.
