#!/usr/bin/env python3
"""Independent falsification test of the crossed-scan read-pair dichotomy
(communication-bound-for-public-crossed-scans.md, 'Read pairs of an adaptive scan').

Written from the prose statement; imports nothing from the audited repository.

Machine: addresses Z_L. Read i has p = i*d mod L, x = M[p]. Then optionally
M[x] <- (i+delta)*d mod L with 0 <= delta <= r, chosen adversarially (or skipped).
Claim: with m reads, P = ceil(m/L), H = image of initial memory, B = r*P,
U = H shifted by 0..B scan steps: every (p, x) has x = p shifted by b, |b| <= B,
or p in U, or x in U.
"""
import itertools
import math
import random


def holds(L, d, r, init, choices, payload=None):
    m = len(choices)
    P = math.ceil(m / L)
    B = r * P
    U = {(h + s * d) % L for h in set(init) for s in range(B + 1)}
    local = {(b * d) % L for b in range(-B, B + 1)}
    mem = list(init)
    for i, delta in enumerate(choices):
        p = (i * d) % L
        x = mem[p]
        if not ((x - p) % L in local or p in U or x in U):
            return False
        if delta is not None:
            mem[x] = ((i + delta) * d) % L if payload is None else payload()
    return True


def exhaustive():
    n = 0
    for L, m in [(4, 8), (4, 10), (5, 8)]:
        for d in [d for d in range(1, L) if math.gcd(d, L) == 1]:
            for h in range(L):  # constant initial alphabet of one word
                for r in (0, 1):
                    opts = [None] + list(range(r + 1))
                    for ch in itertools.product(opts, repeat=m):
                        assert holds(L, d, r, [h] * L, ch), (L, d, r, h, ch)
                        n += 1
    return n


def randomized(trials, seed=1):
    rng = random.Random(seed)
    for t in range(trials):
        L = rng.choice([8, 16, 32, 64, 128])
        d = rng.choice([1, 3, 5, L - 1, L - 3])
        r = rng.randrange(0, 4)
        alpha = rng.sample(range(L), rng.randrange(1, 4))
        init = [rng.choice(alpha) for _ in range(L)]
        m = rng.randrange(1, 6 * L)
        opts = [None] + list(range(r + 1))
        # mix of uniform and heavily biased schedules
        bias = rng.choice(opts)
        q = rng.choice([0.0, 0.5, 0.9, 0.99])
        ch = [bias if rng.random() < q else rng.choice(opts) for _ in range(m)]
        assert holds(L, d, r, init, ch), (t, L, d, r, init, ch)
    return trials


def negative_control(trials=20000, seed=2):
    """Same checker, payload restriction removed. Violations must appear."""
    rng = random.Random(seed)
    L, bad = 64, 0
    for _ in range(trials):
        init = [rng.choice([1, 3]) for _ in range(L)]
        if not holds(L, 1, 1, init, [0] * L, payload=lambda: rng.randrange(L)):
            bad += 1
    return bad


if __name__ == "__main__":
    print("exhaustive schedules checked:", exhaustive())
    print("random schedules checked:", randomized(200000))
    print("negative control violations (must be > 0):", negative_control())
