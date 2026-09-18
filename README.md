# Induced-`P6` graphs and Erdős–Hajnal structure

The target is the Erdős–Hajnal property for induced-`P6`-free graphs:

\[
\exists c>0\ \forall G\text{ induced-}P_6\text{-free},\qquad
\max(\omega(G),\alpha(G))\ge |V(G)|^c.
\]

This repository develops a local structural theory for the stable interactions that arise in one route to that problem. The clearest result is an exact normal form: under the relevant nonadjacent-handle hypotheses, the bipartite interaction between two stable slices is a complete bipartite graph with pairwise-disjoint rectangular holes.

## The one-edge rectangle obstruction

Suppose `x,x'` and `y,y'` are stable pairs attached to two nonadjacent handles in the configuration used here. Their cross-edges cannot consist of exactly one edge.

Indeed, if the unique edge is `x'y`, then the six vertices can be ordered to form an induced path

\[
x-a_j-x'-y-a_i-y'.
\]

That is an induced `P6`, a contradiction.

This elementary obstruction is the local engine for the stronger classification below.

## Disjoint defect sets

Fix two stable slices `S` and `T`. For a row vertex `s\in S`, record the set of nonneighbors it has in `T`.

The rectangle obstruction implies:

> **Any two distinct nonempty row-defect sets are disjoint.**

Consequently the entire bipartite interaction has the form

\[
K_{|S|,|T|}\setminus\bigcup_r (S_r\times D_r),
\]

where the `S_r` partition the nonuniversal row classes and the nonempty defect sets `D_r\subseteq T` are pairwise disjoint.

Equivalently: the interaction is **complete bipartite minus disjoint complete bipartite holes**.

The finite verifier exhaustively checks the corresponding stable `0/1` matrices through size `4\times4`, while the theorem itself has a symbolic proof from the induced-`P6` obstruction.

## Sharp trace bound and a pure pair

Because distinct nonempty defect sets are disjoint, each consumes at least one distinct column. Therefore the number of distinct row traces is at most

\[
\boxed{|T|+1}.
\]

Choosing a largest trace class yields a pure pair: there is a pair of vertex sets with one side of size at least

\[
\frac{|S|}{|T|+1}
\]

and the other of size at least

\[
\frac{|T|}{2},
\]

such that the two sides are either complete or anticomplete to one another.

After equal row profiles are merged, the quotient interaction is a blow-up of

\[
K_{q,q}\text{ minus a matching},
\]

with optional universal blocks. This is the repository's **crown normal form**.

## Why this matters for the larger problem

The Erdős–Hajnal route needs large homogeneous pairs to survive repeated decomposition. The results above turn one potentially complicated stable interaction into a rigid combinatorial object with only linearly many row types and an explicit pure-pair guarantee.

Other proved pieces in the repository include:

- common-nonneighbor / symmetric-difference completeness for nonadjacent row pairs;
- near-twin profile covering by Hamming balls;
- exact-profile classes that form cliques after trimming;
- a bridge from a large near-twin cluster to a large complete or anticomplete pair;
- a proof that recursive anchors in the nested-neighborhood route form a clique.

The remaining work is global rather than local: extract the required structured slices at polynomial scale, aggregate the crown structure across the decomposition, and connect the resulting pure pairs to a full Erdős–Hajnal recursion.

## Verification and source map

The finite verification checks all four orientations of the one-edge rectangle and exhaustively enumerates the small stable matrices used as regression tests for the normal form.

The historical source files retain their original internal labels:

- [`COURT-THEOREMS.md`](COURT-THEOREMS.md) — 30 theorem statements and proofs;
- [`NEGATIVE-BANK.md`](NEGATIVE-BANK.md) — routes that were falsified or superseded;
- [`LIVE-CANDIDATES.md`](LIVE-CANDIDATES.md) — open local lemmas;
- [`CLOSURE-PROGRAMS.md`](CLOSURE-PROGRAMS.md) — remaining global reductions.

Those filenames are provenance. The mathematical entry point is the rectangle obstruction, disjoint-defect theorem, trace bound, pure-pair theorem, and crown normal form stated above.

Author: Jared Wilder.