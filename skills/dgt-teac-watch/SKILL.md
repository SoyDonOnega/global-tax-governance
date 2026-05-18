---
name: dgt-teac-watch
description: >
  Tax-position check against DGT binding rulings (V-NNNN-AA) · TEAC resolutions
  (RG NNNN/AAAA) · Spanish Supreme Court (ECLI:ES:TS) · CJEU (C-XXX/AA).
  Detects retroactive criterion changes (legitimate expectations as defensive
  argument). Use when the user says "DGT consulta on", "TEAC criterion", "tax
  administrative doctrine", "is there a binding ruling on", "TEAC has resolved",
  "casación TS open on", "legitimate expectations".
---

# /global-tax-governance:dgt-teac-watch

> Coverage: cross-cutting. ★ Tax Advice.

## SUBCOMMANDS

| Command | Action |
|---|---|
| `pull` | Pull from official sources (if `~~tax-authority-search` connected) |
| `digest` | Doctrine summary on one issue |
| `affects-matter <id>` | Cross-reference against active matters |
| `unify-criterion-flag` | Flag when TEAC unifies criterion retroactively |

## FLOW

1. **Scope the issue** — restate the legal question; identify the applicable norm (`Art. X.Y.Z [Ley]`) and the relevant administrative bodies.
2. **Read source documents** — if the user supplies resolutions (PDF / VDR link), read each in full; extract the operative paragraph and the supporting authority chain.
3. **Extract citations** — every cited authority normalised to plugin format (DGT `V[NNNN]-AA`, TEAC `RG [NNNN]/AAAA`, TS `STS Sala III · ECLI:ES:TS:AAAA:NNN`, CJEU `C-XXX/AA`). Verify each against primary source before quoting.
4. **Build doctrine table** — for each authority: date, body, position (in favour / against / nuanced), binding force, key reasoning.
5. **Currency check** — explicit pass against `references/resources/tax-currency-watch.md` and the relevant `references/jurisdictions/<iso>.md` to flag retroactive criterion unification or post-publication overturn.
6. **Retroactivity flag** — if a recent TEAC unification reverses a prior position the client relied on: surface the legitimate-expectations argument (TC, CJEU) explicitly.
7. **Critic pass** — `critic-citation-exactness` (every citation), `critic-currency-watch`, `critic-reviewer-note`, `critic-decision-tree`.
8. **Close** — digest with verdict per close decision tree.

## BINDING FORCE (important for argument strength)

- **DGT binding ruling**: binds Administration only with respect to the petitioner; for third parties, strong interpretive effect.
- **TEAC criterion unification**: binds Administration + economic-administrative tribunals.
- **TEAC ordinary resolution**: doctrine, not strictly binding but strong criterion.
- **TS Sala III**: case law (≥ 2 judgments) binding; single judgment = strong criterion.

## STRATEGY ANGLE

Detect **retroactive criterion changes** = open the **legitimate expectations** argument (TC, CJEU) in defense.

## TRAPS

- Citing a 2018 DGT consulta when the norm changed in 2022 → obsolete criterion.
- Without MCP connected: declare the limitation honestly; do not invent.
- A position validated today can break if TEAC unifies against it.

## DELIVERABLES
- `matters/<id>/findings/dgt-teac-digest-<issue>-<date>.md`
- Update `references/resources/tax-currency-watch.md` with new entries

## CLOSE
- A — Incorporate citation into the in-progress memo / report
- B — Request your own DGT binding ruling
- C — Seek doctrinal contrast (if your position is contrary)
- D — Monitor — TEAC criterion unification pending or TS casación open
- E — Other
