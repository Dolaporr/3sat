# How fast can a deterministic RAM decide SAT?

**Research status, 2026-11-23.** The requested unconditional lower bound remains open in this journal. The target is to exclude a worst-case bound of O(n²), or more strongly O(n³), for a uniform deterministic RAM deciding ordinary explicit SAT. Here n counts bits in the input. The machine may keep everything it computes. All arguments here leave both clocks possible.

We use binary-encoded literal indices, a conventional explicit formula encoding, words of Θ(log n) bits with a constant sufficient for the polynomial address range in use, and a fixed instruction set with ordinary word arithmetic, Boolean operations, and indirect reads and writes. Word operations have polylogarithmic-size Boolean implementations. Exact timing statements about promise families identify their encoding. A hard family of explicit width-three instances in this encoding would suffice for the general SAT target. At the endpoints a bound of Ω(n³) alone would still allow O(n³).

The strongest counterexample concerns communication between parts of the input. We found a family of width-three formulas with k independent input signs. Across **every equal split** of those signs, the log rank of the satisfiability matrix is at least k/2 − O(k/log k), close to the largest possible k/2. Yet a RAM decides this promised family in linear time in the encoded length by evaluating its forced gates. High rank across many different cuts can result from the same computation. [Construction and proof](field-cuts.md)

The closest route to a positive proof uses a putative fast SAT solver to test whether a compressed computation has a bad step. For a particular unary hierarchy language with a clock of order n¹², small enough circuits for its accepting histories would rule out cubic SAT. The unresolved step is proving such circuits exist for a suitable verifier. The journal gives fixed verifiers that defeat a claim made for every verifier, at exactly the proposed block sizes. [Simulation and counterexample](history.md)

## Research journal

| Attempt | Result and outstanding step |
| --- | --- |
| [Compressing RAM histories](history.md) | A conditional speedup with an explicit budget for checking blocks. Counting attacks show when even unary computations can be made to have expensive blocks. The required compression for a time-hierarchy verifier remains unproved. |
| [Locally generated clauses and succinct witnesses](succinct.md) | A hypothetical fast SAT solver forces large assignment circuits on infinitely many outputs of a local reduction. Clause locality alone supplies no small witness. |
| [Hardness and derandomization](hardness.md) | The hypothesis constructs hard truth tables in exponential time in their arity. Hitting a single accepting assignment remains a separate problem. |
| [Static cuts](transcript.md) | A uniformly easy family of SAT instances nearly saturates an aggregate communication bound while every balanced split has linear log rank in the number of free bits. |
| [Diagonalization and adaptive queries](diagonal.md) | Splitting an explicit computation across SAT calls still charges for every written row. A communication obstruction for joining projected blocks weakens sharply when a deterministic prefix has a unique endpoint. |
| [Monotone clause selectors](local.md) | Perfect matching defeats the proposed family-wise transfer. An exact characterization of monotone decoding explains how a single precomputed word can supply all input complements. |
| [Monotone summaries with spare codes](palette.md) | With q spare codes, at most 2q+1 distinct codes occur on the immediate extensions of any set. This is sharp. A summary attaining the bound can still be computed efficiently. |
| [Finite-field cut construction](field-cuts.md) | Nearly maximal rank on every balanced cut coexists with a quasi-linear-size circuit and a linear-time promise evaluator. |

## Literature checks

Fortnow, Lipton, van Melkebeek and Viglas obtain polynomial time exclusions with simultaneous space bounds. Williams's alternation-trading work also charges space. Mudigonda and Williams state the subpolynomial-space SAT bound for exponents strictly below 2 cos(π/7), approximately 1.802. Even that exponent lies below two. [Fortnow et al.](https://doi.org/10.1145/1101821.1101822) · [Williams](https://people.csail.mit.edu/rrw/automated-lbs.pdf) · [Mudigonda and Williams](https://arxiv.org/abs/2012.00330)

Williams's square-root-space simulation concerns multitape Turing machines. The 2026 two-fifths-power preprint concerns a machine with one writable tape. Both give space upper bounds for simulation. Our trace-checking approach requires an actual time saving on a specified language in the appropriate machine model. [Williams, STOC 2025](https://arxiv.org/abs/2502.17779) · [One-tape simulation, 2026 preprint](https://github.com/openai/math/tree/main/preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026)

The individual notes distinguish literature precedents, elementary deductions, finite checks, and unproved premises. Priority of the auxiliary constructions has not been established.

## Reproducing the checks

Use Lean 4.19.0 with its bundled Std library and Python 3.11 or later. Run from the repository root.

```sh
lean TraceCheck.lean
lean Adaptive.lean
lean CutPacking.lean
lean SwapCount.lean
lean local_summary.lean
python3 history_experiment.py
python3 transcript_experiment.py
python3 local_experiment.py
python3 palette_experiment.py
python3 field_experiment.py
```

The Lean files state the parts checked by the kernel. The asymptotic constructions, reductions, and complexity estimates are manuscript arguments.
