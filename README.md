# How fast can a deterministic RAM decide SAT?

## Research goal

The first target is to rule out a uniform deterministic **O(n)** worst-case algorithm for ordinary explicit SAT on a standard logarithmic-word RAM with unrestricted workspace. An unconditional proof of this linear target alone completes the project. Here n counts bits in the encoded formula. Exclusions of **O(n²)** and **O(n³)** remain successively stronger goals. All three targets are open in this journal. To meet the linear target, the proof must show that for every correct deterministic solver the ratio of worst-case time to encoded input length is unbounded. Equivalently, for every correct solver, every constant C and every length threshold N, some formula of encoded length n≥N requires more than Cn steps. A bound such as Ω(n log log n) would meet the linear goal. An unbounded ratio along a subsequence also suffices.

We use binary-encoded literal indices, a conventional explicit formula encoding, words of Θ(log n) bits with a constant sufficient for the polynomial address range in use, and a fixed instruction set with ordinary word arithmetic, Boolean operations, and indirect reads and writes. Word operations have polylogarithmic-size Boolean implementations. Exact timing statements about promise families identify their encoding. A hard family of explicit width-three instances in this encoding would suffice for the general SAT target. Each target excludes the stated big-O bound. A matching big-Omega bound alone is compatible with it.

## Current results

One bit about the fraction of exceptional lengths would suffice for a lower bound. If a uniform SAT formula can certify this bit on infinitely many blocks, within the specified size, linear-time SAT is impossible. The verifier can even make mistakes at a quantified rate. I found explicit windows in which at least half the blocks have the desired bit. Turning that group argument into a short proof for even one block in infinitely many windows remains open. [One-bit criterion, failed predictors and individual proof lengths](exceptional-fraction-bit.md)

For the linear target, I changed the search from finding an individual missing output to certifying a count across input lengths. Among lengths from 2ʲ through 2ʲ⁺¹−1, the fraction with an early missing output tends to one as j grows. The last block whose exceptional fraction exceeds 2⁻ᵏ is bounded above and below by busy beaver values with arguments k+O(1) and k−O(1). A sufficiently small SAT certificate for one favorable block at each of unboundedly many precisions would exclude linear-time SAT. Constructing those certificates remains open. [Counting across lengths](prefix-lengths.md)

For the cubic target, I found a criterion that tolerates false proofs. Let v be the first n-bit word omitted by a bounded universal machine, and W(z) the number of proofs accepted by a short verifier for word z. If a cubic SAT solver exists, every consecutive interval of K words immediately below v on which each word has more proofs than v must satisfy K+1 ≤ C(W(v)+1), for a fixed verifier-dependent constant C. A second test checks all program–output candidates jointly by matching. It tolerates ambiguous rows and matchings that change with the public challenge. The missing ingredient is a verifier that violates either bound on the actual outputs. [Witness-count criterion](multiplicity-dips.md) · [Matching and Hall certificates](matching-holes.md)

One approach asks whether a few public questions about a claimed memory history can rule out a false computation. On a fixed 12-cell example, three adaptively chosen field evaluations rule out every false pair of logs, while each of the 23,426 fixed triples lets a false pair pass. Achieving a suitable separation at infinitely many lengths for the actual first missing output of a bounded universal machine would exclude linear-time SAT. [Argument and experiment](public-memory-fingerprints.md)

A linear-time SAT solver would make it cheap to ask two questions about a proposed stream of computation records. Does it allow any locally realizable run, and does it allow any run with a wrong memory value? A short description for which the answers are yes and no would certify acceptance. Finding such descriptions for a particular unary language with a known time lower bound could exclude linear SAT. For a stream that simply carries independent bits between fixed locations, the largest number of legal streams that one sound filter can accept is exactly a power of two given by interval scheduling. [Hierarchy criterion](streaming-transport.md) · [Exact filter capacity](filter-capacity.md)

One test of the linear-time hypothesis now reaches the graph of block visits in an actual unary hierarchy computation. Under that hypothesis, at infinitely many accepted lengths every accepting run of the chosen verifier must have nearly linear treewidth in its number of epochs. Two writable tapes can already realize graphs of linear treewidth with three reversals on one head and two on the other. The open step is finding an accepting run whose words across the cuts have shorter descriptions, or a verifier whose graph has smaller cuts. [Tape partitions and the two-tape construction](tape-partitions.md)

For the linear target, I tested what an O(n) SAT solver would imply for checking long computation histories. It would decide an O(N)-space nondeterministic tape computation on N input bits in deterministic time 2^{O(√(N log N))}. It would also let a verifier check many partial tape transitions in time quasilinear in their combined description length. A lower bound for unrestricted SAT still requires showing that a computation with a known time lower bound admits sufficiently short checks. [Quantifier elimination and checkpoint lengths](linear-quantifiers.md) · [Checking adaptive queries together](linear-sat-batches.md) · [Partial transitions and the equality test](epoch-dictionaries.md)

The permanent graph proof from PR 249 still applies if a verifier searches over finite binary witnesses. At a generic complex input one can make every test in a countable family agree on a graph point and an off-graph point. For an integer grid we quantify the input precision needed as the number of tests grows. This yields no superlinear bound in the encoded bit length. [Boolean witnesses on the permanent graph](pr249-witnesses.md) · [Original PR](https://github.com/1337isnot1337/solved-conjectures/pull/249)

For a unary hierarchy computation, infinitely many accepted lengths force many distinct transitions between tape blocks. A cubic SAT algorithm would nevertheless suffice to check large groups of partial transition descriptions, if those descriptions covered an accepting run and worked for every block they admitted. A second test characterizes exactly how the gap of a verifier for a graph of Boolean implications depends on the shortest path between conflicting pins. [Tape-block transitions](epoch-dictionaries.md) · [Sampling gate values](probe-allocation.md) · [Checking joint gate distributions](local-bag-consistency.md)

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
| [One bit about exceptional lengths](exceptional-fraction-bit.md) | On every fast infinite list both values of the bit have upper relative density one. A simple predictor achieves logarithmic accuracy one. The two notions of accuracy give different SAT criteria. |
| [Limits of fast producer covers](delayed-prefix-covers.md) | A self-referential program prevents a sound finder from excluding any entries of one fixed prefix at all large lengths, even when none of the programs there halts. |
| [Late outputs across many lengths](time-by-length.md) | Linear SAT forces almost all words in many complete prefix blocks to acquire their first short producer during a final interval of the native clock. |
| [The distribution of first production times](clock-release.md) | A timely sampler forces new outputs in each targeted time interval and output class under linear SAT. |
| [Approximate counts near the native cutoff](near-native-counting.md) | Linear SAT would give quasilinear projected approximate counts. They bound how often a joint model can have an anomaly at the actual missing output, even after conditioning on a rare event. |
| [Prefix-free programs across input lengths](prefix-lengths.md) | A global Kraft bound gives dense blocks of favorable lengths. Their convergence has no computable modulus. A checkable upper bound on the exceptions in one block would suffice under an explicit clock. |
| [Coordinate tests on one omitted word](coordinate-omissions.md) | An adaptive exposure inequality bounds the number of local witness-count dips, accounting for advice and dependence on other coordinates. |
| [Computations stored in fewer physical cells](address-folding.md) | Faithful replay can be checked one virtual address at a time under linear SAT. Five binary operations per address can already force a separate physical cell for every address. |
| [Program outputs with shared answers](shared-answer-coverage.md) | If all admissible tables are injective and the shared bits obey affine constraints, depth k per row permits at most 2ᵏ possible holes. The bound is attained. |
| [Multiplicity of proofs near the first missing word](multiplicity-dips.md) | A one-witness advantage throughout a sufficiently long interval would exclude cubic SAT, even with false proofs at its endpoint. The integer-array packing bound has an exact finite maximum. |
| [Matching program names to candidate words](matching-holes.md) | The actual omitted word must remain among many possible matching holes even after intersecting over public challenges, assuming cubic SAT. Sparse candidate lists alone can leave all holes possible. |
| [The first incorrect read](first-fault-cache.md) · [Recovering the incoming words](native-first-reads.md) | Linear SAT would force many potential first faults on one genuine trajectory and expensive incoming-word predictions on every genuine producer of many predecessors. |
| [Incorrect returns of stack symbols](stack-packet-faults.md) · [Isolating an owner's possible words](local-word-isolation.md) | On rejecting hierarchy inputs, one false chronology can contain a large nested set of erroneous pops. On accepting inputs, the cost of identifying only one endpoint's words gives a separate criterion. |
| [Running the missing-word decoder natively](native-missing-word.md) | A different bounded interpreter eliminates two tape simulation costs. Fast polynomial evaluation lets a fixed number of adaptive rounds test B/polylog(B) points at the first word omitted within B steps. |
| [Public fingerprints at the first missing output](public-memory-fingerprints.md) | Under linear SAT, every sufficiently short public tuple eventually lets some false log pair pass at the actual first omitted word. To exclude linear time, one separating tuple there at infinitely many lengths would suffice. |
| [Sound one-pass filters](streaming-transport.md) · [Capacity on repeated records](filter-capacity.md) | A filter can admit many distinct accepting streams. For repeated independent bits in a fixed order, interval packing gives its exact maximum coverage. Finding a short sound filter for a hierarchy verifier remains open. |
| [Information crossing the proof tape](crossing-bits.md) | On a family of RAM logs, certifying every consistent raw input costs quadratic weighted head movement, even with data-dependent ordering. A verifier that chooses which runs to admit has more freedom. |
| [Completing the bounded decoder](semantic-completion.md) | Processing names online gives a total injection missing just the original first gap. Every predecessor keeps its earliest original producer. |
| [Factoring local lookup functions](factored-lookups.md) | A fixed diagonal's local lookups admit efficient field evaluation. The published recursive schedule still calls them exponentially many times. |
| [Partitioning the tape visits](tape-partitions.md) | A universally selected part of an accepting run can be checked with the descriptions of the words on its ancestral cuts. Two writable tapes already realize expander minors. |
| [Checking changed cells](checkpoint-pullbacks.md) | Following a cell to its source can determine the truth of a proposed update even over an unknown starting memory. No qualifying shared description has been obtained for enough actual diagonal outputs. |
| [Simultaneous time and space](simultaneous-space.md) | A specific language has separate fast and small-space algorithms. A combined bound or a sufficiently short one-tape head movement on a hierarchy source would exclude linear SAT. |
| [Tuning the first missing output](tuned-first-hole.md) | A fixed universal decoder can make an arbitrarily high constant fraction of preceding addresses easy. Allowing this fraction to tend to one incurs a matching cost in the decoder header for this construction. |
| [Adaptive batches under linear SAT](linear-sat-batches.md) | Checking the answer transcript lets a deterministic decoder pay for one controller replay and one oracle test. A resulting bound on the actual producers still leaves a missing compression step. |
| [Growing-depth checkpoint checks under linear SAT](linear-quantifiers.md) | Quasilinear elimination at each block gives a quantitative time simulation for short configurations. It still pays for the configuration bits of the computation being checked. |
| [Adaptive bit probes on a finite permanent grid](pr249-bit-probes.md) · [Signed integer construction](pr249-integer-pivot.md) | A finite-grid extension of PR #249 allows partial access to digits of every matrix entry, or full access to the candidate value with a hidden rational entry. Both cases still restrict matrix probes and algebraic degree. |
| [Discrete witness families on the permanent graph](pr249-witnesses.md) | The finite-grid calculation handles proofs chosen separately on each input, including randomized checks. It still requires many bits per matrix entry. |
| [Short descriptions of block transitions](epoch-dictionaries.md) | A concrete sufficient condition on a unary hierarchy language uses partial records that work for every compatible input. Their existence remains open. |
| [Probing a graph of implications](probe-allocation.md) · [Overlapping gate distributions](local-bag-consistency.md) | Optimal probing of an implication graph has an exact shortest-path formula. Joint distributions strengthen the check on a reconvergent circuit, with a gap that can still shrink with its length. |
| [Choosing an order to fill missing outputs](adaptive-unranking.md) | One order captures every position reachable by interval producers. Repeated sweeps cover all positions reachable with arbitrary fixed lists and impose a quantitative limit on certification near the first omission. |
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

For the linear-time target, the deterministic random-access results of Fortnow, Lipton, van Melkebeek and Viglas impose a simultaneous space bound. A pure time bound by van Melkebeek and Raz applies to a machine with one geometrically organized work tape. [Fortnow et al., full text](https://lance.fortnow.com/papers/files/tst.pdf) · [Van Melkebeek and Raz](https://www.sciencedirect.com/science/article/pii/S0304397505005402)

Williams's alternation-trading work also charges space. Mudigonda and Williams state the subpolynomial-space SAT bound for exponents strictly below 2 cos(π/7), approximately 1.802. Even that exponent lies below two. [Williams](https://people.csail.mit.edu/rrw/automated-lbs.pdf) · [Mudigonda and Williams](https://arxiv.org/abs/2012.00330)

Williams's square-root-space simulation concerns multitape Turing machines. The 2026 two-fifths-power preprint concerns a machine with one writable tape. Both give space upper bounds for simulation. Our trace-checking approach requires an actual time saving on a specified language in the appropriate machine model. [Williams, STOC 2025](https://arxiv.org/abs/2502.17779) · [One-tape simulation, 2026 preprint](https://github.com/openai/math/tree/main/preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026)

The individual notes distinguish literature precedents, elementary deductions, finite checks, and unproved premises. Priority of the auxiliary constructions has not been established.

## Reproducing the checks

Use Lean 4.19.0 with its bundled Std library and Python 3.11 or later. The finite permanent-grid and matching experiments use SymPy. Run from the repository root.

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
lean WitnessCoupling.lean
lean LinearElimination.lean
lean ProbeAllocation.lean
lean LocalBagConsistency.lean
lean RankAllocation.lean
lean EpochDictionary.lean
lean PartitionWitness.lean
lean StackVisit.lean
lean PullbackEvaluation.lean
lean TapeTravel.lean
lean TunedFirstHole.lean
lean CrossingLoad.lean
lean FactoredLookup.lean
lean FilterRectangle.lean
lean SemanticCompletion.lean
lean StreamFilter.lean
lean MomentTest.lean
lean FirstFaultCache.lean
lean FirstReadReplay.lean
lean HoleExchange.lean
lean MultiplicityDips.lean
lean StackPacket.lean
lean PrefixLengthMass.lean
lean CoordinateOmissions.lean
lean AddressFolding.lean
lean SharedAnswerMass.lean
lean ClockRelease.lean
lean DelayedPrefixCover.lean
lean ExceptionalBands.lean
lean TimeByLength.lean
python3 near_native_counting_experiment.py
python3 coordinate_omissions_experiment.py
python3 shared_answer_coverage_experiment.py
python3 hole_exchange_experiment.py
python3 multiplicity_dips_experiment.py
python3 native_first_reads_experiment.py
python3 filter_capacity_experiment.py
python3 finite_grid_experiment.py
python3 public_fingerprint_experiment.py
python3 history_experiment.py
python3 phase_experiment.py
python3 filling_experiment.py
python3 difference_experiment.py
python3 conserved_observation_experiment.py
python3 coded_diagonal_experiment.py
python3 tail_advice_experiment.py
python3 advised_claims_experiment.py
python3 referee_experiment.py
python3 probe_allocation_experiment.py
python3 unranking_experiment.py
python3 tape_routes_experiment.py
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
