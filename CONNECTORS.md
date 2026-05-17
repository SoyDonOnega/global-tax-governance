# CONNECTORS

> Categories of external tools the skills may use.
> By default the plugin is **filesystem-only** — it requires no external connectors.
> The connectors listed below are **optional** and extend capabilities.

---

## HOW TOOL REFERENCES WORK

The plugin describes workflows in terms of **categories** of tools, not specific products. This lets any user customize per the connectors available in their Cowork or Claude Code environment.

Where a skill references a category with `~~`, substitute the concrete tool configured in that category.

---

## CATEGORIES USED

| Category | Placeholder | Typical options | Skills that use it |
|---|---|---|---|
| **Document storage (VDR)** | `~~vdr` | Box · Datasite · iManage · Egnyte · Drive · SharePoint | `tp-analysis review-existing` · `audit-defense` (administrative file documents) · `cbcr-review` (entity FS) |
| **CLM / Contract management** | `~~clm` | Ironclad · Icertis · LinkSquares · Agiloft · Conga | `tp-analysis` (intercompany agreements) |
| **ERP / accounting** | `~~erp` | SAP · Oracle · NetSuite · Workday · Sage | `excel-replicate` (ERP support) · `cbcr-review` (financial data) · `pillar-two-rollout` (covered-taxes data) |
| **Mail client** | `~~mail` | Outlook · Gmail · Proton · Apple Mail | `query-email send-ready` · `audit-defense` (administrative correspondence) |
| **Project tracker** | `~~tracker` | Jira · Asana · Linear · Monday | `tcf-program roadmap` (controls and milestones surface to the tracker) |
| **Tax authority search** | `~~tax-authority-search` | (custom MCP) per-jurisdiction (e.g. AEAT PETETE · TEAC · BOE · CENDOJ for ES) | `dgt-teac-watch pull` |
| **Tax engine** | `~~tax-engine` | Vertex · OneSource · Avalara · SAP TDF | `excel-replicate` (large-corporate VAT) — optional |
| **AI inventory tool** | `~~ai-inventory` | GovernAI · Credo · OneTrust AI | `ai-tax-governance inventory` — alternative to manual inventory |
| **CbCR transmission** | `~~cbcr-platform` | (non-standard) AEAT modelo 231 · transmission portal | `cbcr-review validate` (payload prep) |
| **Slack / Teams** | `~~chat` | Slack · Teams · Discord | Notifications on `phase_complete` — optional |

---

## OPERATING MODES

### Mode 1 — Filesystem-only (default)
No connectors. All interaction is with local files (PDF, Excel, markdown). Skills `tp-analysis`, `cbcr-review`, `excel-replicate`, `query-email`, `audit-defense` work at 100%.

### Mode 2 — Filesystem + Web (optional)
Adds WebFetch / WebSearch so `dgt-teac-watch pull` can query official primary-source search engines (per active jurisdiction profile §3). Honest limitation: when no connector is present, `dgt-teac-watch` declares the gap and asks the user to supply the consultas / resoluciones.

### Mode 3 — Filesystem + Web + connected MCPs (recommended)
When the user has Cowork with enterprise connectors (Box VDR, Outlook, ERP), skills detect and use them via `~~` references.

---

## CONNECTOR DETECTION

The skill `onboarding --check-integrations` re-probes which connectors are active and updates the `## INTEGRATIONS` section of the plugin's `CLAUDE.md`.

Example resulting section:

```markdown
## INTEGRATIONS

Last probed: 2026-05-16

| Category | Placeholder | Configured tool | Status |
|---|---|---|---|
| Document storage | `~~vdr` | Box | OK |
| Mail | `~~mail` | Outlook | OK |
| Tax authority search | `~~tax-authority-search` | — | NOT CONFIGURED |
| ERP | `~~erp` | SAP | OK |
```

Skills that require a `NOT CONFIGURED` connector detect the absence and operate in degraded mode (with a flag to the user) — they do not fail.

---

## PYTHON DEPENDENCIES (orchestrator)

The `orchestrate/orchestrate.py` component requires Python 3.10+ and the dependencies pinned in `requirements.txt`:

```
jsonschema>=4.0
pyyaml>=6.0
openpyxl>=3.1   # excel-replicate (Excel rollforward)
pypdf>=4.0      # audit-defense, cbcr-review (PDF intake)
reportlab>=4.0  # tp-analysis, cbcr-review public narrative (PDF output)
```

Install:

```bash
pip install -r requirements.txt
```

The rest of the plugin (skills, sub-agents in markdown) **does not require Python** — it runs purely on markdown files interpreted by Claude.

---

## SKILLS BY CONNECTOR DEPENDENCY

| Skill | Filesystem | Web | MCPs |
|---|---|---|---|
| onboarding | ✓ required | optional (check-integrations) | optional |
| customize | ✓ | — | — |
| matter-workspace | ✓ | — | — |
| pillar-two-rollout | ✓ | — | optional `~~erp` |
| tcf-program | ✓ | — | optional `~~vdr` · `~~tracker` |
| tp-analysis | ✓ | — | optional `~~vdr` · `~~clm` |
| cbcr-review | ✓ | — | optional `~~erp` · `~~cbcr-platform` |
| dac-reporting | ✓ | — | — |
| ai-tax-governance | ✓ | — | optional `~~ai-inventory` |
| dgt-teac-watch | ✓ | recommended | recommended `~~tax-authority-search` |
| excel-replicate | ✓ | — | optional `~~erp` · `~~tax-engine` |
| query-email | ✓ | — | optional `~~mail` |
| audit-defense | ✓ | recommended | recommended `~~tax-authority-search` |

---

## NOTE ON PRIVILEGE AND CONFIDENTIALITY

Connectors that grant access to client data (VDR, ERP, mail, CLM) imply **trust boundaries**:
- The plugin does not export client data outside the local filesystem unless the user explicitly directs it to.
- When `Cross-matter context: off` (default), skills cannot read matters other than the active one.
- `critic-cross-matter-leak` runs before closing any deliverable.
- `orchestrate/audit/handoff-audit.jsonl` records every handoff but **never** the payload body — only metadata (timestamp, sprint_id, agents, intent, payload hash).
