# Independent partial audit: the five-instruction DIMACS SAT bound

Repository: `aeyakovenko/3sat` at `a1c4285` (2026-11-25). Audited with AI assistance (Claude).

**Result.** No error found in the parts checked. The headline theorem is a manuscript proof. It is not formalized in the Lean files linked from its proof notes. This is not a verification of the theorem.

## What the statement needs

Short form: "no program with at most five stored instructions decides DIMACS SAT in N^(1.5−ε)". The notes prove something narrower, and these conditions matter:

- Time bound is O(N^(3/2−ε)), for every fixed ε > 0.
- A *separate-operation* RAM: LOAD/STORE take a register or immediate address; no indexed or auto-increment addressing, fused operations, indirect jumps or memory-valued verdicts. The listed ALU set has no division.
- Byte-aligned width w = 16⌈D·log2(N+2)/16⌉, little-endian input, ASCII DIMACS.
- Accept/reject exits are terminals and are not among the five slots (as I read the control-graph argument).
- `research-steering.md` says no correct SAT program in the five-slot model has been exhibited.

## Lean (4.19.0)

All five files linked from the proof notes compile. A text scan found no `sorry`, `native_decide` or declared `axiom`. `#print axioms` reports at most `propext`, `Classical.choice`, `Quot.sound`.

| File | What its theorems cover |
|---|---|
| `ResetEpisodePacking.lean` | counting bound for reset episodes |
| `BoundedRamWitnesses.lean` | quantifier and accounting lemmas |
| `CrossedScanAncestry.lean` | last-writer links, 0/1 offsets |
| `AdaptiveCrossedCommunication.lean` | the same for bounded offsets |
| `SparseDecimalNames.lean` | window capacity and exponent arithmetic (for the 6/5 refinement) |

None of these defines the RAM, a five-slot program, DIMACS SAT, the communication protocol or the final lower bound. The case analysis, the equality reduction and the protocol are prose. The communication note says so itself for the last two.

## Independent tests (written from the prose, no repository code)

1. `check_dichotomy.py`: the crossed-scan read-pair dichotomy. 671,460 exhaustive small schedules and 200,000 random ones, no counterexample. With the payload restriction removed, the same checker finds 17,719 violating runs out of 20,000.
2. `check_layout.py`: the DIMACS layout behind "Property 1" at w = 256, 512, 1024. All words even, small word alphabet, tail words above the norm threshold, each full tail word holds a whole clause, and in one sampled flip per case only that word changed. This is my reconstruction of the layout. It does not test the SAT/UNSAT claim, and these lengths do not follow the width rule.

## Other checks

- Final step of the 3/2 argument: with h ≤ N^η and η < 2ε, the protocol cost is o(k). Consistent.
- Time-space step: the threshold ((c+2)/c² − c)/2 is 0.7286 at c = 1.101 and 0.0265 at c = 1.501, matching the notes. I saw FLMV Corollary 5.8 only through an automated extract with a garbled exponent, so check it against the PDF.

## Not checked

Completeness of the five-slot case analysis line by line; the sparse-name alphabet bound; the virtual-input simulation; the 6/5 refinement; the one-register N²/log²N claim.

## Open question

Is any five-slot program correct on SAT at all, at any speed? Some instruction allocations are shown to fail regardless of time. If all of them do, the time bound still holds, but the exponent is not what excludes them. A proof either way would sharpen the result.

## Reproduce

    lean <file>.lean                      # Lean 4.19.0, then append #print axioms <name>
    python3 check_dichotomy.py
    python3 check_layout.py
