# SECURITY

## Scope

`global-tax-governance` is a Claude plugin made of markdown skills, sub-agent definitions and a single Python orchestrator (`orchestrate/orchestrate.py`). It runs locally inside Claude Code or Claude Desktop. It does not ship a server, does not call external APIs on its own, and does not transmit data outside the host machine.

## Data handling

- **No client data in this repository.** Per-matter workspaces live under `matters/<slug>/` on the user's machine and are excluded from version control via `.gitignore`. The repository ships only templates under `references/templates/`.
- **No telemetry.** The plugin does not phone home.
- **Audit log is metadata only.** `orchestrate/audit/handoff-audit.jsonl` records timestamp, sprint id, source/target agent, intent and a SHA-256 hash of the payload. The payload body itself is never written to disk by the orchestrator.
- **Connectors are user-configured.** Any external integration (VDR, ERP, mail, CLM, tax-authority search) is connected by the user through their own Claude Code / Cowork configuration. Credentials are never stored in this plugin.
- **Cross-matter isolation by default.** `CLAUDE.md` ships with `Cross-matter context: off`. A dedicated critic (`critic-cross-matter-leak`) flags any reference to a matter other than the active one before a deliverable closes.

## User responsibilities

- Do not commit `matters/`, `out/`, `.env`, secrets files, or any client document to a public fork.
- Treat `orchestrate/audit/handoff-audit.jsonl` as potentially sensitive — even hashed, the metadata trail (timestamps, sprint ids, intent sequence) can reveal a matter's existence. The default `.gitignore` excludes it.
- Review the connector list in `CONNECTORS.md` before enabling integrations on a host that holds privileged work product.

## Reporting a vulnerability

If you find a security issue — for example, a path that could exfiltrate matter data, a schema validation bypass that allows free-text injection into a steering prompt, or a way to leak audit-log payload bodies — please **do not open a public issue**.

Open a private security advisory on GitHub:

> https://github.com/SoyDonOnega/global-tax-governance/security/advisories/new

Expect an acknowledgement within 7 days. Fixes for confirmed issues will be released as a patch version with a `Security` entry in `CHANGELOG.md`.

## Out of scope

- Hardening of the host operating system, of Claude Code itself, or of any third-party MCP connector.
- Correctness of substantive tax conclusions produced by the plugin. The plugin is a structured drafting harness; the practitioner remains responsible for the legal output.
