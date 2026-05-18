---
name: tcf-program
description: >
  Multi-phase Tax Control Framework program (audit as-is → design → implementation
  → monitoring) against OECD FTA · Netherlands Horizontal Monitoring · HMRC
  SAO/CCO · Spanish CBPT (Cooperative Compliance Code). Not pure compliance —
  designs the tax function around the TCF as a lever for cooperative relationship,
  reduced inspection probability and D&O premium reduction. Use when the user
  says "TCF review", "audit TCF", "evaluate the TCF", "TCF maturity", "horizontal
  monitoring", "CBPT readiness", "cooperative compliance", "tax assurance program".
---

# /global-tax-governance:tcf-program

> Flagship workflow W2. Multi-quarter. TCF as the controls layer of the tax function.

## SUBCOMMANDS

| Command | Action |
|---|---|
| `assess` | Phase 1 — As-is mapping of the tax function and controls |
| `design` | Phase 2 — Control design per gap |
| `roadmap` | Phase 3 — Implementation with quarterly sprints |
| `status` | Current maturity scorecard + open gaps |
| `cbpt-readiness` | Readiness test for AEAT CBPT adhesion |

## FLOW (4 phases, self-contained)

1. **Phase 1 — As-is** — read every supplied TCF document (policy, manual, control inventory, prior maturity scorecards). Build the entity table and the consolidated financial scope. Map controls against `references/criteria/tcf.criteria.yaml` and produce a baseline maturity scorecard against the chosen reference (OECD FTA · NL HM · HMRC SAO/CCO · local cooperative-compliance code).
2. **Phase 2 — Design** — for each gap: define the control (purpose · trigger · owner · frequency · evidence · escalation). Group controls by risk domain (governance, identification, monitoring, reporting). Run `critic-reviewer-note` on each control card.
3. **Phase 3 — Implementation roadmap** — sequence the controls in quarterly waves with explicit owners and acceptance criteria. Identify dependencies (ERP changes, training, tooling). Output `roadmap.md`.
4. **Phase 4 — Monitoring** — for each quarter: status of each control (designed · in implementation · operating · audited), updated maturity scorecard, list of new gaps detected. If adhesion to a cooperative-compliance regime is targeted, run a readiness gate against the regime's eligibility checklist.
5. **Critic pass at close** — `critic-citation-exactness` over the regime references, `critic-currency-watch` over the regime's current criteria, `critic-reviewer-note` over the consolidated deliverable, `critic-decision-tree`.

## COVERAGE

- Function (★): core
- Strategy (★): TCF as a lever (cooperative relationship, D&O premium reduction, pre-IPO readiness)
- Corp Tax (partial): operating controls
- ESG (partial): TCF feeds into GRI 207 disclosure 207-2

## STRATEGY ANGLE (mandatory)

TCF is not compliance, it's a **lever**:
- CBPT adhesion opens cooperative relationship with AEAT (fewer random audits, greater predictability).
- A mature TCF with external attestation reduces D&O premium.
- A structured TCF eases pre-IPO readiness (controlling-level disclosure).
- A framework applied against the client's sector / scale → overengineering. Target maturity must be realistic.

## FUNCTION LENS

- **Tax director**: ultimate TCF owner.
- **Audit committee**: independent reviewer.
- **CFO**: budget and priorities.
- **CRO** (if extant): integrates TCF into enterprise risk management.

## TRAPS

- OECD FTA applied to a mid-size client without international presence.
- CBPT proposed to a client under active AEAT investigation → `escalate_to_human`.
- Generic risk matrix without sector adaptation.
- "Paper controls" without a testable evidence pattern.
- Three lines of defence misallocated.
- Listed SOX-403 client vs. private without SOX — different frameworks.

## DELIVERABLES

- `matters/<id>/findings/tcf/tcf-as-is.yaml`
- `matters/<id>/findings/tcf/maturity-scorecard.yaml`
- `matters/<id>/findings/tcf/control-<id>.md` × N
- `matters/<id>/findings/tcf/tcf-roadmap.md`
- `matters/<id>/findings/tcf/cbpt-readiness.md` (if adhesion)

## CLOSE

- A — Draft paper to audit committee with maturity baseline + roadmap
- B — Escalate to partner if material gaps require a tax-function redesign beyond the controls layer
- C — Request additional documentation (existing policies, manuals, control operating evidence)
- D — Monitor OECD FTA + AEAT CBPT annual updates
- E — Other
