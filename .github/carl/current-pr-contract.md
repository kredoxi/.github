# Current PR contract: Kredoxi visual identity

## Goal and contract status

Active. Establish `logos/` in `kredoxi/.github` as the canonical,
organisation-wide source of truth for Kredoxi visual identity and document the
approved asset roles and naming conventions without changing the existing
artwork.

## Approved scope

- Add `docs/BRANDING.md` documenting the approved product name, tagline, logo
  paths and uses, source-asset status, canonical raw URLs, and restrictions on
  creating or modifying variants.
- Update `profile/README.md` to use the primary wordmark and exact approved
  product name and tagline.
- Link the branding guidance from the root `README.md`.
- Record the canonical logo location and approved asset roles in
  `.github/carl/memory.md`.
- Include the branding guide in the existing public-document link validation
  so the regression-test fixture contains every linked public document.
- Open a separate pull request for these changes. Do not merge it.

## Non-goals and forbidden scope

- Do not modify, regenerate, replace, rename, or remove any logo binaries.
- Do not invent, establish, or publish additional branding variants.
- Do not change organisation or repository settings, or edit other repositories.
- Do not add a licence, dependency, release, publishing workflow, or automatic
  merge.
- Do not alter unrelated governance, security, CI, or product architecture.

## Constraints

- Preserve the three existing assets and their verified bytes:
  - `logos/kredoxi_logo_optimized.png` — primary wordmark, 1200x900.
  - `logos/kredoxi_github_avatar.png` — compact logo, 512x512.
  - `logos/kredoxi-logo.png` — original master source, 1448x1086.
- Use the exact product name **Kredoxi** and tagline **Steal the config. Not
  the secret.**
- In the profile, link the displayed wordmark to the canonical `logos/`
  directory, use alt text `Kredoxi — Steal the config. Not the secret.`, and
  set its width to 240px only so its aspect ratio is preserved.
- Describe only the security properties established by repository evidence;
  branding must not imply unverified product guarantees.

## Contract assertions and validation

1. The branding guide identifies the exact three canonical paths and their
   distinct roles, and prohibits unofficial variants.
2. The profile uses the exact approved product name and tagline; its 240px
   primary wordmark links to the canonical logo directory and has alt text
   `Kredoxi — Steal the config. Not the secret.`
3. Root documentation links to the branding guide, and all repository-local
   links added by this change resolve; `docs/BRANDING.md` is covered by the
   validator's fixture and link checks.
4. The logo files retain their original SHA-256 hashes and dimensions.
5. `python scripts/validate_governance.py` passes; inspect the final diff and
   open (but do not merge) a separate PR using the repository PR template.

## Stop conditions and escalation

Stop if any canonical logo is missing or differs from its verified bytes, if
the requested naming or asset roles conflict with checked-in evidence, or if
completing the task would require changing another repository, image asset,
security guarantee, or organisation setting. Do not merge the resulting PR.

## Reconciliation and context reset

The branding guide, organisation profile, root README, and memory entry are the
durable record of this decision. Keep this contract active while the PR is under
review. After the PR is merged or closed, reset it so this task's scope does not
constrain unrelated future work.
