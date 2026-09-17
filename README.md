# Induced-`P6` Erdős–Hajnal program

The target is the Erdős–Hajnal property for induced-`P6`-free graphs:

\[
\exists c>0\ \forall G\text{ induced-}P_6\text{-free},\qquad
\max(\omega(G),\alpha(G))\ge |V(G)|^c.
\]

This repository contains a structural theorem package, finite verification, negative results, and explicit remaining reductions for that problem.

## Main structural chain

The strongest internally verified chain is recorded as

```text
T-006 -> T-021 -> T-022 -> T-023/T-025 -> T-026.
```

In mathematical terms it gives:

1. a forbidden one-edge `2×2` rectangle under nonadjacent comb handles;
2. disjoint nonempty stable-slice defect sets;
3. a complete-bipartite-minus-disjoint-rectangles normal form;
4. a sharp `|T|+1` trace bound and exact pure-pair lower bound;
5. a crown quotient: a blow-up of `K_{q,q}` minus a matching, with optional universal blocks.

The deterministic verifier checks all four canonical one-edge orientations and exhaustively checks every stable `0/1` matrix from `2×2` through `4×4` for the corresponding local normal-form claims.

## Repository contents

- [`COURT-THEOREMS.md`](COURT-THEOREMS.md) — 30 retained theorem statements.
- [`NEGATIVE-BANK.md`](NEGATIVE-BANK.md) — 16 refuted or retired routes.
- [`LIVE-CANDIDATES.md`](LIVE-CANDIDATES.md) — 22 candidate lemmas.
- [`CLOSURE-PROGRAMS.md`](CLOSURE-PROGRAMS.md) — 18 explicit remaining proof programs.

The negative bank is useful mathematically: several tempting reductions fail, including the old wonderfulness shortcut, single-wall reduction, Ferrers-staircase branch, naive pairwise-refinement multiplication, and standalone single-anchor recursion.

## Remaining frontier

The unresolved steps include structured-slice extraction, global crown aggregation, a cotree mass dichotomy, a polynomial Rödl/viral bridge, a PMC-to-pure-pair bridge, and wonderfulness/property-(*) reductions.

The bounded matrix verification supports the local lemmas; it is not an unbounded proof of the Erdős–Hajnal target. The full induced-`P6` case remains open in this repository.

Historical source material is preserved in `jaredwilder/unpublished-math-papers/p6-six-vertex-wall/`.

Author: Jared Wilder.
