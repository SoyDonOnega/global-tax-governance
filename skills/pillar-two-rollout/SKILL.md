---
name: pillar-two-rollout
description: >
  Full multi-jurisdictional Pillar Two / GloBE rollout (IIR · UTPR · QDMTT ·
  safe harbours · GIR · top-up tax computation and consolidation) for multinational
  groups. Identifies strategic impact (holdings without post-P2 rationale, optional
  restructuring) alongside the technical calc. Multi-phase, multi-entity,
  multi-fiscal-year. Use when the user says "Pillar Two rollout", "GloBE
  assessment", "Pillar Two implementation", "P2 top-up", "QDMTT analysis", "safe
  harbour test", "GIR preparation", "P2 holding restructuring".
---

# /global-tax-governance:pillar-two-rollout

> Multi-phase Pillar Two rollout. Self-contained recipe — the skill plans, computes and reviews internally; the six transversal critics are invoked at close.

## SUBCOMMANDS

| Command | Action |
|---|---|
| `scope` | Define entity table + jurisdictions in scope; emit a per-jurisdiction worklist into `matters/<id>/findings/pillar-two/scope.yaml`. |
| `run-jurisdiction <iso>` | Execute one jurisdiction: per-entity GloBE adjustments, QDMTT / IIR / UTPR computation, safe-harbour tests. |
| `consolidate` | Aggregate top-up across all jurisdictions in `consolidated-<fy>.yaml`. |
| `safe-harbour-test` | Standalone CbCR transitional + QDMTT eligibility test. |
| `gir-prep` | Build the GloBE Information Return payload. |
| `strategy-impact` | Identify holdings without post-P2 rationale; surface restructuring options. |

## FLOW

1. **Scope** — load the matter's entity table; classify by jurisdiction and tier (UPE · IPE · POPE · constituent entity); list the fiscal years in scope and the data dependencies (consolidated FS, statutory FS per entity, CbCR, tax provision detail).
2. **Per jurisdiction**:
   - Apply the local transposition (verify against `references/jurisdictions/<iso>.md` and the currency watch).
   - Compute GloBE Income / Loss and Covered Taxes per entity; reconcile to deferred tax accounting.
   - Test safe harbours in order: CbCR transitional (three tests with exact CbCR figures) → QDMTT (only if qualified).
   - Compute Top-up Tax and allocate IIR / UTPR / QDMTT charges.
3. **Consolidate** — aggregate top-up; reconcile to the group's effective tax rate; identify outliers.
4. **Adversarial pass** — challenge the consolidated figure: assumed entity classifications, tested ratios, CFC interaction (e.g. Spanish Art. 100 LIS · US GILTI · ATAD2 CFC), JV / investment entity / stateless income corners.
5. **Strategy angle** — if consolidated top-up > matter materiality threshold: list holdings with low SBIE and high top-up exposure; sketch restructuring options with cash-tax / ETR / complexity / regulatory trade-offs.
6. **Critic pass** — invoke (via `Task` to `critic-<name>`):
   - `critic-citation-exactness` over every cited norm, OECD guidance, jurisprudence and admin criterion.
   - `critic-currency-watch` over every cited date, threshold and transposition status.
   - `critic-reviewer-note` over the final memo header.
   - `critic-decision-tree` over the close.
7. **Close** — escalate via the close decision tree.

## COVERAGE

- P2 (core): IIR · UTPR · QDMTT · safe harbours · GIR · SBIE
- IT (partial): UTPR–CDI conflicts (acknowledge minority but relevant doctrinal critique re: customary international law where applicable)
- Corp Tax (partial): covered taxes consistent with deferred tax accounting
- Strategy (★): identify low-substance holdings without post-P2 rationale

## TRAPS

- Applying CbCR transitional safe harbour without passing the three real tests (Routine Profits + De Minimis + Simplified ETR) using exact CbCR figures.
- Assuming QDMTT safe harbour without verifying "qualified" status — only qualified QDMTT reduces top-up to zero.
- Confusing IIR/UTPR ordering — UTPR is backstop, not primary.
- Ignoring interaction with CFC rules (Spanish Art. 100 LIS, US GILTI, ATAD2 CFC) — risk of double inclusion.
- Not modelling deferred tax under P2 — GloBE adjustments hit deferred tax accounting.
- Stock-based comp timing differs in P2 vs. tax accounting.
- Joint ventures · investment entities · stateless income · transition rules not treated explicitly.

## STRATEGY ANGLE (mandatory in the consolidated output)

If consolidated top-up exceeds the matter's materiality threshold:
- Identify holdings with low SBIE and high top-up exposure.
- Options: operational consolidation · re-domicile · upstream merger · liquidation.
- Trade-offs: cash tax · ETR · complexity · regulatory risk · exit timing.
- Surface the option set with trade-offs; the close decision tree lets the practitioner pick whether to convert the option set into a steps memo or escalate to partner first.

## FUNCTION LENS

- **Controller**: consumes per-entity calcs for provision.
- **CFO**: consumes consolidated figure + cash tax impact.
- **Audit committee**: executive summary + safe harbour eligibility status.
- **Treasury**: cash tax timing per jurisdiction.
- **External auditor**: full trail for the GloBE provision audit.

## DELIVERABLES

- `matters/<id>/findings/pillar-two/calc-<entity>-<fy>.yaml` × N
- `matters/<id>/findings/pillar-two/jurisdictional-<iso>-<fy>.md` × jurisdiction
- `matters/<id>/findings/pillar-two/consolidated-<fy>.yaml`
- `matters/<id>/findings/pillar-two/gir-prep-<fy>.yaml`
- `matters/<id>/findings/pillar-two/strategy-impact-<fy>.md` (if materiality)
- Reviewer note headers on each

## CLOSE

- A — Draft formal memo to CFO with consolidated figure + strategy impact
- B — Escalate to responsible partner + client's tax director
- C — Request refreshed TP study / CbCR / consolidated statements
- D — Monitor OECD Administrative Guidance + pending national transpositions
- E — Other
