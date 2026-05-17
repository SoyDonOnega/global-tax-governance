---
slug: critic-decision-tree
role: critic
invoked_by: skill:memo-draft
emits_handoffs_to: []
output_shapes: [deliverable, error]
---

# critic-decision-tree

> Decision tree at memo close exists with ≥3 concrete, actionable branches. No generic placeholders.

## INPUTS

- Deliverable path (memo)

## RESPONSIBILITY

1. Locate decision tree section at end of memo.
2. Count branches.
3. Verify each branch is:
   - **Concrete**: not "review further" but "redactar memo formal a board"
   - **Actionable**: clear who does what
   - **Distinct**: not redundant with another branch
4. Verify ≥3 branches (typical: redactar · escalar · más hechos · monitorizar · otro — but variants per output type).
5. Return pass/fail.

## DONE WHEN

- Verdict emitted.

## TRAPS

- Aceptar "review further" como branch concreto.
- Pass con 2 branches.
- Aceptar branches redundantes.
