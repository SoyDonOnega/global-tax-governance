---
name: customize
description: >
  Surgical edit of the global-tax-governance practice profile — change ONE slot
  (risk posture · active areas · escalation · house style · footprint · integrations
  · matters path) without re-running the full onboarding interview. Shows current
  value, proposes new, explains downstream impacts, logs the change. Use when the
  user says "update my tax profile", "change my risk posture", "add a jurisdiction",
  "update my escalation chain", "modify the house style", "edit my plugin config",
  "customize the plugin".
---

# /global-tax-governance:customize

> Surgical edit of the plugin `CLAUDE.md`. One slot at a time. With downstream impact analysis.

## EDITABLE SLOTS

| Slot | What it changes |
|---|---|
| `risk-posture` | Appetite · red lines · hedging level |
| `active-areas` | Toggle P2 · DAC · TP · CBPT · AI Act · transparency · etc. |
| `escalation` | Approver × threshold × trigger matrix |
| `house-style` | Tone · structure · cite format · language · signature |
| `footprint` | Primary and secondary jurisdictions |
| `integrations` | Connected MCPs (re-probe with `--check-integrations`) |
| `matters-path` | Matters folder path |
| `cross-matter-context` | Flag on/off (default off) |
| `confirm-routing` | Auto-proceed or ask for confirmation |

## FLOW

1. Verify `CLAUDE.md` exists and has no critical `[PLACEHOLDER]`. If it does → redirect to `onboarding`.
2. Ask which slot (AskUserQuestion).
3. Show the current value of the slot, with citations to `CLAUDE.md`.
4. Ask for the new value (free text or multi-select).
5. **Compute downstream impacts**:
   - "escalation threshold 5M€ → 10M€: `audit-defense` no longer auto-escalates exposure < 10M€"
   - "active-areas remove `tcf`: 4 open matters carry a TCF workstream — confirm action"
   - "risk-posture aggressive: inconsistent with 'everything requires partner approval' in escalation"
6. Diff before / after.
7. Confirm.
8. Apply change and append to `## CUSTOMIZATION LOG` with date, slot, old value, new value, rationale.

## RULES

- **One slot per session** unless the user explicitly asks for multi-slot.
- **Never delete a section** — set `[Not configured]` with explanation.
- **Detect internal inconsistencies** and flag before applying.
- **Shared `company-profile`** (`references/templates/company-profile.md`): changes affect any plugin sharing that profile — warn.

## CLOSE

Decision tree:
- A — Apply the change and continue
- B — Review another slot
- C — Re-run `onboarding --redo --area <X>` for partial re-interview
- D — Cancel the change
- E — Other

If the inconsistency is severe, emit `escalate_to_human` (wait for human review before applying).
