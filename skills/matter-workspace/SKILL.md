---
name: matter-workspace
description: >
  Matter management (clients or assignments) for the global-tax-governance plugin
  — create, list, switch the active one, close, detach. Isolates context across
  clients (cross-matter-context off by default for privilege protection). Use
  when the user says "new matter", "switch matter", "list matters", "close
  matter", "current matter", "detach from matter", or when any substantive skill
  needs to identify the active matter.
---

# /global-tax-governance:matter-workspace

> Matter management with isolation by default. One matter = one client or one delimited assignment.

## SUBCOMMANDS

| Command | Action |
|---|---|
| `new <slug>` | Create matter from a free-form brief |
| `switch <slug>` | Change active matter |
| `list` | List matters (active · archived) |
| `close <slug>` | Archive matter (read-only, history retained) |
| `detach` | Work at practice level (no active matter) |
| `current` | Show the active matter |
| `add-workstream <slug> <ws>` | Add a workstream to an existing matter |

## MATTER STRUCTURE

```
matters/<slug>/
├── matter.md                # client · sector · listed Y/N · jurisdictions · subject · milestones · team · areas · risk
├── verification-log.md      # dated log of primary-source verifications
├── history.md               # append-only event log
├── findings/                # substantive outputs per workstream
│   ├── pillar-two/
│   ├── tcf/
│   ├── tp/
│   ├── cbcr/
│   ├── audit-defense/
│   ├── aia/
│   ├── strategy/
│   ├── function/
│   └── transparency/
├── inputs/                  # client material (with authorization)
└── correspondence/          # query emails, AEAT correspondence
```

## FLOW `new <slug>`

1. Verify the slug does not exist; create the directory and sub-directories listed above.
2. Parse the user's brief and populate `matter.md` with:
   - Client · sector · listed Y/N · jurisdictions (per `references/jurisdictions/`)
   - Subject (2–3 sentences)
   - Critical milestones / deadlines (verify each against current date)
   - Client team (primary contact + email) and internal team
   - Relevant areas (multi-select against `references/resources/tax-currency-watch.md`)
   - Matter risk classification (Low · Medium · High · Critical) based on amount at stake, jurisdictions, sensitivity
   - Strategic posture declared by the client (conservative / medium / aggressive within the post-BEPS frame)
3. Initialise `verification-log.md` (empty header) and `history.md` (first entry: matter creation).
4. Mark the matter active in the plugin's `.active-matter` file.
5. Close with a decision tree: launch the next skill now (which workstream is driving)?

## ISOLATION RULES

- `Cross-matter context: off` (default): no skill may read a matter other than the active one.
- `critic-cross-matter-leak` runs before closing any deliverable.
- `_archived/` matters: read-only, never delete without explicit instruction.

## CLOSE

Tree for `switch` / `new`:
- A — Launch the main workstream skill for the matter
- B — Review `matter.md` and complete `[PENDING]` fields
- C — Request additional information from the client via `query-email`
- D — List other matters
- E — Other
