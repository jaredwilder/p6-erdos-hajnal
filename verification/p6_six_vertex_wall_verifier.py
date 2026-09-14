#!/usr/bin/env python3
"""
Deterministic bounded verifier for the Six-Vertex Wall campaign.

Checks:
1. The canonical six-vertex comb witness: with two nonadjacent handles,
   stable pairs in the two teeth, and exactly one cross-edge, the induced
   graph is P6.
2. Exhaustive stable-slice matrix classification through 4 x 4:
   every 0/1 matrix avoiding a 2 x 2 submatrix with exactly one 1 has
   row nonneighbor traces that are equal or disjoint.
3. The equivalent complete-minus-disjoint-rectangles normal form.
4. The sharp local trace bound: number of distinct row traces <= n_cols + 1.

This verifier proves bounded exhaustions and validates the local symbolic
lemmas. It does not prove the unbounded Erdős-Hajnal conjecture for P6.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path
from typing import List, Sequence, Set, Tuple


def is_connected(n: int, edges: Set[Tuple[int, int]]) -> bool:
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    seen = {0}
    stack = [0]
    while stack:
        v = stack.pop()
        for u in adj[v]:
            if u not in seen:
                seen.add(u)
                stack.append(u)
    return len(seen) == n


def is_p6_graph(n: int, edges: Set[Tuple[int, int]]) -> bool:
    if n != 6 or len(edges) != 5 or not is_connected(n, edges):
        return False
    deg = [0] * n
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    return sorted(deg) == [1, 1, 2, 2, 2, 2]


def canonical_witness_check() -> dict:
    # vertices: 0=x, 1=x', 2=y, 3=y', 4=ai, 5=aj
    # fixed comb edges: aj-{x,x'}, ai-{y,y'}
    fixed = {(0, 5), (1, 5), (2, 4), (3, 4)}
    cross_pairs = [(0, 2), (0, 3), (1, 2), (1, 3)]
    checked = []
    for unique in cross_pairs:
        edges = set(fixed)
        edges.add(tuple(sorted(unique)))
        ok = is_p6_graph(6, {tuple(sorted(e)) for e in edges})
        checked.append({"unique_cross_edge": unique, "is_induced_P6": ok})
    return {
        "all_four_single_edge_orientations_are_P6": all(x["is_induced_P6"] for x in checked),
        "cases": checked,
    }


def matrix_from_mask(rows: int, cols: int, mask: int) -> List[List[int]]:
    return [
        [((mask >> (r * cols + c)) & 1) for c in range(cols)]
        for r in range(rows)
    ]


def avoids_singleton_rectangle(M: Sequence[Sequence[int]]) -> bool:
    rows, cols = len(M), len(M[0])
    for r1, r2 in itertools.combinations(range(rows), 2):
        for c1, c2 in itertools.combinations(range(cols), 2):
            s = M[r1][c1] + M[r1][c2] + M[r2][c1] + M[r2][c2]
            if s == 1:
                return False
    return True


def row_defects(M: Sequence[Sequence[int]]) -> List[frozenset[int]]:
    return [
        frozenset(c for c, bit in enumerate(row) if bit == 0)
        for row in M
    ]


def equal_or_disjoint(defects: Sequence[frozenset[int]]) -> bool:
    for A, B in itertools.combinations(defects, 2):
        if A != B and not A.isdisjoint(B):
            return False
    return True


def normal_form_holds(M: Sequence[Sequence[int]]) -> bool:
    defects = row_defects(M)
    if not equal_or_disjoint(defects):
        return False
    # Rows with the same nonempty defect form a class; distinct defects are disjoint.
    # Every row is exactly complete outside its own defect by construction.
    classes = {}
    for r, D in enumerate(defects):
        classes.setdefault(D, []).append(r)
    nonempty = [D for D in classes if D]
    return all(A.isdisjoint(B) for A, B in itertools.combinations(nonempty, 2))


def enumerate_size(rows: int, cols: int) -> dict:
    total = 1 << (rows * cols)
    survivors = 0
    max_traces = 0
    classification_failures = []
    trace_bound_failures = []
    for mask in range(total):
        M = matrix_from_mask(rows, cols, mask)
        if not avoids_singleton_rectangle(M):
            continue
        survivors += 1
        defects = row_defects(M)
        if not normal_form_holds(M):
            classification_failures.append(mask)
            if len(classification_failures) >= 5:
                break
        distinct = len(set(defects))
        max_traces = max(max_traces, distinct)
        if distinct > cols + 1:
            trace_bound_failures.append(mask)
            if len(trace_bound_failures) >= 5:
                break
    return {
        "rows": rows,
        "cols": cols,
        "all_matrices": total,
        "survivors": survivors,
        "max_distinct_row_traces": max_traces,
        "trace_bound": cols + 1,
        "classification_pass": not classification_failures,
        "trace_bound_pass": not trace_bound_failures,
        "classification_failure_masks": classification_failures,
        "trace_bound_failure_masks": trace_bound_failures,
    }


def main() -> None:
    results = {
        "schema": "oracle.p6-six-vertex-wall.local-verification.v1",
        "canonical_witness": canonical_witness_check(),
        "matrix_exhaustions": [],
    }
    for rows in range(2, 5):
        for cols in range(2, 5):
            results["matrix_exhaustions"].append(enumerate_size(rows, cols))
    results["pass"] = (
        results["canonical_witness"]["all_four_single_edge_orientations_are_P6"]
        and all(x["classification_pass"] and x["trace_bound_pass"]
                for x in results["matrix_exhaustions"])
    )
    out = Path(__file__).with_name("p6_six_vertex_wall_verification.json")
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
