"""Regression tests for the governance check's exact security assertions."""

from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

import yaml

import validate_governance as governance


class GovernanceValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        paths = list(governance.PUBLIC_DOCS) + [
            ".github/workflows/governance.yml",
            ".github/dependabot.yml",
            ".github/carl/packs.json",
            ".github/ISSUE_TEMPLATE/config.yml",
            ".github/ISSUE_TEMPLATE/bug_report.yml",
            ".github/ISSUE_TEMPLATE/feature_request.yml",
        ]
        for relative in paths:
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(governance.ROOT / relative, destination)
        self.addCleanup(patch.stopall)
        patch.object(governance, "ROOT", self.root).start()

    def mutate_workflow(self, mutate) -> None:
        workflow = governance.load_yaml(".github/workflows/governance.yml")
        mutate(workflow)
        path = self.root / ".github/workflows/governance.yml"
        path.write_text(yaml.safe_dump(workflow), encoding="utf-8")

    def test_current_contract_passes(self) -> None:
        governance.validate_files()
        governance.validate_workflow()

    def test_write_token_is_rejected(self) -> None:
        self.mutate_workflow(lambda workflow: workflow.update(permissions={"contents": "write"}))
        with self.assertRaisesRegex(ValueError, "read-only"):
            governance.validate_workflow()

    def test_privileged_trigger_is_rejected(self) -> None:
        self.mutate_workflow(lambda workflow: workflow[True].update(pull_request_target=None))
        with self.assertRaisesRegex(ValueError, "privileged"):
            governance.validate_workflow()

    def test_path_filtered_required_check_is_rejected(self) -> None:
        self.mutate_workflow(lambda workflow: workflow[True].update(pull_request={"paths": ["docs/**"]}))
        with self.assertRaisesRegex(ValueError, "filters"):
            governance.validate_workflow()

    def test_unpinned_action_is_rejected(self) -> None:
        self.mutate_workflow(lambda workflow: workflow["jobs"]["governance"]["steps"][0].update(
            uses="actions/checkout@v4"))
        with self.assertRaisesRegex(ValueError, "full commit SHAs"):
            governance.validate_workflow()

    def test_ignored_validation_failure_is_rejected(self) -> None:
        self.mutate_workflow(lambda workflow: workflow["jobs"]["governance"]["steps"][2].update(
            {"continue-on-error": True}))
        with self.assertRaisesRegex(ValueError, "silently"):
            governance.validate_workflow()

    def test_retained_checkout_credentials_are_rejected(self) -> None:
        self.mutate_workflow(lambda workflow: workflow["jobs"]["governance"]["steps"][0]["with"].update(
            {"persist-credentials": True}))
        with self.assertRaisesRegex(ValueError, "retain credentials"):
            governance.validate_workflow()

    def test_unapproved_licence_is_rejected(self) -> None:
        (self.root / "LICENSE").write_text("Unapproved", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "owner decision"):
            governance.validate_files()

    def test_broken_document_link_is_rejected(self) -> None:
        (self.root / "README.md").write_text("[Missing](missing.md)", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Broken link"):
            governance.validate_files()

    def test_escaping_document_link_is_rejected(self) -> None:
        (self.root / "README.md").write_text("[Outside](../outside.md)", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Escaping link"):
            governance.validate_files()


if __name__ == "__main__":
    unittest.main()
