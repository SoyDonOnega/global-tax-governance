# CHANGELOG

All notable changes to this plugin will be documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] — 2026-05-17

### Initial release

Tax governance skill library for senior practitioners. Thirteen skills, six transversal critics, jurisdiction-agnostic practice profile.

#### Skills (13)

- **Core**: `onboarding` · `customize` · `matter-workspace`
- **Flagship tax**: `pillar-two-rollout` · `tcf-program` · `tp-analysis` · `cbcr-review` · `dac-reporting` · `audit-defense` · `dgt-teac-watch` · `ai-tax-governance`
- **Utility**: `excel-replicate` · `query-email`

Each skill is a self-contained recipe (plan · draft · adversarial pass · critic pass · close decision tree).

#### Critics (6)

The only sub-agents shipped. Invoked by skills at the close pass via the `Task` tool.

- `critic-citation-exactness` — every cited authority matches the format declared in the active jurisdiction profile.
- `critic-currency-watch` — every cited date / threshold / transposition is current against the supranational + local watch.
- `critic-reviewer-note` — header complete and dated.
- `critic-decision-tree` — close carries a decision tree with ≥3 actionable branches.
- `critic-finding-state` — every finding has a state (`answered` · `not_present` · `unclear` · `needs_review`); no blanks.
- `critic-cross-matter-leak` — no leak across matters when isolation is `off`.

#### Practice profile

- `CLAUDE.md` jurisdiction-agnostic. The active jurisdiction is declared via an ISO 3166-1 alpha-2 code that points to `references/jurisdictions/<iso>.md`.
- `references/jurisdictions/`: `README.md` (convention) · `_template.md` (8-section template) · `es.md` (Spain seed profile carrying LGT · LIS · LIRPF · LIVA · LIRNR · LIP · TRLRHL · DGT · TEAC · CBPT references).
- Onboarding asks the user for jurisdiction and either loads the matching profile or walks them through the template.

#### Disciplinary artifacts (transversal)

- Reviewer-note header template (`references/templates/reviewer-note-header.md`).
- Decision-tree close template (`references/templates/decision-tree-close.md`).
- Verification-log template (`references/templates/verification-log.md`).
- Company-profile template (`references/templates/company-profile.md`).
- Tax currency watch — supranational layer (`references/resources/tax-currency-watch.md`); the local layer lives in each jurisdiction profile §5.

#### Closed-schema handoffs

Three intents survive: `critic_check`, `request_clarification`, `escalate_to_human`. JSON Schema in `references/handoff-schemas/intents.schema.json`. Per-intent payload schemas under `references/handoff-schemas/payloads/`.

#### Runtime — audit-only

- `hooks/post_task.py` registered as a `PostToolUse` hook on the `Task` tool. Appends one record per invocation to `orchestrate/audit/handoff-audit.jsonl` (timestamp · source · target · prompt hash · response hash). Metadata only — bodies are never stored.
- Rotation at `GTG_AUDIT_ROTATE_BYTES` (default 5 MiB).
- `orchestrate/orchestrate.py` is a CLI validator + replay tool (does not orchestrate anything at runtime).

#### Customization

- Cold-start interview branched by practice type (in-house tax director · Big Four advisor · boutique · academic-practitioner · combination).
- Seed extraction with delta computation from six seed types (technical memo · TCF doc · board paper · opinion letter · query email · recurring Excel).
- Semantic placeholders: `[PLACEHOLDER]` · `[PENDING]` · `[DEFAULT]` · `[LIMITED DATA — N docs reviewed]`.
- `customize` skill for surgical slot edits with downstream impact analysis.

#### Tests + CI

- `tests/test_contracts.py`: 13 skills, 3 intents, allowlist shape, intents module parity.
- `tests/test_hooks.py`: passthrough · audit-on-task · rotation. 4/4 green.
- GitHub Actions CI runs both suites + JSON Schema and YAML validation on push and PR.

#### Documentation

- `README.md` — install · skills · critics · jurisdiction model · runtime · repo links.
- `GUIDE.md` — operational walkthrough end-to-end.
- `CONNECTORS.md` — MCP integration categories.
- `SECURITY.md` — vulnerability disclosure via GitHub Security Advisories.
- `CONTRIBUTING.md` — required checks · style · scope discipline.
- `CODE_OF_CONDUCT.md` — Contributor Covenant 2.1 by reference.
- `references/coverage-matrix.md` — skills mapped to areas of the discipline.
- `references/tax-function-lens.md` — operationalises the function-and-strategy lens.
