# JURISDICTIONS

Per-jurisdiction profile files. Each file is the local supplement to the supranational layer (OECD · EU). Skills load the active jurisdiction from `CLAUDE.md` (field `Primary jurisdiction`) and read the matching profile here.

## File naming

`<iso2>.md` using ISO 3166-1 alpha-2 lowercase. Examples: `es.md`, `nl.md`, `de.md`, `ie.md`, `lu.md`, `uk.md`, `us.md`, `mx.md`.

## What goes in a jurisdiction profile

A profile is short, dense, and **citation-exact**. Sections:

1. **Source-of-law hierarchy** — the legal corpus (constitution · code · regulations · administrative criteria · jurisprudence) with the authoritative bodies named.
2. **Citation formats** — exact templates for every authority a practitioner cites (norm · supreme court · administrative ruling · tribunal · doctrine).
3. **Tax authorities & cooperative compliance** — the administration, the cooperative-compliance regime (if any), the body that publishes binding rulings.
4. **Core taxes** — income · corporate · VAT · withholding · wealth · non-resident, with the local act name and the standard reference vocabulary.
5. **Currency watch (local layer)** — the Pillar Two transposition status, DAC implementation, public CbCR transposition, AI Act intersection — with primary-source links.
6. **Anti-hallucination guardrails** — the bodies and ruling types the practitioner relies on; the plugin will reject invented references against this list.
7. **Escalation triggers (local)** — adverse precedent, retroactive criterion change, etc., specific to the local enforcement environment.

## Conventions

- **One profile per jurisdiction, no shadow copies.** If you advise on multiple jurisdictions, list them in `CLAUDE.md` and create one profile per jurisdiction. The active jurisdiction is the one in scope for the running matter.
- **Citation format is non-negotiable.** Every cited authority follows the format declared in the profile. Skills surface raw citations and the citation critic checks the form.
- **Primary source link required.** Every entry under "currency watch (local layer)" carries the link to the authoritative publication (BOE, Staatsblad, Bundesgesetzblatt, etc.).
- **Update by `/customize`.** Use `/global-tax-governance:customize` to amend a profile rather than edit raw — the customize skill keeps the change log consistent across `CLAUDE.md` and the jurisdiction file.

## Adding a new jurisdiction

Copy `_template.md` to `<iso2>.md` and populate it from primary sources. Cite the bodies, the codes, the formats. Run the citation critic against a sample deliverable from that jurisdiction before relying on the profile in production.

Profiles shipped with the plugin:

- `es.md` — Spain (the seed profile; rich because it is the maintainer's home jurisdiction).
- `_template.md` — empty template for any other jurisdiction.
