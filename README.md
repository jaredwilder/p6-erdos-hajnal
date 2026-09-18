# Induced-`P6` graphs and Erdős–Hajnal structure

The target is the Erdős–Hajnal property for induced-`P6`-free graphs:

\[
\exists c>0\ \forall G\text{ induced-}P_6\text{-free},\qquad
\max(\omega(G),\alpha(G))\ge |V(G)|^c.
\]

This repository develops a local structural theory for stable interactions arising in one route to that problem. The clearest result is an exact normal form: under the relevant nonadjacent-handle hypotheses, the bipartite interaction between two stable slices is a complete bipartite graph with pairwise-disjoint rectangular holes.

## The one-edge rectangle obstruction

Suppose `x,x'` and `y,y'` are stable pairs attached to two nonadjacent handles. Their cross-edges cannot consist of exactly one edge.

If the unique edge is `x'y`, the six vertices form an induced path

\[
x-a_j-x'-y-a_i-y',
\]

contradicting induced-`P6`-freeness.

This elementary obstruction is the local engine for the stronger classification below.

## Disjoint defect sets

Fix two stable slices `S` and `T`. For a row vertex `s\in S`, record its set of nonneighbors in `T`.

The rectangle obstruction implies:

> **Any two distinct nonempty row-defect sets are disjoint.**

Consequently the entire bipartite interaction has the form

\[
K_{|S|,|T|}\setminus\bigcup_r(S_r\times D_r),
\]

where the `S_r` are row classes and the nonempty defect sets `D_r\subseteq T` are pairwise disjoint.

Equivalently: the interaction is **complete bipartite minus disjoint complete bipartite holes**.

## Sharp trace bound and pure pair

Because distinct nonempty defect sets are disjoint, each consumes a distinct column. Hence the number of row traces is at most

\[
\boxed{|T|+1}.
\]

Choosing a largest trace class yields a pure pair with one side of size at least

\[
\frac{|S|}{|T|+1}
\]

and the other of size at least

\[
\frac{|T|}{2}.
\]

After equal row profiles are merged, the quotient is a blow-up of

\[
K_{q,q}\text{ minus a matching},
\]

with optional universal blocks. This is the **crown normal form**.

The strongest proved chain is therefore

```text
one-edge rectangle obstruction
    ↓
disjoint defect sets
    ↓
complete bipartite minus disjoint rectangles
    ↓
sharp trace bound
    ↓
large pure pair
    ↓
crown quotient
```

[`THEOREMS.md`](THEOREMS.md) gives the complete 30-item theorem index in ordinary mathematical language.

## Verification

The one-edge rectangle is checked in all four orientations. The disjoint-defect and normal-form statements were also exhaustively checked on stable `0/1` matrices through `4×4` in addition to their symbolic proofs.

The finite computations are regression checks for the local lemmas; the unbounded statements come from the written arguments rather than extrapolation from those finite cases.

## Remaining mathematical problem

The local crown structure does not by itself prove the full induced-`P6` Erdős–Hajnal property. The remaining problem is global: extract sufficiently large structured slices and aggregate the local crown/pure-pair information without losing polynomial mass.

The repository also records several tested routes that fail, including a one-wall shortcut, a Ferrers-staircase branch, naive pairwise-refinement multiplication, and standalone single-anchor recursion. Those negative results are retained because they narrow the viable global reductions.

## Repository map

- [`THEOREMS.md`](THEOREMS.md) — recommended theorem index;
- `NEGATIVE-BANK.md` — explicit counterexamples and retired proof routes;
- `LIVE-CANDIDATES.md` — unresolved candidate lemmas;
- `CLOSURE-PROGRAMS.md` — remaining proof programs;
- `COURT-THEOREMS.md` — historical theorem-ledger filename retained for provenance.

Historical source material is preserved under `jaredwilder/unpublished-math-papers/p6-six-vertex-wall/`.

Author: Jared Wilder.
