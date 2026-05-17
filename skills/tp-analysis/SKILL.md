---
name: tp-analysis
description: >
  End-to-end transfer pricing analysis: documentation (master file · local file ·
  CbCR alignment) · DEMPE per intangible · financial transactions (OECD TPG
  Chapter X 2020) · cost-sharing · business restructurings (OECD TPG Chapter IX) ·
  benefit test / willingness-to-pay over intercompany service charges using
  email and contract evidence (OECD TPG Chapter VII). Aligned with the
  active jurisdiction profile (e.g. Spanish Art. 18 LIS + RIS Arts. 13-16 +
  Order HFP/816/2017 + OECD TPG 2022). Use when the user says "TP
  documentation", "master file", "local file", "benefit test", "willingness
  to pay", "intercompany services", "Chapter VII", "TP review", "OECD TPG",
  "DEMPE analysis", "financial transactions TP", "comparables".
---

# /global-tax-governance:tp-analysis

> End-to-end TP analysis workflow. Documents today the positions you'll defend tomorrow.

## SUBCOMMANDS

| Command | Action |
|---|---|
| `master` | Produce the master file (section by section) |
| `local <entity>` | Produce the local file for one entity |
| `cbcr` | Produce CbCR Tables 1/2/3 (invokes `cbcr-review map`) |
| `review-existing` | Audit client's / target's existing TP doc |
| `dempe <intangible>` | Specific DEMPE analysis (OECD TPG Chapter VI) |
| `financial-tx <type>` | Intercompany finance analysis (OECD TPG Chapter X 2020) |
| `benefit-test <service-category>` | Benefit / willingness-to-pay test on intercompany services using email and contract evidence (OECD TPG Chapter VII) |

## FLOW

1. **Scope** — confirm whether the build is Master file, Local file, CbCR alignment, DEMPE for one intangible, financial transaction, **benefit test** on intercompany services, APA prep or MAP prep. Identify the in-scope transactions and the tested party per transaction.
2. **Section build** (per OECD TPG / local TP rules — verify the current local TP rules in `references/jurisdictions/<iso>.md`):
   - Group overview · industry · controlled-transaction inventory · functional analysis (functions · assets · risks)
   - Comparability analysis · method selection · economic analysis · arm's-length range
   - Conclusion per transaction, with documentation of judgement calls.
3. **Arm's-length stress test** — challenge each tested figure against the strongest contra-argument (selection of comparables, range bounds, year selection, working-capital adjustments, loss-making comparables). For financial transactions, separately stress credit rating, implicit support, currency-of-funding, term-spread.
4. **DEMPE & substance** — for intangibles or financial functions, document who actually performs Development · Enhancement · Maintenance · Protection · Exploitation; flag mismatches between contractual allocation and substance.
5. **Benefit test (if `benefit-test <category>`)** — see the dedicated subsection below; validated against [`references/criteria/benefit-test.criteria.yaml`](../../references/criteria/benefit-test.criteria.yaml).
6. **Critic pass** — `critic-citation-exactness` (OECD TPG paragraphs, local TP article numbers), `critic-currency-watch` (TPG editions move; local TP doctrine moves), `critic-reviewer-note`, `critic-decision-tree`.
7. **Close** — deliverable bundle + recommendation per close decision tree.

## BENEFIT TEST — `benefit-test <service-category>`

OECD TPG Chapter VII frames intra-group services under the benefit test (the recipient receives economic or commercial value enhancing its commercial position) and the willingness-to-pay equivalence (an independent enterprise in comparable circumstances would have been willing to pay, or perform the activity itself). Five categorical exclusions must be ruled out before a charge is recognised: shareholder activities · duplicative services · incidental benefits · on-call services with no actual call · passive association benefits.

### Inputs

- `matters/<id>/inputs/intercompany-emails/<category>/` — corpus of intercompany correspondence (`.eml`, `.md`, or plain text). The skill reads up to ~50 items directly (standalone mode). For larger corpora, the behaviour depends on the `Companion plugins` field in `CLAUDE.md`:
  - `claude-for-legal: present` → the skill offers to delegate batch extraction to `/corporate-legal:tabular-review` with the schema described below and ingest its grid.
  - `claude-for-legal: absent` → the skill processes the corpus in chronological batches of ≤50, producing one evidence grid per batch, then merges them at the close. Slower but standalone; warns the user that claude-for-legal would have made the run faster.
- `matters/<id>/inputs/intercompany-contracts/<category>/` — service agreements, addenda, SLAs.
- The active local file's service charge schedule (cost base, allocation key, mark-up) — read from `matters/<id>/findings/tp/local-file-<entity>-<fy>.md` if it exists.

### Per-category procedure

1. **Restate the charge.** Service category · provider · recipient · cost base composition · allocation key · mark-up (typically 5% under the OECD simplified approach for low value-adding services, OECD TPG §7.43-7.65). If the simplified approach is elected, verify the local jurisdiction has adopted it (see `references/jurisdictions/<iso>.md` §5).
2. **Apply the five exclusions in order**:
   - **Shareholder activity** — is the activity performed for the parent's interest as shareholder (consolidation accounting, parent-level governance, parent's investor relations, SOX-equivalent compliance solely required by the parent)? If yes → no charge defensible.
   - **Duplication** — does the recipient already perform the function locally? Documented duplications fail unless temporary, in-transition, or short-term decision support.
   - **Incidental benefit** — is the benefit a side-effect of services rendered to other group members (e.g. group purchasing volume → incidental price benefit)? Side-effects don't carry a charge.
   - **On-call without actual call** — if the charge is for availability, is there evidence the service was effectively available and used during the period? Empty on-call fails.
   - **Passive association** — uplift from being part of the group (credit rating, branding spillover) is not a service.
3. **Willingness-to-pay test.** For each surviving sub-category, build the evidence pack from the email/contract corpus:

   | Evidence type | What counts | Where it comes from |
   |---|---|---|
   | Request from recipient | The local entity asks for the service in writing | Inbound emails to provider |
   | Acknowledgement of value | The local entity confirms benefit received | Outbound emails after delivery |
   | Specification | Scope of work, deliverables, deadlines | Emails or SoW addenda |
   | Delivery confirmation | The provider documents the deliverable handed over | Provider's outbound emails |
   | Cost-base trace | The work hours / cost items in the charge map to documented work | Timesheets, project codes, expense receipts referenced in emails |
   | Repeat-purchase test | If the same service has been requested across years from the same provider, infer continued willingness to pay | Multi-year email comparison |

   Cite **verbatim** per evidence row: `date · sender · recipient · subject · quote` and the source location (`inputs/intercompany-emails/<category>/<file>.eml#L<line>`). No paraphrase passed as literal — the citation critic will reject.
4. **Cost-base sanity check.** Trace each cost element back to a documented work item. Pure overhead allocation with no work mapping fails the benefit test even if WTP evidence exists for the category.
5. **Cross-check against simplified approach (if elected).** OECD TPG §7.45 enumerates qualifying activities (accounting, HR admin, IT support, legal, public relations, etc.) and excludes core business activities, R&D, manufacturing services, intermediation, insurance, etc. If the elected category is non-qualifying, simplified approach not available — full TP analysis required.
6. **Conclusion per category.** Verdict: `pass` · `pass with conditions` · `partial fail` · `fail`. For each: what evidence supports, what is missing, what would close the gap (e.g. "request a written delivery confirmation from <party> for project X covering Q2-Q3").
7. **Critic pass.** Same as the main flow; `critic-finding-state` is mandatory here — every service category must carry a state, never blank.

### Output

- `matters/<id>/findings/tp/benefit-test-<category>-<fy>.md` — per category memo with verdict, evidence table, and gaps.
- `matters/<id>/findings/tp/benefit-test-summary-<fy>.md` — roll-up across all categories with the verdict matrix and total deductible / non-deductible breakdown.
- `matters/<id>/findings/tp/benefit-test-evidence-<category>-<fy>.csv` — the evidence grid (one row per email, columns: date · sender · recipient · subject · evidence_type · verbatim_quote · location · category).

### Trade-off note

The benefit test is the **most evidence-dependent** TP analysis. Strong substantive conclusions stand only if the evidence is exact-cite. If the email corpus is sparse, mark the verdict as `partial fail — evidence gap` and emit the gap list. Do not bluff. The skill **never invents email content** — if a quoted line is not literally in the inputs, it is not in the deliverable.

### When the benefit test result feeds defense

If the matter is in `audit-defense` (the tax authority is challenging deductibility of intercompany service charges under the recipient's deduction rules — e.g. Art. 15.e LIS in Spain, equivalent in other jurisdictions), the `benefit-test-summary` is the primary evidence pack to attach to alegaciones / recurso. The audit-defense skill cross-references this output.

## COVERAGE

- TP (★): core
- IT (partial): CDI relevance · MAP · APA framework
- Strategy (partial): positioning vs. AEAT and foreign tax authorities

## STRATEGY ANGLE

TP doc is **pre-built defensive posture**. The quality of the local file determines the strength of any later MAP / APA / audit. Weak documentation today = weak defense tomorrow.

For decisions: posturing aggressively with ex-post disclaimer (HTVI) vs. conservatively with bilateral APA.

## FUNCTION LENS

- **Controller**: reconciliations between TP doc and accounts.
- **CFO**: executive summary of TP exposure.
- **External auditor**: reads in full during the financial audit.
- **AEAT**: receives modelo 232 + local file as required under Art. 18.

## TRAPS

- Master / local inconsistent across jurisdictions (AEAT compares).
- CbCR contradicts the local-file narrative.
- Method elected without explicit discard of alternatives (OECD hierarchy not strict but motivate).
- Stale comparables (>3 years without refresh).
- Secondary adjustment (Art. 18.11 LIS) not considered.
- Pre-2020 treatment of financial transactions (without Chapter X) → mandatory update.
- DEMPE light — function-by-entity analysis, not boilerplate.
- Hard-to-value intangibles without ex-post adjustment disclaimer.

## DELIVERABLES

- `matters/<id>/findings/tp/master-file-<fy>.md`
- `matters/<id>/findings/tp/local-file-<entity>-<fy>.md` × entity
- `matters/<id>/findings/tp/cbcr-narrative-<fy>.md`
- `matters/<id>/findings/tp/dempe-<intangible>.md` × intangible
- `matters/<id>/findings/tp/financial-tx-<type>.md` × transaction type
- `matters/<id>/findings/tp/benefit-test-<category>-<fy>.md` × service category
- `matters/<id>/findings/tp/benefit-test-summary-<fy>.md`
- `matters/<id>/findings/tp/benefit-test-evidence-<category>-<fy>.csv` × service category

## CLOSE

- A — CFO sign-off + submission to regulator (modelo 232 if AEAT)
- B — Escalate — high-risk transactions to senior reviewer before submission
- C — Refresh comparables / additional economic analysis
- D — Monitor Pillar One Amount B + OECD TPG amendments
- E — Other
