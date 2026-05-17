"""Shared utilities for the PostToolUse hook on the Task tool.

Tiny surface: read hook input from stdin, infer the calling agent,
hash strings for the audit log, rotate the log when it crosses a
size threshold, append a record, and exit cleanly. The hook
(`post_task.py`) wires these together; this module is intentionally
small so the hook itself stays under one screenful.
"""
from __future__ import annotations

import hashlib
import json
import os
import pathlib
import sys
from typing import Any

PLUGIN_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PLUGIN_ROOT / "orchestrate"))

ORCHESTRATE_OK = True
try:
    import orchestrate as _orch  # type: ignore
except Exception as e:  # pragma: no cover
    ORCHESTRATE_OK = False
    _ORCH_IMPORT_ERROR = str(e)


def read_hook_input() -> dict[str, Any]:
    try:
        return json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        return {}


def is_task_tool(payload: dict) -> bool:
    return payload.get("tool_name") == "Task"


def is_plugin_agent(subagent_type: str) -> bool:
    if not ORCHESTRATE_OK:
        return False
    return subagent_type in _orch.ALLOWED_TARGETS


def infer_source_agent(payload: dict) -> str:
    for key in ("agent_id", "subagent_id", "calling_agent", "agent"):
        v = payload.get(key)
        if isinstance(v, str) and v:
            return v
    return "main"


def audit_path() -> pathlib.Path:
    return PLUGIN_ROOT / "orchestrate" / "audit" / "handoff-audit.jsonl"


AUDIT_ROTATE_BYTES = int(os.environ.get("GTG_AUDIT_ROTATE_BYTES", str(5 * 1024 * 1024)))


def _maybe_rotate(p: pathlib.Path) -> None:
    """Rename the active log to a timestamped sibling once it exceeds the
    threshold, then start a fresh file. No-op if the file is still small."""
    try:
        size = p.stat().st_size
    except FileNotFoundError:
        return
    if size < AUDIT_ROTATE_BYTES:
        return
    import datetime as _dt
    stamp = _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rotated = p.with_name(f"handoff-audit.{stamp}.jsonl")
    try:
        p.rename(rotated)
    except OSError:
        pass


def append_audit(record: dict) -> None:
    p = audit_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    _maybe_rotate(p)
    import datetime as _dt
    record = {**record, "ts": _dt.datetime.now(_dt.timezone.utc).isoformat()}
    with open(p, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def hash_text(text: str) -> str:
    return hashlib.sha256((text or "").encode("utf-8")).hexdigest()[:16]


def emit_passthrough() -> None:
    sys.exit(0)
