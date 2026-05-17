# TAX FUNCTION LENS — applied guide

> How every plugin deliverable applies the two mandatory lenses on top of the technical analysis.

---

## WHY TWO LENSES

A technically correct memo that fails to address **(a) who consumes it and for what decision** or **(b) how it fits the client's strategy** is useless to a tax director or a CFO. The two lenses lift each deliverable from "technical response" to "executive input".

This rule is **mandatory**. No substantive deliverable closes without both lenses applied.

---

## LENS 1 — TAX FUNCTION

### Question 1.1 — Who consumes?

| Output | Primary consumer | Secondary consumer |
|---|---|---|
| Per-entity Pillar Two calc | Controller | Tax director |
| Consolidated Pillar Two | CFO + tax director | Audit committee · Treasury |
| TCF maturity scorecard | Tax director · Audit committee | CFO · CRO |
| TP local file | AEAT · external auditor | Controller · CFO |
| Master file | AEAT · external auditor · client legal department | CFO · CTO |
| Public CbCR | Investor relations · sustainability · comms | Board · CFO |
| AIA | DPO · CIO · CTO · AI / ethics committee | Legal · CFO |
| Opinion memo | Client (specific contact named in matter.md) | Responsible partner |
| Board paper memo | Board · audit committee | CFO · GC |
| Defense pleading | AEAT/TEAR/TEAC · senior reviewer | Client legal department |
| Tax strategy paper | CFO · board · tax director · corporate development | Treasury · M&A team |
| Tax function design | CFO · CHRO · CIO | Tax director |

### Question 1.2 — Where in the tax-function cycle?

Five typical cycles:

| Cycle | Cadence | Typical outputs |
|---|---|---|
| **Monthly / quarterly close** | M / Q | provision · withholding · VAT · modelo 232 |
| **Year-end close** | A | IS · BIN · BI adjustments · modelo 200 |
| **Accounting provision** | T+1 from close | ETR forecast · deferred tax · UTPs |
| **Quarterly planning** | Q | ETR planning · restructuring · M&A · new positions |
| **Response cycle** | event-driven | AEAT requirements · audit · MAP · APA |

Each deliverable identifies which of the five it supports.

### Question 1.3 — Which KPI moves?

Typical corporate tax function KPIs:
- **Consolidated ETR** (target · actual · variance vs. budget)
- **Cash tax** (vs. accounting ETR; temporary differences)
- **Days from close to firm liquidation** (efficiency)
- **Open controversies** (count · amount · resolution probability)
- **Self-assessment errors** (self-detected vs. AEAT-detected)
- **CBPT adherence** (annual reporting status)
- **TP doc coverage** (% of material transactions documented)
- **Time-to-respond to requirements** (days)

### Question 1.4 — Which organisational change does it suggest?

If the deliverable reveals structural problems:
- Missing roles (is there a regional tax lead for this jurisdiction?)
- Insufficient tech stack (does the ERP support the data needed?)
- Wrong reporting line (does tax controlling report to CFO or to accounting?)
- Skills gap (does anyone on the team understand Pillar Two?)

These suggestions feed into `/tax-function-design`.

---

## LENS 2 — STRATEGY

### Question 2.1 — Which strategic decision does it enable or constrain?

Not "the calc is X". Instead:
> "The calc X enables decision D" — e.g.:
> "With consolidated top-up < 2M€, maintaining the current structure is viable.
> With > 2M€, open a restructuring analysis."

### Question 2.2 — What options exist?

Every strategic deliverable produces **options**, not a single recommendation.

Typical options:
- Do X · don't do X · do X partially · wait
- Appeal · sign conformity · settle
- Request a DGT ruling · operate under silent risk · bilateral APA
- Restructure · maintain status quo · partial restructure

With explicit trade-offs:
- ETR · cash tax · complexity · reputational · regulatory risk · timing · cost

### Question 2.3 — What is the second-order effect?

Downstream effects:
- What does AEAT do when it sees this?
- What do competitors do if we publish this?
- What happens in N+1 fiscal years if this position becomes general?
- Does it create an internal precedent that is hard to reverse?

### Question 2.4 — When does the answer change by client profile?

| Client | Typical variation |
|---|---|
| Listed IBEX35 | High reputational risk · mandatory public CbCR · SOX testing |
| Private family-owned | Medium reputational risk · more tolerance for complexity |
| PE-owned | Exit-driven horizon · structure can pivot pre-IPO |
| Family office | Owner's personal liability · more conservative |
| Spanish subsidiary of foreign group | Subordinated to HQ strategy · less optionality |

---

## HOW TO REPORT THE TWO LENSES

In every substantive deliverable, two sections:

```markdown
## STRATEGY — DECISION ENABLED

<1–3 paragraphs.
- The specific decision the output enables.
- The options identified.
- Main trade-offs.
- Second order.>

## TAX FUNCTION — WHO AND WHEN

<1–2 paragraphs.
- Primary and secondary stakeholders.
- Cycle in which it fits.
- KPI principally affected.
- (Optional) Suggested organisational change.>
```

---

## INDISPENSABILITY RULE

If genuinely neither lens applies to the deliverable (rare — typically only in ultra-technical outputs like a calc QC report), **justify in one sentence**:

> "Strategy lens: not applicable — output is purely verificational, no position or decision contained."

Never leave the section empty. The absence must be deliberate and explained.

---

## STRATEGY-FIT SELF-CHECK (run inside every flagship skill)

Before close, the skill checks that the strategy lens does not contradict the posture declared by the client in `matter.md`:

- **ETR impact**: positive · neutral · adverse vs. target
- **Risk posture**: aligned · stretched · contradicted vs. declared appetite
- **Strategic horizon**: short · medium · long match

If `contradicted` → emit an `escalate_to_human` handoff. The technical position contradicts the declared strategy and requires human review before communicating to the client.

---

## ROLE OF `critic-reviewer-note`

This critic verifies that the reviewer note header includes both lens sections when the deliverable is substantive:

- `strategy_angle` section present in reviewer note
- `function_lens` section present in reviewer note

If any required section is missing → `pass: false` with `missing_fields: [strategy_angle | function_lens]`.

---

## CHECKLIST FOR THE LAWYER

Before closing any substantive deliverable, read:

- [ ] Do I explicitly identify the primary consumer?
- [ ] Do I specify which cycle of the tax function it fits?
- [ ] Do I cite the KPI affected?
- [ ] Do I articulate the decision the output enables?
- [ ] Do I present options (where applicable) with trade-offs?
- [ ] Do I identify the second order?
- [ ] Is the strategy lens consistent with the client profile?
- [ ] Have I run the strategy-fit self-check if the output takes a position?
- [ ] Have I invoked `critic-reviewer-note` to validate both lens sections are present?

If any answer is "no" — the deliverable is not ready to send.
