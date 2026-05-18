# COVERAGE MATRIX

> Skill × discipline-area mapping with coverage grades.
> Ensures every active area has ≥ 1 skill with core coverage.

---

## LEGEND

- **★** core — the skill covers the area as a primary topic
- **◐** partial — the skill touches the area laterally or in specific scenarios
- **◯** tangential — the skill may invoke the area in edge cases
- **meta** — configuration / orchestration skill, applies to every area

---

## AREAS

- **P2** — Pillar Two / GloBE
- **TP** — Transfer Pricing (incl. intra-group services benefit test)
- **IT** — International Taxation (treaty · PE · MAP · withholding · CFC · MLI · exit · ATAD2)
- **Tax Advice** — Memos · opinions · binding-ruling requests · APAs · MAP requests
- **Local Corp Tax** — Local corporate taxation, sourced from the active jurisdiction profile
- **Function** — Tax function design & controls (TCF · cooperative compliance)
- **AI + Tax** — AI Act in the tax function · AIA · taxpayer defense against AI-driven inspection
- **ESG / Discl** — Tax transparency · public CbCR · GRI 207 · ESG tax disclosure

---

## MATRIX

| Skill | P2 | TP | IT | Tax Advice | Local Corp Tax | Function | AI + Tax | ESG / Discl |
|---|---|---|---|---|---|---|---|---|
| `onboarding` | meta | meta | meta | meta | meta | meta | meta | meta |
| `customize` | meta | meta | meta | meta | meta | meta | meta | meta |
| `matter-workspace` | meta | meta | meta | meta | meta | meta | meta | meta |
| `pillar-two-rollout` | ★ | ◐ | ◐ | ◯ | ◐ | ◯ | ◯ | ◐ |
| `tcf-program` | ◐ | ◯ | ◯ | ◯ | ◐ | ★ | ◐ | ◯ |
| `tp-analysis` | ◯ | ★ | ◐ | ◐ | ◐ | ◯ | ◯ | ◯ |
| `cbcr-review` | ◐ | ★ | ◐ | ◯ | ◯ | ◯ | ◯ | ★ |
| `dac-reporting` | ◯ | ◯ | ★ | ★ | ◐ | ◯ | ◐ | ◯ |
| `ai-tax-governance` | ◯ | ◯ | ◐ | ★ | ◯ | ★ | ★ | ◯ |
| `dgt-teac-watch` | ◐ | ◐ | ◐ | ★ | ★ | ◯ | ◯ | ◯ |
| `excel-replicate` | ★ | ◐ | ◯ | ◯ | ★ | ◐ | ◯ | ◯ |
| `query-email` | ◐ | ◐ | ◐ | ★ | ★ | ◯ | ◯ | ◯ |
| `audit-defense` | ◐ | ◐ | ◐ | ★ | ★ | ◯ | ◐ | ◯ |

---

## VERIFICATION — NO GAPS

| Area | Skills with ★ coverage |
|---|---|
| P2 | `pillar-two-rollout` · `excel-replicate` (GloBE worksheet) |
| TP | `tp-analysis` · `cbcr-review` |
| IT | `dac-reporting` |
| Tax Advice | `dac-reporting` · `ai-tax-governance` · `dgt-teac-watch` · `query-email` · `audit-defense` |
| Local Corp Tax | `dgt-teac-watch` · `excel-replicate` · `query-email` · `audit-defense` |
| Function | `tcf-program` · `ai-tax-governance` |
| AI + Tax | `ai-tax-governance` |
| ESG / Discl | `cbcr-review` |

✓ Every area has ≥ 1 skill with core coverage.

---

## OBSERVATIONS

- **`audit-defense`** and **`dgt-teac-watch`** are the most cross-cutting substantive skills (★ in three or more areas each) — reflecting that both procedural defense and doctrine-watching span every technical area.
- **Strategy** is not a separate column — every substantive skill carries a mandatory strategy lens (per the workspace transversal rules). It surfaces inside each skill's "Strategy angle" section rather than as a standalone skill.
- **Tax function design does not have a standalone skill**: `tcf-program` (controls layer) and `ai-tax-governance` (AI in the function) cover the operating-model dimension together. If a redesign of the operating model itself is needed, it surfaces as an `audit-defense` or `tcf-program` close decision tree branch toward escalation.
- **ESG / Disclosure** rests primarily on `cbcr-review` with feed-ins from `tcf-program`. Add a dedicated skill in a later version if the practice volume justifies it.
- **`tp-analysis benefit-test`** materially strengthens TP coverage at the audit-defense intersection — the resulting evidence pack is the canonical attachment when AEAT (or equivalent) challenges intercompany service deductibility.

---

## HOW TO USE THIS MATRIX

- **Pre-flight skill selection**: given a question, identify the area(s) → choose the skill with ★ coverage (or ◐ if ★ doesn't fit the matter).
- **Plugin customization**: if an area is `off` in `## ACTIVE AREAS` of `CLAUDE.md`, skills with that area as core can stay dormant — they are not surfaced as suggestions.
- **Gap analysis**: if the user's portfolio includes an area marked only ◯ or ◐ across every skill, consider adding a dedicated skill in the next version.
