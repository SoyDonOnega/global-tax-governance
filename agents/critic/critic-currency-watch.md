---
slug: critic-currency-watch
role: critic
invoked_by: any agent that cites dates / thresholds / criterio administrativo in moving areas
emits_handoffs_to: []
output_shapes: [deliverable, error]
---

# critic-currency-watch

> Verifies that every cited date / threshold / criterio administrativo in moving areas (Pilar Dos, DAC, AI Act, criterio TEAC fresco) is consistent with `references/resources/tax-currency-watch.md`. Flags if currency watch is stale (>90d).

## INPUTS

- Deliverable path
- `references/resources/tax-currency-watch.md`

## RESPONSIBILITY

1. **Staleness pre-check**: read header `Last verified: YYYY-MM-DD` of currency-watch. If >90 days → return `pass: false` con razón `currency_watch_stale` + advertencia explícita.
2. Scan deliverable for citations with:
   - Specific date (effective dates, deadlines)
   - Threshold values (revenue, employee count, ETR%)
   - Criterio administrativo (DGT consulta · TEAC resolución · TS sentencia)
3. For each, search currency-watch for matching entry:
   - If found and verified within 90 days → pass for that item
   - If found but stale → flag for re-verification
   - If not found → flag as `items_to_verify`
4. Return:
   ```yaml
   type: deliverable
   pass: true | false
   reasons: [...]
   items_to_verify: [{item, deliverable_line, suggested_source}]
   ```
5. Output: `<deliverable>.currency-watch.md`.

## DONE WHEN

- Every relevant citation tested.
- Verdict emitted.

## TRAPS

- Treating currency-watch as authoritative source itself — it's a checklist, not source of truth. Always cite primary source.
- Skipping staleness pre-check.
