"""Check exact prefix witnesses, streaming bases, and inverse-permutation queries."""
from itertools import combinations, permutations
from math import comb, factorial
from random import Random


def masks(n, size):
    return [sum(1 << i for i in items) for items in combinations(range(n), size)]


def false_at(row, assignment):
    negative, positive = row
    return assignment & negative == negative and not assignment & positive


def proposed_chain(n, k):
    seen = []
    for size in reversed(range(k + 1)):
        for negative in masks(n, size):
            available = [i for i in range(n) if not negative >> i & 1]
            positive = sum(1 << i for i in available[:k - size])
            row = negative, positive
            assert all(not false_at(old, negative) for old in seen)
            assert false_at(row, negative)
            for x in range(1 << n):
                if (x ^ negative) & (positive | negative) == 0:
                    assert false_at(row, x)
            seen.append(row)
    assert len(seen) == sum(comb(n, size) for size in range(k + 1))
    return len(seen)


def basis_test(n, k, random):
    monomials = [m for size in range(k + 1) for m in masks(n, size)]
    pos = {m: i for i, m in enumerate(monomials)}
    clauses = [(neg, scope ^ neg) for scope in masks(n, k) for neg in range(1 << n)
               if not neg & ~scope]
    random.shuffle(clauses)
    basis = {}
    all_solutions = set(range(1 << n))
    basis_solutions = all_solutions.copy()
    for neg, positive in clauses:
        all_solutions = {a for a in all_solutions if not false_at((neg, positive), a)}
        row = sum(1 << pos[neg | p] for p in range(1 << n) if not p & ~positive)
        while row:
            j = row.bit_length() - 1
            if j not in basis:
                basis[j] = row
                basis_solutions = {a for a in basis_solutions if not false_at((neg, positive), a)}
                break
            row ^= basis[j]
        assert all_solutions == basis_solutions
    assert len(basis) <= len(monomials)
    return len(clauses)


def permutations_recovered(n, k):
    triples = masks(n, k)
    bit_positions = {s: sum(1 << x for x in range(1 << n) if false_at((s, 0), x))
                     for s in triples}
    signatures = set()
    for ordering in permutations(triples):
        surviving = (1 << (1 << n)) - 1
        earliest = {}
        for time, item in enumerate(ordering, 1):
            surviving &= ~bit_positions[item]
            for key in triples:
                if not surviving & bit_positions[key]:
                    earliest.setdefault(key, time)
        for key, when in earliest.items():
            prefix_value = 0
            for bit in reversed(range((len(triples) - 1).bit_length())):
                midpoint = (prefix_value * 2 + 1) << bit
                has_appeared = when <= min(midpoint, len(triples))
                prefix_value = prefix_value * 2 + int(not has_appeared)
            assert prefix_value == when - 1
        assert tuple(sorted(earliest, key=earliest.get)) == ordering
        signatures.add(tuple(earliest[key] for key in triples))
    assert len(signatures) == factorial(len(triples))
    return len(signatures)


if __name__ == "__main__":
    rng = Random(883)
    sizes = [(n, k) for n in range(1, 8) for k in range(1, n + 1)]
    print(f"{sum(proposed_chain(n, k) for n, k in sizes)} private prefix witnesses")
    print(f"{sum(basis_test(n, k, rng) for n, k in sizes)} simultaneous prefix bases checked by update")
    print(f"{sum(permutations_recovered(n,k) for n,k in [(4,2),(4,3),(5,4)])} permutations recovered via pinned SAT")
