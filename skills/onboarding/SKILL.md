---
name: onboarding
description: >
  Initial interview for the global-tax-governance plugin. Learns the user's
  practice (role · footprint · risk posture · escalation · house style · active
  areas · integrations) through a branched interview by profile (in-house / Big
  Four / boutique / academic-practitioner / combination) and extracts real
  house style from supplied seeds (memo · TCF doc · board paper · opinion
  letter · query email · recurring Excel) with delta computation. Writes the
  practice profile into CLAUDE.md with semantic placeholders ([PLACEHOLDER] /
  [PENDING] / [DEFAULT] / [LIMITED DATA — N docs reviewed]). Use on first
  install · when CLAUDE.md contains [PLACEHOLDER] · when the user says "set up
  the plugin", "configure global-tax-governance", "onboard me", "first time",
  "let's get started", "--redo".
---

# /global-tax-governance:onboarding

> Initial interview. Runs once (re-runnable with `--redo`). Every later skill reads the `CLAUDE.md` this produces.

## WHEN TO RUN

- First time after installation
- If `CLAUDE.md` contains `[PLACEHOLDER]` in critical fields
- If the user invokes `--redo` (full re-interview) or `--redo --area <X>` (partial)
- If the user invokes `--check-integrations` (re-probe MCPs)
- If the user invokes `--add-seed <path>` (add a seed without re-interviewing fully)

**Do not re-run unsolicited**. For surgical changes: `/customize`.

## PRE-FLIGHT

1. Read the current `CLAUDE.md` (if it exists).
2. Detect markers:
   - `[PLACEHOLDER]` → never filled → proceed with cold-start
   - `[PENDING]` → user paused → offer "Welcome back, pick up where left off"
   - `[DEFAULT]` → sensible but not seed-verified → offer "validate with seed"
   - `[LIMITED DATA — N docs reviewed]` → seeds < 10 → OK with caveat
3. If `<!-- SETUP PAUSED AT: <section> -->` detected → offer resume from that section.

## INTERVIEW TREE

Pyramid structure — the first answer determines the next subtree.

### Block 1 — SETTING (always)

**Q1.** What type of practice?
- In-house tax director (corporation)
- Big Four advisor (global firm)
- Boutique tax practice (independent firm)
- Academic-practitioner (research + occasional consulting)
- Combination (specify)

**Q2.** What is your specific role on the team?
- Solo (sole practitioner)
- Manager / Senior associate
- Director / Partner
- Researcher (academic side)

**Q3.** Relevant team size?

---

### Block 2 — FOOTPRINT (always)

**Q4.** Primary jurisdiction? (ISO 3166-1 alpha-2 code — e.g., `ES`, `NL`, `DE`, `IE`, `LU`, `UK`, `US`, `MX`).

After the answer:
1. Check whether `references/jurisdictions/<iso>.md` exists.
2. If it does → load it; confirm to the user the profile is available.
3. If it does not → walk the user through `references/jurisdictions/_template.md` to author one. Required minimums to proceed: source-of-law hierarchy · citation formats · tax authority and binding-ruling body · core taxes · anti-hallucination guardrails. The rest can be filled later via `/customize`.

**Q5.** Recurring secondary jurisdictions? (multi-select, ISO 3166-1 alpha-2). For each: same check as Q4. Missing profiles are listed as `[PENDING]` until populated.

**Q6.** Majority of your portfolio?
- Listed multinational
- Private multinational
- PE-owned
- Family office
- Domestic mid-sized groups
- Mixed (specify)

---

### Block 3 — RISK AND ESCALATION (always)

**Q7.** Overall risk appetite? (Conservative / Medium / Aggressive within the post-BEPS frame)

**Q8.** Escalation chain? (free text — who is escalated to before sending)

**Q9.** Non-negotiable red lines? (multi-select + free text)

**Q10.** Materiality threshold for automatic partner escalation (€).

---

### Block 4 — ACTIVE AREAS (always)

**Q11.** Areas in which you work actively? (multi-select)
- Pillar Two / GloBE
- DAC 6 / 7 / 8 (or local equivalents)
- CbCR (public and non-public)
- AI Act + tax function (or local equivalent)
- Transfer pricing
- CFC rules (jurisdiction-specific — verify exact reference in the active jurisdiction profile)
- TCF / tax governance
- Local cooperative-compliance regime (jurisdiction-specific — verify in the active jurisdiction profile)
- Tax strategy
- Tax dispute / audit defense
- ESG tax / GRI 207

---

### Block 5 — LANGUAGE AND CITATION (always)

**Q12.** Default working language? (specify which language for which recipient — domestic client / international HQ / academic publication).

**Q13.** Default doctrine citation style? (APA 7 default · adapted Bluebook · ISO 690 · other). Statute and jurisprudence formats come from the jurisdiction profile §2 — not from this answer.

---

### Block 6 — PROFILE BRANCH

#### If **in-house tax director**:
- Reporting line to CFO or GC?
- Internal tax committee?
- Current tax tech stack? (ERP · tax engines · RPA / OCR / NLP / LLM)
- Co-source with Big Four in which areas?

#### If **Big Four advisor**:
- Client portfolio (sector · scale)?
- How is partner escalation handled?
- Position vs. firm peers in technical areas?
- Independence restrictions (audit clients)?

#### If **boutique**:
- Specialisation (corp · litigation · advisory · expat · etc.)?
- Team capacity · areas where you co-source?

#### If **academic-practitioner**:
- Active research lines?
- Target journals · conferences?
- How is practice separated from research?

---

### Block 7 — COMPANION PLUGINS (always)

**Q14.** Do you have `claude-for-legal` installed and active?

The plugin runs standalone by default — small-corpus extraction, in-line tabular review, and direct evidence handling happen inside each skill. If `claude-for-legal` is present, the skills offer to delegate larger or generic workloads (batch tabular review on >50 docs, M&A diligence issue extraction across hundreds of contracts, cross-version regulatory diffs, AIA generation as a standalone exercise).

Options: `present` · `absent`. Default: `absent`. Record under `## COMPANION PLUGINS` in `CLAUDE.md`.

Honest framing for the user: "Companion plugins are optional. Mark `absent` if you're not sure — every skill will work in standalone mode and tell you when claude-for-legal would have made a workload easier."

---

### Block 8 — INTEGRATIONS (always — re-probe with `--check-integrations`)

**Q15.** Probe available MCPs:
- `~~vdr` · `~~mail` · `~~erp` · `~~clm` · `~~tracker` · `~~tax-authority-search` · `~~chat`

For each: detect connection · mark OK / NOT CONFIGURED.

---

### Block 9 — SEEDS (optional but strongly recommended)

Request **at least one seed of each type**. More seeds = better delta extraction.

#### Seed 1 — Prior technical memo
Extract: section structure · citation standard · hedging level · tone · reviewer signature · typical length.

#### Seed 2 — TCF document
Extract: framework · depth · emphasised building blocks · three lines of defence applied.

#### Seed 3 — Board paper or executive summary
Extract: executive summary length · decision framing · quantified risk · visual vs. table vs. prose.

#### Seed 4 — Opinion letter / ruling request
Extract: opinion structure · conclusion language · reliance language · disclaimer style.

#### Seed 5 — Prior query email
Extract: vocative · per-question structure · format · signature · per-question normative cite.

#### Seed 6 — Recurring Excel
Extract: input vs. calc convention · sheet structure · named ranges · pivots / charts.

---

### DELTA EXTRACTION — the real posture

> "Read what the templates / policies say. Read what the actual signed/sent docs show. Compute the delta. The delta is the real playbook."

Applied to tax:
- "Templates say 'exhaustive citation with DGT + TEAC'. Actual memos cite DGT only. **Real**: DGT-first, TEAC optional."
- "TCF doc declares 'three lines of defence'. Actual control inventory shows only 1st line + audit (no 2nd-line operational). **Real**: two-line + audit as 3rd."

These deltas are recorded in `## HOUSE STYLE LEARNED FROM SEEDS` of `CLAUDE.md`.

---

## OUTPUT — WRITING THE CLAUDE.md

After collecting answers + extracting seeds:

1. Read template `references/templates/company-profile.md` and instantiate.
2. Build `CLAUDE.md` with all sections.
3. Show the user the complete `CLAUDE.md` for final confirmation.
4. If approved → save.
5. If paused → write `<!-- SETUP PAUSED AT: <section> -->` + `[PENDING]` markers.

## RESUME-FROM-PAUSE FLOW

If pre-flight detected pause:
- "Welcome back. The interview was paused at `<section>`. Continue from there or restart?"
- Continue: go to the section and complete it.
- Restart: `--redo` invoked internally.

## CLOSE

At the end of onboarding:
- Summary of key settings (5 lines).
- Decision tree:
  - A — Create the first matter (`/matter-workspace new <slug>`)
  - B — Customize a specific slot before starting
  - C — Re-onboard if something doesn't fit
  - D — Other

## HARD RULES

- **Never invent user answers**. If a section was not covered → explicit `[PENDING]`.
- **Do not dump all questions in one go**. Small blocks with visible confirmation.
- **Detect internal inconsistencies** during the interview (e.g., "in-house" + portfolio of clients → flag).
- **Seeds are optional**: never block onboarding for missing seeds; use `[DEFAULT]` with caveat.
- **Confidentiality**: seeds are processed locally · NEVER exported nor persisted beyond `CLAUDE.md`.

## TRAPS

- User marks "in-house" but mentions Big Four context → flag.
- Active areas marked but seeds don't cover them → `[LIMITED DATA]` per area.
- Aggressive appetite + "everything requires partner approval" → inconsistency.
- Conservative + footprint in listed jurisdictions without justification → flag.
