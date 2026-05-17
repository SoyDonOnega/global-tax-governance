# VERIFICATION LOG

> Dated record of primary-source verifications. Avoids re-verifying what is already verified. Builds an audit trail across matters and sessions.
> Lives in every matter / project. One log per matter.

---

## TEMPLATE

```
─────────────────────────────────────────────
VERIFICATION LOG — [matter or topic]
─────────────────────────────────────────────
| Date        | Item verified                  | Primary source                           | Result        | Verified by    |
|-------------|--------------------------------|------------------------------------------|---------------|----------------|
| 2026-05-16  | IIR/UTPR calendar Spain        | RD-ley 7/2024 BOE-A-2024-XXXXX           | confirmed     | [initials]     |
| 2026-05-16  | Mosquera UTPR/customary law    | Hongler/Mosquera Tax Notes Intl Jul 2023 | confirmed     | [initials]     |
| 2026-05-15  | TEAC criterion Art. 18 LIS range | TEAC RG XXXX/2024                      | confirmed     | [initials]     |
| 2026-04-30  | AI Act Implementing Act status | EUR-Lex direct lookup                    | pending       | [initials]     |
─────────────────────────────────────────────
```

---

## RULES

1. **One entry per material verification.** If you had to go to the primary source and check it, log it.
2. **Literal primary source**, not "what Mosquera said" — the ECLI, the BOE, the DGT URL, the DOI.
3. **Three-state result**: `confirmed` · `discrepancy` (with note) · `pending`.
4. **Implicit expiry.** A verification > 6 months old in moving areas (Pillar Two, AI Act, recent TEAC criteria) must be re-validated. For stable norms (Art. 31.3 Spanish Constitution, structural Art. 18 LIS) there is no expiry.
5. **Cross with currency-watch.** If the verified item matches an area of `tax-currency-watch.md`, update the last-verified date there too.

---

## WHERE TO STORE IT

- Per matter: `matters/<matter>/verification-log.md`
- For academic research: `Research/<topic>/verification-log.md`
- For workspace-level transversal verifications: `references/templates/verification-log.md` (this file as the template) — but ideally each verification lives in its matter.
