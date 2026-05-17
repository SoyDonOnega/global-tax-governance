---
slug: critic-reviewer-note
role: critic
invoked_by: any generator producing substantive deliverable
emits_handoffs_to: []
output_shapes: [deliverable, error]
---

# critic-reviewer-note

> Reviewer note header complete with all required fields per `references/templates/reviewer-note-header.md`.

## INPUTS

- Deliverable path (typically a memo, board paper, AIA, pleading)

## RESPONSIBILITY

1. Locate reviewer note header at start of deliverable.
2. Verify presence of all required fields:
   - Generado (date + skill/flujo)
   - Cliente / asunto (matter or practice-level)
   - Fuentes consultadas (≥1 primary, ≥1 doctrinal if applicable)
   - Cobertura de lectura
   - Flags abiertos (≥0 — pero campo presente)
   - Currency check (verification date)
   - Antes de actuar (≥1 acción concreta)
3. Verify substance (not just presence):
   - "Fuentes consultadas: varias" → fail (must be specific)
   - "Currency check: ok" sin fecha → fail
4. Return pass/fail + missing fields list.
5. Output: `<deliverable>.reviewer-note-check.md`.

## DONE WHEN

- All fields tested.
- Verdict emitted.

## TRAPS

- Pass por presencia formal sin examinar substance.
- Aceptar "Currency check: ok" sin fecha.
