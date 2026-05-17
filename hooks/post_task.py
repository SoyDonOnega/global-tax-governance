#!/usr/bin/env python3
"""PostToolUse hook on the Task tool.

Logs every Task invocation (regardless of whether a handoff block was used)
to orchestrate/audit/handoff-audit.jsonl. Metadata only — never the prompt
body or the subagent's response. Hashes serve as integrity references.

Hook input shape includes the tool result (truncated):

    {
      "tool_name": "Task",
      "tool_input": {...},
      "tool_response": {...} | "...",
      ...session metadata...
    }
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import handoff_lib as H


def main() -> int:
    payload = H.read_hook_input()
    if not H.is_task_tool(payload):
        H.emit_passthrough()

    tool_input = payload.get("tool_input") or {}
    response = payload.get("tool_response")
    response_str = response if isinstance(response, str) else json.dumps(response or {}, ensure_ascii=False)

    H.append_audit({
        "event": "post_task",
        "target": tool_input.get("subagent_type"),
        "source": H.infer_source_agent(payload),
        "is_plugin_agent": H.is_plugin_agent(tool_input.get("subagent_type") or ""),
        "prompt_hash": H.hash_text(tool_input.get("prompt") or ""),
        "response_hash": H.hash_text(response_str),
        "response_chars": len(response_str),
        "ok": True,
        "reason": "logged",
    })

    H.emit_passthrough()
    return 0


if __name__ == "__main__":
    sys.exit(main())
