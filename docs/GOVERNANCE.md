# Governance controls and verification

## Scope and evidence

This repository supplies organisation-profile and community defaults. Files in a
feature PR are not live until merged; no automatic merge is permitted. Repository
defaults do not install cARL, workflows, Dependabot, or branch rules elsewhere.

The verification record below is updated only after successful read-back.
Do not infer enablement from repository visibility or API write success.

| Control in `kredoxi/.github` | Observed state |
| --- | --- |
| Repository administration | Authenticated account has admin permission |
| Dependabot vulnerability alerts | Enabled; GET returned HTTP 204 |
| Secret scanning | Enabled; repository security analysis read-back |
| Push protection | Enabled; repository security analysis read-back |
| Dependabot security updates | Enabled and not paused; automated-security-fixes read-back |
| Private vulnerability reporting | Enabled; private-vulnerability-reporting read-back |
| Actions permissions | Read-only token; workflow PR approvals disabled |
| Allowed actions | Only `actions/checkout@*` and `actions/setup-python@*`; GitHub-owned blanket allowance and verified-publisher allowance disabled; full SHA pinning required |
| Default-branch protection/checks | `main` requires PRs, resolved conversations, and up-to-date passing `Governance validation` from GitHub Actions (app ID 15368); admins enforced; force pushes/deletion disabled; zero mandatory approvals |

Repository settings in this table were successfully read back on 2026-10-31.
The required check first passed in
[GitHub Actions run 41215398198](https://github.com/kredoxi/.github/actions/runs/41215398198),
including ten regression tests, the pinned archive checksum, exact effective-pack
membership, runtime health, and synced Copilot adapter. Protection was applied
only after that successful run and its check producer were verified.

## Organisation configuration and remaining owner actions

The account's organisation membership is active with admin role. The current
token lacks `admin:org`, and organisation Actions permission endpoints return HTTP 403:
"You must be an org admin or have the actions policies fine-grained permission."
Do not broaden tokens silently. Configure organisation Actions through **Settings**
or an explicitly authorised credential with the required scope, then read back.

Organisation profile name and bounded description were set and read back on
2026-10-31. After confirming there was only one member (the owner), base repository
permission was set to `none` and member repository creation disabled. Dependabot
alerts/security updates and secret scanning/push protection were enabled as
new-repository defaults, with successful read-back for all four fields.
These defaults do not prove that existing repositories changed.
Two-factor authentication remains not required.

| Owner action | Target |
| --- | --- |
| Public profile settings | Name and bounded description are verified. Merge the profile PR and inspect the organisation page; no website was invented. |
| Member privileges | Base permissions `none` and member repository creation disabled are verified. Explicitly grant necessary roles when adding contributors; review existing grants separately. |
| Two-factor authentication | Recommend 2FA now, preferably phishing-resistant. Review member/collaborator readiness before enforcement because it can remove access. This session will not enable disruptive enforcement. |
| Actions defaults | Read-only tokens, workflow PR approval disabled, reviewed action allowlist and SHA pinning where supported. |
| Security defaults | New-repository defaults for secret scanning, push protection, Dependabot alerts/security updates are verified enabled. Verify every existing repository separately. |

## Repository protection target

Protect the actual default branch with an active rule: require PRs, resolved review
conversations, demonstrated passing checks, no force pushes or deletion, and
administrator enforcement. Avoid broad bypass actors.

While there is a single maintainer, require zero approving reviews; an author
cannot approve their own PR. Seek independent review when available. Do not
silently remove an existing stronger approval policy. Require only exact check
contexts that have actually run successfully, without deadlocking bootstrap.

Verify each repository's saved settings independently, including private reporting.
The shared [security policy](../SECURITY.md) supplies a private fallback route.
Unsupported features need their exact permission or plan limitation documented.

## Effective cARL governance

cARL v1.0.2 was installed using the explicitly selected WinGet binary. Bundled
assets retain upstream provenance; project-owned memory replaces the upstream
repository narrative. Copilot's production adapter was synced with
`carl harness sync copilot`.

Relevant core, dependency, security, identity, cognition, memory, PR-contract,
tool-boundary, CI/CD, Python-validation, and additive Kredoxi project packs are
selected in `.github/carl/packs.json`. Cloud and other language packs are installed
but inactive. No active profile file exists; explicit selection supplies active seeds.

Use `carl pack effective --json`, `carl status`, `carl trace`, and
`carl harness status` to verify composition and artifact health. A healthy adapter
does not prove a model loaded or followed the contract. CI checks effective pack
membership and healthy runtime state, not natural-language rule compliance.

On Windows, select the intended CLI when PATH resolves an older version:

```powershell
$carl = "$env:LOCALAPPDATA\Microsoft\WinGet\Packages\goldjg.cARL_Microsoft.Winget.Source_8wekyb3d8bbwe\carl.exe"
& $carl status
& $carl pack effective
```

For a fresh repository use `carl init`; if existing artifacts lack a manifest,
inspect them and use supported `carl init --adopt` to preserve their content.
Discover actual CLI help before composing new packs. Do not handwrite generated
loaders or weaken contracts to satisfy implementation preferences.
