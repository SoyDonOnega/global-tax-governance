---
slug: critic-citation-exactness
role: critic
invoked_by: any generator
emits_handoffs_to: []
output_shapes: [deliverable, error]
---

# critic-citation-exactness

> Every cited norm, jurisprudence, doctrina must resolve to a real source with exact format. No invented citations. No paraphrased "verbatim". Spot-checks samples character-for-character.

## INPUTS

- Deliverable path
- Verification log (citations previously verified)

## RESPONSIBILITY

1. Extract every citation in deliverable:
   - Norm references (`Art. X.Y.Z [Ley]`, with or without BOE-A)
   - Jurisprudence (TS ECLI · TJUE C-XXX/AA · STC)
   - DGT (V[NNNN]-AA)
   - TEAC (RG [NNNN]/AAAA)
   - Doctrina (APA + DOI)
2. For each:
   - Format check: matches the canonical pattern?
   - Existence check: resolves to a known source (cross-reference against verification-log + currency-watch)?
   - If unverifiable: flag as `unverified_citation` (not necessarily wrong, but not in our verification trail)
3. For verbatim quotes inside the deliverable (tabular review cells, memo extractions):
   - Spot-check ≥10% by re-reading source at cited location, character-for-character
   - Any mismatch → `quote_mismatch` flag and propose downgrade to needs_review
4. Return pass/fail + flags.
5. Output: `<deliverable>.citation-exactness.md`.

## DONE WHEN

- All citations classified.
- Spot-check done.

## TRAPS

- Treating an unverified citation as wrong (it may be correct but not in our trail) — distinguish unverified vs. invalid.
- Skipping spot-check on verbatim — that's the strongest defense against paraphrase camouflage.
