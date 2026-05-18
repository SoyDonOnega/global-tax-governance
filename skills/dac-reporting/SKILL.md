---
name: dac-reporting
description: >
  Triage and reporting preparation under DAC6 (intermediary hallmarks) · DAC7
  (digital platforms) · DAC8 (crypto-assets). Identifies reportable arrangement,
  reporter, deadline. Use when the user says "DAC6", "DAC7", "DAC8", "hallmark",
  "reportable arrangement", "tax intermediary", "DAC7 platform", "DAC8 crypto",
  "tax professional secrecy".
---

# /global-tax-governance:dac-reporting

> Coverage: ★ IT · ★ Tax Advice.

## SUBCOMMANDS

| Command | Action |
|---|---|
| `triage <directive>` | Applicability test |
| `prepare-payload` | Structured payload (modelo 234 / 235 / 238) |
| `file-checklist` | Pre-submission checklist |
| `marketable-quarterly-update` | Quarterly update for marketable arrangements |

## FLOW

1. **Triage** — identify the applicable directive (DAC6 / DAC7 / DAC8) and the current local transposition status; verify against `references/jurisdictions/<iso>.md` and the currency watch.
2. **Hallmark / category mapping** — for DAC6: list the hallmarks triggered (Category A–E) with the main-benefit test where required; for DAC7: platform-operator categories of in-scope sellers; for DAC8: crypto-asset reporter and reportable users.
3. **Reporter identification** — primary intermediary vs. secondary intermediary vs. taxpayer reporting. Verify tax professional secrecy (e.g. Art. 45 LGT for Spanish abogados) — it does not cover non-lawyer advisors.
4. **Deadline** — 30 days from the relevant trigger; quarterly updates for marketable arrangements; periodic platform-operator reporting.
5. **Payload draft** — build the report payload per the local form / XML schema; populate identifiers, arrangement summary, value, taxpayers, hallmark codes.
6. **Critic pass** — `critic-citation-exactness`, `critic-currency-watch` (DAC8 transpositions are still moving), `critic-reviewer-note`, `critic-decision-tree`.
7. **Close** — submission package + escalation per close decision tree.

## STRATEGY ANGLE

Triage early — the decision is binary but the cost is asymmetric (sanction vs. loss of privilege). Spanish tax professional secrecy (Art. 45 LGT) **only covers lawyers** — verify the intermediary's exact role.

## TRAPS

- Hallmark forced by risk aversion.
- Cross-border arrangement reported in wrong EU MS → double sanction.
- DAC8 Spanish transposition still evolving → currency check.

## DELIVERABLES
- `matters/<id>/findings/dac/triage.md`
- `matters/<id>/findings/dac/payload.json`
- `matters/<id>/findings/dac/filing-checklist.md`

## CLOSE
- A — Submit modelo 234/235/238 on time
- B — Escalate if intermediary status disputed
- C — Request additional certificates / VAT-IDs
- D — Monitor DAC8 transposition
- E — Other
