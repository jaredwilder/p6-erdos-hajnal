# Theorem index — induced-P6 Erdős–Hajnal structure

This file is the human-readable index of the retained theorem package. The historical source ledger is preserved separately; the labels below describe the mathematics in ordinary terms.

## Local P6 obstructions

### T1 — leaf reduction
The singleton family `{P6}` is leaf-reducible: deleting an endpoint leaves `P5`.

### T2 — two-reduction implication
If the standard wonderfulness and property-(*) reductions hold for `{P6}`, then the Erdős–Hajnal property follows.

### T3 — diameter-four barrier
A one-subdivision of `K_{1,t}` contains no induced `P6`.

### T4 — small auxiliary-witness barrier
No graph on at most five vertices can witness the second wonderfulness criterion for `{P6}`.

### T5 — mixed-component purification
Contracting connected components of a blockade mixedness graph gives pairwise pure quotient blocks.

### T6 — forbidden one-edge rectangle
Under nonadjacent comb handles, stable pairs `x,x'` and `y,y'` cannot have exactly one cross-edge. A unique edge would produce an induced `P6` in the order

```text
x - a_j - x' - y - a_i - y'.
```

This is one of the principal local lemmas and has also been checked exhaustively in all four orientations.

### T7 — crossing domination
A distinguishing vertex across a nonadjacent pair is adjacent to every suitable common-nonneighbor column.

### T8 — stable-handle rectangle exclusion
Every tooth pair indexed by a stable handle family inherits the forbidden one-edge rectangle on internal nonedges.

### T9 — common-nonneighbor / symmetric-difference completeness
For nonadjacent `x,x'`, the common nonneighbors in `Y` are complete to the vertices that distinguish `x` and `x'`.

### T10 — pure-pair trichotomy
For any threshold `t`, either there is a `t×t` complete pair, or the common-nonneighbor set has size `<t`, or the neighborhood symmetric difference has size `<t`.

### T11 — sparse-neighborhood near-twins
When all rows have degree at most `rho|Y|` with `rho<1/2`, absence of a large complete pair forces nonadjacent rows to have small neighborhood symmetric difference.

## Profile compression

### T12 — separated profiles form a clique
If every internal nonedge has profile distance `<epsilon|Y|`, then every `epsilon|Y|`-separated profile family is a clique.

### T13 — neighborhood profile cover
The profile family is covered by at most `omega(X)` Hamming balls of radius `epsilon|Y|`.

### T14 — polynomial near-twin cluster
If `omega(X)<|X|^gamma`, one profile ball contains more than `|X|^(1-gamma)` rows.

### T15 — error crossing domination
On a template-zero region, a distinguishing error between nonadjacent rows forces secondary errors across every suitable column nonedge.

### T16 — low-degree agreement
After removing columns within `2epsilon|Y|` of complete, nonadjacent rows in a near-twin cluster have identical error supports.

### T17 — exact-profile clique bound
Representatives of distinct trimmed exact profiles form a clique; hence the number of trimmed profiles is at most `omega(C)`.

### T18 — type-to-pure-pair bridge
A large near-twin cluster and a large trimmed region contain a large complete or anticomplete pair under the corresponding clique bound.

### T19 — joint-profile implication
If each tooth has at most `ell^2` exact joint profiles, it admits a pure refinement of width at least `w/ell^2`. The implication is exact; the global premise remains a separate target.

## Stable-slice normal form

### T20 — stable-tooth laminarity
Stable-slice row nonneighbor traces are laminar. This is subsumed by the stronger disjointness theorem below.

### T21 — disjoint-defect classification
Any two distinct nonempty stable-slice row defect sets are disjoint.

This has both a symbolic proof and exhaustive checks through `4×4` stable matrices.

### T22 — complete-minus-disjoint-rectangles normal form
Every stable interaction is a complete bipartite graph with disjoint complete bipartite holes removed:

\[
K_{S,T}\setminus\bigcup_r (S_r\times D_r).
\]

### T23 — sharp trace bound
The number of distinct row traces is at most

\[
|T|+1.
\]

### T24 — dual pure-pair certificate
Every nonuniversal row class `S_r` is anticomplete to its defect block `D_r` and complete to `T\setminus D_r`.

### T25 — guaranteed stable-slice pure pair
There is a pure pair with sides at least

\[
\frac{|S|}{|T|+1}
\qquad\text{and}\qquad
\frac{|T|}{2}.
\]

### T26 — crown normal form
After merging equal profiles, the stable interaction is a blow-up of

\[
K_{q,q}\setminus M_q,
\]

with optional universal blocks.

This is the terminal local structural description supplied by the stable-slice analysis.

## Recursive and dominating-set reductions

### T27 — dominator size dichotomy
Using the cited cograph domination input, a connected `P6`-free graph with a sufficiently large `P4`-free dominating set contains a polynomial-size homogeneous set.

### T28 — recursive anchors form a clique
In the nested open-neighborhood recursion, all selected anchors are pairwise adjacent.

### T29 — nested-neighborhood size ledger
Under denial of a polynomial homogeneous set, repeated neighborhood restriction retains the stated polynomial-scale mass, up to the recorded rounding terms.

### T30 — cotree union-node activation
At an anticomplete split of a dominating cograph, subordinate stable pairs with the required anchor incidences satisfy the forbidden one-edge rectangle theorem.

## Main proved chain

The strongest fully internal structural chain is

```text
forbidden one-edge rectangle
    ↓
disjoint nonempty defect sets
    ↓
complete bipartite minus disjoint rectangles
    ↓
sharp trace bound
    ↓
large pure pair
    ↓
crown quotient
```

In theorem labels:

```text
T6 -> T21 -> T22 -> T23/T25 -> T26.
```

The full induced-`P6` Erdős–Hajnal theorem is not supplied by this chain alone. The remaining work is global: extracting and aggregating the local crown structure strongly enough to obtain the required polynomial homogeneous pair.

The historical `COURT-THEOREMS.md` file is retained byte-for-byte as provenance for the original theorem ledger; this file is the recommended reading surface.
