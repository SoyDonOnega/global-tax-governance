---
name: ai-tax-governance
description: >
  AI Impact Assessment for AI systems in the tax function (corporate AI use ·
  AEAT risk-selector defense). Two lenses — (a) corporate governance: provider/
  deployer obligations under AI Act + conformity assessment readiness · (b)
  taxpayer defense against AI-driven inspection: Art. 22 GDPR + Art. 34 LGT +
  reinforced motivation Art. 102 LGT + Mosquera Intertax 53(11) 2025 doctrine.
  Use when the user says "tax AIA", "AI Act tax function", "AEAT selector",
  "AI tax tool review", "Art 22 GDPR audit", "AI high-risk tax".
---

# /global-tax-governance:ai-tax-governance

> Flagship workflow W3. Coverage: ★ Tax Advice · ★ Function · ★ Strategy · ★ IT (AI Act).

## SUBCOMMANDS

| Command | Action |
|---|---|
| `inventory` | Inventory of AI systems in the tax function |
| `aia <system>` | Full AIA for one system |
| `governance-design` | Internal governance design (policy, AI committee, responsibility matrix) |
| `aeat-selector-analysis` | Defensive analysis of AEAT algorithmic selection |

## FLOW

1. **Inventory** — list every AI system in or adjacent to the tax function (selector, OCR, NLP, predictive provision, RPA + LLM, vendor tools). For each: provider · deployer · function · data class.
2. **Classify per AI Act** — assign each system to a tier (prohibited · high-risk · limited · minimal · GPAI · GPAI+systemic). Map Annex III categories explicitly. Tag GDPR Art. 22 implications.
3. **AIA per system** — for high-risk or GPAI: data sources, training boundaries, accuracy / bias / robustness assessment, human oversight design, transparency obligations, conformity assessment path. Cite `references/criteria/aia.criteria.yaml` for the required structure.
4. **Governance design** — internal AI policy commitments, AI committee composition, responsibility matrix (tax director · DPO · CIO · GC). Cross-check against the practice profile and any AI policy already in force.
5. **AEAT selector defense (if applicable)** — analyse algorithmic selection against motivation duty (Art. 102 LGT), prueba electrónica, automated decision (GDPR Art. 22) and Annex III.5 of the AI Act. Identify defensible points.
6. **Critic pass** — `critic-citation-exactness`, `critic-currency-watch` (AI Act milestones move fast), `critic-reviewer-note`, `critic-decision-tree`.
7. **Close** — board paper or memo per the close decision tree.

## AI ACT CLASSIFICATION (testable)

- **Prohibited (Art. 5)**: social scoring · workplace emotion inference · sensitive biometric categorisation
- **High-risk (Annex III, especially III.5)**: AEAT selector directing inspection → falls under Annex III.5
- **GPAI (Art. 50)**: general LLMs with disclosure obligations
- **Limited / minimal**: must be justified

## ART. 22 GDPR ANALYSIS

- Exclusively automated decision with legal effects?
- Exception Art. 22.2.b? (authorised by EU/national law with safeguards)
- Minimum safeguards: qualified human intervention · right to express viewpoint · right to contest

## TAXPAYER RIGHTS (LGT)

- Art. 34: information about algorithmic selection
- Art. 102: motivation of tax assessments explaining the system's role
- Reversal of burden of proof → flag
- Equality (Art. 14 + 31.3 Spanish Constitution)

## STRATEGY ANGLE

Two radically different lenses:
- **Corporate AI**: provider obligations + deployer obligations + liability against the vendor + conformity assessment readiness.
- **AEAT selector (taxpayer defense)**: defensive argument in audit — reinforced motivation Art. 102 + Art. 22 GDPR + Mosquera doctrine + foreseeable relevance (Berlioz C-682/15).

## FUNCTION LENS

- **DPO**: Art. 22 GDPR + DPIA
- **CIO / CTO**: tech stack + vendor management
- **Tax director**: integration with the tax function
- **AI / ethics committee**: governance
- **GC**: liability

## TRAPS

- Tier classification without literal Annex III test.
- Presuming limited risk where it's high-risk.
- Conflating provider / deployer obligations.
- Ignoring GPAI when a general LLM is used.
- AEAT selector: Spanish doctrine virtually non-existent — flag normative uncertainty.

## DELIVERABLES
- `matters/<id>/findings/aia/ai-inventory.yaml`
- `matters/<id>/findings/aia/aia-<system>.md` × N
- `matters/<id>/findings/aia/governance-design.md`
- `matters/<id>/findings/aia/aeat-selector-defense.md` (if applicable)

## CLOSE
- A — Draft formal AIA for DPO / AI committee / client
- B — Escalate (CDO, DPO, ethics committee, GC, client)
- C — Request additional technical documentation (model card, training data, logs)
- D — Monitor EU Implementing Acts + Spanish transposition + CJEU doctrine
- E — Other
