import Std

namespace TaggedParityImages

/-- Every vector obtainable from the left equalities has zero discrepancy. -/
def ZeroImage {I J V : Type} (tag : I → J) (payload : I → V) (target : J → V) : Prop :=
  ∀ (high : J → Bool) (low : V → Bool),
    (∀ i, high (tag i) = low (payload i)) → ∀ j, high j = low (target j)

/-- A missing tag lets its free variable violate a target equality. -/
theorem missing_tag {I J V : Type} [DecidableEq J] (tag : I → J)
    (payload : I → V) (target : J → V) (j : J) (absent : ∀ i, tag i ≠ j) :
    ¬ ZeroImage tag payload target := by
  intro h
  have hleft : ∀ i, decide (tag i = j) = false := by
    intro i
    simp [absent i]
  have impossible := h (fun k => decide (k = j)) (fun _ => false) hleft j
  simp at impossible

/-- With inverse tags, a zero image is precisely the routed payload test. -/
theorem permutation_payload {I J V : Type} [DecidableEq V] (tag : I → J)
    (row : J → I) (payload : I → V) (target : J → V)
    (leftInv : ∀ i, row (tag i) = i) (rightInv : ∀ j, tag (row j) = j) :
    ZeroImage tag payload target ↔ ∀ j, payload (row j) = target j := by
  constructor
  · intro h j
    let low : V → Bool := fun v => decide (payload (row j) = v)
    let high : J → Bool := fun k => low (payload (row k))
    have hleft : ∀ i, high (tag i) = low (payload i) := by
      intro i
      simp [high, leftInv]
    have eq := h high low hleft j
    simpa [high, low] using eq
  · intro correct high low hleft j
    rw [← correct j]
    simpa [rightInv] using hleft (row j)

/-- A finite binary linear image contributes one modulo two exactly at rank zero. -/
theorem parity_of_image_card (r : Nat) : 2^r % 2 = 1 ↔ r = 0 := by
  cases r with
  | zero => decide
  | succ r => simp [Nat.pow_succ]

end TaggedParityImages
