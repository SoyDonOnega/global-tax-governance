# OUTPUT CONTRACT — applied by every critic

> Critics emit one of three output shapes. Skills delegating to a critic via the `Task` tool can rely on this contract being honoured.

---

## SHAPE 1 — VERDICT

The default output of a critic.

```yaml
type: verdict
critic: critic-citation-exactness | critic-currency-watch | critic-reviewer-note | critic-decision-tree | critic-finding-state | critic-cross-matter-leak
deliverable_path: <relative path under matters/<id>/findings/>
pass: true | false
issues:
  - line: <line ref or N/A>
    rule: <which rule failed>
    severity: blocker | high | medium | low
    fix: <concrete suggestion>
notes: |
  <short free-text justification — what was checked, what was found>
```

The calling skill consumes the verdict and either ships or iterates. A `blocker` issue in any verdict blocks close.

---

## SHAPE 2 — REQUEST CLARIFICATION

When the critic cannot apply its rule without additional information.

```json
{
  "type": "request_clarification",
  "question": "<specific question>",
  "blocking": true | false,
  "matter_id": "<active matter slug>"
}
```

The question is surfaced to the practitioner. The calling skill pauses if `blocking: true`.

---

## SHAPE 3 — ESCALATE

When the critic detects a condition that requires human review before publishing.

```json
{
  "type": "escalate_to_human",
  "reason": "<concrete reason>",
  "severity": "low | medium | high | critical",
  "deliverable_path": "<path>",
  "matter_id": "<active matter slug>"
}
```

Used when, for example, `critic-cross-matter-leak` finds a reference to another matter under `Cross-matter context: off`, or `critic-currency-watch` finds a stale citation in a moving area beyond the staleness threshold.

---

## NO FREE-FORM PROSE

Critics do NOT emit free-form prose. Every response fits one of the three shapes. This keeps the calling skill's parsing deterministic and the audit log defensible.
