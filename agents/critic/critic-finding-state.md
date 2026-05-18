---
slug: critic-finding-state
role: critic
invoked_by: any agent producing findings (tabular review, evaluation, AIA)
emits_handoffs_to: []
output_shapes: [deliverable, error]
---

# critic-finding-state

> Every finding labelled with one of the 4 states: `answered` · `not_present` · `unclear` · `needs_review`. No blanks. No invented states.

## INPUTS

- Deliverable path (tabular review · evaluation · AIA · etc.)

## RESPONSIBILITY

1. Walk deliverable, identify every finding / cell / claim.
2. Verify each has a state attached.
3. Reject blanks (empty cells) and invented states (`tbd`, `pending`, `ok`).
4. Return pass/fail + list of bad findings.

## DONE WHEN

- Every finding tested.
- Verdict emitted.

## TRAPS

- Treating `[DEFAULT]` (a placeholder semántico) as a finding state — they're distinct concepts.
