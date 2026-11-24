# How fast can a deterministic RAM decide SAT?

**Research status, 2026-11-24.** The target is to exclude a worst-case bound of O(n²), or more strongly O(n³), for a uniform deterministic RAM deciding ordinary explicit SAT. Here n counts bits in the input. The machine may keep everything it computes. Even excluding O(n) time in this model remains open.

We use binary-encoded literal indices, a conventional explicit formula encoding, words of Θ(log n) bits with a constant sufficient for the polynomial address range in use, and a fixed instruction set with ordinary word arithmetic, Boolean operations, and indirect reads and writes. Word operations have polylogarithmic-size Boolean implementations. Exact timing statements about promise families identify their encoding. A hard family of explicit width-three instances in this encoding would suffice for the general SAT target. At the endpoints a bound of Ω(n³) alone would still allow O(n³).

For the first missing output of the diagonal machine, a single certificate can cover many preceding words. Almost-complete coverage on one interval ending at that output would suffice, even if its length is unknown. A concrete version asks for short circuits that answer a probabilistic proof verifier's queries on those predecessors. I also tested a competing-prover game built directly from the gates of the diagonal computation. Its independent questions are cheap, but its decision gap can be exponentially small in circuit depth. [Batch coverage at every scale](predecessor-batches.md) · [Proof circuits and competing witnesses](referee-certificates.md)

A suggested permanent-graph lower bound gives a precise test for transferring an algebraic decision result to SAT. Its generic-path argument survives on a large finite integer grid. On Boolean matrices the same tree model decides the permanent graph in depth m²+1 by storing an answer at each leaf. We also checked what happens if the complex machine can call an oracle on explicit Boolean strings. [Integer-grid calculation](pr249-grid.md) · [Boolean oracle calls](pr249-oracles.md) · [Original PR #249](https://github.com/1337isnot1337/solved-conjectures/pull/249)

The current search reduces cubic SAT exclusion to a question about two marked addresses per length. For one explicit exponential-time language, a fixed nondeterministic predicate running in 2ⁿ poly(n) time would suffice if it catches either mark on infinitely many lengths while accepting a vanishing fraction of all addresses along those lengths. False positives are allowed. The construction uses time-bounded incompressibility, and the outstanding step is to exhibit that predicate. A separate construction studies what parity information can be recovered from two or three unknown points over a finite field. [Two marked addresses](address-diagonal.md) · [Field moment construction](advised-claims.md) · [Information in support coordinates](moment-information.md)

A partial verifier could help even if it only certifies parities of a computation's answers. On one explicit diagonal language, a cubic SAT algorithm would force each sound uniform verifier within the specified clock to certify only a bounded number of linearly independent parities per length. The constructed truth table is sparse and takes only polynomially many bits of advice to describe. Turning that advice into reliable uniform claims is unresolved. A second construction quantifies how much bias a verifier could have if it makes wrong predictions and receives advice. [Coded diagonal computations](coded-diagonal.md) · [Interpolation from sparse certificates](erasure-hierarchy.md)

A new attempt recovers a RAM verdict by testing the rank of a matrix of changes to selected state observations. The test allows an exponentially large set of observations and arbitrary work memory. On an explicit SAT family that tests equality of k-bit strings, the choice of which verdict gets a common signature matters. Giving every rejection the same signature can force an exponential rank requirement even if each acceptance gets its own signature. Giving every acceptance the same signature permits k simple observations. Adding one flag to switch between equality and inequality forces many signatures for both verdicts under the stated rank bounds, although the formula family still has a linear-time algorithm. A separate attempt certifies a predicted output stream with one SAT query and identifies exactly why a late acceptance flag defeats it. [Conserved observations](conserved-observations.md) · [Prediction from a short prefix](observable-recurrences.md)

A verifier can sometimes leave the bits of an entire satisfying assignment unknown. For a not-all-equal clause it suffices to show that two literals differ. A descending graph of XOR equations and a locally checked relation on pairs of vertices can certify all these differences. Some such certificates are short even when extracting an ordinary assignment would solve a polynomial-space computation. The outstanding step is to construct sufficiently small relations for the satisfiable formulas of a time-hierarchy verifier. Two related tests examine a common hidden tape word and the success probability of generators that share random bits across all tape positions. [Difference certificates](difference-witnesses.md) · [Shared tape words](boundary-factors.md) · [Random witness generators](witness-feedback.md)

The address part of the phase check can now be met on a time-hierarchy verifier itself. An oblivious tape simulation has head positions computable from the clock. Under a hypothetical fast SAT algorithm, first and last visits to a cell can therefore be located in time polynomial in the logarithm of the clock. What remains is a bound on the description lengths of the symbols and states along an accepting run. A separate construction certifies the final parity of some long words by routing matched positions on a grid. On duplicated words an exact bit-probe bound quantifies when this avoids computing a middle state. [Tape addresses](address-orders.md) · [Parity certificates](parity-fillings.md)

A phase-by-phase check of an unrestricted RAM history now uses the intervals of addresses touched in each phase. Across all phases, overwriting those intervals identifies only linearly many pieces on which a read needs a value from an earlier phase. A hypothetical fast SAT solver supplies polynomial-size circuits for testing whether an address occurs in a time interval. The missing bound concerns the number of phases and the size of their chronological row circuits on an actual hierarchy language. A separate test tolerates scattered errors in an assignment and gives a quantitative limit on what solving local restrictions can predict. [Phase histories](phase-histories.md) · [Sparse corrections](restriction-histories.md)

On the algebraic side, the exact-cycle predicate has a polynomial-size representative of individual degree two over every field, although its unique multilinear representative is hard. On the dynamic side, a single increasing chain of Horn formulas forces superlinear total change in the solver’s trace across executions. Each formula on the chain has a fast static algorithm. [Degree-two construction](cycle-representatives.md) · [Trace changes along a chain](edit-amplification.md)

An earlier search studied the polynomial that an ordinary Boolean algorithm can compute when its gates are interpreted arithmetically. For a cycle predicate embedded in valid SAT inputs, every small representing circuit has many distinct monomials that repeat many variables, even on supports of maximum indegree and outdegree three. The cycle predicate itself has a linear-time RAM algorithm. A separate dynamic argument shows that flipping one literal sign can force changes at many time steps of a SAT computation, even on templates with a linear-time static solver. [Polynomial supports](partial-multilinearization.md) · [Changes to execution traces](dynamic-cuts.md)

An earlier search considered short certificates that a succinct constraint system has no solution. When a common seed of b bits determines the labels reached along chosen paths, a gap ε gives a refutation with at most ⌈(b+1)/ε⌉ comparisons. Without a gap, degree-r comparison polynomials on those bits admit a refutation using at most Σⱼ₌₀ʳ binom(b,j) original comparisons. The sharp bound is a special case of a 1999 theorem of Dol’nikov and Igonin. The journal gives an explicit Boolean example and verifies in Lean that deleting any equation gives a satisfying assignment. Evaluating over a larger field can bypass this exact list bound when the comparisons have an efficiently computable multilinear extension in their index. [Root paths and two-to-one obstruction](rooted-propagation.md) · [Algebraic construction and extension](algebraic-residuals.md)

Another approach lets the witness see a probabilistic verifier’s private random bits and supply just the queried answers. A single SAT call can check that enough of those answers agree, even if some proof addresses are disputed. This relaxes the earlier requirement for a circuit computing the whole witness. Obtaining sufficiently small local views for an appropriate hierarchy verifier remains open. [Local views and their weighted agreement test](local-views.md)

The first search found a family of width-three formulas with k independent input signs. Across every equal split of those signs, the log rank of the satisfiability matrix is at least k/2 − O(k/log k). Yet a RAM decides this promised family in linear time by evaluating its forced gates. It also gave a conditional speedup for checking a compressed accepting computation, and verifiers that defeat the proposed compression parameters. [Cut construction](field-cuts.md) · [History simulation](history.md)

## Research journal

| Attempt | Result and outstanding step |
| --- | --- |
| [Joint certificates before the first missing output](predecessor-batches.md) | A sharp interval bound allows false positives and unknown interval lengths. Under cubic SAT every trailing interval retains a fixed fraction of predecessors outside a sound batch verifier's coverage, up to an endpoint term. |
| [Competing witnesses and probabilistic proof circuits](referee-certificates.md) | A perfect refutation reduces to three bounded quantifiers. A sampled check handles bounded likelihood ratios. A local gate game achieves independent questions for the actual computation but misses the required quantitative gap. |
| [Repairing approximate phase products](phase-products.md) · [Pairing dense errors](paired-phase-products.md) | A batched SAT test can verify the locations of defects in a guessed tree of block products. A second verifier can cancel dense inverse pairs, including schedules whose midpoint is PSPACE-hard. |
| [Permanent graph decision trees](pr249-grid.md) · [Discrete oracles](pr249-oracles.md) | The algebraic graph test transfers to an explicit large integer grid. A Boolean matrix admits an unrestricted-size tree of depth m²+1. A nonuniform tree can also absorb ordinary SAT-oracle answers to explicit bit queries. |
| [Two marked addresses](address-diagonal.md) | A list hitting one mark can have vanishing density and arbitrary false positives. A forward-probe swap argument limits how well certificates can narrow a unique missing value in an oracle model. |
| [A bounded amount of advice](advised-claims.md) | An ordinary language with two or three untagged marks resists sound parity predictions past the advice budget. Small lists locating actual marks would suffice under a cubic SAT hypothesis. |
| [Three-point moments](moment-information.md) | Knowing the three abscissas lets sublinear advice determine over 2n independent labels. Merely knowing n linear measurements leaves every next independent label undetermined. |
| [A public coefficient interval](tail-advice.md) | For every possible table on the interval, s advice bits can guarantee exactly s+1 independent signed CRT claims when s is the interval length divided by the modulus degree, rounded down, and s≥2. |
| [Tally recovery of the span](tally-span.md) | The rank-certificate premise for the original sparse diagonal also implies a fixed-exponent time separation on a tally language and on a sparse family of explicit formulas. |
| [Decoding missing outputs](range-decisions.md) | Robust decisions from logarithmically many range-avoidance calls admit a bounded-error simulation, even at unit stretch. Forward-only probes have exponential cost in the call count in the worst case. |
| [Partial and noisy parity claims](coded-diagonal.md) | One diagonal turns unbounded independent sound claims into a sufficient condition against cubic SAT. Another uses a polynomial remainder code to tolerate false claims, abstentions and sublinear-in-table-length advice. Neither supplies the uniformly reliable information. |
| [Sparse certified field evaluations](erasure-hierarchy.md) | Certificates on roughly m/q of a multilinear extension suffice to interpolate at every Boolean point. A gap in distinct certified positions also permits incorrect labels. |
| [Handoffs between local certificates](guarded-covers.md) | Width-w clauses need at most a degree-w monomial dimension minus one counterexample steps for failure. This bound is attained on a safe initialized run. |
| [Ordered searches for valid candidates](ordered-certificates.md) | A map with a small set of separated suffix labels gives a deterministic shortlist. A menu may use a different successful map on each positive input. Producing that menu remains a substantive condition. |
| [Learning conserved observations](conserved-observations.md) | Nonsingular minors certify which terminal verdicts are compatible with the initial observations. On an equality template, merging all rejecting signatures can require exponentially greater rank than merging all accepting ones. |
| [Certifying an observed recurrence](observable-recurrences.md) | One local SAT test certifies a fitted recurrence even if different starts require incompatible predictors. An accepting latch first set at time j has exact recurrence order j+1. |
| [Differences between hidden assignment bits](difference-witnesses.md) | Compatible forks in a descending graph give a potential for every selected literal pair. A relation that progresses on paired vertices can replace circuits for exponentially long individual walks. Even one further comparison on a succinct tree can be PSPACE-complete. |
| [Eliminating one shared word](boundary-factors.md) | Few state changes or a fixed aperiodic relation monoid permit direct verification. Two independently easy sweeps can still have PSPACE-complete joint feasibility. |
| [Locally randomized witnesses](witness-feedback.md) | Bounds on Hamming distance in a dense width-b CNF and pseudorandom generators let the verifier replace shared random bits. A lower bound on the probability of global success is missing. |
| [Calibrating oracle clocks](relativized-clock.md) | Recursive oracles give matching O(nᵖ) and infinitely-often Ω(nᵖ) clocks for oracle-gate CircuitSAT in the specified packed model. The cutoff persists with a known length census and unique witnesses for both answers relative to the oracle. An ordinary uniform test for the hard bit is missing. |
| [Addresses on a hierarchy computation](address-orders.md) | Tape head positions can be made public. Under fast SAT, conditional block hardness already occurs in chronological symbols and states. A finite-field RAM stream defeats common-address interval orders even with flexible short phases. |
| [Certifying parity on a grid](parity-fillings.md) | On a duplicated N-bit word, an edge evaluator using b input probes needs worst-case cut width at least ⌈N/b⌉, achieved explicitly. A second bound allows guessed advice and arbitrarily high grids. |
| [Strategies for interactive checks](succinct-prover.md) | A fixed challenge tree for sumcheck requires exactly two branches per round of degree at least two in the minimum leaf count. Under fast SAT, sufficiently large counting discrepancies admit short adaptive challenge strategies. |
| [Precision on sparse integer cycle tests](exponent-transfer.md) | One extra output bit on sparse inputs forces a global Hamiltonian-cycle parity evaluator. Higher precision recovers the formal polynomial modulo two. A single exact division suffices on the same sparse promise. |
| [Phase histories and address intervals](phase-histories.md) | A sweep replaces the global memory sort in three conditional simulations. General dyadic occupancy circuits are equivalent to NP ⊆ P/poly. Constructing uniformly short visit ranks on arbitrary succinct streams under SAT ∈ P would give exact #P counting in polynomial time. |
| [Sparse corrections to a prediction](restriction-histories.md) | Sort corrections and batch checks of untouched clause ranges. Under a fast solver this forces nearly linear-in-the-exponent Hamming distance from short predictors on infinitely many hierarchy instances. |
| [Trace variation on increasing inputs](edit-amplification.md) | One increasing chain of length-M formulas has Ω(M log M / (log log M)³) cumulative change in aligned execution rows. Static evaluation of the Horn templates takes O(M/log M) word operations. |
| [Degree two and unique solver traces](cycle-representatives.md) | A matrix-tree determinant gives a small degree-two representative of the exact-cycle predicate. Summing out the unique trace of an arbitrary deterministic decision circuit can require superpolynomial arithmetic size. |
| [Determinant tests from matchings](determinant-tests.md) | Exact fixed sums of masked determinant squares require at least m! positive terms. For deciding existence with preselected signs on a three-choice family, the optimal list equals a ternary-cube covering number. |
| [Templates on sparse promised inputs](diagonal-promises.md) | A selector-aware diagonal excludes small interchangeable-block witnesses on a dense part of its square-input promise. The resulting restriction is a hypothesis on how a computation is represented. |
| [Correcting repeated variables](partial-multilinearization.md) | Truncated interpolation recovers the low-degree part under a bound on repeated variables. Row filtering and a random bounded-degree restriction force many exceptional supports in any small circuit for the cycle test. |
| [Which coordinates must repeat?](powered-coordinates.md) | Embedding a bounded-degree cycle instance in the coordinates that never repeat bounds their number across the full polynomial. |
| [Time cuts and changes to RAM histories](dynamic-cuts.md) | An exact bound on charges across intervals, a dynamic range-parity reduction, and a lower bound on the number of trace rows changed by one sign flip. |
| [Boolean threshold accelerators](boolean-accelerators.md) | Two SAT threshold queries give a diagonal contradiction if long computations have short exact queries. Balanced partitions of ordered streams encounter a quantitative obstruction. |
| [The cost of preserving accepting-path counts](linear-encoding.md) | Exact bit budgets for splitting a path count across positive SAT counts. Signed integer computations evade that obstruction when their final values stay bounded. |
| [Rooted constraint systems](rooted-propagation.md) | A short list of paths refutes a constant-gap instance with deterministic transports or output-unique relations. Two reverse choices per edge already allow diameter-six examples with no small inconsistent edge set. |
| [Algebraic comparisons](algebraic-residuals.md) | Boolean specialization of the Dol’nikov–Igonin theorem, with machine-checked sharpness. Changing from Boolean indices to field evaluations can sharply reduce certificate size. The missing algorithm must evaluate the extension cheaply on hierarchy instances. |
| [VP, VNP and the multilinear extension of SAT](sat-extension.md) | The November 23 arithmetic circuit separation supplies the hypothesis of Hrubeš's theorem on monotone 2-CNFs. A restriction of valid SAT encodings transfers the quantitative Hamiltonian cycle bound to SAT's formal multilinear extension. Even ruling out worst-case O(n) time for Boolean SAT on a deterministic word RAM with unrestricted workspace remains open. |
| [Challenge-dependent local views](local-views.md) | A single SAT query tests a weighted consistency threshold. A verifier with small views exceeding its soundness threshold on every YES input would give a hierarchy contradiction. |
| [Relations at time boundaries](dyadic-relations.md) | A NO certificate can use overapproximations to reachability over doubling time intervals. The needed small separating relations have been obtained for restricted transitions. |
| [Sparse easy lengths](sparse-lengths.md) | A conditional hard progression would contradict even one short accepting history or one rejecting input at each length in arbitrarily long intervals. Patching a machine to make its own history short breaks the required equivalence. |
| [Reconciling trace blocks](batch-verification.md) | A coding argument lower-bounds the combined cost of checking parity with separate headers. A transpose example isolates the cost of fixed block access. Adaptive random access remains a possible escape. |
| [Proofs of solver soundness](certificate-reflection.md) | A delayed-error construction transfers finite consistency to soundness. If a fast solver exists, the first error lengths of other programs with the same clock have no computable uniform upper bound in program length. |
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
lean RootTransport.lean
lean LocalViews.lean
lean ResidualBasis.lean
lean SignRestriction.lean
lean TruncatedCorrection.lean
lean BoundaryRelation.lean
lean BatchProbe.lean
lean SparseDiagonal.lean
lean Reflection.lean
lean PhaseAccess.lean
lean SparseRepairs.lean
lean EditAmplification.lean
lean SigningBoxes.lean
lean AddressOrders.lean
lean ParityFilling.lean
lean EvenJets.lean
lean DifferenceWitness.lean
lean BoundaryFactors.lean
lean OracleReplay.lean
lean ObservableRecurrence.lean
lean ConservedObservation.lean
lean CodedDiagonal.lean
lean ErasureHierarchy.lean
lean GuardedCovers.lean
lean OrderedCertificates.lean
lean HoleSwap.lean
lean DiscreteOracle.lean
lean TailAdvice.lean
lean AdvisedClaims.lean
lean RangeDecisions.lean
lean TallySpan.lean
lean GapMaximal.lean
lean PhaseProducts.lean
lean RefereeSupport.lean
python3 history_experiment.py
python3 phase_experiment.py
python3 filling_experiment.py
python3 difference_experiment.py
python3 conserved_observation_experiment.py
python3 coded_diagonal_experiment.py
python3 tail_advice_experiment.py
python3 advised_claims_experiment.py
python3 referee_experiment.py
python3 even_jets_experiment.py
python3 transcript_experiment.py
python3 local_experiment.py
python3 palette_experiment.py
python3 field_experiment.py
python3 propagation_experiment.py
python3 residual_experiment.py
python3 repeat_experiment.py
python3 matching_experiment.py
python3 batch_probe_experiment.py
```

The Lean files state the parts checked by the kernel. The asymptotic constructions, reductions, and complexity estimates are manuscript arguments.
