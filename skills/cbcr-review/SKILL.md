---
name: cbcr-review
description: >
  Review of non-public CbCR (BEPS Action 13) and public CbCR (EU Directive
  2021/2101 · Australian stricter regime). Reconciliation with consolidated
  statements, consistency with master / local file, GRI 207, reputational risk
  assessment for the public version. Use when the user says "CbCR review",
  "public CbCR", "Directive 2021/2101", "country-by-country", "GRI 207".
---

# /global-tax-governance:cbcr-review

> Coverage: ★ TP · ★ ESG/disclosure · ◐ P2 (safe harbour consistency) · ◐ IT.

## SUBCOMMANDS

| Command | Action |
|---|---|
| `map` | Build Tables 1/2/3 from financial data |
| `reconcile` | Reconciliation with consolidated statements |
| `validate` | Pre-submission validation (modelo 231 if AEAT) |
| `public-prep` | Public CbCR preparation with voluntary narrative |
| `gri-207` | GRI 207-1 through 207-4 disclosures |

## FLOW

1. **Extract** — pull financial data per constituent entity from the consolidation package (revenue, profit before tax, current tax paid, current tax accrued, stated capital, accumulated earnings, employees, tangible assets, related-party vs. unrelated-party revenue split).
2. **Normalise** — map every entity to an ISO 3166-1 alpha-2 code; convert all amounts to the group's reporting currency at the right rate (period-average vs. closing per the table).
3. **Build Tables 1, 2, 3** — Table 1 (income, taxes, business activities per jurisdiction); Table 2 (list of constituent entities per jurisdiction); Table 3 (additional information narrative).
4. **Schema check** — every table cell typed and reconciled to source. Total revenue reconciles to consolidated revenue; total current tax reconciles to the P&L tax line. Flag any unexplained delta.
5. **Disclosure-risk pass (if public CbCR)** — reputational (low-ETR jurisdictions without visible substance · jurisdictions with adverse press coverage), regulatory (Directive 2021/2101 scope · transposition status), competitive (segment disclosure risk). Build the additional-information narrative addressing each flagged item with neutral, accurate framing.
6. **Critic pass** — `critic-citation-exactness` over the regulatory citations, `critic-currency-watch` over the directive transposition status per jurisdiction, `critic-reviewer-note`, `critic-decision-tree`.
7. **Close** — internal CbCR + (if public) the disclosure narrative + recommendation per close decision tree.

## STRATEGY ANGLE

Public CbCR is **reputational footprint**. A coherent narrative protects; a raw figure without context becomes a headline. The decision on voluntary narrative is strategic — it creates precedent for future periods.

## TRAPS

- Total CbCR revenue vs. consolidated without reconciliation.
- Jurisdictions with ETR < 12% without visible substance → flag.
- Pillar Two safe harbour based on this CbCR — figures must be consistent.
- FTE vs. headcount confused.

## DELIVERABLES
- `matters/<id>/findings/cbcr/cbcr-map.xlsx`
- `matters/<id>/findings/cbcr/cbcr-narrative.md`
- `matters/<id>/findings/cbcr/gri-207-disclosure.md` (if elected)

## CLOSE
- A — Submit to regulator (modelo 231 or equivalent)
- B — Escalate to IR + sustainability + comms if public
- C — Refresh data if reconciliation fails
- D — Monitor AU CbCR + future disclosure standards
- E — Other
