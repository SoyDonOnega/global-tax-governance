"""Tests for the PostToolUse audit hook.

The plugin ships one hook — post_task.py — which deterministically
appends one record per Task invocation to the audit log. These tests
run it as a subprocess feeding JSON to stdin, exactly like Claude Code
invokes it in production.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POST = ROOT / "hooks" / "post_task.py"


def run_hook(
    script: Path, payload: dict, env: dict | None = None
) -> subprocess.CompletedProcess[str]:
    full_env = os.environ.copy()
    if env:
        full_env.update(env)
    return subprocess.run(
        [sys.executable, str(script)],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        timeout=10,
        cwd=str(ROOT),
        env=full_env,
    )


def _audit_size() -> int:
    p = ROOT / "orchestrate" / "audit" / "handoff-audit.jsonl"
    return p.stat().st_size if p.exists() else 0


def test_post_ignores_non_task():
    r = run_hook(POST, {"tool_name": "Read", "tool_input": {"file_path": "/x"}})
    assert r.returncode == 0, r.stderr


def test_post_logs_task_invocation():
    before = _audit_size()
    r = run_hook(POST, {
        "tool_name": "Task",
        "tool_input": {
            "subagent_type": "critic-citation-exactness",
            "prompt": "anything",
        },
        "tool_response": "produced a verdict",
    })
    assert r.returncode == 0, r.stderr
    assert _audit_size() > before, "audit log should have grown"


def test_post_logs_non_plugin_agents_too():
    """The audit log records every Task call, plugin agent or not.

    This is by design — the user can grep the log to inventory delegation
    patterns regardless of which subagent type was used.
    """
    before = _audit_size()
    r = run_hook(POST, {
        "tool_name": "Task",
        "tool_input": {
            "subagent_type": "general-purpose",
            "prompt": "anything",
        },
        "tool_response": "ok",
    })
    assert r.returncode == 0
    assert _audit_size() > before


def test_audit_log_rotates_at_threshold():
    audit = ROOT / "orchestrate" / "audit" / "handoff-audit.jsonl"
    audit.parent.mkdir(parents=True, exist_ok=True)
    if audit.exists():
        audit.unlink()
    for sibling in audit.parent.glob("handoff-audit.*.jsonl"):
        sibling.unlink()
    try:
        for _ in range(5):
            r = run_hook(
                POST,
                {
                    "tool_name": "Task",
                    "tool_input": {
                        "subagent_type": "critic-citation-exactness",
                        "prompt": "x" * 1000,
                    },
                    "tool_response": "y" * 1000,
                },
                env={"GTG_AUDIT_ROTATE_BYTES": "200"},
            )
            assert r.returncode == 0, r.stderr
        rotated = list(audit.parent.glob("handoff-audit.*.jsonl"))
        assert rotated, "expected at least one rotated archive"
        assert audit.exists(), "expected the active log to still exist"
    finally:
        for f in audit.parent.glob("handoff-audit*.jsonl"):
            f.unlink()


def main() -> int:
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    failed = []
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}")
        except AssertionError as e:
            failed.append((t.__name__, str(e)))
            print(f"  FAIL  {t.__name__}: {e}")
        except Exception as e:
            failed.append((t.__name__, f"{type(e).__name__}: {e}"))
            print(f"  ERROR {t.__name__}: {type(e).__name__}: {e}")
    print(f"\n{len(tests) - len(failed)}/{len(tests)} hook tests passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
