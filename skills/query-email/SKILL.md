---
name: query-email
description: >
  Drafts a client query email with determinative (not generic) questions and
  normative basis per question. Identifies grey areas in the support and the
  calc (catalogue grey-areas-catalog.md per IS, VAT, withholding, modelo 232,
  Pillar Two). Learns house style from prior emails and avoids re-asking
  already-answered questions. Use when the user says "draft query email",
  "client queries", "open items", "what questions do I need to ask", "year-end
  open items".
---

# /global-tax-governance:query-email

> Coverage: cross-cutting. ★ Tax Advice · ★ Corp Tax.

## SUBCOMMANDS

| Command | Action |
|---|---|
| `draft` | Identify grey areas + draft the email |
| `send-ready` | Final version (.txt / .html / Outlook-ready) |
| `from-log <path>` | Re-use the prior-period queries-log |

## FLOW

1. **Scan** — read the supporting documents and (if present) the working calc; catalogue the grey areas where the position turns on a fact the practitioner does not have.
2. **House-style ingest** — if prior client emails were supplied, extract the vocative, the typical structure, the level of detail expected, and the list of questions already answered (avoid re-asking).
3. **Determinative filter** — every candidate question must change the calc, the compliance status, or the defensive posture. Drop the rest.
4. **Group** — PRIORITY (impact on liability or penalty risk) · SECONDARY (refinement) · ALREADY ANSWERED IN PRIOR EMAIL (confirm currency).
5. **Draft the email** — one question per item with the per-question structure below (item · question · normative basis · why it matters · effect A vs. B).
6. **Critic pass** — `critic-citation-exactness` (every normative basis is cited exactly), `critic-currency-watch` (any cited threshold or rate is current), `critic-reviewer-note`.
7. **Outputs** — `correo.md` / `correo.txt` / `correo.html` + `queries-log.yaml` appended to the matter's correspondence log.

## ANTI-NOISE RULE

Every question must be **determinative**. If the answer does not change the calc, the compliance status, or the defensive posture → it is noise and must be removed.

## PER-QUESTION STRUCTURE

```
N. <Item> — <amount / brief context>
   Question: <specific question>
   Normative basis: <Art. X.Y LIS / V-NNNN-AA / RG NNNN/AAAA>
   Why it matters: <one line on effect A vs. B>
```

## GREY AREAS CATALOGUE

See `references/grey-areas-catalog.md`. Covers:
- IS: BDR provisions · client entertainment · donations · director compensation · sanctions · listed jurisdictions · Art. 21 impairment · NOLs · R&D · patent box · DTAs/DTLs · reorganisations · subsidies
- VAT: intra-EU · reverse charge · prorrata · exemptions · capital-goods regularisation · self-supply · cash regime · BI modification by non-payment
- Withholding: listed jurisdictions · CDIs · Art. 7 exemptions · benefits in kind
- Modelo 232: thresholds · listed jurisdictions · patent box
- Pillar Two: covered taxes · GloBE adjustments · CbCR safe harbour · QDMTT

## DELIVERABLES
- `matters/<id>/correspondence/correo-<subject>-<date>.md/.txt/.html`
- `matters/<id>/correspondence/queries-log.yaml`

## CLOSE
- A — Send to client
- B — Partner review if > 5 PRIORITY items
- C — Phone call if close is imminent
- D — Move to internal checklist (resolve internally without involving client)
- E — Other
