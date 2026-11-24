import Std

namespace SeedFilterAdvice

/-- A list hits the sets of seeds covered by all concentrated offer programs.
Both proposed pins on each list entry are false. -/
theorem sound_program_misses_coverage
    {Code Seed Index : Type} (offer : Code → Seed → Bool → Prop)
    (truth : Seed → Bool → Bool) (dense : Code → Prop) (selected : Index → Seed)
    (hits : ∀ c, dense c → ∃ i b, offer c (selected i) b)
    (flips : ∀ i b, truth (selected i) b = !b)
    (c : Code) (sound : ∀ r b, offer c r b → truth r b = b) : ¬ dense c := by
  intro high
  obtain ⟨i, b, path⟩ := hits c high
  have wrong := flips i b
  have right := sound _ _ path
  rw [right] at wrong
  cases b <;> contradiction

/-- Counts on an equal-size expansion of the two halves of the mixture.
Matching the proposed pin differs from correctness on at most `exceptions`
uniform samples. Every list sample reverses the pin. -/
theorem mixture_correct_count {total uniformMatch listMatch uniformCorrect listCorrect
    exceptions discrepancy : Nat}
    (uniform : uniformCorrect ≤ uniformMatch + exceptions)
    (flipped : listCorrect + listMatch = total)
    (sample : uniformMatch ≤ listMatch + discrepancy) :
    uniformCorrect + listCorrect ≤ total + discrepancy + exceptions := by
  omega

/-- Deterministic gap estimates suffice to certify a list. Integer counts
use a common scaling of the true and estimated means. -/
theorem certified_discrepancy {u v approxU approxV tolerance gap : Nat}
    (left : u ≤ approxU + tolerance) (close : approxU ≤ approxV + gap)
    (right : approxV ≤ v + tolerance) : u ≤ v + gap + 2 * tolerance := by
  omega

end SeedFilterAdvice
