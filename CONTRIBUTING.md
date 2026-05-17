# Contributing

`global-tax-governance` is a personal-use Claude plugin published as open source. Pull requests are welcome but the maintainer's roadmap takes priority. This document describes the structural conventions a contribution must follow and the checks it must pass.

---

## Ground rules

1. **No client data, ever.** Do not include real matter content, real client names, real entity tables, real returns, real ruling requests, or any document that could plausibly contain privileged information. Anything matter-shaped that lands in a PR must be synthetic.
2. **No invented authority.** New skill, agent or reference content must not introduce fabricated jurisprudence, DGT consultations, TEAC resolutions, OECD guidance numbers or doctrinal citations. If you reference primary source material, cite it exactly per the conventions in `README.md` §CITATION CONVENTIONS.
3. **Scope discipline.** One PR = one concern (a single skill, a single agent, a single bugfix). Multi-area refactors should be split.

---

## Repository layout

```
.claude-plugin/plugin.json     Plugin manifest (name, version, keywords)
CLAUDE.md                      Practice profile (template — populated by /onboarding)
skills/<name>/SKILL.md         User-facing entry points (one folder per skill)
agents/<role>/<slug>.md        Sub-agents (planner / generator / evaluator / critic / monofunctional)
agents/_shared/                Shared frames loaded by every agent
orchestrate/orchestrate.py     Python orchestrator (closed-intent dispatch + audit log)
orchestrate/intents.py         Intent enum mirror of references/handoff-schemas/intents.schema.json
orchestrate/allowlist.yaml     Per-source (source_agent → target_agent) handoff matrix
references/handoff-schemas/    JSON Schema for intents + per-intent payloads
references/criteria/           YAML validation criteria (aia, disclosure, memo, tcf, tp)
references/jurisdictions/      Per-jurisdiction profile files (one per ISO 3166-1 alpha-2)
references/templates/          Reviewer-note header · decision-tree close · verification log · company profile
references/resources/          Tax currency watch (moving areas: Pillar Two, DAC, AI Act, …)
```

When adding a new skill or sub-agent, follow the existing structure in the same folder. Do not invent new top-level directories without a prior issue.

---

## Required checks before opening a PR

Run locally (or rely on CI, which runs the same):

```bash
# 1. Python orchestrator parses
python -m py_compile orchestrate/*.py

# 2. JSON Schemas are self-consistent
python -c "import json, jsonschema; jsonschema.Draft202012Validator.check_schema(json.load(open('references/handoff-schemas/intents.schema.json')))"

# 3. Sprint contracts and criteria YAML load cleanly
python tests/test_contracts.py

# 4. (Optional) Run the orchestrator in validate-only mode against a sample payload
python orchestrate/orchestrate.py --validate-only --payload <your-sample.json>
```

CI must be green before review.

---

## PR description

Include:

- **What** — one-paragraph summary of the change.
- **Why** — the concrete tax-practice problem it addresses (no abstract refactors without a use case).
- **Surface** — list of files touched, grouped by category (skill / agent / reference / orchestrator / docs).
- **Verification** — the exact commands or steps you ran. If the change is in a skill that produces a deliverable, attach a sanitized excerpt of the output.

---

## Style

- English for all operational instructions to Claude. Spanish primary-source references are preserved as-is (proper-noun citations).
- B&W minimalist aesthetic — no color, no gold, no emoji, no ornament. ALL CAPS section headings in deliverable templates.
- One topic per markdown section. Avoid prose padding.

---

## Security issues

Do **not** file a public issue or PR for a security concern. Open a private security advisory — see `SECURITY.md`.
