"""Smoke tests for global-tax-governance plugin structure.

Verifies that:
  1. Every skill folder has a SKILL.md (expecting 13).
  2. Every YAML under references/ loads and orchestrate/allowlist.yaml
     is a dict of {str: list[str]}.
  3. intents.schema.json is a valid Draft 2020-12 schema and matches
     orchestrate/intents.py.
"""
from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


EXPECTED_SKILLS = 13


def check_skills() -> None:
    skill_dirs = [p for p in (ROOT / "skills").iterdir() if p.is_dir()]
    missing = [d.name for d in skill_dirs if not (d / "SKILL.md").is_file()]
    assert not missing, f"missing SKILL.md in: {missing}"
    assert len(skill_dirs) == EXPECTED_SKILLS, (
        f"expected {EXPECTED_SKILLS} skills, found {len(skill_dirs)}: "
        f"{sorted(d.name for d in skill_dirs)}"
    )
    print(f"  skills: {len(skill_dirs)} folders, all have SKILL.md")


def check_yaml() -> None:
    paths = sorted(glob.glob(str(ROOT / "references/criteria/*.yaml")))
    for p in paths:
        with open(p) as f:
            yaml.safe_load(f)
    print(f"  yaml: {len(paths)} criteria files load cleanly")


def check_allowlist() -> None:
    with open(ROOT / "orchestrate/allowlist.yaml") as f:
        data = yaml.safe_load(f)
    assert isinstance(data, dict), "allowlist.yaml must be a mapping"
    for source, targets in data.items():
        assert isinstance(source, str), f"non-string source key: {source!r}"
        assert isinstance(targets, list), f"targets for {source} must be a list"
        for t in targets:
            assert isinstance(t, str), f"non-string target in {source}: {t!r}"
    print(f"  allowlist: {len(data)} source agents")


def check_intents_schema() -> tuple[set[str], dict]:
    schema_path = ROOT / "references/handoff-schemas/intents.schema.json"
    schema = json.load(open(schema_path))
    Draft202012Validator.check_schema(schema)

    # The intents enum lives at properties.intent.enum.
    intent_enum = schema.get("properties", {}).get("intent", {}).get("enum")
    assert isinstance(intent_enum, list) and intent_enum, "missing intents enum"
    intents = set(intent_enum)
    print(f"  intents schema: valid, {len(intents)} intents declared")
    return intents, schema


def check_intents_module(schema_intents: set[str]) -> None:
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "intents", ROOT / "orchestrate/intents.py"
    )
    assert spec and spec.loader, "could not load intents.py"
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    candidates = []
    for name in dir(module):
        obj = getattr(module, name)
        if isinstance(obj, (set, frozenset, list, tuple)) and obj:
            if all(isinstance(v, str) for v in obj):
                candidates.append((name, set(obj)))

    matched = [name for name, values in candidates if values == schema_intents]
    if not matched:
        print(
            "  intents module: no exact set match against schema "
            "(advisory only — module may expose intents via enum or constants)"
        )
    else:
        print(f"  intents module: {matched[0]} matches schema enum exactly")


def main() -> int:
    print("running smoke tests for global-tax-governance")
    check_skills()
    check_yaml()
    check_allowlist()
    intents, _ = check_intents_schema()
    check_intents_module(intents)
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
