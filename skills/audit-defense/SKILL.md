---
name: audit-defense
description: >
  Tax defense across the full procedural cycle — information request → audit →
  acta → reposición → TEAR/TEAC → contencioso administrativo → casación TS.
  Calibrates argument strength (alta/media/baja/marginal) and designs procedural
  strategy. Integrates with dgt-teac-watch for current doctrine and ai-tax-governance
  when the selection that triggered the inspection was AI-driven. Use when
  the user says "tax audit", "AEAT requirement", "alegaciones", "acta", "reposición",
  "TEAR", "TEAC", "contencioso", "casación TS", "tax defense", "audit notice".
---

# /global-tax-governance:audit-defense

> Flagship workflow W4. Multi-phase procedural workflow with hard deadlines under Art. 30 LPACAP + Art. 150 LGT.

## SUBCOMMANDS

| Command | Action |
|---|---|
| `intake` | Receive AEAT communication, identify phase, compute deadlines |
| `phase <n>` | Work a specific phase (1–7) |
| `pleading <type>` | Concrete draft (alegaciones · recurso · reclamación · demanda · escrito casación) |
| `status` | Deadlines calendar + state of each argument |
| `strength-rebalance` | Re-calibrate argument strength after new doctrine |

## PROCEDURAL PHASES

1. **Initial requirement / start** (Art. 141 LGT, Art. 150 deadlines: 18 months ordinary · 27 complex)
2. **Audience trámite / proposal** (Art. 99.8, Art. 156 LGT)
3. **Acta** (conformidad · disconformidad · acuerdo Art. 155)
4. **Recurso de reposición** (Art. 222 LGT — 1 month)
5. **Reclamación TEAR/TEAC** (Art. 229 LGT — 1 month)
6. **Contencioso-administrativo** (Law 29/1998 LJCA — 2 months)
7. **Casación TS** (Art. 88 LJCA)

## FLOW

1. **Intake** — reconstruct the procedural calendar (`plazos.md`): every act notified, every reply deadline, every step that interrupts prescription. Identify the active phase (alegaciones · acta · liquidación · recurso reposición · TEAR · TEAC · jurisdicción).
2. **Transversal checklist (10 items)** — apply against the active phase. Output `findings/audit-defense/transversal-check.md`.
3. **Per phase** — draft the pleading or recurso: structure (hechos · fundamentos · solicitud), grounds prioritised, antecedents cited (TS, TEAC, DGT, doctrina), evidence list, anexos.
4. **Strength stress-test** — challenge the pleading against the strongest contra-argument the administration would deploy. If strength is low, iterate with the missing grounds before moving on.
5. **Doctrine watch** — run `dgt-teac-watch` over the cited authorities to detect retroactive doctrine changes against the position. Escalate if material change appears.
6. **AI selection branch** — if the selection that triggered the inspection involved AEAT algorithmic scoring, run `/global-tax-governance:ai-tax-governance aeat-selector-analysis` and incorporate the resulting defensive analysis.
6a. **Intercompany services deductibility branch** — if the inspection challenges deductibility of intercompany service charges (e.g. Art. 15.e LIS in Spain or equivalent), run `/global-tax-governance:tp-analysis benefit-test <category>` to build the evidence pack from email and contract corpora; attach the resulting summary memo + evidence grids to the alegaciones.
7. **Critic pass** — `critic-citation-exactness` (every authority cited exactly), `critic-currency-watch` (recent TEAC criteria especially), `critic-reviewer-note`, `critic-finding-state` (each issue in scope must carry a state), `critic-decision-tree`.
8. **Close** — submission package + escalation per close decision tree.

## TRANSVERSAL CHECKLIST (10 items applicable to any phase)

1. **Prescription** (Art. 66 LGT) — interrupted/opposable
2. **Procedure expiry** (Art. 104 management · Art. 150 audit)
3. **Insufficient motivation** Art. 102 LGT — invalidating defect
4. **Improper reversal of burden of proof**
5. **Prior favourable DGT binding doctrine**
6. **Retroactive TEAC/TS criterion change** — legitimate expectations (TC, CJEU)
7. **Separate sanctioning procedure** (Art. 208 LGT) — presumption of innocence, culpability not strict, reinforced motivation
8. **Non bis in idem** if sanction + criminal tax offence
9. **Proportionality** of the sanction
10. **Algorithmic / AI selection** — integrates `ai-tax-governance` (Art. 22 GDPR + Art. 34 LGT + reinforced motivation Art. 102 LGT)

## ARGUMENT STRENGTH CALIBRATION

| Strength | When |
|---|---|
| **Alta** | Clear norm + favourable DGT/TEAC/TS in force |
| **Media** | Norm with interpretation + divided or absent doctrine |
| **Baja** | Against TEAC/TS but qualified doctrinal support |
| **Marginal** | No doctrinal support — preserve rights for later phases |

## COVERAGE

- Tax dispute (★): core
- Tax advice (★): parallel to defense, strategic advisory
- IT (partial): CJEU doctrine, MAP if double taxation
- AI (partial): if algorithmic AEAT selection
- Strategy (★): sign vs. litigate decision

## STRATEGY ANGLE

Material decisions:
- **Sign conformity acta** (reduces sanction 30% but firm) **vs. appeal**.
- **Reposición** before the same body (rarely succeeds, gains time) **vs. direct jump to TEAR**.
- **TEAR** vs. **per saltum TEAC** by amount and complexity.
- **Contencioso** vs. **out-of-court settlement**.

Not everything appeals: low amount + medium-low strength → conformity can be optimal (cost / benefit).

## FUNCTION LENS

- **Client tax director**: primary defense owner.
- **GC**: if material exposure or reputational risk.
- **CFO**: accounting provision.
- **Responsible Big Four partner**: senior reviewer pre-submission of pleadings.
- **Board**: if exposure > matter materiality threshold.

## TRAPS

- Miscomputed deadlines (Art. 30 LPACAP — calendar vs. business days).
- Confusing tax liability with sanctioning procedure.
- Doctrine post-audit-year applied to defend an earlier year.
- Signing conformity without strength analysis.
- Marginal arguments in the front line.
- Legitimate expectations not invoked when criterion changed retroactively.

## DELIVERABLES

- `matters/<id>/findings/audit-defense/plazos.md`
- `matters/<id>/findings/audit-defense/strength-arguments.md`
- `matters/<id>/findings/audit-defense/alegaciones-<date>.md` / `recurso-<date>.md` / `reclamacion-<date>.md` / `demanda-<date>.md` / `casacion-<date>.md`
- `matters/<id>/findings/audit-defense/transversal-checklist.md`
- `matters/<id>/findings/audit-defense/phase-log.yaml`

## CLOSE

- A — Submit pleading (prepare suplico + signature + filing)
- B — Escalate to responsible partner — high amount or doubtful strength
- C — Request additional documentation from client
- D — Negotiation / acuerdo (Art. 155 LGT) — explore before proceeding
- E — Wait within statutory deadline
- F — Accept liquidation — cost/benefit doesn't justify appeal
