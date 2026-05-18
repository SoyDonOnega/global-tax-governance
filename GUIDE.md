# GUIDE

Operational walkthrough for the `global-tax-governance` plugin, v0.1.0.

This guide reads top-down: install → onboard → jurisdiction profile → matter → run a skill → close. Each section is short on purpose.

---

## 1 — INSTALL

Inside Claude Code:

```text
/plugin marketplace add SoyDonOnega/global-tax-governance
/plugin install global-tax-governance
```

Optional: install the Python runtime so you can validate handoff payloads and replay the audit log from the CLI.

```bash
pip install -r requirements.txt
```

---

## 2 — ONBOARD

```text
/global-tax-governance:onboarding
```

The interview asks, in order:

1. **Setting** — type of practice (in-house · Big Four · boutique · academic-practitioner), role, team size.
2. **Footprint** — primary jurisdiction (ISO 3166-1 alpha-2) + secondary recurring jurisdictions.
   - Each ISO must match a profile under `references/jurisdictions/`. If a profile is missing, onboarding walks you through `_template.md` to author one.
3. **Risk posture** — overall appetite, red lines, materiality threshold, hedging level.
4. **Active areas** — multi-select against the supranational currency watch.
5. **Language & doctrine citation** — default working language + doctrine citation style. Statute and jurisprudence formats come from the jurisdiction profile.
6. **Profile branch** — specific questions per practice type.
7. **Integrations** — probe available MCPs (`~~vdr`, `~~mail`, `~~erp`, `~~clm`, `~~tracker`, `~~tax-authority-search`, `~~chat`).
8. **Seeds (optional, strongly recommended)** — supply one of each: prior technical memo, TCF doc, board paper, opinion letter, query email, recurring Excel. The skill extracts the **delta between declared style and actual style** and records it in `## HOUSE STYLE LEARNED FROM SEEDS`.

Output: `CLAUDE.md` populated, semantic placeholders cleared, `[PENDING]` markers where you paused.

---

## 3 — JURISDICTION PROFILE

The active jurisdiction's profile is the source of truth for: source-of-law hierarchy, citation formats, tax authority, core taxes, local currency watch, anti-hallucination guardrails, escalation triggers.

```
references/jurisdictions/
├── README.md       Convention and file naming
├── _template.md    8-section template — copy and fill for a new jurisdiction
└── es.md           Spain seed profile (LGT · LIS · LIRPF · LIVA · LIRNR · LIP · TRLRHL · DGT · TEAC · CBPT)
```

To add your jurisdiction:

```bash
cp references/jurisdictions/_template.md references/jurisdictions/<iso2>.md
```

Then run `/global-tax-governance:customize` to walk through the eight sections (or fill manually and run the citation critic against a sample deliverable to verify).

---

## 4 — MATTER

Every substantive piece of work happens inside a matter.

```text
/global-tax-governance:matter-workspace new <slug>
```

Creates the structure:

```
matters/<slug>/
├── matter.md            client · sector · listed Y/N · jurisdictions · subject · milestones · team · areas · risk
├── verification-log.md  dated log of primary-source verifications
├── history.md           append-only event log
├── findings/            substantive outputs per workstream
├── inputs/              client material
└── correspondence/      query emails, tax-authority correspondence
```

Switch with `matter-workspace switch <slug>`. Close with `matter-workspace close <slug>` (archive, read-only). Default isolation: `Cross-matter context: off` — no skill may read a matter other than the active one.

---

## 5 — RUN A SKILL

Each skill is self-contained: it plans, drafts, runs an adversarial pass and invokes the relevant critics at close. The thirteen are:

| Skill | Trigger |
|---|---|
| `pillar-two-rollout` | `/...:pillar-two-rollout scope` then `run-jurisdiction <iso>` then `consolidate` |
| `tcf-program` | `/...:tcf-program assess` then `design`, `roadmap`, `status` |
| `tp-analysis` | `/...:tp-analysis master` or `local` or `dempe <intangible>` or `financial-tx <type>` or `benefit-test <service-category>` |
| `cbcr-review` | `/...:cbcr-review map` then optionally `public-prep` |
| `dac-reporting` | `/...:dac-reporting triage <arrangement>` then `payload` |
| `audit-defense` | `/...:audit-defense intake` then per-phase commands |
| `dgt-teac-watch` | `/...:dgt-teac-watch digest <issue>` or `affects-matter <id>` |
| `ai-tax-governance` | `/...:ai-tax-governance inventory` then `aia <system>` or `aeat-selector-analysis` |
| `excel-replicate` | `/...:excel-replicate template <gold.xlsx> period <YYYY-Q>` |
| `query-email` | `/...:query-email draft` |
| `matter-workspace` | `new` · `switch` · `list` · `close` · `detach` · `current` · `add-workstream` |
| `customize` | `customize <slot>` — surgical edit with downstream impact analysis |
| `onboarding` | First run · `--redo` · `--check-integrations` · `--add-seed <path>` |

---

## 6 — CRITIC PASS

At the close of every substantive deliverable, the active skill invokes the relevant transversal critics via the `Task` tool. The six critics are:

| Critic | Checks |
|---|---|
| `critic-citation-exactness` | Every cited authority matches the format declared in the jurisdiction profile. |
| `critic-currency-watch` | Every cited date / threshold / transposition status is current. |
| `critic-reviewer-note` | Header complete and dated. |
| `critic-decision-tree` | Close has ≥3 actionable branches. |
| `critic-finding-state` | Every finding carries a state (`answered` · `not_present` · `unclear` · `needs_review`). |
| `critic-cross-matter-leak` | No leak across matters when isolation is `off`. |

Critics are terminal — they return a verdict to the calling skill and do not delegate further.

---

## 7 — CLOSE

Every substantive deliverable closes with a decision tree carrying at least three actionable branches. Pattern from `references/templates/decision-tree-close.md`:

```
A — <draft a final memo + escalation>
B — <escalate to partner / GC>
C — <request specific additional facts / documents>
D — <monitor / await>
E — Other
```

The decision is the practitioner's; the skill produces the structure.

---

## 8 — AUDIT LOG

Every `Task` call is recorded in `orchestrate/audit/handoff-audit.jsonl` (metadata + hashes, never the body). Rotation at `GTG_AUDIT_ROTATE_BYTES` (default 5 MiB).

Inspect:

```bash
python orchestrate/orchestrate.py --replay orchestrate/audit/handoff-audit.jsonl
```

Validate a hand-written handoff payload without sending it:

```bash
python orchestrate/orchestrate.py --validate-only --payload sample.json
```

Three intents are defined: `critic_check`, `request_clarification`, `escalate_to_human`.

---

## 9 — KEEPING THE PROFILE FRESH

Use `/customize` rather than editing files raw. Patterns:

- `customize jurisdiction es` — re-walk the Spanish profile.
- `customize materiality 5_000_000_EUR` — change one slot with downstream impact analysis.
- `customize active-areas` — re-tick the active-areas multi-select.
- `customize integrations` — re-probe MCPs.

`/customize` appends an audit row to `## CUSTOMIZATION LOG` so you can diff later.

---

## 10 — STANDALONE VS. WITH `claude-for-legal`

The plugin runs **standalone by default** — every skill processes its data in-line and the six critics ship inside the plugin. When `claude-for-legal` is also installed (declared during `/onboarding` and stored under `## COMPANION PLUGINS` in `CLAUDE.md`), the tax skills offer to delegate larger or generic workloads to it. Either mode produces the same tax-specific deliverable; the difference is throughput and where the heavy lifting happens.

If `claude-for-legal` is **present**, the following delegations become available (always opt-in, never automatic):

| Need | Use |
|---|---|
| Batch tabular review across many documents | `corporate-legal:tabular-review` |
| M&A diligence issue extraction | `corporate-legal:diligence-issue-extraction` |
| Diff a new regulation against current compliance | `regulatory-legal:reg-gap-analysis` |
| Diff between two versions of a norm | `regulatory-legal:policy-diff` |
| Track a clause's evolution across versions | `commercial-legal:amendment-history` |
| AI Impact Assessment as a standalone exercise | `ai-governance-legal:aia-generation` |

The tax-specific framing of those workflows lives in this plugin's skills (e.g., `cbcr-review`, `dgt-teac-watch`, `tp-analysis benefit-test`); the generic engines, when available, live in `claude-for-legal`. Cross-reference rather than duplicate.

If `claude-for-legal` is **absent**, each skill handles its workload in-line: small corpora are read directly (≤50 docs typical threshold), larger corpora are processed in chronological batches and merged at close. The deliverable shape is identical; only the throughput differs. The skill announces the mode at the start of the run so the user knows what to expect.

