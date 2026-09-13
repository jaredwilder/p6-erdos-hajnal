# The Six-Vertex Wall — Court theorem bank

**Flagship:** Erdős–Hajnal for induced-P6-free graphs. **NOT CLOSED.**

Statuses are preserved from the audited 2026-08-06 theorem bank. Conditional entries are not unconditional theorems.

## T-001 — P6 leaf-reducibility
**Round:** 1 · **Status:** `COURT - elementary proof`

The singleton family {P6} is leaf-reducible.

**Proof:** Delete an endpoint; the remainder is P5, which has EH by PUB-01.

**Dependencies:** PUB-01

**Verification:** Symbolic one-line proof.

## T-002 — Correct two-wall reduction
**Round:** 3 · **Status:** `COURT - conditional reduction`

If {P6} is wonderful and has property (*), then P6 has EH.

**Proof:** Combine T-001 with PUB-05 and PUB-04.

**Dependencies:** T-001, PUB-04, PUB-05

**Verification:** Dependency composition; no claim that either wall is discharged.

## T-003 — Diameter-four wonderfulness barrier
**Round:** 3 · **Status:** `COURT - elementary proof`

A one-subdivision of K_{1,t} contains no induced P6.

**Proof:** Its diameter is at most four; an induced P6 has endpoints at path distance five.

**Dependencies:** None

**Verification:** Elementary graph-distance proof.

## T-004 — Small auxiliary-witness barrier
**Round:** 3 · **Status:** `COURT - elementary proof`

No H on at most five vertices can witness the second wonderfulness criterion for {P6}.

**Proof:** For |H|<5 the extensions are too small; for |H|=5 the added vertex has degree two while co-P6 has minimum degree three.

**Dependencies:** None

**Verification:** Finite degree argument.

## T-005 — Mixed-component purification
**Round:** 3 · **Status:** `COURT - elementary proof`

Contracting connected components of a blockade mixedness graph gives pairwise pure quotient blocks.

**Proof:** A mixed quotient pair would contain an original mixed pair joining the components.

**Dependencies:** None

**Verification:** Component argument.

## T-006 — Forbidden single-edge rectangle
**Round:** 4 · **Status:** `COURT - proved and bounded-verified`

Under nonadjacent comb handles, stable pairs x,x' and y,y' cannot have exactly one cross-edge.

**Proof:** With unique edge x'y, the order x-a_j-x'-y-a_i-y' is an induced P6.

**Dependencies:** None

**Verification:** All four orientations exhaustively verified.

## T-007 — Crossing domination
**Round:** 4 · **Status:** `COURT - corollary`

A distinguishing vertex across a nonadjacent pair forces adjacency on every suitable common-nonneighbor column.

**Proof:** Otherwise the four vertices realize T-006.

**Dependencies:** T-006

**Verification:** Direct.

## T-008 — Stable-handle rectangle exclusion
**Round:** 4 · **Status:** `COURT - corollary`

Every tooth pair indexed by a stable handle family satisfies T-006 on internal nonedges.

**Proof:** Apply T-006 pairwise.

**Dependencies:** T-006

**Verification:** Direct.

## T-009 — Common-nonneighbor / symmetric-difference completeness
**Round:** 5 · **Status:** `COURT - proved`

For nonadjacent x,x', their common nonneighbors in Y are complete to the vertices distinguishing x and x'.

**Proof:** A missing edge gives a one-edge rectangle.

**Dependencies:** T-006

**Verification:** Symbolic proof.

## T-010 — Canonical pure-pair trichotomy
**Round:** 5 · **Status:** `COURT - quantitative corollary`

For threshold t, either a t-by-t complete pair exists, or the common-nonneighbor set is <t, or the neighborhood symmetric difference is <t.

**Proof:** The two relevant sets are complete by T-009.

**Dependencies:** T-009

**Verification:** Threshold corollary.

## T-011 — Sparse-neighborhood twin forcing
**Round:** 5 · **Status:** `COURT - quantitative corollary`

If each x has at most rho|Y| neighbors, rho<1/2, then absent a large complete pair every nonedge has small Y-neighborhood symmetric difference.

**Proof:** The common-nonneighbor set has size at least (1-2rho)|Y|; apply T-010.

**Dependencies:** T-010

**Verification:** Union bound.

## T-012 — Separated profiles form a clique
**Round:** 6 · **Status:** `COURT - metric lemma`

If every internal nonedge has profile distance <epsilon|Y|, any epsilon|Y|-separated profile family is a clique.

**Proof:** Separated vertices cannot be nonadjacent.

**Dependencies:** None

**Verification:** One-line metric proof.

## T-013 — Neighborhood profile cover
**Round:** 6 · **Status:** `COURT - metric lemma`

The profile family is covered by at most omega(X) Hamming balls of radius epsilon|Y|.

**Proof:** A maximal separated set is a clique by T-012; maximality gives the cover.

**Dependencies:** T-012

**Verification:** Greedy packing/covering.

## T-014 — Polynomial near-twin cluster
**Round:** 6 · **Status:** `COURT - quantitative corollary`

If omega(X)<|X|^gamma, one profile ball contains >|X|^(1-gamma) vertices.

**Proof:** Pigeonhole over T-013.

**Dependencies:** T-013

**Verification:** Pigeonhole.

## T-015 — Error crossing domination
**Round:** 6 · **Status:** `COURT - proved`

On a template-zero region, a distinguishing error between nonadjacent rows forces secondary errors across every suitable column nonedge.

**Proof:** Otherwise T-006 occurs.

**Dependencies:** T-006

**Verification:** Direct.

## T-016 — Low-degree agreement
**Round:** 6 · **Status:** `COURT - proved`

After removing columns within 2epsilon|Y| of complete, nonadjacent rows in a near-twin cluster have identical error supports.

**Proof:** A disagreement plus T-015 would force too many nonneighbors into two sparse error sets.

**Dependencies:** T-015

**Verification:** Counting proof; formalization must fix strict inequalities.

## T-017 — Trimmed exact-profile clique bound
**Round:** 6 · **Status:** `COURT - proved`

Representatives of distinct trimmed exact profiles form a clique, so the profile count is at most omega(C).

**Proof:** Distinct representatives cannot be nonadjacent by T-016.

**Dependencies:** T-016

**Verification:** Direct.

## T-018 — Trimmed type-to-pure-pair bridge
**Round:** 6 · **Status:** `COURT - proved`

A large near-twin cluster and large trimmed region contain a large complete or anticomplete pair under a clique bound.

**Proof:** Choose a large exact-profile class and take its common neighborhood or nonneighborhood.

**Dependencies:** T-017

**Verification:** Pigeonhole.

## T-019 — Joint-profile quadratic sufficiency
**Round:** 7 · **Status:** `COURT - conditional bridge`

At most ell^2 exact joint profiles in each tooth implies a pure refinement of width at least w/ell^2.

**Proof:** Choose a largest class in each tooth; full external profile equality makes pairs pure.

**Dependencies:** None

**Verification:** Exact implication; premise unproved.

## T-020 — Stable-tooth laminarity
**Round:** 8 · **Status:** `COURT - true but superseded`

Stable-slice row nonneighbor traces are laminar.

**Proof:** A proper overlap without containment gives T-006.

**Dependencies:** T-006

**Verification:** Superseded by T-021.

## T-021 — Disjoint-defect classification
**Round:** 9 · **Status:** `COURT - proved and bounded-verified`

Any two distinct nonempty stable-slice row defect sets are disjoint.

**Proof:** Laminarity plus the fact that proper nonempty containment also gives T-006.

**Dependencies:** T-006, T-020

**Verification:** Exhaustively verified through 4x4.

## T-022 — Complete-minus-disjoint-rectangles normal form
**Round:** 9 · **Status:** `COURT - proved and bounded-verified`

Every stable interaction is complete bipartite minus disjoint complete bipartite holes S_r x D_r.

**Proof:** Group rows by common defect; T-021 makes distinct defects disjoint.

**Dependencies:** T-021

**Verification:** Symbolic and bounded exhaustive verification.

## T-023 — Sharp trace bound
**Round:** 9 · **Status:** `COURT - proved and bounded-verified`

The number of distinct row traces is at most |T|+1.

**Proof:** Each nonempty disjoint defect consumes a distinct column, plus the empty trace.

**Dependencies:** T-021

**Verification:** Symbolic and bounded exhaustive verification.

## T-024 — Dual pure-pair certificate
**Round:** 9 · **Status:** `COURT - proved`

Every nonuniversal row class S_r is anticomplete to D_r and complete to T\D_r.

**Proof:** Definition of the defect trace.

**Dependencies:** T-022

**Verification:** Direct.

## T-025 — Guaranteed stable-slice pure pair
**Round:** 9 · **Status:** `COURT - exact quantitative theorem`

There is a pure pair with sides at least |S|/(|T|+1) and |T|/2.

**Proof:** Choose a largest trace class using T-023 and the larger of its defect and complement using T-024.

**Dependencies:** T-023, T-024

**Verification:** Exact counting proof.

## T-026 — Crown normal form
**Round:** 9 · **Status:** `COURT - proved`

After merging equal profiles, the stable interaction is a blow-up of K_{q,q} minus q matching edges, with optional universal blocks.

**Proof:** Quotient T-022 by row classes and defect blocks.

**Dependencies:** T-022

**Verification:** Exact quotient.

## T-027 — Dominator size dichotomy
**Round:** 10 · **Status:** `COURT - conditional on PUB-08`

A connected P6-free graph with a P4-free dominating set D of size >=n^(2theta) has a homogeneous set of size >=n^theta.

**Proof:** Cographs are perfect, so alpha(D)omega(D)>=|D|.

**Dependencies:** PUB-08

**Verification:** Standard perfect-graph inequality.

## T-028 — Recursive anchors form a clique
**Round:** 10 · **Status:** `COURT - proved`

Nested open-neighborhood recursion makes all selected anchors pairwise adjacent.

**Proof:** Every later anchor lies in every earlier retained neighborhood.

**Dependencies:** None

**Verification:** Induction.

## T-029 — Nested-neighborhood size ledger
**Round:** 10 · **Status:** `COURT - schema with rounding caveat`

Under denial of an n^theta homogeneous set, r recursion rounds retain roughly n^(1-2rtheta) vertices.

**Proof:** Each step loses at most a factor n^(2theta), up to closed-neighborhood/integer losses.

**Dependencies:** PUB-08, T-027

**Verification:** Exact floors and +/-1 remain for formalization.

## T-030 — Cotree union-node activation
**Round:** 10 · **Status:** `COURT - conditional local bridge`

At an anticomplete split of a dominating cograph, subordinate stable pairs with the required anchor incidences obey T-006.

**Proof:** The cotree anchors provide the nonadjacent-handle relation.

**Dependencies:** T-006, PUB-08

**Verification:** Assignment must certify every incidence.
