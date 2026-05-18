# TAX CURRENCY WATCH — SUPRANATIONAL LAYER

**Last verified: 2026-05-17.**

> **STALENESS CHECK.** If the last-verified date above is more than 90 days old, treat this file as stale and re-verify each entry against its primary source before acting. A stale watch is worse than no watch — it looks current and lies. When a skill reads this file it must check the last-verified date first. If stale, warn: "Tax currency watch last verified [date] — [N] months ago. Using as a checklist of areas to verify, not as source of truth." When updating any entry, also update the header's last-verified date.

This file tracks **OECD and EU-level** instruments. Local transposition status, local administrative criteria and local jurisprudence live in `references/jurisdictions/<iso>.md` §5 — never duplicate them here.

---

## PILLAR TWO / GLOBE

| Item | Status | Source | Re-check |
|---|---|---|---|
| Directive (EU) 2022/2523 | In force; IIR rules apply for fiscal years starting ≥ 31-Dec-2023 | EUR-Lex 32022L2523 | quarterly |
| OECD Pillar Two Model Rules | Consolidated; verify subsequent Administrative Guidance | oecd.org/tax/beps/globe | monthly |
| OECD Administrative Guidance | Multiple documents (Feb-23 · Jul-23 · Dec-23 · Jun-24 …) — verify latest consolidated version | OECD inclusive framework | monthly |
| Transitional safe harbours | CbCR transitional safe harbour in force; progressive expiration | OECD Pillar Two Rules | quarterly |
| Local IIR / UTPR / QDMTT transposition | Per `references/jurisdictions/<iso>.md` §5 | (local profile) | quarterly |

## DAC (EU)

| Item | Status | Source | Re-check |
|---|---|---|---|
| DAC6 (Directive 2018/822) | In force; operational hallmarks | EUR-Lex 32018L0822 | half-yearly |
| DAC7 (Directive 2021/514) | In force; digital-platform reporting | EUR-Lex 32021L0514 | half-yearly |
| DAC8 (Directive 2023/2226) | Applicable from 1-Jan-2026 for crypto-assets | EUR-Lex 32023L2226 | quarterly |
| Local DAC transpositions | Per `references/jurisdictions/<iso>.md` §5 | (local profile) | quarterly |

## PUBLIC CBCR

| Item | Status | Source | Re-check |
|---|---|---|---|
| Directive (EU) 2021/2101 | In force; first reporting for fiscal years starting ≥ 22-Jun-2024 | EUR-Lex 32021L2101 | half-yearly |
| Australia public CbCR | In force; stricter design than EU — relevant for multinationals with AU presence | ATO | half-yearly |
| Local transposition | Per `references/jurisdictions/<iso>.md` §5 | (local profile) | half-yearly |

## AI ACT — TAX FUNCTION (EU)

| Item | Status | Source | Re-check |
|---|---|---|---|
| Regulation (EU) 2024/1689 | In force. Staggered application: prohibitions from 2-Feb-2025; GPAI from 2-Aug-2025; high-risk from 2-Aug-2026 | EUR-Lex 32024R1689 | monthly |
| Annex III.5 (public services, including tax administration) | High-risk classification for tax-admin scoring / selector systems. Implementing acts pending | EUR-Lex + Commission AI Office | monthly |
| Digital Omnibus (provisional 7-May-2026) | Changes to GPAI transparency deadlines; pending formal Council/Parliament adoption | EUR-Lex | monthly |
| Art. 22 GDPR — automated decision making | CJEU doctrine evolving. Verify 2025-2026 judgments | curia.europa.eu | quarterly |
| Local tax-admin AI use cases (selectors, scoring) | Per `references/jurisdictions/<iso>.md` §5 | (local profile) | monthly |

## TRANSFER PRICING (OECD)

| Item | Status | Source | Re-check |
|---|---|---|---|
| OECD TP Guidelines 2022 (consolidation) | In force; verify amendments | oecd.org/tax/transfer-pricing | half-yearly |
| Pillar One Amount B | OECD framework Feb-2024 + implementation timeline. National adoption varies | OECD | quarterly |
| Local TP rules | Per `references/jurisdictions/<iso>.md` §5 | (local profile) | half-yearly |

## SUPRANATIONAL JUDICIAL DOCTRINE

| Item | Status | Source | Re-check |
|---|---|---|---|
| CJEU — ATAD and fundamental freedoms | Continuous watch. Cases on GAAR, CFC, exit tax | curia.europa.eu | quarterly |
| CJEU — DAC and confidentiality | Watch judgments on lawyer-client privilege in DAC6 | curia.europa.eu | quarterly |

## TCF / TAX GOVERNANCE DOCTRINE (SUPRANATIONAL)

| Item | Status | Source | Re-check |
|---|---|---|---|
| OECD Tax Control Frameworks (2016 + updates) | Reference framework. Verify subsequent FTA reports | oecd.org/tax | half-yearly |
| Netherlands Horizontal Monitoring / TCF | Reformed 2020+. Verify latest Belastingdienst updates | belastingdienst.nl | half-yearly |
| HMRC Corporate Criminal Offences (CCO) | In force. Watch enforcement actions | gov.uk/hmrc | half-yearly |
| Local cooperative-compliance regime | Per `references/jurisdictions/<iso>.md` §5 | (local profile) | half-yearly |

---

## HOW THIS FILE IS USED

When an output cites a date, threshold, criterion or administrative position **in one of these areas**, it must add a note: *"This area moves — verify against [source]. See `tax-currency-watch.md` (supranational) and `jurisdictions/<iso>.md` §5 (local)."*

If any entry is updated → update the header's last-verified date.

To record each individual material verification, see `templates/verification-log.md` (dated control format).

---

*This file goes stale. Verified as of 2026-05-17. Update when drift is detected.*
