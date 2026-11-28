# Seven minimum test suites for four stored RAM instructions

Independent 3sat.live research, 28 November 2026. Computational census and model argument, not Lean-checked or independently refereed. Priority unestablished.

This follows the small-machine enumeration discussion and the open classification in [Static program size on two sign planes](https://github.com/aeyakovenko/3sat/blob/713aebb1888f7f3300b4dc21bf0ea5863480423a/notes/static-program-size-on-two-sign-planes.md). The earlier note proves minimum cardinality six, gives three examples, and explicitly leaves the complete static minimum-suite list unclassified. Its [dynamic clock companion](https://github.com/aeyakovenko/3sat/blob/713aebb1888f7f3300b4dc21bf0ea5863480423a/notes/exact-clocks-for-two-word-sat-inputs.md) establishes exactly three minimum suites for the four-step model.

## Result

In the same finite two-bit sign-plane machine and instruction basis, the following seven six-input masks defeat every program with at most four static slots, with no time limit on the tested inputs:

    5570, 5572, 5576, 5584, 6080, 7048, 21952

The four additional masks beyond the previously exhibited static examples are 5572, 6080, 7048, 21952. Bit P+4N marks the row with initial words P,N in {0,1,2,3}. The target is (P AND N)==0 and N!=3. A program fits a suite if it halts correctly on every selected row; outside the suite no correctness or termination is required.

The claim is finite and specific to the stated instruction basis, memory layout and separate control operations. It is not a four-to-five-slot induction for arbitrary SAT encodings, nor a time lower bound for unrestricted word RAMs.

## Coverage and finite census

First reproduce the upstream two-direct-load subclass. Its 1,162 distinct prediction tables cover all 6,885 suites of size at most five. Of the 8,008 six-input subsets, only eight are not covered:

    5570, 5572, 5576, 5584, 6020, 6080, 7048, 21952

On each of these eight suites, both P and N are essential, and P=0 occurs with both target verdicts. Therefore a program with no load or a single fixed-address load cannot fit. A cyclic program with a single self-addressed load and no other data site reads zero forever on the P=0 row, so it too fails. These elementary checks allow the upstream control-graph classification to apply even to programs allowed to diverge outside the tested suite.

For cyclic programs, reuse the upstream exhaustive shape reduction: two branches and two data sites, one a load. Enumerate 6 first-load sources, 286 second data instructions (semantic tables), and 60 control schedules. Evaluate states until repetition; compare first exit times for all 32 predicates or evaluate the final predicate after the first exit. A separate local C++ implementation found no fitting cyclic configuration among 102,960 cases for each of the eight masks.

For acyclic programs, at least two loads are needed. Before the first load, any data instruction has only constant inputs. With at most four slots and one branch, all useful data instructions precede the branch; enumerate two or three data sites containing at least two loads, including constant ALU or stores preceding the first load. At most three registers are written; normalize fresh register names, and replace never-written registers by literal zero. With two branches there are exactly two useful loads. Before the first load, branches have constant outcomes. After that load the first branch either exits directly, skips the second load and joins the final branch, or both loads precede both branches. Enumerate conjunctions/complements for direct exits, and the shared final predicate evaluated on both states for the skip-load join. The enumerated acyclic class tested 814,970 verdict tables with repetitions; only mask 6020 has a fitting program.

Its explicit four-slot witness is:
    
    0: r0 = LOAD [1]       // N
    1: r1 = N AND 1
    2: r1 = LOAD [r1]
    3: return YES iff r1 != r0

It returns the prediction mask 2830. This agrees with SAT on all six rows of mask 6020; it is not a globally correct solver.

The seven remaining domains are excluded by both finite searches. This closes the finite classification subject to review of the control-shape reduction and the enumerator. It also distinguishes the static and dynamic suite counts (seven versus three).

## Reproduction

Run the companion acyclic and subclass audits in this directory. For the cyclic census, the upstream checker at the pinned commit can be compiled with g++ -O3 -std=c++17 and invoked with arguments `all MASK` for each of the eight masks. A separate local implementation was also used to reproduce these cyclic negative results. All results are about this finite ISA only.

## Question for discussion

Does the additional static suite structure give a useful invariant for the next code-size induction? In particular, any such invariant must distinguish fixed control topology from a depth-bounded unrolled tree, and account for indirect loads like the 6020 witness. The seven masks are concrete regression cases for future changes to the synthesis model, not evidence that a growing native-clock deficit persists.

Independent project: https://3sat.live. The original research and the prior reductions are Anatoly Yakovenko's; this is an AI-assisted independent computational extension.
