---
name: excel-replicate
description: >
  Replicates a recurring tax Excel from the prior period preserving format +
  formulas + named ranges + data validations + pivots/charts. Updates only
  inputs with the new period's source data. Reconciliation sheet with deltas.
  Automatic QC. Covers IS, VAT, withholding, modelo 232, accounting-tax
  reconciliations, ETR, GloBE worksheet, CbCR data prep. Use when the user
  says "replicate prior-period Excel", "update calc with new period support",
  "same format new data", "Excel rollforward", "period roll".
---

# /global-tax-governance:excel-replicate

> Coverage: ★ Corp Tax (IS/VAT/withholding) · ★ P2 (GloBE worksheet) · ◐ TP · ◐ TCF.

## SUBCOMMANDS

| Command | Action |
|---|---|
| `template <path>` | Define the "gold" file |
| `period <YYYY-Q>` | Run replication for new period |
| `reuse-mapping <path>` | Re-use prior-period mapping (skip detection) |

## FLOW (6 phases, self-contained)

1. **Analysis of the gold file** — enumerate sheets, named ranges, formulas, input regions; identify the period-stamped sheet name(s) and any pivots/charts that depend on input dimensions.
2. **Input-region detection** — apply the yellow-fill convention; recognise sheets named `Inputs` / `Datos` / `Soporte` / `Raw`; recognise ListObjects (Excel tables).
3. **Map new support → inputs** — three modes: (a) same-structure (file mirrors the gold input region), (b) ERP export (column mapping + aggregation), (c) individual values (the user provides cell-by-cell). If ambiguous, ask.
4. **Build the new file** — copy the gold workbook, clear input cells only, write the new inputs; never touch a formula cell, never overwrite a name.
5. **Reconciliation sheet** — append `_Reconciliacion_<period>` with line-level deltas vs. the prior period and a totals tie-out.
6. **QC** — formula count match across sheets, named range integrity, type checks (no text in numeric inputs), no formula written.
7. **Currency check on the logic** — if the regulation, threshold or rate behind the gold model has moved since it was built (Pillar Two safe-harbour, IS rate, retentions table, etc.), warn before delivering. Verify against `references/resources/tax-currency-watch.md` and the active jurisdiction profile.
8. **Critic pass** — `critic-citation-exactness` (if the model carries citations in notes), `critic-currency-watch`, `critic-reviewer-note`, `critic-decision-tree`.
9. **Close** — deliverable file in the active matter + reviewer note per close decision tree.

## HARD RULES

- **NEVER write over a formula cell.**
- **NEVER infer a missing value** — ask the user.
- **Currency check on the logic**: if regulation changed since the gold file, warn.
- Output to the active matter, **never** to general Outputs.
- `_<period>` suffix mandatory.

## TRAPS

- Touching a gold formula.
- Pivots/charts misaligned by input dimensional change.
- .xlsm with macros: openpyxl does not preserve VBA 100%.
- Conditional formatting with absolute ranges: extend manually.

## DELIVERABLES
- `matters/<id>/findings/excel-replicate/<name>_<period>.xlsx`
- `matters/<id>/findings/excel-replicate/_reconciliation.md`
- `matters/<id>/findings/excel-replicate/_input-mapping.yaml`
- `matters/<id>/findings/excel-replicate/_qc-report.md`

## CLOSE
- A — Send to recipient (controller, CFO, AEAT)
- B — Iterate if QC revealed inconsistencies
- C — Request clarification via `query-email` if grey areas in the support
- D — Retemplate (if the tax logic changed, the gold file must be redone)
- E — Other
