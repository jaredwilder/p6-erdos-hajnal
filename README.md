# The Six-Vertex Wall — Erdős–Hajnal for induced-P6-free graphs

Public release of the audited 2026-08-06 Encirclement campaign.

## Flagship status

**NOT CLOSED.** The target is the Erdős–Hajnal property for induced-P6-free graphs:

`exists c>0, for every induced-P6-free G: max(omega(G),alpha(G)) >= |V(G)|^c`.

No weakening to bounded clique number, algorithmic MWIS, quasi-polynomial homogeneous sets, a finite census, or a two-forbidden family is counted as closure.

Historical novelty of the local theorem package has not been adjudicated.

## Released estate

- **30 Court theorems** — `COURT-THEOREMS.md`
- **16 negative/retracted routes** — `NEGATIVE-BANK.md`
- **22 live candidate lemmas** — `LIVE-CANDIDATES.md`
- **18 closure programs** — `CLOSURE-PROGRAMS.md`

The source campaign also tracked 10 published inputs and 12 machine missions.

## Strongest verified local blade

The highest-leverage internally verified chain is:

`T-006 -> T-021 -> T-022 -> T-023/T-025 -> T-026`.

In words:

1. a forbidden one-edge 2x2 rectangle under nonadjacent comb handles;
2. disjoint nonempty stable-slice defect sets;
3. a complete-bipartite-minus-disjoint-rectangles normal form;
4. a sharp `|T|+1` trace bound and an exact pure-pair lower bound;
5. a crown quotient: a blow-up of `K_{q,q}` minus a matching, with optional universal blocks.

The deterministic campaign verifier checked all four canonical one-edge orientations and exhaustively checked every stable 0/1 matrix from 2x2 through 4x4 for the relevant local normal-form claims. **That bounded verification is regression evidence, not an unbounded proof of the flagship.**

## What remains load-bearing

The public closure programs expose the real walls rather than hiding them. Among them are noncircular structured-slice extraction, global crown aggregation, a cotree mass dichotomy, a polynomial Rödl/viral bridge, a PMC-to-pure-pair bridge, and wonderfulness/property-(*) obligations.

Killed routes remain public so they cannot silently return as assumptions. In particular, the old wonderfulness shortcut, the single-wall reduction, the Ferrers staircase branch, naive pairwise-refinement multiplication, and standalone single-anchor recursion are explicitly retired or bounded.

## Provenance

Canonical subject home: this repository.

Historical extraction source: `jaredwilder/unpublished-math-papers/p6-six-vertex-wall/`. The archive copy remains public for chronology and provenance; this repository is the preferred reading surface for the mathematics.
