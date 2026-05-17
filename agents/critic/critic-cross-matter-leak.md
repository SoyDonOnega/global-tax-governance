---
slug: critic-cross-matter-leak
role: critic
invoked_by: pre-close of any deliverable when active matter exists
emits_handoffs_to: [escalate_to_human]
output_shapes: [deliverable, error]
---

# critic-cross-matter-leak

> When `Cross-matter context: off` in CLAUDE.md (default), verifies no deliverable leaks data from matters other than the active one. Privilege protection.

## INPUTS

- Deliverable path
- `CLAUDE.md` con flag `Cross-matter context: on/off`
- Active matter id (from `.active-matter` file)

## RESPONSIBILITY

1. Read flag. If `on` → pass trivially (intentional cross-matter context).
2. If `off`:
   - Scan deliverable for matter ids other than active
   - Scan for client names from other matters (load `matters/_index.yaml` if exists)
   - Scan for entity names known to be in other matters
3. Any leak → fail with explicit `leak_items[]` + emit `escalate_to_human` con severity `high`.

## DONE WHEN

- Verdict emitted.

## TRAPS

- False positives: name overlap (Acme Corp en dos matters distintos) → flag pero permite override.
- Skipping when flag is unset (treat unset as `off`).
