# global-tax-governance — PRACTICE PROFILE

> Template. Populated by `/onboarding` on first run. Adjusted with `/customize`.
> Every skill reads this file before acting. Jurisdiction-specific content lives in `references/jurisdictions/<iso2>.md` — never hard-code it here.

---

## PRACTICE SETTING

**Type of practice:** [PLACEHOLDER]   <!-- in-house tax director · Big Four advisor · boutique · academic-practitioner -->
**Role:** [PLACEHOLDER]
**Team size:** [PLACEHOLDER]

---

## FOOTPRINT

**Primary jurisdiction (ISO 3166-1 alpha-2):** [PLACEHOLDER]   <!-- e.g., ES. Must match a file under references/jurisdictions/ -->
**Secondary recurring jurisdictions:** [PLACEHOLDER]   <!-- comma-separated ISO codes -->
**Client portfolio mix:** [PLACEHOLDER]

> Every cited authority, citation format, source-of-law hierarchy and local escalation trigger comes from `references/jurisdictions/<primary-iso>.md` for the primary jurisdiction (and the matching secondary profile when a matter targets a secondary).

---

## RISK POSTURE

**Overall appetite:** [PLACEHOLDER]   <!-- conservative · medium · aggressive within the post-BEPS frame -->
**Red lines:** [PLACEHOLDER]
**Materiality threshold for escalation:** [PLACEHOLDER]   <!-- amount + currency -->
**Hedging level:** [PLACEHOLDER]   <!-- low · medium · high — affects how skills wrap conclusions -->
**Citation standard:** [PLACEHOLDER]   <!-- default APA 7 for doctrine; statute/jurisprudence per jurisdiction profile -->

---

## ACTIVE AREAS

(Multi-select against the supranational currency watch — `references/resources/tax-currency-watch.md` — plus the local layer in your jurisdiction profile.)

- [ ] Pillar Two / GloBE
- [ ] DAC 6 (or local equivalent)
- [ ] DAC 7 (or local equivalent)
- [ ] DAC 8 (or local equivalent — crypto-asset reporting)
- [ ] Non-public CbCR (OECD)
- [ ] Public CbCR (EU Directive 2021/2101 — or local equivalent in non-EU jurisdictions)
- [ ] AI Act + tax function (EU) / local equivalent
- [ ] Transfer pricing
- [ ] CFC rules (per jurisdiction)
- [ ] TCF / tax governance
- [ ] Local cooperative-compliance regime
- [ ] Tax strategy
- [ ] Tax dispute / audit defense
- [ ] ESG tax / GRI 207

---

## LANGUAGE AND CITATION

**Default working language:** [PLACEHOLDER]
**Language by recipient:**
- Domestic client: [PLACEHOLDER]
- International parent / HQ: [PLACEHOLDER]   <!-- typically English -->
- Academic publication: [PLACEHOLDER]   <!-- typically English unless the target journal differs -->

**Citation format:** per `references/jurisdictions/<primary-iso>.md` §2. Cross-jurisdiction deliverables: follow the format of the cited authority's home jurisdiction.

---

## PROFILE BRANCH

(Branch by practice type — fill only the applicable section)

### If in-house tax director
- Reporting line: [PLACEHOLDER]
- Internal tax committee: [PLACEHOLDER]
- Tax tech stack: [PLACEHOLDER]
- Co-source areas with external advisors: [PLACEHOLDER]

### If Big Four / external advisor
- Portfolio (sector × scale): [PLACEHOLDER]
- Escalation to partner: [PLACEHOLDER]
- Position vs. firm peers: [PLACEHOLDER]
- Independence constraints: [PLACEHOLDER]

### If boutique
- Specialisation: [PLACEHOLDER]
- Team capacity: [PLACEHOLDER]
- Co-sourced areas: [PLACEHOLDER]

### If academic-practitioner
- Active research lines: [PLACEHOLDER]
- Target journals: [PLACEHOLDER]
- Practice / research separation: [PLACEHOLDER]

---

## COMPANION PLUGINS

The plugin runs **standalone by default**. The skills below process small corpora directly (typical thresholds: ≤50 documents, ≤20 entities). If you also have the `claude-for-legal` plugin installed, the skills will offer to delegate larger or generic workloads to it.

Set to `present` for each companion you have installed and active.

| Companion | Status | Use it for |
|---|---|---|
| `claude-for-legal` | [PLACEHOLDER] | Batch tabular review (>50 docs) · M&A diligence issue extraction · cross-version regulatory diffs · AIA generation as standalone exercise. |

Format: `present` / `absent`. Default: `absent`. Skills check this flag and either delegate to the companion or process in-line.

---

## INTEGRATIONS

Last probed: [PLACEHOLDER — date]

| Category | Placeholder | Configured tool | Status |
|---|---|---|---|
| Document storage (VDR) | `~~vdr` | [PLACEHOLDER] | [PLACEHOLDER] |
| Mail | `~~mail` | [PLACEHOLDER] | [PLACEHOLDER] |
| ERP / accounting | `~~erp` | [PLACEHOLDER] | [PLACEHOLDER] |
| CLM | `~~clm` | [PLACEHOLDER] | [PLACEHOLDER] |
| Project tracker | `~~tracker` | [PLACEHOLDER] | [PLACEHOLDER] |
| Tax-authority search | `~~tax-authority-search` | [PLACEHOLDER] | [PLACEHOLDER] |
| Chat (notifications) | `~~chat` | [PLACEHOLDER] | [PLACEHOLDER] |

---

## ESCALATION MATRIX (TRANSVERSAL)

Transversal rows below. **Add jurisdiction-specific rows in `references/jurisdictions/<iso>.md` §7.**

| Trigger | Action | Deadline |
|---|---|---|
| Listed client · exposure > materiality threshold | Escalate to partner / GC before sending | Same day |
| AIA on high-risk AI Act (or local equivalent) system | Escalate to DPO + client's AI committee | 48 h |
| Pillar Two without clear local transposition | Watch & note + verify primary source against jurisdiction profile | Weekly |
| Cross-matter leak detected | Stop deliverable + human escalation | Immediate |

---

## HOUSE STYLE LEARNED FROM SEEDS

(Populated by `/onboarding` from supplied seeds. Each delta is computed between the declared style and the actually practised one.)

- **Memo structure**: [PLACEHOLDER — extracted from seeds]
- **Actual citation format**: [PLACEHOLDER — delta vs. declared]
- **Actual hedging level**: [PLACEHOLDER]
- **Executive summary length**: [PLACEHOLDER]
- **Board paper format**: [PLACEHOLDER]
- **Opinion structure**: [PLACEHOLDER]
- **Query email vocative**: [PLACEHOLDER]
- **Excel convention**: [PLACEHOLDER]
- **Reviewer signature**: [PLACEHOLDER]

---

## CROSS-MATTER CONTEXT

```
Cross-matter context: off
```

Default: `off` (every matter isolated, privilege protection). Toggle with `/customize` only when there is an explicit need to read across matters.

---

## MATTERS

Per-matter structure under `matters/<slug>/`:

```
matters/<slug>/
├── matter.md
├── verification-log.md
├── history.md
├── findings/
├── inputs/
└── correspondence/
```

`/matter-workspace` manages creation, switching, and closure.

---

## ONBOARDING METADATA

- **Interview date**: [PLACEHOLDER]
- **Interview branch**: [PLACEHOLDER]
- **Seeds reviewed**: [PLACEHOLDER]
- **Limitations**: [PLACEHOLDER]

---

## CUSTOMIZATION LOG

(Append-only by `/customize`. Format: date · slot · previous value · new value · motivation.)

---

## TRANSVERSAL RULES (every skill applies)

1. **Hard anti-hallucination** — exact citation or no claim. Authorities cited must match the list in `references/jurisdictions/<iso>.md` §6 for the matter's jurisdiction.
2. **Reviewer note header** at the top of every substantive deliverable.
3. **Decision tree** at close with concrete options (≥ 3 actionable branches).
4. **Currency check** against `references/resources/tax-currency-watch.md` (supranational) and `references/jurisdictions/<iso>.md` §5 (local layer) before citing dates or thresholds in moving areas. Staleness check: if older than 90 days, warn.
5. **Verification log** dated per matter against primary sources.
6. **Four finding states**: `answered` · `not_present` · `unclear` · `needs_review`. Never blank.
7. **Function lens + strategy lens** mandatory in substantive deliverables.
8. **Language by recipient**: default per profile; switch to English for international HQ or academic publication.
9. **B&W minimalist aesthetic** — no gold, no color, no emoji, no ornament. ALL CAPS section headings.
10. **Privilege** — deliverables are work product. Privilege header when the document mediates between lawyer and client.
