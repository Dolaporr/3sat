# How fast can a deterministic RAM decide SAT?

## Research goal

The first target is to rule out a uniform deterministic **O(n)** worst-case algorithm for ordinary explicit SAT on a standard logarithmic-word RAM with unrestricted workspace. An unconditional linear-time exclusion would settle the first milestone. The full project seeks an unconditional quadratic- or cubic-time exclusion. Here n counts bits in the encoded formula. Exclusions of **O(n²)** and **O(n³)** remain successively stronger goals. All three targets are open in this journal. To meet the linear target, the proof must show that for every correct deterministic solver the ratio of worst-case time to encoded input length is unbounded. Equivalently, for every correct solver, every constant C and every length threshold N, some formula of encoded length n≥N requires more than Cn steps. A bound such as Ω(n log log n) would meet the linear goal. An unbounded ratio along a subsequence also suffices.

We use binary-encoded literal indices, a conventional explicit formula encoding, words of Θ(log n) bits with a constant sufficient for the polynomial address range in use, and a fixed instruction set with ordinary word arithmetic, Boolean operations, and indirect reads and writes. Word operations have polylogarithmic-size Boolean implementations. Exact timing statements about promise families identify their encoding. A hard family of explicit width-three instances in this encoding would suffice for the general SAT target. Each target excludes the stated big-O bound. A matching big-Omega bound alone is compatible with it.

## Interactive verification on an unrestricted RAM

Fix the native $M$-step computation used for the two hard SAT instances at each scale. For any sound interactive verifier of one of its answers, a pruned tree of executions on which one prover already beats the soundness threshold has a nondeterministic check linear in the explored work $Q$. Its ordinary 3-CNF takes $O(Q\log^3 M)$ bits for polynomially related clocks. Infinitely many correct scales with $Q=o(M^{1/k}/\log^3 M)$ would exclude $O(n^k)$ SAT. The needed small trees are open. A separate theorem turns fixed-round private-coin proofs into exact alternating decisions while charging verifier work, private bits and communication. [Tree check and SAT transfer](few-coin-sat-transfer.md) · [Private-coin alternation cost](statistical-proof-alternation-cost.md)

An arbitrary two-word, one-bit opcode preserves a hypothetical ordinary alternating speedup that handles a public transcript of $T$ bits. A fixed recursive opcode defeats statistical verification even with a public, uniformly generated circuit that disagrees with it on at most one operand pair. At true equality instances a correct verifier can require expected work linear in the entire operand domain. One universal operand challenge checks agreement. [Lifting proof and single-error construction](binary-opcode-speedups.md) · [The case of an exact public circuit](explicit-circuit-row-verification.md)

Under the hypothesis that SAT takes $n^{1+o(1)}$ time, every solver must have cumulative occupied-word count, including one unit per step, at least $n^{2-o(1)}$ on both members of every sufficiently large pinned pair. The proof tests just the values returned by reads of writable memory, with no guessed address ordering. [Read replies on the explicit pinned family](priority-pinned-load-replies.md)

## Superlinear SAT time with one geometric tape and polynomial random-access scratch

On a deterministic machine with unrestricted use of one fixed $d$-dimensional work tape, random input access and time-average occupancy of $O(T^\omega)$ nonzero random-access scratch words over a run of $T$ steps, no $O(N^c)$ worst-case algorithm for ordinary SAT exists whenever $(d+1+d\omega)c^2<c+d+1$, for $0\le\omega<1/d$. On a planar tape with $O(T^{1/4})$ scratch, this excludes even $c=1.075$. The proof gives a checkable description of the actual execution across revisits to tape regions. [Theorem and proof](hybrid-tape-cut-trading.md) · [Independent two-block derivation](hybrid-tape-crossing-chart.md)

A separate unrestricted-RAM promise problem consists of two explicit 3-CNFs at each scale. They differ in one known literal sign. Even when given the scale, sign, and promise for free, every correct deterministic solver takes $\Omega(N/\log^3 N)$ on **both** members at every sufficiently large scale. Direct evaluation matches the bound on that promise. [Construction and matching algorithm](priority-pinned-sat.md)

## What can a hard register history say about SAT time?

For both SAT verdicts there are explicit word-order families on which every timely sound solver must load every movable word. On almost all orders even a circuit with $\eta N/\log N$ gates fails on most first-load register rows. One fixed solver decides both entire families in $O(N/\log N)$ word steps. When each tag has an independent payload of the same bit length, even a carefully chosen order allows only about half the fresh words to be predicted on almost every table, and half is attainable. The same holds for a cycle of actual XOR constraints with a positive fraction of its variable-name bits individually sensitive on both verdicts. [Logical cycle theorem](logical-cycle-word-payloads.md) · [Sharp prediction rate](word-payload-order-rate.md) · [Unconditional circuit bound](scan-time-register-complexity.md)

Under the quadratic or cubic SAT hypothesis, all $B!$ word orders of a different positive family require hard register histories, including orders that directly reveal a satisfying assignment. [Hard positive histories across all word orders](word-permutation-positive-histories.md) · [Common hard lengths and variable names](common-positive-histories.md)

For the quadratic and cubic targets a single SAT call suffices to check certain alternating strategies on a high-clock diagonal. An inexpensive verdict extractor itself supplies an opponent program on whose entire prefix it fails, even when success is required only on sparse favorable paddings. [Strategy verification and quantitative targets](strategy-dag-certificates.md) · [Padded-game analysis](padded-game-separation.md)

## Reviewed results and the next working milestone

One planar work tape and one linear work tape suffice to realize a fault-tolerant directed grate when the linear head visits $\Theta(\sqrt T)$ cells in $T$ steps. Below that threshold every such access graph has a sublinear segregator. In every fixed dimension $d\ge2$, the matching threshold becomes $T^{1/d}$. A grate requires that many auxiliary cells to be live simultaneously on a positive fraction of all time cuts. [Dimension and live-cell proof](mixed-tape-dimension-threshold.md) The release also gives the growing-dimension nondeterministic tape simulation and collects the cumulative-memory, treewidth and locally decodable state bounds for actual SAT solvers. [Master theorem, proofs and priority review](computation-history-theorem.md)

The next working milestone is the native question $\mathrm{NTIME}_{\rm RAM}[n]\ne\mathrm{DTIME}_{\rm RAM}[n]$, using bounded nondeterministic RAM acceptance with a unary clock. A linear solver for this complete problem must occupy $\Omega(n)$ bits in currently nonzero work words on inputs of both verdicts at every sufficiently large length. Its time budget permits $O(n\log n)$ work bits. An explicit-SAT linear lower bound would imply this native separation because explicit SAT has a linear nondeterministic verifier on this RAM. For example, it can intern binary variable names in a trie as it scans the formula and guess a consistent value at each new name. Deriving a SAT lower bound from a native separation requires a reduction that preserves linear encoded length and time. [Native language, encoding and lower bound](native-unary-clock-band.md) · [Alternating speedup criterion for the native diagonal](alternating-native-speedup.md) · [A multilinear oracle at the linear clock](multilinear-oracle-clock.md)

## What does algebraic hardness force on the physical bits of SAT?

On a dense fixed-stride 3-CNF encoding, **any** set of $h^\epsilon$ input bits at the specified $h$-bit lengths contains a face testing a polynomial-size directed cycle matrix. These can all be bits in variable names. Using the reported formal Hamiltonian cycle lower bound, a polynomial-size arithmetic representative of SAT on the Boolean cube cannot remain multilinear on that many positions after every Boolean pinning of the others. A scan-time unit-propagation language has the same restriction property. The result leaves the unrestricted SAT time objective open. [Construction, bounds and test on actual records](arbitrary-sat-coordinate-faces.md)

For the complex permanent graph, permitting numerical queries to an arbitrary degree-two extension of a fixed SAT table preserves the graph lower bound from PR 249. The unique multilinear SAT extension is different: a single numerical query recovers the permanent. A sparse perturbation version quantifies the number of redundant calls needed. [Oracle theorem and circuit simulation](quadratic-oracle-exclusion.md) · [Consequences for the Boolean permanent itself](matching-coordinates-permanent.md)

## How much can a fast solver compress its own states?

At linear time with constant-time word lookup, some unsatisfiable inputs force $\Omega(N/\log^3 N)$ bits across independent descriptions of the solver's actual memory on one prescribed grid of $K\log^6 N$ intervals. One checkpoint needs $\Omega(N/\log^9 N)$ bits. [Fixed-grid proof](solver-snapshot-descriptions.md) · [A discovery cut with exponentially many easily decoded states](selected-input-rereads.md) · [What can be inferred from the remaining accepted inputs at a switch](conditional-switch-residuals.md)

There is a sharp trade on genuine SAT inputs between the information retained after $\ell$ distinct input-bit discoveries and the number of those bits the solver must read again. If the state and the discovered set have $o(\ell)$ joint entropy on the code family, almost every prefix forces at least $(1/2-o(1))\ell$ rereads on **every** codeword completion. On a family satisfying the same code-distance hypotheses, a scan-time solver attains the full fixed-fraction trade using a Hamming covering code. [The cut, the counting proof and the matching programs](selected-prefix-rank.md)

For every fixed time exponent below $2\cos(\pi/7)$, a deterministic SAT solver meeting that clock must reach states for which a fixed decoder cannot simultaneously use a subpolynomial-length description and subpolynomial time per word. The decoder receives the physical input and the instruction time. A nested checkpoint test needs correctness only from a genuine predecessor. This permits consecutive speedups in the published alternation-trading proof. No bound on the solver's physical workspace is assumed. [Statement, quantifiers and hierarchy argument](true-start-snapshot-trading.md)

A solver running in $N^{8/5+o(1)}$ time on unsatisfiable inputs must, for each fixed decoder, have arbitrarily long inputs of that sign with $\lceil N^{79/80}\rceil$ consecutive states where $N^{1/100}$ bits of advice and $N^{1/100}$ word-lookup steps do not suffice together. [Signed-window bound](signed-snapshot-windows.md) · [Linear-time example testing the limit of this approach](inverse-snapshot-frontier.md)

At near-linear time an explicit construction gives a whole family with the SAT verdict of parity. On **every** odd payload, hard indexed snapshots survive permuting a specified number of arbitrary clauses. Another choice of guard makes hard indexed snapshots, later native reads of old data, and difficult proof queries occur on the same actual rejecting run. The charges proved for those distinct reads still fit a linear clock. [Indexed snapshots and clause permutations](guarded-indexed-snapshots.md) · [Disjoint discovery intervals](noisy-dual-solver-cuts.md)

## What must a solver retrieve after it has read half the data?

On an explicitly generated family of $n$-bit 3-CNFs, stop each actual deterministic solver when it first sees half the designated data bits, in its own read order. At every large scale some input forces it either to reread $\Omega(n/\log n)$ distinct earlier data bits or to retrieve $\Omega(n/\log^2 n)$ distinct **nonzero** work words written before the cut. The solver has unlimited workspace. The proof treats arbitrarily many reads of initial zeros for free. A globally correct solver matches the work-word count on the family by packing the bits and finishes in $O(n/\log n)$ steps. Counting all incoming work addresses also gives a version on almost every input of each verdict. [Proof for the actual read order](half-read-reuse.md) · [Uniform expander construction](expander-cut-signs.md) · [Sparse graph bounds](sparse-quadratic-sat-cuts.md) · [Finite sign argument in Lean](PositiveQueryLeaves.lean)

A snapshot theorem applies to **every actual solver**, with no time or space hypothesis. Give a reconstruction procedure the original formula, the complete history before a block of $t$ fresh pin discoveries, the controller just after the block, and advice chosen after the entire input is known. On almost every input, for many disjoint blocks, reconstructing the true work array with at most $\beta t$ advice bits for a fixed small constant $\beta>0$ requires the reconstruction or the subsequent solver run to inspect $\Omega(t/\log(2+2m/t))$ distinct pins from that block. A separate result charges actual work changes or actual later reads. Even eliminating the spacing between sign locations cannot shrink this verdict's explicit fixed-layout width-three encoding below $\Omega(m\log m)$ bits. [Whole-array reconstruction theorem](discovery-epoch-snapshot-codes.md) · [Changes in disjoint intervals](sparse-epoch-changes.md) · [Encoding bound](certificate-width-encoding.md)

The nonzero-word bound now has an almost-everywhere version for linear-time solvers. Except on a $2^{-\Omega(n/\log^4 n)}$ fraction of the inputs of either verdict, the actual suffix rereads $\Omega(n/\log n)$ distinct old pins or retrieves $\Omega(n/\log^4 n)$ distinct nonzero earlier words. A product inequality also counts errors of a suffix-side forecaster that receives every genuine reply after predicting it. Independently, with unlimited time a constant fraction of runs retrieve information from $\Omega(n/\log^2 n)$ distinct source intervals, each acquiring logarithmically many fresh pins. The same explicit family admits a solver in which all the store/load pairs cross one midpoint. [Forecast error theorem](sparse-reply-sat-cuts.md) · [Adaptive polynomial lemma](adaptive-default-polynomial.md) · [Independent source intervals](birth-epoch-reuse.md) · [Matching solver](tile-matching-sat.md)

Finite-field hashes reduce the degree cost of checking long lists of default answers. A pattern-matrix example gives a lower bound for any attempt to convert them to a uniformly accurate real inner product. A canonical hard table and a construction with randomly matched local blocks illustrate the separate costs of large addresses and joint preprocessing. For a self-referential family, a translated verifier test gives one common samplable distribution of hard proof addresses at every timely rejection. [Finite-field and pattern-matrix bounds](hashed-default-leaves.md) · [Large-address counterexamples](canonical-nonzero-cuts.md) · [Local block preprocessing](random-matching-blocks.md) · [Translated verifier and permutation counterexample](shifted-proof-challenges.md)

A random polynomial on the data gives a separate test across every balanced input split. The prefix and suffix may each probe the opposite side and may check an arbitrarily long independently decoded snapshot for equality. A three-bank construction permits private unordered fragments. An explicit pair of optimal solvers shows how all transfers of one solver can cross the same midpoint, while another solver returns the same verdicts with no writable transfers. A separate proof tests whether a small number of checks can certify the computation that selected a SAT verdict. [Two-sided input probes](spectral-sat-cuts.md) · [Adaptive memory reads and partial array checks](spectral-work-reads.md) · [Three-bank argument](three-bank-solver-phases.md) · [Unordered fragment verification](unordered-solver-fragments.md) · [Single-cut counterexample](single-cut-transfer-graphs.md) · [Sampled verdict checks](exact-sampled-verdicts.md)

A separate self-referential construction uses a Reed–Solomon code to produce two distributions with identical small input marginals. One stays far from every timely rejection. On almost every input from the other distribution the physical formula is unsatisfiable, and any sufficiently fast solver must actually reject it. Every rejecting computation must inspect both bits of many coordinate pairs even after a quarter of the symbol locations, up to rounding, are discarded. The proof-read lower bound also survives a later change of proximity verifier under the stated probe bound. [Guarded-code proof and model](guarded-code-rejections.md)

## How long do opposite SAT verdicts take on the same clause layout?

At every sufficiently large scale a uniform generator gives pairs of $n$-bit 3-CNFs. Exactly one member of each pair has a satisfying assignment, and that assignment is unique. Across the whole list only $O(\log\log n)$ designated literal signs vary. For every fixed correct deterministic SAT solver, **both members of all but a solver-dependent constant number of pairs take more than $n/\operatorname{polylog} n$ steps**. The index and the locations of the varying signs can be given to the solver. The proof also bounds how many pairs a sound shortcut with shared advice can answer, with a converse for the overhead of supporting many advice lengths. Under an explicit padding choice, one globally correct solver recognizes and decides every family member in $O(n/\log n)$ steps. [Proof, advice bounds and exact clock](shortcut-capital.md) · [Lean mass argument](ShortcutCapital.lean)

A second construction allows a long shared random input and measures how many distinct bits of it a predictor reads after receiving advice. With $2^b$ selectors and a fixed polynomial work allowance in $2^b$, an inverse-polynomial advantage in $b$ requires the product of advice length (plus $b+1$) and distinct bit probes (plus one) to exceed $2^b/\operatorname{poly}(b)$ on almost every public tape at infinitely many scales. Here $b\le\log_2 n\le b^{O(1)}$. Other entries bound the information retained at a cut in an actual SAT run, verify RAM loads using a forward permutation, and extract the formal permanent under explicit restrictions on its degree-two Boolean representative. [Shared public inputs](semantic-public-tapes.md) · [Sharp moment estimates](semantic-moment-transfer.md) · [Cut information](semantic-cut-permutations.md) · [RAM load verification](succinct-claw-checkpoints.md) · [Degree-two extraction](symmetric-cube-slices.md)

## Can the same formulas test every solver?

At every sufficiently large scale, an unconditional construction gives a list of $O(\log n)$ equal-length 3-CNFs. Its first unsatisfiable member defeats every sound nondeterministic rejection certifier in a growing program pool within $n/\operatorname{polylog} n$ steps, even with the list index supplied. The shortest list that could do this has the same order in the pool size. Under a linear-time SAT hypothesis, on that same member *every* fixed correct near-linear solver has cumulative locally decodable snapshot length at least $n^2/\operatorname{polylog}n$, with a decoder-dependent log power. [List construction, finite matching and selection cost](first-missing-certificate-level.md) · [Lean proof](FirstMissingCertificateLevel.lean)

Under near-linear SAT, a second generator produces pairs differing in one literal sign. At every sufficiently large scale all but a vanishing fraction of random seeds produce an unsatisfiable and a satisfiable member with the same snapshot lower bound for every admitted sound solver and decoder. One incorrect program can spoil only its first offering seed. A short program that names a seed can force it to be exceptional. Local parity-verdict protocols and solver-specific shortcut tests give further limits on recognizing easy answers. [Shared seeds, time budgets and both signs](common-solver-seeds.md) · [Certification of solver-specific shortcuts](signed-specialization-index.md) · [Parity challenge and proof-length tradeoff](alternating-parity-certificates.md)

At the first failed index, every Hall witness names exactly the neighboring programs. Every matching on the preceding, satisfiable prefix reveals the same answers for programs that ignore their row. This places true, expensive-to-certify missing edges inside every actual Hall witness. With near-linear SAT, batching the positive checks allows both the program pool and the individual offer clock to grow to $n/\operatorname{polylog}n$. A separate sampler for the common signed family makes bounded-time randomized decisions only slightly better than chance under that hypothesis. [First-failure witnesses](first-failure-hall-witnesses.md) · [Advice bounds and randomized sampler](seed-filter-advice.md) · [Canonical witness bits and easy promised verdicts](canonical-witness-pins.md)

## What can a short description predict about an actual SAT run?

Suppose a deterministic linear-time SAT solver and a fixed polylogarithmic-time decoder share arbitrary advice about a run. On some unsatisfiable inputs of length $n$, advice of at most a sufficiently small constant times $n/\log^7 n$ bits leaves at least $\Omega(n/(\log^7 n\log\log n))$ errors on distinct bit coordinates of words actually read before a write in their block. For whole words, let $M$ count distinct incoming block–address pairs and $R$ be the predicted word XOR the true word. Advice length plus $M$ times the empirical entropy of $R$ is at least $\Omega(n/\log^7 n)$. This still holds for conditional entropy when each pair receives one of at most $n^\alpha$ efficiently computed tags, for any fixed $0\le\alpha<1$, on the specified decoder grid. A weaker bound reaches a tag range of $n/\log^{8+\rho}n$ for each fixed $\rho>0$. [Proof, parameters and error correction](partial-domain-snapshot-errors.md) · [Finite filter semantics](CascadeSnapshotErrors.lean)

A decoder may instead retain mutable scratch across reads within each forecast. A cumulative charge for description length and private work beyond a fixed per-prefix allowance is outside $O(n^{1.3622})$ unconditionally on unsatisfiable inputs. Under near-linear SAT there are at least $n/\operatorname{polylog}n$ genuine starting times on one run at which either the proposed description is long or its online reconstruction takes substantial time. Even an approximate predictor receiving the genuine native history after each guess has an unconditional cumulative lower bound, charging its advice, excess work, used tags and exceptions. A correct SAT solver can attain order $n^{1.97}$ in this charge on explicit inputs handled in $\Theta(n)$ time, by repeatedly scanning a validated inverse permutation. With the original short permutation source available, a padded version still reaches $n^{3/2}/\operatorname{polylog} n$ in linear time at the encoded-length relation of the square-clock diagonal. [Sharp linear-run counterexample](stateful-inverse-windows.md) · [Stateful replay and quantifiers](stateful-incoming-decoders.md) · [Cumulative clock in Lean](OnlineDecoderClock.lean)

## Reading decision answers with a public isolation hash

Assume SAT takes $O(n^d\operatorname{polylog}n)$ deterministic time for $d=1,2,3$. Infinitely many positive short inputs have isolated-proof families on which a decoder can see the whole random hash even after preprocessing. On almost every isolating tape at a suitable level, a fixed correct solver takes at least $n^{1/d}/\operatorname{polylog}n$ time on **both** pins for all but an inverse-polylogarithmic fraction of short random checksums. The two pins ask opposite questions about the same unique proof. The bound remains below the linear milestone. The proof charges a single product of advice length (plus the short-input length) and per-query work. [Long public tapes, proof sampling and decision runs](random-tape-decision-witnesses.md) · [Timely answers and erasures](timely-checksum-lines.md) · [Polynomial sampling obstruction](coset-sum-tape-obstruction.md) · [Constructing and checking the isolation hash](nested-witness-isolation.md)

An independent unconditional result concerns a single actual rejecting run. At each large scale an explicit unsatisfiable formula forces a sufficiently slow run or a large constant-depth modular circuit for the chronological controller or the timestamps sorted by work address. A separate proof removes the sorted-timestamp function for runs with enough address reuse inside short blocks. On a set of distinct prehalt indices, one bit of the controller or the sorted timestamps resists prediction better than chance by all smaller circuits of this class, up to a vanishing advantage. Multiplication and division use the word-operation annotations specified in the proof. [Prehalt hard sets](trace-bit-hard-sets.md) · [Single-index check](one-index-solver-memory.md) · [Block verification](block-controller-addresses.md)

## Checking a global assertion at a solver checkpoint

A checkpoint can assert that the entire writable array, after a locally specified change of coordinates, is a permutation of a prescribed sign. If a RAM block can break one such assertion starting from another, it can do so from a memory with at most $2q+4$ nonzero words, where $q$ counts the addresses accessed or pinned. This lets the verifier replay one sparse counterexample even when the actual memory is dense. With two simultaneous permutation assertions, deciding whether a single load can produce a specified value is NEXP-complete on succinct inputs. The reduction uses only two disjoint swaps per color. Both assertions hold on the genuine zero memory. The test ranges over all states they permit. On some succinct affirmative instances every memory triggering the load requires superpolynomial-size constant-depth modular circuits in the address width, unconditionally. [Sparse-window theorem](signed-permutation-checkpoints.md) · [Succinct reduction](rainbow-permutation-defects.md)

## Which previous memory accesses matter to a SAT decision?

A linear-time deterministic solver would have arbitrarily long inputs of each sign with $n/\operatorname{polylog}n$ genuine reads returning nonzero words that have gone untouched for $n/\operatorname{polylog}n$ steps. This conclusion also holds, on verifier-dependent inputs, for reads whose values cannot be uniquely certified with polylogarithmic-time local witnesses in the total-relation model. Unconditionally, elapsed time plus the sum of read gaps at errors of such a verifier is outside $O(n^{1.3622})$ on each sign. If all previously written words count, the exponent reaches every fixed value below the golden ratio. [Gap-weighted tradeoff and positive cutoff](weighted-read-gaps.md) · [Locally checked replies and block quotas](certified-read-gaps.md) · [103-step exponent certificate](LiveValueReplay.lean) · [Phase averaging](ReadGapPhases.lean)

These lower bounds do not force a superlinear number of instructions. An explicit guarded SAT computation costs linear time yet has linearly many reads with linear gaps that defeat every small-advice total verifier making polylogarithmically many input probes. Changing any of their values changes its terminal verdict. The construction uses the transpose of a tensor-product code and limited-independence bounds for narrow Boolean formulas; a simpler permutation scan is hard to forecast but easy to verify. [Certified-read obstruction, including short-source variants](verified-code-reads.md) · [Permutation example](long-gap-inverse-bits.md) · [Code-fiber experiments](code_fiber_audit.py)

## What a fast solver must retain on satisfiable inputs

Suppose a deterministic solver decides SAT in $O(n)$ time. On infinitely many satisfiable formulas, the sum over its steps of one plus the shortest memory description with polylogarithmic-time word access is at least $n^2/\operatorname{polylog}n$. The decoder gets the formula and time. Each step can use its own best advice, chosen after the run. For a fixed decoder supporting ordinary sparse memory lists, an inverse-polylogarithmic fraction of steps on these inputs require $n/\operatorname{polylog}n$ description bits. The hierarchy proof applies to the solver's own positive signal. [Positive snapshot and witness hierarchy](positive-witness-hierarchy.md) · [Negative snapshot theorem](cumulative-snapshot-descriptions.md) · [Finite witness lemmas](PositiveWitnessSlots.lean)

If a fixed procedure can also extract a candidate description from the *actual* memory in polylogarithmic time per bit, the unconditional golden-ratio exponent holds for the positive sum of the declared description lengths plus one per step. The extractor only has to supply a truthful offer on satisfiable runs. It may offer up to $n^\beta$ strings per step for any fixed $\beta\le1/\varphi$. A terminal failure can be certified by one wrong address per offer. For affine decoders the actual coefficients can be entirely nonuniform: a program signaling SAT in $O(n^{6/5})$ time cannot have every positive snapshot covered by $n^{3/5}$ coefficient bits. The same exclusion holds for nonlinear decoders that read at most two adaptive advice bits per requested output bit. [Solver-side theorem and proof](advertised-snapshot-offers.md)

There is an unconditional cumulative lower bound even for a program that only proposes assignments. For every fixed $c<(1+\sqrt5)/2$, the sum of one plus the number of occupied work words through the first satisfying proposal is outside $O(n^c)$ in the worst case on positive inputs. The program can emit point edits and try again after every instruction. A gap reduction with charged preprocessing lets the verifier watch $O(\log n)$ clauses through the entire stream. A linear run can incur quadratic cumulative cost. [Edit-stream proof](gap-edit-watchdogs.md) · [Full-assignment streams](positive-output-watchdogs.md) · [Finite list and replay proofs](GapEditMonitors.lean) · [Experiment](gap_edit_experiment.py)

## Time and the graph of actual memory transfers

On an unsatisfiable input, let $T$ be the time to rejection and $h$ the largest clique-minor order in the graph joining consecutive instructions and each writable-memory read to its last write. For every fixed $c<(1+\sqrt{17})/4\approx1.2807764$, the worst-case product $(1+T)(1+h)$ is outside $O(n^c)$. The proof also permits a read to cite an earlier write if every intervening write stored the same value. Under near-linear SAT some rejecting graphs retain a clique minor of order $\sqrt n/\operatorname{polylog} n$ even after transfers supplied by a short, correct predictor are removed. [Separator and replay proof](slab-product-tradeoff.md) · [Finite replay lemmas](SlabProduct.lean) · [Exhaustive two-cell experiment](separator_replay_experiment.py) · [Earlier pathwidth proof](pebbling-live-producers.md)

A fixed linear-time RAM returning a constant can generate such a graph unconditionally on explicit permutation inputs. For each fixed polylog-probe evaluator, even after deleting its correct predictions with arbitrary advice within the budget, a clique minor of order $\Omega(\sqrt{n/\log n})$ survives on some inputs. This holds when the evaluator also receives the true writer time. A conditional version uses an all-zero input at every eligible length. Monitors that must preserve an actual accepting verdict give a separate way to measure spurious accepting transcripts. [Permutation and unary constructions](robust-transfer-minors.md) · [Finite clique-branch and prediction lemmas](TransferMinorBranches.lean) · [Projected traces and accepting verdicts](projected-trace-lists.md)

The weighted extension forces $(1+T)f(h)$ outside $O(n)$ whenever $f(h)\ge1$ and $f(h)/\log(2+h)\to\infty$. A one-bit guard forces input reads and a large minor on the same rejecting formula. Native linear-time RAMs can attain the intermediate separator scales in the proof. [Weighted tradeoff and guard](weighted-time-minor.md) · [Separator examples](sharp-native-separators.md)

Treewidth gives a stronger product bound. The worst-case product of elapsed time and one plus the treewidth of the actual dependency graph is outside $O(n^c)$ for every $c$ below the golden ratio. The treewidth can itself be linear in elapsed time. On the conditional common two-sign family, every fixed near-linear solver needs treewidth at least $n/\operatorname{polylog}n$ on both members. [Treewidth tradeoff, graph definition and proof](native-treewidth-trade.md)

## Truth tables generated by a fast SAT solver

If SAT takes $O(n^k)$ time for $k=1,2,3$, a deterministic RAM can write a packed $M$-bit truth table from an all-zero input in $O(M/\log M)$ word steps at every sufficiently large arity. Its bit function requires $M^{1/k^2}/\operatorname{polylog}M$ Boolean gates. The table records one actual run with a previous-touch index per writable access. Coding the table preserves packed-output speed and limits predictors of size $M^{1/k^2-\eta}$ to agreement $1/2+M^{-\delta}$, for a fixed $\delta>0$ depending on $k,\eta$. [Exact construction and the ordered-scan counterexample](output-linear-hard-tables.md) · [Approximate lookup](biased-hard-table-lookup.md) · [Matrix consequence](coded-hard-tables.md) · [Predecessor checks in Lean](TouchPredecessors.lean) · [Exact logarithmic gate counts](tight-hard-table-lookup.md) · [Rare approximate outputs from small-space programs](rare-approximate-output.md)

## Cumulative writable memory on unsatisfiable formulas

For every deterministic SAT solver on this RAM and every fixed $c<(1+\sqrt5)/2$, the worst-case cumulative cost on unsatisfiable formulas is not $O(n^c)$. At each instruction the sum charges one plus the number of currently nonzero writable words. There is no bound on elapsed time, peak workspace, or behavior on satisfiable inputs beyond soundness. If a separate near-linear recognizer for UNSAT exists, the cumulative cost lower bound for every deterministic recognizer approaches quadratic up to explicit logarithmic factors. The same golden-ratio bound holds if each step charges one unit plus the fewest bits describing its memory with polylogarithmic access time, given the input. The cumulative theorem leaves all three elapsed-time goals open. [Theorem, relation to the known time–peak-space bound, and proof](cumulative-sat-memory.md) · [Queryable descriptions and polynomial access times](cumulative-snapshot-descriptions.md) · [Finite argument in Lean](CumulativeSnapshotCuts.lean)

## Can a solver certify rejection without describing its whole history?

An inductive invariant can describe many possible memories at once. On solver-dependent unsatisfiable inputs, a hypothetical linear-time solver needs $\Omega(n/\log^5 n)$ verification cost in the adaptive row-checking format defined in the journal. For a product of per-word predicates with nonempty allowed-value sets this is a lower bound on ordinary Boolean circuit size. The respective bounds for quadratic and cubic solvers are $\Omega(\sqrt n/\log^{5/2}n)$ and $\Omega(n^{1/3}/\log^2 n)$. A concrete identity transition shows why the choice of proof matters. Locating a failed old equation requires linearly many memory probes, while a parity identity certifies preservation with constant-size local checks on the public equations. [Solver theorem](adaptive-invariant-selectors.md) · [Separation on the same invariant](row-selection-gap.md) · [Dense affine implications](affine-row-cancellation.md)

On an explicit parity-chain family of 3-CNFs, a sound rejection certificate of $s$ shared bits checked by at most $q$ packed input probes per challenge satisfies $(s+1)q=\Omega(n/\log n)$ if the format covers all rejections. Block parities attain the tradeoff. This places a limit on extracting small, locally checkable rejection proofs even from easy instances. [Proof, prior parity bounds and Lean verification](parity-chain-verdict-checks.md)

A hypothetical linear-time solver also has an interval of $\Omega(\sqrt n/\log^6 n)$ steps before it halts on which every snapshot satisfies $sq=\Omega(n/\log^9 n)$ for every per-time description of $s$ bits answering all word queries in $q\le\sqrt n$ steps. Programs and preprocessing can differ at every time. The proof allows a bounded common data bank in addition. [Persistent query bound](persistent-snapshot-query-cost.md) · [Checkpoint circuits and input costs](bulk-snapshot-selection.md)

There is a longer interval of $\Omega(n/\log^8 n)$ consecutive times where even the **sum** of description length and query time satisfies $s+q=\Omega(n/\log^{12}n)$. The verifier can check a whole list of adaptively guessed memory reads by challenging one entry. Without assuming linear SAT, the sum over a rejecting run of the independently minimized $1+s+q$ also has a worst-case lower bound excluding every exponent below $1.3760858894\ldots$, the root specified in the proof. [Additive interval bound](first-moment-snapshot-audits.md) · [Unconditional cumulative bound](first-moment-heavy-bootstrap.md) · [Transcript induction and exact exponent checks](FirstMomentSnapshotTrade.lean)

The prediction problem can be restricted to values the solver will actually read before overwriting them. For any fixed $0<\kappa<\gamma<1$, a near-linear-time solver has an interval of $w=\lceil n^\gamma\rceil$ consecutive start times at each of which predicting just those incoming words in the next $2w$ instructions costs $s+q>n^\kappa$. The decoder may see the current registers and the actual preceding events of that segment. [Live-read proof](live-segment-snapshot-queries.md) · [Finite adaptive replay lemma](LiveSegmentReads.lean)

The hard reads include disjoint collections of actual writer–reader pairs even after revealing past selected intervals. An explicit permutation scatter illustrates the failure of a universal predictor on arbitrary inputs; shallow programs generating writes from short sources do admit faster lookup under the SAT hypothesis. [Repeated exposures and accuracy](recurrent-live-prediction.md) · [Permutation experiment](scatter-inverse-live-reads.md) · [Shortcut for priority writes](succinct-priority-writes.md)

## A limit of the tape-graph approach

Two writable planar tapes can produce a $T$-step computation graph in which deleting a sufficiently small fixed fraction of the steps leaves $\Omega(T^2)$ reachable ordered pairs. The construction also gives an exact realization with one spatial block per head per epoch. It rules out the proposed sublinear-segregator theorem for all these two-dimensional trajectories. A stronger construction retains mutually connected sets of designated inputs and outputs after faults. Such a graph can compute a decision as simple as OR. [Two-plane construction](two-plane-directed-grates.md) · [Robust terminals and Boolean influence](two-tape-robust-terminals.md) · [Path lifting in Lean](TwoTapeGratePaths.lean)

## What quadratic and cubic solvers would have to compute

For each correct $O(n^2)$ or $O(n^3)$ SAT solver on the specified load/store RAM, consider the function that takes a binary time and returns its registers and program counter on one actual input. On a family of unsatisfiable formulas, the Boolean circuit sizes of these functions are respectively $\Omega(n^{1/4}/\log^{13/4}n)$ and $\Omega(n^{1/9}/\log^{7/3}n)$. There is no space cap. A shortcut can recognize a fixed diagonal family once another solver has been diagonalized against; this change of solver explains why the uniformity of the formulas has not produced the unrestricted time lower bound. [Register-history proof](chronological-solver-registers.md) · [Memory check, shared hard families and recognition shortcut](succinct-memory-defects.md)

There is also a direct bound on a summary that answers queries for every address and time up to the first rejecting halt. For a fixed decoder using constant time, the summary needs $\Omega(\sqrt n/\log^{3/2} n)$ bits for a quadratic-time SAT solver and $\Omega(n^{1/3}/\log n)$ bits for a cubic-time solver, on solver- and decoder-dependent unsatisfiable inputs. [Proof and the tradeoff for adaptive probes](polynomial-solver-state-queries.md)

## What a linear-time solver would have to store

Fix any correct linear-time solver and any fixed constant-time decoder that can read the original formula. On a solver- and decoder-dependent family of unsatisfiable formulas, a shared string describing the solver's writable memory at $\lceil L^7\rceil-1$ evenly spaced internal checkpoints needs $\Omega(n/L^4)$ bits, where $L=\max(2,\lceil\log_2(n+2)\rceil)$. A decoder for independent snapshots needs $\Omega(n/L^{11})$ bits for at least one such snapshot. These statements impose no workspace cap. The proof checks a single addressed word at a time, then diagonalizes against a fast certificate of rejection. A second verifier charges only word values actually read before a local write. With $\lceil L^{10}\rceil$ intervals, these values alone need $\Omega(n/L^7)$ shared bits. The existence of a linear-time solver remains open. [Main proof](solver-snapshot-descriptions.md) · [Cross-block writes](solver-cross-block-writes.md) · [Lean verification](SolverSnapshotReplay.lean)

On the specified packed binary encoding, linear time and $O(n/\log^{6.15484525} n)$ auxiliary bits cannot hold simultaneously. An exact finite calculation also shows that the mixed checkpoint rule used here cannot reach $b\le6.15475$, where the proposed space cap is $O(n/\log^b n)$. For time $O(n\log^a n)$, $a\ge0$, the sufficient exclusion is $b\ge1.71828175a+6.15484525$. Both numerical statements are specific to the charged transfers and rule. [Mixed checkpoint proof](mixed-checkpoint-profiles.md) · [Finite lower envelope in Lean](MixedCheckpointBarrier.lean) · [Earlier space bands](log-factor-trades.md) · [Packed model](packed-band-transfer.md)

The journal also derives a $2^{O_{M,d}(t/\sqrt{\log t})}$ deterministic simulation of nondeterministic time $t$ for a fixed number of fixed-dimensional tapes using the circuit-CSP algorithm of Strassle and Subercaseaux. A two-dimensional sweep tests which part of the PPST segregator proof survives, and a circuit transformation handles degree-two representatives of the Boolean permanent whose powers follow a fixed pattern with bounded exceptions. [Tape simulation](multidimensional-tape-simulation.md) · [PPST test](two-dimensional-segregators.md) · [Permanent extraction](degree-two-permanent.md) · [Research journal and scope](research-steering.md)

## Earlier research and conditional tests

I obtained an unconditional approximation for the times when short programs first produce new words. At each length, most of a family of clock resolutions give a histogram with vanishing total absolute error and a description using fewer than a linear number of bits in the number of bins. If SAT takes linear time, **no fixed algorithm can choose such accurate resolutions by the first cutoff at infinitely many lengths**, even when the forecaster gets the exact counts for all preceding cutoffs. The missing step is finding a timely resolution for the actual programs. An explicit family of abstract measures shows why dividing the programs among resolutions loses too much accuracy. [Forecasting theorem](causal-first-outputs.md) · [Unconditional approximation](regular-clock-scale.md) · [Counterexample for scale selection](cascade-allocation.md) · [Online choice in Lean](CausalForecastChoice.lean)

Three separate tests use the actual decisions of candidate solvers. At most $k+1$ local checks can characterize the correct XOR combinations of $k$ solvers on a finite restriction-closed family. For unit propagation, deterministically finding a local error from a dense layer of favorable restrictions would give deterministic search for dense Boolean circuits. For a unique witness, a decision trace consisting of one layer of products of linear forms leads to recovery of the diagonal of a symmetric matrix over the binary field. [XOR combinations](linear-verdict-pivots.md) · [Unit propagation and dense search](restrictions-of-unit-propagation.md) · [Recovering a diagonal](quadratic-trace-diagonals.md)

I narrowed the matrix question in the linear SAT test. For a sufficiently large binary square of side $J$, if at most $\lfloor0.2883J\rfloor$ rows are nonzero, one can change at most $J^2/16$ entries to reduce its rank to $\lfloor J/16\rfloor$. For $\lfloor0.2816J\rfloor$ nonzero rows I obtained a deterministic algorithm producing the factors in matrix-multiplication time up to logarithmic factors. Thus it would suffice to prove the first row-count bound infinitely often for the fixed program's actual output. Under linear SAT its matrix instead has between about $0.2883J$ and $0.29805J$ nonzero rows asymptotically. Which behavior occurs remains open. [Rectangular approximation and explicit factors](anchored-matrix-covers.md) · [Improvement using triples](triple-anchor-cover.md) · [The matrix used in the SAT test](lex-factor-responses.md) · [Reproducible checks](anchored_cover_experiment.py)

The linear target has an exact test using the last output bit of one fixed program. Arrange those bits in a square of side $L=2^m$. If a linear SAT solver exists, at every sufficiently large phase its table is more than $L^2/16$ bits away from every binary matrix of rank at most $L/16$. If every linear-time candidate fails, the table is identically zero throughout intervals $j\le m<2^j$ for arbitrarily large $j$. The program checks which candidate agrees with brute-force SAT on growing sets of short formulas. Neither behavior has been proved unconditionally. On the candidate rigid table, clearing any one-entry already brings it within the allowed distance. This identifies exactly where an approximation argument can miss by one bit. [Fixed program and equivalence](fixed-program-parity.md) · [Window approximation and counterexample](substring-template-rigidity.md) · [Phase checks in Lean](TrialResetIntervals.lean)

I found a way to use **parities of short programs** to test all three SAT time targets. Arrange the words of even length $q$ in a square with $L=2^{q/2}$ rows. Select short programs by a random polynomial on their names, and enter the parity of the selected names that produce each word. Under linear-time SAT, at most a $2^{-\Omega(q^2)}$ fraction of these matrices can be changed in a small constant fraction of their entries to give binary rank at most $\kappa L$. The test can ignore every word already produced by time $2^q$. Thus a low-rank construction for a fraction $2^{-o(q^2)}$ of the selections would suffice. I obtained low rank for every selection on a particular nonlinear program family; the full interpreter remains unresolved. The quadratic and cubic versions have smaller target ranks. Even a single power of the name index must give hard parity matrices for almost every scalar multiplier at some exponent in every sufficiently long run of consecutive powers. [Parity criterion and inverse calculation](parity-of-program-fibers.md) · [Finite-field experiments](fiber_selector_syndrome_experiment.py) · [Tuple count](FiberMomentTuples.lean) · [Sparse fiber moments](SparseFiberMoments.lean)

I also tested covers of the actual outputs. A dense set avoiding almost all easy words must use a different suffix pattern on a positive fraction of prefixes, even if each prefix gets a projective semilinear change of coordinates and each pattern allows a fixed Hamming error. Sparse XOR lists can meet that diversity requirement and still contain many easy words. Other arguments restrict the shorter side of an XOR cover and the algebraic degree of rational images with arbitrary overlaps. [Suffix patterns and relabeling](suffix-patterns-and-relabeling.md) · [Projective marker experiment](projective_row_markers_experiment.py) · [XOR cover widths](escaping-xor-covers.md) · [Rational images](rational-image-covers.md) · [Finite sieve in Lean](RationalRangeSieve.lean)

A separate approach gives each cell of a computation tableau several possible states. Local permutations can certify a globally consistent computation even with many defects, provided the defects are rare and involve sufficiently few shared registers. Finding such certificates for the required accepting computations remains open. [Permutation certificates and the local lemma](tableau-permutations.md)

I extended the circuit-approximation test to the quadratic and cubic goals for the same fixed language of time-bounded incompressible strings. A quadratic SAT algorithm would force every circuit with at most $\kappa 2^{q/9}/q$ gates to err on at least $\epsilon 2^q$ words of length $q$, for fixed $\kappa,\epsilon>0$. For cubic SAT the denominator in the exponent is 19. A sufficiently accurate smaller circuit at infinitely many lengths would give the corresponding SAT lower bound. I have no such circuit. [Proof and witness-recovery costs](suffix-block-sat-exponents.md)

I also tested whether pairs of sparse lists can describe many hard words by their bitwise XORs. For the cubic target, partition the $N=2^q$ words by all but their last $\lfloor q/10\rfloor$ bits. Two lists per prefix would suffice if they had $o(N)$ entries in total and their distinct sums covered a fixed fraction of the cube with $o(N)$ easy words. Unconditionally, such dense sets contain at least $\Omega(N^{29/30})$ easy words. A construction between these bounds remains open. A separate attempt uses lists to cover the actual program outputs and leaves the hard words in the complement. [XOR sums, entropy loss and the cubic criterion](xor-sumset-advice.md) · [Covering program images](covering-program-images.md)

Ruling out **linear time** remains the first success condition. I derived a way to do it by proving a Boolean circuit **upper bound** for one auxiliary language. On $q$ bits, the language asks whether every program saving at least two bits misses a specified exponential deadline. If SAT takes linear time, every circuit with at most $c\,2^q/q$ gates gets at least $\epsilon 2^q$ answers wrong at all sufficiently large lengths, for some fixed $c,\epsilon>0$. An accurate small circuit on infinitely many lengths would contradict that implication. I have no such circuit. A hitting-set argument by Buhrman, Fortnow, Koucký and Loff precedes this approach for programs without a deadline. [Deadline, proof and attempted upper bound](full-cube-advice.md)

A randomized search could also suffice. It can return a different large set on every successful run and include some easy words. I bounded the probability of getting so few easy words under the linear-SAT hypothesis. Removing all outputs detected at an earlier deadline and sampling the remaining words independently already fails at the required rate. [Sampled sets and the probability bound](hitting-sampled-batches.md) · [Unconditional bound for short descriptions](sampled-batch-descriptions.md)

The usual random affine hash isolates any specified hard $m$-bit table with probability at most $2^{-m}$ per trial when at most $L$ tables have short programs and $L(L+1)\le 2^m-1$. This holds even with an oracle that returns the sole hard table when it exists. For general pairwise-independent buckets I derived the exact maximum probability at each marginal and number of hard tables. A fast randomized hardness test on a short initial list would give a different route. On some candidate, the random tapes certifying its correct answer must evade even a covering test that can fix a quarter of the log deadline in arbitrary positions. No such tester has been found. [Isolation bounds, extremizers and remaining test](dense-hard-table-sampling.md)

A deterministic program can match the sampling probability, up to a constant in program length, when success follows from fixing sufficiently few random bits in each tape prefix. The decoder enumerates a family of almost-independent tapes whose prefixes use few seed bits at every deadline. Adding one parity check to any sampler preserves half the probability of every answer while forcing all narrow certificates to come from early runs. [Coding theorem, second-moment extension and parity obstruction](cube-tape-coding.md)

The linear-SAT coding test now covers whole truth tables of length polynomial in the logarithm of the sampling deadline. A contradiction can come from a frequently sampled table for which every sufficiently short deterministic program misses the deadline even after any fixed polylogarithmic slowdown. I used polynomial evaluations to reduce this test to the earlier one for short integers. A private-coin program can already reproduce an explicitly printed output of any length at the required bit cost when the output is frequent. I have not found a table that separates the two kinds of programs. [Deterministic transfer and finite checks](recovering-longer-outputs.md) · [Private-coin coding for long words](private-coin-long-words.md)

Under the same coding hypothesis, a total bounded-error language running in $T(n)=2^{2^n}$ has a deterministic simulator correct on every input for a set of lengths of positive upper density, in $T(n)2^{O(n+1)}$ time. A language defeating every such simulator would rule out linear SAT. The argument shares the cost of reproducing an input across several deadlines. [Conditional coding with a shared input](conditional-clock-coding.md)

I constructed a single ordinary sampler whose completion times defeat every rule in a specified class that sees only the output word and its timestamp. Its words themselves still have short deterministic programs. A separate construction shows that every frequently sampled short word already has a private-coin prefix program of optimal length up to a constant. The remaining question on this route is whether a deterministic program can match its length and reproduce its output at a nearby deadline. [Timestamp construction and the failed inference](timestamp-allocation.md) · [Private-coin coding and the required deterministic replacement](private-coin-prefix-coding.md)

A possible way to rule out linear SAT is to find a word that a fixed randomized sampler prints frequently by a deadline, even though every short deterministic program is too slow. For inverse-polylogarithmic probabilities and words no longer than the logarithm of the deadline, this test is equivalent to checking a single interpreter on binary integers, giving the integer itself as the starting time allowance. The equivalence is unconditional. A randomized search can detect even one qualifying violation in a block $[N,2N)$ in $N\,\mathrm{polylog}(N)$ time for each fixed inverse-polylogarithmic probability threshold and program budget of order $\log\log N$ bits. Finding violations that persist for every fixed clock exponent is still open. [Equivalence and probability transfer](sampling-at-a-numeric-length.md) · [Search guarantees and finite test](dilated-program-mass.md)

There is now a test for linear SAT using only programs that print zeros. Give a program a cost of its length plus the logarithm of its running time. For each word of n zeros, compare the best cost with the total weight of all programs printing it, where each program’s ordinary probability is divided by its running time. Linear SAT would bound the difference between the best cost and the negative logarithm of that weight by O(log log n), for every n on each fixed efficient interpreter. An ordinary interpreter can attain this order, even with any prescribed fixed coefficient as the interpreter varies. The search needs an unbounded ratio on one fixed interpreter. I also proved the upper bound unconditionally outside a quantitatively small set of lengths and constructed very deep lengths where the test still passes. [Unary test and the unsuccessful diagonal](unary-speed-gap.md) · [Ordinary examples attaining the scale](native-coding-delays.md) · [All-output bound](discounted-program-mass.md)

A separate test asks whether two programs can match the best description of an ordered pair when both programs pay only once for the longer running time. Linear SAT would allow the split with logarithmic overhead in the pair’s optimal cost. I constructed pairs that incur an asymptotically sharp extra cost when the shorter running time also receives a positive charge. They leave the shared-time test open. [Splitting the description of a pair](shared-levin-clock.md)

If SAT had a linear-time algorithm, the following coding bound would hold. Suppose a fixed randomized machine prints a particular word by time t with probability p. For words of polylogarithmic length in t, some deterministic program of at most ⌈log₂(1/p)⌉ + O(1) bits would print that word in time t · polylog(t), without being told the deadline. For much longer words, one program of the same length can answer each individual bit query within that clock when log₂(1/p) is polylogarithmic in t. An explicit sampler that violates either guarantee would rule out linear SAT. The constructed example that violates the first bound relies on an external oracle. [Full-word coding argument](near-clock-coding.md) · [Single program for bit queries](implicit-output-coding.md)

A second consequence involves the combined probability of all programs that print a given word by a deadline. Linear SAT would force this probability to multiply by a power of m across Ω(m/log m) disjoint intervals for some m-bit words. At each sufficiently large m, words with this property would carry a constant fraction of the eventual probability of printing any m-bit word. Merely increasing the probability by a positive amount in many intervals happens unconditionally even for the all-zero word. [Probability growth across deadlines](mass-clock-cells.md) · [Interpreter comparison](occupied-clock-cells.md)

One candidate separation now concerns a single word’s successive shortest programs. At each large length m, count how often the best description of one word improves between times 2³ᵐ and 2⁴ᵐ, among words having a final description of at most 3⌈log₂(m+2)⌉ bits. On every efficient universal machine I can force at least a constant times √m improvements on some such word, unconditionally. Linear SAT would force at least a constant times m/log m at every large length. Finding one machine with a smaller count along an unbounded sequence of lengths would suffice if its ratio to m/log m tends to zero. A machine that publishes only at scheduled times attains an upper bound of order m/log m, with an arbitrarily small fixed coefficient as the machine varies. [Conditional count](successive-description-times.md) · [Unconditional square-root count](adaptive-description-times.md)

A fixed additive gap now suffices for one test of the linear-time target. For each output word of length m, record how many bits its shortest program saves over m at a late deadline. Under the linear-SAT hypothesis the two-clock sum must be algorithmically random for at least one saving in every H consecutive savings, for a constant H depending on the machine. A single efficient universal machine with arbitrarily long gaps would therefore rule out O(n) time for SAT. I constructed machines with any prescribed fixed gap size, and even prescribed bounded-gap patterns indexed by enumerable processes. The construction still needs a finite bound on each machine’s gaps. [Conditional constant-gap bound](exact-saving-blocks.md) · [Which patterns a machine can realize](programmable-clock-spectrum.md)

A related linear-SAT test can be stated using only shortest program lengths at two clocks. For each word, measure how much its best description improves when the deadline grows by a polynomial factor. Under linear SAT the sum of these improvements over words whose best descriptions are within ⌈log₂ log₂ m⌉ bits of their length m must be algorithmically random, with the precise weighting below. The argument also forces random sums at particular fixed description-length savings, with gaps of at most logarithmic size between them. Showing sufficiently large gaps would suffice. Removing the length restriction makes the sum random unconditionally, by an explicit family of short programs. [Clocked complexity increments](clocked-complexity-increments.md)

On a constructed optimal prefix machine, a positive fraction by weight of selected words have a shortest program of exactly m−1 bits whose earliest completion takes between 2^(3m) and 2^(5m) steps. An m-bit program prints each of the same words in quasilinear time. This is unconditional. Under linear SAT the slow endpoint can be confined to a polynomial factor of a prescribed deadline. A second test on a single fixed machine lets the required description-length saving grow with the phase. [One additional description bit](one-bit-production.md) · [Growing description-length savings](varying-description-savings.md)

The weighted averages of the remaining production-time distributions converge to a particular measure. The second Turing jump can compute it. Computing it with the first jump would rule out linear SAT. A bounded computable observation on the same phase weights attains the second-jump bound, so improving it requires a property of the actual first production times. [Canonical tail limit and counterexample](tail-rate-mixtures.md)

One sufficient condition for ruling out linear SAT concerns the limits of an explicit sequence of distributions. Each distribution records when the first short programs for specified words finish on a fixed universal machine. It would suffice to find even one limiting distribution on the specified phases that can be approximated by a computable sequence, without knowing how fast those approximations converge. Under linear SAT, every such limit would instead have a positive atom at every limit-computable rate in [3,4]. A general compactness argument does not yield the needed limit. [Proof and compactness counterexample](phase-limit-measures.md) · [Distribution across a growing number of rates](rate-bin-credits.md)

A partial proof can now receive credit for each target word it certifies. On a fixed universal machine, even the first short programs for a positive fraction of the selected words take between 2^(3m) and 2^(9m) steps at infinitely many stages, where m is output length. The connection to linear SAT requires a fast verifier that captures enough actual outputs on the specified stages. One program family fills omissions of a proposed verifier, and the next verifier can recognize its outputs. Under linear SAT the same construction would force many first outputs into a time interval ending at a prescribed clock, even when its endpoints differ by only a polynomial factor in m. [Word-by-word proof costs and first production times](word-completion-cost.md) · [Allocating halting probability to actual outputs](fifo-producer-credits.md) · [Prescribed production deadlines](near-clock-credits.md)

An earlier test uses candidate lists that may be wrong. Even infinitely many successful lists would suffice to exclude linear SAT if their total normalized size were computable and each list could be obtained through a sufficiently small SAT test. An adaptive procedure gave a counterexample to replacing computability by a known upper bound: its cost is at most 3/2, but the fractional part encodes halting information. This leads to a proof search for positive claims about actual program outputs on failed windows. Short programs certify all the claims on an infinite explicit subfamily; enough other failures still lack certificates. [Adaptive lists, positive witnesses and the missing bound](adaptive-window-lists.md) · [Shortening a group proof](shorter-window-proofs.md)

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
| [Approximating arbitrary rectangular matrices](anchored-matrix-covers.md) | A block algorithm fits both row and column data using the same rank budget. An existence proof uses sparse perturbations of the generators to protect an initial set of columns. |
| [Sharing a rank dimension across three columns](triple-anchor-cover.md) | Sparse perturbations combined with a four-symbol error calculation extend the unconditional approximation guarantee through $0.2883J$ rows. |
| [Responses to earlier lexicographic competitors](lex-factor-responses.md) | A fast procedure returning factors for all earlier competitors would remove the quadratic sequential search factor. Direct-sum column spaces fall short of covering that set. |
| [Column subspace dimensions and actual late outputs](column-subspace-tests.md) | The ambient label space can be arbitrarily large. A small intrinsic dimension in each column would suffice if its incidence test accepted many hard words and few late outputs. |
| [A sign change on one routed path](one-break-paths.md) | An internal sign break removes an endpoint constraint. Even with an identical pairing of the ends, one marked site can hide the parity of a whole switch sequence. |
| [Local tests for a disjunction of candidate solvers](portfolio-local-defects.md) | Failure of all possible subcollections has a certificate using at most one elimination per candidate and one final local test. Proving that every fast menu has such a certificate is open. |
| [Delayed verdicts on larger formulas](delayed-diagonal-relays.md) | Ruling out one pattern of joint outputs on sufficiently many program tuples could refute a proposed solver. The required predictions have not been obtained. |
| [One program for all three SAT clocks](fixed-program-parity.md) | In each mode a fixed prefix selects a program whose last bit gives either eventually rigid tables under the SAT hypothesis or arbitrarily long intervals of zero tables if that hypothesis fails. |
| [Checking a solver with its own verdicts](checking-a-solver-with-its-own-verdicts.md) | A positive answer to an explicit query certifies that the program is wrong. For every finite correctness horizon one wrong linear-time program passes all its own queries forever. |
| [Rows drawn from a few common strings](substring-template-rigidity.md) | Extends a Toeplitz nonrigidity bound to repeated windows and proves restrictions on the lexicographically first rigid matrix. Some logarithmic-rank matrices defeat the window test in both orientations. |
| [Paired names and adaptive raw-bit probes](paired-name-probes.md) | On a different universal encoding a query tree reading $t$ bits separates at most $t/B$ of the paired names. The constructor attains this fraction up to saturation. |
| [Boolean polynomials on program names](boolean-name-projections.md) | Fixed-degree parities suffice for a quantitative conditional rigidity bound. Some nonlinear program families admit low-rank representations, and a bounded-fiber example attains the exponent in the dimension estimate. |
| [Counts and spectral tests on actual output words](spectra-of-program-counts.md) | A fixed odd prime detects enough nonempty program fibers. A second test pairs positive-density subsets of words missed by the deadline and words first reached late with small spectral discrepancy under the SAT hypothesis. |
| [Local queries to a path formula's unique witness](locally-decoding-path-witnesses.md) | Gives the exact success probability for a batch of linear observations with an input-specific description and adaptive linear probes. A width-one 2-CNF exhibits the cost of recovering a particular checkpoint. |
| [Suffix tables under quadratic or cubic SAT](suffix-block-sat-exponents.md) | Gives conditional almost-everywhere circuit approximation bounds for the same language and the same program deadline as the linear test. |
| [Two sparse lists of XOR summands](xor-sumset-advice.md) | Gives lower bounds on the number of distinct easy sums, an entropy obstruction for arbitrary independent marginal laws, and a cubic-SAT test with one pair of lists per prefix. |
| [Covering the output image with short lists](covering-program-images.md) | A cover of controlled capacity would suffice. An injective field multiplication routine defeats separation into row and column functions while admitting a simple image cover. |
| [Local advice about late programs](late-block-prediction.md) | A predictor with separate tips for early-omission blocks and small total advice necessarily makes a positive fraction of errors, even with local feedback. |
| [Local patches for computation histories](mixed-tableau-patches.md) | Individual SAT calls bound the cost of circuit-described patches. A sufficiently economical cover of every needed accepting history is still missing. |
| [Circuit approximation of time-bounded incompressibility](full-cube-advice.md) | Canonical finite-set selection under linear SAT would make every circuit below a constant times the Shannon size scale err on a constant fraction of inputs to a specified language. |
| [Rectangle covers across all balanced partitions](all-cuts-plain-outputs.md) | Constructs one set of genuine short-program outputs hitting dense disjoint unions of rectangles, even when each rectangle uses a different partition. |
| [Sampled sets with few easy words](hitting-sampled-batches.md) | Derives a sufficient rare-event criterion for linear SAT, including the case of advice describing one successful set. |
| [Short descriptions of sampled sets](sampled-batch-descriptions.md) | Gives an unconditional bound on the combined weight of all timely descriptions of poor hitting sets, accounting for repeated descriptions of the same result. |
| [Fourier tests for sets of late outputs](fourier-batch-tests.md) | Constructs late program outputs that hit all dense address masks with sufficiently small Fourier norm, even after removing every early easy word. |
| [Choosing a pivot in a random subspace](random-linear-masks.md) | The first one in a row can name a frequent hard word if a hidden subspace has enough conditional entropy and vanishes on all easy coordinates. |
| [Learning easy tables with adaptive queries](adaptive-singleton-replay.md) | Gives bounds for a hidden affine relabeling, including a three-discovery example where an XOR recovers a designated hard word. |
| [Completing large affine flats](adaptive-hash-tables.md) | A missing vertex of a sufficiently large flat has a timely short description when every other vertex has one, by polynomial closure and enumeration. |
| [Several witness-recovery traces](multitrace-witnesses.md) | Coordinate-wise agreement across traces suffices for extraction under the stated seed bounds. Boolean correctness alone leaves the formal trace derivatives unconstrained. |
| [Induction from sparse RAM states](sparse-state-induction.md) | A failed polynomial invariant has a sparse counterexample after the touched cells and registers are fixed. A short invariant for the missing output remains to be found. |
| [Isolating a hard truth table](dense-hard-table-sampling.md) | Bounds the probability that any specified hard word is isolated with pairwise or three-wise independent tests. |
| [Few fixed positions on a random tape](cube-tape-coding.md) | Gives unconditional deterministic codes from fractional or second-moment coverage, and relates narrow certificates after a parity gate to the original early output mass. |
| [Extracting all bits of a unique witness](unique-witness-batches.md) | A linear SAT hypothesis permits batch recovery when a small correction to the linear forms on one RAM trace exists. An explicit parity RAM needs one correction per bit. |
| [Algebraic covers in different variable orders](ordered-parity-refutations.md) | Tests succinct ordered refutations near the native missing-word clock and exhibits a cyclic-shift formula forcing large width under the stated order conditions. |
| [Reconstructing sampled truth tables](recovering-longer-outputs.md) | Reduces deterministic coding of polylogarithmic-length outputs to the short-word test through polynomial list recovery. |
| [Private-coin descriptions of long words](private-coin-long-words.md) | Empirical cumulative probabilities yield short private-coin programs even when the explicit output nearly fills the sampling clock. |
| [Sharing the cost of a sampler’s input](conditional-clock-coding.md) | Derives a deterministic length-versus-time tradeoff under the inputless coding hypothesis and an advice-free simulation on a positive upper density of lengths. |
| [Choosing from cumulative truth tables](cumulative-table-lists.md) | One choice succeeds in every sufficiently wide block at a quantified cost. A recursive oracle separates that guarantee from eventual correctness even with indefinitely extensible lists. |
| [Predicting an encoded bit on a common query stream](length-free-prediction.md) | Soft-decision list decoding turns a small prediction advantage for a sampled table into a short exact program, with recovery cost polynomial in table length. |
| [Bounded deviations from predicted proof choices](default-escape-games.md) | Relates exponential-size default strategies on uniform games to unrestricted circuit hardness for a language in exponential time. |
| [Shallow refutations after partial assignments](horn-gap-rounds.md) | Bounds Horn propagation depth by the reciprocal residual violation gap. A constant-gap family needs linear branching depth to expose q-Horn contradictions on every leaf. |
| [Assigning numeric labels from completion times](timestamp-allocation.md) | Proves a sharp squared-logarithm loss for timestamp-only rules and realizes failures of bounded rules on one ordinary sampler. Its output words remain easy to print. |
| [Short private-coin prefix programs](private-coin-prefix-coding.md) | Gives a randomized encoder and decoder at nearby deadlines for high-mass outputs. Deterministic replacement at that length remains open. |
| [Races between partly observed workers](independent-clock-races.md) | Order-statistic circuits of bounded width allow constant-bit deterministic coding from independently certified worker intervals. |
| [Local proofs of a real program’s output](forcing-pebble-layouts.md) | Gives a size and width criterion for proofs about predecessors of the first missing word. A pyramid circuit shows how even an easy true output can have large width in a chosen encoding. |
| [Synchronizing publication times on a single numeric length](sampling-at-a-numeric-length.md) | Transfers a constant fraction of a short word’s sampling probability to an integer that encodes it. The high-probability deadline test is equivalent to a single-interpreter numeric test. |
| [One deadline for the full discounted probability](dilated-program-mass.md) | Proves a sharp probability inequality and gives a thresholded search for exceptional lengths. Under linear SAT one program attains a constant fraction of the total mass after increasing its time allowance. |
| [Pathwidth of a real computation](trace-pathwidth.md) | Local checks authenticate a guessed decomposition of a tape run. The width needed by the shortest timely descriptions near the first missing output remains unknown. |
| [Nondeterministic descriptions with large checkpoints](single-valued-checkpoints.md) | Under linear SAT the number of strings forcing a large checkpoint on every successful low-cost description reaches the unconditional leading-exponent counting bound. |
| [Searching the random-input computation tree](fair-tape-work.md) | Bounds the fraction of successful runs that can survive two deterministic searches. One shares common prefixes and one merges identical RAM configurations. |
| [Quadratic readouts of random bits](quadratic-sampler-fibers.md) | Exact output counts give a short program when the combined output and free selector dimensions fit the deadline. |
| [Reciprocal-time program mass](discounted-program-mass.md) | Relates the weighted mass to public-randomness Levin cost. Under linear SAT its negative logarithm approximates the deterministic best cost to logarithmic error. |
| [Unary outputs at their own numeric deadlines](unary-speed-gap.md) | Reduces the target to one interpreter’s binary descriptions with a soft deadline and bounds the fraction of exceptional lengths unconditionally. |
| [An ordinary interpreter with delayed generic programs](native-coding-delays.md) | Each fixed polylogarithmic slowdown can fail on a different efficient interpreter. The all-zero words also realize a nonconstant gap for reciprocal-time mass. |
| [One time charge for two descriptions](shared-levin-clock.md) | Under linear SAT a split program can match joint Levin cost up to logarithmic error; ordinary two-charge examples saturate a different bound. |
| [Sampling the interpreter’s current distribution](sampling-own-clock-law.md) | An efficient universal machine reproduces near its own deadlines the output laws of a class of routines that sample those same deadlines. |
| [Induction on paired RAM memories](relational-memory-induction.md) | Affine constraints on shared hidden bits allow an exact test for inductive relations on large memories. A diagonal language still lacks enough certified equalities. |
| [Coding timely sampling probability](near-clock-coding.md) | Approximate counts suffice to build a deterministic prefix decoder under linear SAT, even when a batch has too many entries to enumerate. |
| [Recovering one bit of a long output](implicit-output-coding.md) | Under linear SAT a short field value distinguishes all the heavy outputs of one batch. One short program can answer every coordinate query. Full recovery of an arbitrary long output at that clock remains open. |
| [Growth of a word’s timely program probability](mass-clock-cells.md) | Under linear SAT one set of outputs gains conditional probability by polynomial factors across many common deadline intervals. |
| [Comparing changes across native interpreters](occupied-clock-cells.md) | On a fixed time grid, for each word the number of intervals where its shortest program improves is comparable across all efficient interpreters. |
| [Fast names for the same output](listed-fast-replacements.md) | A fast and a slow program can both be globally shortest, even when predicting any fast name from the slow one needs more than a prescribed logarithmic advice budget at the early deadline. |
| [Two interpreters at individual clock rates](paired-rate-interpreters.md) | Machines with the same program outputs can differ at each nonmultiple of a fixed integer saving, at almost every rate for the specified distributions. |
| [Grammars for batches of RAM histories](batch-trace-grammar.md) | On one universal interpreter, genuine predecessors of the first missing output require large concatenation grammars for their traces. Their computations still have short semantic descriptions. |
| [Testing one coefficient after a signed monomial substitution](monomial-weight-coefficients.md) | An application of real point location gives polynomial-depth comparison trees for an exact signed coefficient, including all ties. A uniform Boolean-to-arithmetic conversion is still missing. |
| [Agreement at every rational exponential deadline](rational-clock-agreement.md) | Two machines can agree on the timely status of every name at every fixed rational rate eventually, while differing on all odd savings within the last polynomial factor of each deadline in (3,4). |
| [Prescribing which exact savings have random increments](programmable-clock-spectrum.md) | Two machines can agree on every program’s output and on all sufficiently late integer-rate outer complexities while disagreeing at every odd saving. A separate construction realizes any uniformly bounded-gap Π⁰₂ pattern. |
| [Constant-width intervals of description savings](exact-saving-blocks.md) | Linear SAT would force random increments in some column in every constant-width interval. The bound holds in each fixed polynomial-ratio clock interval. A separate residual randomness result is unconditional. |
| [Description savings relative to a moving cutoff](moving-saving-cutoffs.md) | Under linear SAT, a timely computable program-length cutoff on powers of two has a random increment sum at a fixed bounded offset. Short cutoffs allow direct enumeration unconditionally. |
| [Using newly completed programs to pay for the next time interval](adaptive-description-times.md) | On every efficient native machine and every large length, an actual word with a short final program has Ω(√m) successive improvements. The joint prefix code adapts to observed arrival mass. |
| [Individual clock rates on all native machines](exceptional-rate-capacity.md) | A closed set of rates of Hausdorff dimension one has only finitely many near-optimal arrivals in each specified window on every machine. Every rate law in the conditional SAT test gives it measure zero. |
| [Avoiding a small list of rate prefixes](rate-list-lookahead.md) | Finite lookahead can avoid a bounded number of forbidden prefixes per level. The lookahead increases the time needed to compute the chosen rate. |
| [Successive improvements on one word](successive-description-times.md) | Quantifies the gap between full enumeration and the consequence of linear SAT at the same clocks, for the same statistic on short final descriptions. |
| [Common improvements across a Hamming ball](common-distortion-balls.md) | Under linear SAT, every word of one ball improves by at least 0.32m bits on every interpreter in a fixed finite list, also between polynomial deadlines. |
| [Predicting the output prefix of an early program](early-prefix-prediction.md) | A machine with a large gap must supply genuine early names that evade all short predictors in a stated bounded-rank class. |
| [Time needed to describe a rate prefix](rate-prefix-depth.md) | A low timely mass on every prefix at one scale coexists with an actual machine where all exact savings have random increments. |
| [Rate distributions including atoms and singular measures](rate-cylinder-laws.md) | Under linear SAT the same constant-width test holds with probability one for every rate law meeting the stated approximation time, including at each atom. |
| [Continuously varying the deadline](continuum-saving-rates.md) | Under linear SAT, almost every individual rate in [3,4] has infinitely many witnesses in every interval of a fixed sufficiently large number of savings. Integrating over rates gives a computable-series test. |
| [Estimating early program outputs from the payload](sampled-prefix-mass.md) | One payload can estimate early prefix probabilities and still appear in the output. A fixed-point obstruction explains why a distribution-free selection rule cannot guarantee a lightly occupied group of tags. |
| [A series over words at two clocks](clocked-complexity-increments.md) | Linear SAT would force randomness of the clock-increment sum even for almost incompressible words. Dropping the length band gives unconditional randomness via simple diagonal words. |
| [The fastest shortest program and one more bit](one-bit-production.md) | A prefix-universal source has many words with an exponentially slow shortest description and a quasilinear description just one bit longer. Changing the padding rule gives an upper bound but costs the compiler the same saving. |
| [Increasing the required program-length saving](varying-description-savings.md) | The word masses at all savings D, scaled by 2^D, are jointly summable. Linear SAT would still force a positive normalized share near a fixed deadline at any timely selected D=g(r)≤r/3. |
| [Canonical tail mixtures](tail-rate-mixtures.md) | A specific weak average lies at most one Turing jump above what is needed for a SAT separation. A different computable observation on the same weights attains that upper bound. |
| [Description costs and local affine dimension](phase-rank-and-description.md) | Under linear SAT, even after removing highly compressible words, the high-phase limits have unbounded affine dimension in every weak neighborhood of a limit point. |
| [A staggered output clock](staggered-release.md) | An explicit modified source has atomless log-rates. Its delays or the cost of representing an eligible suffix prevent the native clock transfer. |
| [Weak limits of first-production rates](phase-limit-measures.md) | Linear SAT would force every limit along certain phases to have atoms at all limit-computable rates in [3,4]. Exhibiting one limit-computable member even of the closed convex hull would exclude linear SAT. |
| [Many rate intervals at once](rate-bin-credits.md) | One stream decoder funds every bin in an exponentially growing library on common phases. Each weak limit there dominates a positive multiple of Lebesgue measure over [3,4]. |
| [Paying for individual output words](word-completion-cost.md) | On infinitely many failed masks, a positive fraction of selected lengths have a positive fraction of genuinely new words between explicit cutoffs. A sufficiently complete fast proof of production would exclude linear SAT. |
| [Assigning halting weight to actual words](fifo-producer-credits.md) | A single compiler spends each halting program's credit on distinct words missed by the verifier. A finite number of rounds with shared demand order has a single combined capacity. |
| [First outputs near a prescribed clock](near-clock-credits.md) | Under linear SAT every fixed finite set of deadlines has simultaneous positive fractions of first outputs near those deadlines on the same infinitely many phases. |
| [Extending a verifier for whole blocks](producer-proof-extension.md) | A shared generator certifies additional bad blocks, exceeding the heavy-length threshold by a chosen factor in every sufficiently late phase. |
| [Parity tests after shared preprocessing](snapshot-parities.md) | A selector can keep just one word of state. Universal checks attain independent equations at a nearby support bound, with an explicit mismatch in the required number of state bits. |
| [Surjectivity with a hidden key](suffix-image-certificates.md) | A public top coefficient certifies all labels across hidden lower coefficients. Disjoint faces give a sharp bound on how many labels can be lost to erroneous program rows. |
| [Lists that need only sometimes succeed](adaptive-window-lists.md) | A finite total normalized list size must have random fractional part if fast lists hit good blocks infinitely often. Enough short proofs of positive producer claims on failed windows would refute linear SAT. |
| [Shortening a group proof](shorter-window-proofs.md) | Any unbounded shortening factor would suffice for certified lists. Copying real producer programs gives a convolution inequality, but nearby scales can have very different exceptional fractions. |
| [Shifting and anonymizing omissions](anonymous-omissions.md) | An aggregate report exceeding the square-root surplus would identify a small list containing the native omission. Taking the union over all genuine holes falls short. |
| [When one producer accounts for a predicted output](exclusive-owner.md) | For independent groups with few anomalous predictions on average, near-native counting isolates one group at the actual missing word under linear SAT. |
| [Relative output equations on parity fibers](parity-fibers.md) | A few certified parity comparisons across predictors would yield a contradiction via a sparse slope. The missing ingredient is a verifier that runs faster than replay. |
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

Use Lean 4.19.0 with its bundled Std library and Python 3.11 or later. The finite permanent-grid and matching experiments use SymPy. The independent singleton optimization check uses NumPy and SciPy. Run from the repository root.

```sh
lean PositiveQueryLeaves.lean
lean CrossProbeSpectrum.lean
lean SingleCutTransfers.lean
lean ThreeBankPhases.lean
lean OrdinalBlindQueries.lean
python3 half_read_reuse_audit.py
python3 spectral_cut_audit.py
python3 sparse_quadratic_cut_audit.py
python3 expander_cut_sign_audit.py
python3 single_cut_transfer_audit.py
python3 three_bank_phase_audit.py
python3 ordinal_blind_query_audit.py
lean ShortcutCapital.lean
lean SemanticSampling.lean
lean SemanticCutPermutations.lean
lean SuccinctClaw.lean
lean SymmetricCubeSlices.lean
python3 shortcut_capital_audit.py
python3 public-tape-semantic-audit.py
python3 semantic_cut_permutation_audit.py
python3 succinct-claw-audit.py
python3 symmetric-cube-slices-check.py
lean CascadeSnapshotErrors.lean
lean OnlineDecoderClock.lean
python3 partial_domain_snapshot_audit.py
python3 stateful_inverse_window_audit.py
lean BlockAddressCertificates.lean
lean DecisionTimeoutTail.lean
lean SampledProofOracle.lean
python3 one_index_memory_audit.py
python3 nested_witness_isolation_audit.py
python3 public_tape_pcp_audit.py
python3 polynomial_tape_sums.py
python3 timely_checksum_lines_audit.py
lean SparsePermutationCompletion.lean
lean PermutationWindowRigidity.lean
lean TwoPermutationSwitch.lean
lean RainbowClausePath.lean
lean NativeTreewidthTrade.lean
lean MajoritySeam.lean
python3 permutation_window_audit.py
python3 rainbow_permutation_audit.py
python3 regular_incidence_audit.py
lean ChainProjection.lean
lean LexFactorResponse.lean
lean AnchoredCoverMoments.lean
lean TwoArmFactors.lean
lean PortfolioLocalDefects.lean
lean RelayTuplePatterns.lean
python3 anchored_cover_experiment.py
python3 lex_factor_response_experiment.py
python3 word_path_flat_experiment.py
python3 projective_incidence_experiment.py
lean LocalVerdictCheck.lean
lean SolverTrialStability.lean
lean TrialResetIntervals.lean
lean LiteralBranchParity.lean
lean PairedProbeBudget.lean
lean BooleanPushforward.lean
lean ModularFiberCounts.lean
python3 paired_name_probes_experiment.py
python3 path_replay_experiment.py
python3 substring_template_experiment.py
lean TraceCheck.lean
lean FullCubeSelection.lean
lean SuffixBlockExponents.lean
lean MixedTableauPatches.lean
lean XorPairCoverage.lean
lean XorButterflies.lean
lean XorPathCounts.lean
lean BatchHitPotential.lean
lean AffineProbeReplay.lean
lean AdaptiveHashTables.lean
lean MultitraceWitnesses.lean
lean PivotRowMass.lean
lean SparseStateInduction.lean
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
lean OneBitProduction.lean
lean ClockSpectrum.lean
lean ResidueHeaders.lean
lean ContinuumSavingRates.lean
lean RateCylinderLaws.lean
lean SuccessiveDescriptions.lean
lean OccupiedClockCells.lean
lean GrammarCell.lean
lean ListedFastReplacements.lean
lean NearClockCoding.lean
lean SharedLevinClock.lean
lean DiscountedMass.lean
lean DilatedMass.lean
lean SingletonIsolation.lean
lean TapeCubeMass.lean
lean UniqueWitnessBatches.lean
lean OrderedParityCovers.lean
lean MarginalGrowth.lean
lean EvaluationRecovery.lean
lean DefaultEscapes.lean
lean HornGapRounds.lean
lean LengthFreePrediction.lean
lean SoftRecovery.lean
lean MovingThreshold.lean
lean TimestampAllocation.lean
lean MidpointProgram.lean
lean RankRace.lean
lean ForcingLayouts.lean
lean MemoryLayout.lean
lean PrefixTreeWork.lean
lean SingleValuedCheckpoints.lean
lean QuadraticFibers.lean
lean DensePrefixQueries.lean
lean RelationalMemory.lean
lean SampleClockFeedback.lean
lean LowWeightPolynomial.lean
lean CommonDistortion.lean
lean PrefixPrediction.lean
lean TailCapacity.lean
lean StaggeredRelease.lean
lean RateBinCredits.lean
lean FifoProducerCredits.lean
lean WordCompletion.lean
lean ProducerProofExtension.lean
lean ParitySnapshots.lean
lean WindowLists.lean
lean AnonymousOmissions.lean
lean ExclusiveOwner.lean
lean ParityFibers.lean
python3 one_bit_production_experiment.py
python3 rational_clock_experiment.py
python3 adaptive_profile_experiment.py
python3 near_clock_code_experiment.py
python3 discounted_mass_experiment.py
python3 batch_hit_experiment.py
python3 partial_rank_experiment.py
python3 dilated_mass_experiment.py
python3 singleton_extremum_experiment.py
python3 cube_tape_experiment.py
python3 evaluation_recovery_experiment.py
python3 moving_threshold_experiment.py
python3 timestamp_allocation_experiment.py
python3 rank_race_experiment.py
python3 trace_pathwidth_experiment.py
python3 quadratic_fiber_experiment.py
python3 relational_memory_experiment.py
python3 sample_clock_feedback_experiment.py
python3 implicit_output_experiment.py
python3 rate_list_game.py
python3 word_completion_experiment.py
python3 suffix_image_experiment.py
python3 window_lists_experiment.py
python3 exclusive_owner_experiment.py
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
