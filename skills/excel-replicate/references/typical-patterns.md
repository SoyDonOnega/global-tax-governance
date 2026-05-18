# TYPICAL PATTERNS — RECURRING TAX EXCEL FILES

Reference for the skill to distinguish inputs from calc cells in Excel files typical of Spanish tax practice.

> Note: Spanish tax form codes (modelo 200, 202, 232, 303, 390, etc.) and concepts (BI, BIN, IS, IVA, IRPF, ISP, RECC, etc.) are preserved as proper-noun references.

---

## CORPORATE INCOME TAX (IS) — Modelo 200 / 202

Typical structure:
- Sheet `Cuentas` or `Balance` — accounting data (INPUT)
- Sheet `Ajustes BI` or `Conciliación` — permanent and temporary adjustments (INPUT)
- Sheet `BI y cuota` — BI · BAI · gross liability · credits · net liability calc (FORMULAS)
- Sheet `Modelo 200` or `Modelo 202` — form replica (FORMULAS, refs)
- Sheet `Pagos a cuenta` — interim payments made (INPUT)

Main outputs to reconcile:
- Accounting result
- BI
- Gross liability
- Net liability
- Differential liability (to pay / refund)

---

## VAT (IVA) — Modelos 303 / 390

Typical structure:
- Sheet `Registro IVA Repercutido` (output VAT register — INPUT)
- Sheet `Registro IVA Soportado` (input VAT register — INPUT)
- Sheet `Calc IVA` — aggregation by rate (FORMULAS)
- Sheet `Modelo 303` — form replica (FORMULAS)
- Sheet `Modelo 390` (if annual)

Outputs:
- Total output VAT by rate (21 / 10 / 4)
- Total deductible input VAT
- Result of the return

---

## WITHHOLDING — Modelos 111, 115, 123, 216, 296

Typical structure:
- Sheet `Datos perceptores` — list of transactions with withholding (INPUT)
- Sheet `Cálculo` — aggregation by income type / key (FORMULAS)
- Sheet `Modelo XXX` (FORMULAS)

Outputs:
- Total withheld base by key
- Total withholding and on-account payments
- Net liability

---

## MODELO 232 — RELATED-PARTY TRANSACTIONS

Typical structure:
- Sheet `Operaciones` — full list per counterparty (INPUT)
- Sheet `Agregación` — grouping by counterparty Tax ID (FORMULAS)
- Sheet `Modelo 232` — form replica (FORMULAS)
- Optional annex: economic comparables analysis

Outputs:
- Transactions sum per counterparty
- Identification of counterparties to declare (> thresholds)

---

## ACCOUNTING — TAX RECONCILIATION

Typical structure:
- Sheet `Contable` — ledger extract by account (INPUT)
- Sheet `Ajustes` — permanent and temporary differences (INPUT with notes)
- Sheet `BI` — aggregated (FORMULAS)

Outputs:
- Accounting result
- Total positive and negative adjustments
- Tax BI

---

## ETR COMPUTATION

Typical structure:
- Sheet `Effective tax rate` — calc per jurisdiction (mixed: financial INPUT + tax FORMULA)
- Sheet `Deferred tax positions` — temporary differences (INPUT + FORMULAS)
- Sheet `Reconciliation` — bridge nominal to effective (FORMULAS)

Outputs:
- Consolidated ETR
- ETR per jurisdiction
- Reconciliation with P&L account

---

## PILLAR TWO — GLOBE WORKSHEET

Typical structure (highly variable by vendor):
- Sheet `Group structure` (INPUT)
- Sheet `Financial data per entity` (INPUT)
- Sheet `Adjustments to GloBE Income/Loss` (INPUT with notes + some FORMULAS)
- Sheet `Covered Taxes` (INPUT + FORMULAS)
- Sheet `Jurisdictional ETR` (FORMULAS)
- Sheet `Top-up Tax calc` (FORMULAS)
- Sheet `Safe harbour tests` (FORMULAS)

Outputs:
- ETR per jurisdiction
- Top-up tax per jurisdiction
- IIR / UTPR / QDMTT amounts
- Safe harbour test results

---

## CBCR DATA PREP

Typical structure:
- Sheet `Entities` (INPUT)
- Sheet `Financial data` (INPUT — from consolidation)
- Sheet `CbCR Table 1 / 2 / 3` (aggregation FORMULAS)

Outputs:
- Table 1 aggregated by jurisdiction
- Entity list by jurisdiction (Table 2)
- Additional information (Table 3 — text)

---

## GENERAL DETECTION RULES

1. **Input sheets** are usually named: `Datos`, `Soporte`, `Inputs`, `Raw`, `Extract`, `Listing`, `Detalle`, `Movements`, `Registros`, `Operaciones`.
2. **Calc sheets** are usually named: `Cálculo`, `Calc`, `Computation`, `Agregación`, `Summary`, `BI`, `Liquidación`.
3. **Output sheets** are usually named: the model number (`200`, `303`, `232`), `Modelo XXX`, `Output`, `Resultado`, `Final`, `Salida`.
4. **Typical colour conventions** (Big Four):
   - Yellow (`FFFFFF00`) → manual input
   - Light green (`FFC6EFCE`) → input from ERP
   - Light orange (`FFFCE4D6`) → check / control
   - No fill → formula / text
5. **Critical cells not to touch**: AEAT form headers, cells with official model numbering.
