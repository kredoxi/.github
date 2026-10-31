"""Validate the public community and least-privilege governance contract."""

import argparse
import json
from pathlib import Path
import re
import subprocess

import yaml


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PACKS = {
    "core/baseline",
    "core/carl",
    "core/cognition-governance",
    "core/dependency",
    "core/identity",
    "core/memory-cache",
    "core/pr-contract",
    "core/security",
    "core/tool-permission-tiers",
    "languages/python",
    "platform/cicd",
    "project/kredoxi",
}
PUBLIC_DOCS = (
    "README.md",
    "profile/README.md",
    "SECURITY.md",
    "SUPPORT.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "docs/GOVERNANCE.md",
    "docs/CI_SECURITY.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def load_yaml(relative: str):
    return yaml.safe_load((ROOT / relative).read_text(encoding="utf-8"))


def validate_files() -> None:
    for relative in PUBLIC_DOCS:
        path = ROOT / relative
        text = path.read_text(encoding="utf-8")
        require(text.strip(), f"Empty document: {relative}")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if target.startswith(("https://", "http://", "#")):
                continue
            linked = (path.parent / target.split("#", 1)[0]).resolve()
            require(linked.is_relative_to(ROOT), f"Escaping link: {relative}: {target}")
            require(linked.is_file(), f"Broken link: {relative}: {target}")

    require(not list(ROOT.glob("LICENSE*")), "Project licence requires an owner decision")
    for path in (ROOT / ".github").rglob("*.yml"):
        require(isinstance(load_yaml(str(path.relative_to(ROOT))), dict),
                f"Expected YAML mapping: {path.relative_to(ROOT)}")

    for name in ("bug_report", "feature_request"):
        form = load_yaml(f".github/ISSUE_TEMPLATE/{name}.yml")
        require(form.get("name") and form.get("description"), f"Incomplete issue form: {name}")
        fields = [field for field in form["body"] if field["type"] != "markdown"]
        ids = [field["id"] for field in fields]
        require(len(ids) == len(set(ids)), f"Duplicate issue field ID: {name}")
        require(all(field["attributes"].get("label") for field in fields),
                f"Missing issue field label: {name}")
        require(all(field.get("validations", {}).get("required") is True for field in fields),
                f"Missing required issue fields: {name}")

    contacts = load_yaml(".github/ISSUE_TEMPLATE/config.yml")["contact_links"]
    require(any(item["url"] == "https://github.com/kredoxi/.github/security/advisories/new"
                for item in contacts), "Missing private vulnerability reporting route")
    dependabot = load_yaml(".github/dependabot.yml")
    require(dependabot["version"] == 2, "Invalid Dependabot version")
    require({update["package-ecosystem"] for update in dependabot["updates"]}
            == {"github-actions", "pip"}, "Dependabot must cover actual CI dependencies")
    selected = json.loads((ROOT / ".github/carl/packs.json").read_text(encoding="utf-8"))
    require(set(selected["selected"]) == EXPECTED_PACKS, "Unexpected selected cARL packs")


def validate_workflow() -> None:
    workflow = load_yaml(".github/workflows/governance.yml")
    # PyYAML's YAML 1.1 loader interprets the unquoted GitHub key "on" as True.
    triggers = workflow.get("on", workflow.get(True))
    require(set(triggers) == {"pull_request", "push", "workflow_dispatch"},
            "Unexpected or privileged workflow triggers")
    require(triggers["push"]["branches"] == ["main"], "Missing default-branch trigger")
    require(triggers["pull_request"] is None, "PR checks must not have path/type filters")
    require(workflow["permissions"] == {"contents": "read"}, "Workflow token must be read-only")
    require(set(workflow["jobs"]) == {"governance"}, "Unexpected governance jobs")
    job = workflow["jobs"]["governance"]
    require(job["name"] == "Governance validation", "Required check context changed")
    require("if" not in job and "permissions" not in job, "Required job must run read-only")
    require(job["runs-on"] == "ubuntu-24.04" and job["timeout-minutes"] <= 10,
            "Use a bounded disposable hosted runner")
    for step in job["steps"]:
        require("if" not in step and not step.get("continue-on-error"),
                "Required validation steps cannot silently skip or pass failures")
        if "uses" in step:
            require(re.fullmatch(r"actions/(checkout|setup-python)@[0-9a-f]{40}", step["uses"]),
                    "Actions must use reviewed full commit SHAs")
        require("secrets." not in json.dumps(step), "PR workflow must not reference secrets")
    checkout = next(step for step in job["steps"] if step.get("uses", "").startswith("actions/checkout@"))
    require(checkout["with"]["persist-credentials"] is False, "Checkout must not retain credentials")
    install = next(step for step in job["steps"] if step["name"] == "Install pinned cARL")
    require("d56eee02d6e008c42feb6b5a97ac86ea94599a0440d596bd3be015112d01c264"
            in install["run"] and "sha256sum --check" in install["run"],
            "cARL download must have a committed integrity check")


def validate_carl(executable: str) -> None:
    def run(*args: str) -> str:
        result = subprocess.run([executable, *args], cwd=ROOT, check=True,
                                capture_output=True, text=True, timeout=60)
        print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="")
        return result.stdout

    effective = json.loads(run("pack", "effective", "--json"))
    require({pack["id"] for pack in effective["packs"]} == EXPECTED_PACKS,
            "Effective cARL pack set differs from the contract")
    require(all(not pack.get("overriddenBy") for pack in effective["packs"]),
            "Project packs must be additive, not overridden")
    status = run("status")
    require(re.search(r"^Status:\s+Healthy\s*$", status, re.MULTILINE),
            "cARL artifacts are missing or drifted")
    run("trace")
    harness = run("harness", "status")
    require(re.search(r"copilot\s+.*present.*synced", harness, re.IGNORECASE),
            "Copilot harness is not present and synced")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--carl", help="Also validate using this cARL executable")
    args = parser.parse_args()
    validate_files()
    validate_workflow()
    if args.carl:
        validate_carl(args.carl)
    print("Governance contract validation passed.")


if __name__ == "__main__":
    main()
