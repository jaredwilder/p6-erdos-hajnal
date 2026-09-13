# P6 Erdős–Hajnal — Round 11 exact bounded classifications

**Status:** three exact finite classification theorems from Round 11.  
**Global P6 Erdős–Hajnal implication:** OPEN in this program.  
**Novelty:** not adjudicated theorem-by-theorem.

The broader P6 project contains many reductions, candidates, and killed routes. This page isolates three Round 11 results with complete bounded search authority so they are not buried under the global open problem.

---

## T11.2 — correct three-cell complement-comb obstruction census

Work in the source-bound three-tooth complement-comb model in `H = complement(G)`:

- `H` is `P6`-free;
- each handle misses its own tooth and sees every other tooth;
- the three tested handles form a stable triple;
- the remaining local freedom is encoded by **15 Boolean bits**.

The complete search space therefore has

\[
2^{15}=32768
\]

configurations.

Exact census:

- `27088` are `P6`-free;
- `5680` contain an induced `P6`;
- the pairwise rectangle law rejects `5440` of those bad configurations;
- exactly
  \[
  \boxed{240}
  \]
  configurations are **pairwise-legal but still contain an induced `P6`**;
- the inclusion-minimal forcing patterns comprise `252` patterns in exactly `8` symmetry orbits.

### Consequence

The pairwise rectangle theorem is sound but **not complete**. A genuinely rank-three/local-three-cell law is required: pairwise compatibility alone misses exactly 240 bounded obstructions in this model.

**Authority:** complete `2^15` enumeration.  
**Source receipt:** `p6_complement_comb_three_cell_verification.json`.

---

## T11.3 — complete H5 mixed-attachment classification

For the Round 11 `H5` seed, enumerate every nontrivial mixed attachment signature on its 11 vertices.

There are

\[
2^{11}-2=2046
\]

such mixed signatures.

Exact result:

- `2015` force an induced `co-P6`;
- exactly
  \[
  \boxed{31}
  \]
  survive;
- every surviving attachment support induces a **clique of size at most 3**.

The surviving supports are exactly the explicitly enumerated family:

- a rim singleton or rim edge, optionally together with the hub;
- the hub alone;
- a pendant leaf, optionally together with its parent.

Thus the bounded classifier is not merely a count: it collapses every legal mixed support to a short closed structural list.

**Authority:** complete 2046-signature enumeration.  
**Source receipt:** `p6_h5_seed_attachment_verification.json`.

The source preserves the 31 raw support masks in the JSON feedstock/receipt.

---

## T11.4 — dominating K3,3 private-representative classification

Take the exact Round 11 model built from an induced dominating `K_{3,3}`. Choose one private representative for each of the six core vertices. The private graph has 15 possible edges, so there are again

\[
2^{15}=32768
\]

states.

Exact enumeration shows that only

\[
\boxed{4}
\]

private graphs extend to a `P6`-free full graph.

All four are cluster graphs:

1. the empty private graph;
2. the `X`-side clique only;
3. the `Y`-side clique only;
4. the complete private graph.

Source census:

- all states: `32768`;
- `P6`-free states: `4`;
- private-`P4`-free states among survivors: `4`;
- private cluster graphs among survivors: `4`;
- private complete-multipartite survivors: `2`.

**Authority:** complete `2^15` enumeration.  
**Source receipt:** `p6_dominating_biclique_private_graph_verification.json`.

### Important boundary

This classification does **not** imply that the surviving private clusters are modules in the full graph. The same Round 11 source explicitly finds nonprivate exterior vertices that can mix on a surviving private connected component without creating a `P6`. That stronger modularity shortcut is false and belongs in the negative bank.

---

# Semantic correction preserved by Round 11

These results use the **correct source-bound anchor semantics**. An earlier private-anchor census in the campaign was retracted after using the wrong anchoring model. The Round 11 feedstock was rebuilt with the intended complement-comb / dominating-biclique incidences before the complete enumerations above were run.

This matters because a bounded exhaustive result is only as meaningful as the finite object it actually enumerates.

---

# What these theorems do not prove

They do not close the global P6 Erdős–Hajnal problem.

The exact finite classifications establish:

- pairwise local laws are incomplete at the three-cell scale;
- `H5` mixed attachments surviving the local test have sharply constrained clique supports;
- the private graph in the exact dominating-`K3,3` representative model has only four possible `P6`-free forms.

The missing global step is a structural quotient/module/recursion theorem strong enough to lift these bounded classifications to arbitrary P6-free graphs. The source explicitly records that several tempting lifts fail.

---

# Source authority

Recovered source objects include:

- `P6-LEAN-FEEDSTOCK-2026-08-06.md`;
- `P6-LEAN-FEEDSTOCK-2026-08-06.json`;
- `P6-ERDOS-HAJNAL-TERMINAL-CLOSE-ATTEMPT-ROUND-11-2026-08-06.md`;
- the three named exact verification receipts.

The feedstock proposes finite Lean encodings, but this page claims the **complete finite enumeration authority** actually present in the source; it does not silently upgrade planned `native_decide` formalizations into completed kernel proofs.
