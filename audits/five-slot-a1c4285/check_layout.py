#!/usr/bin/env python3
"""Independent check of 'Property 1' of the DIMACS layout in
five-instruction-loops-on-dimacs-sat.md, built from the prose alone."""


def build(j, flip=None):
    clauses = 10 ** j
    head = b"p cnf 20 1" + b"0" * j
    head += b" \n" if (len(head) + 1) % 2 else b"\n"
    assert len(head) % 2 == 0

    def line(lits):
        out = bytearray()
        for neg, name in lits:
            if len(out) % 2 == 0:
                out += b" "           # keep the sign slot at an odd offset
            out += b"-" if neg else b" "
            out += str(name).encode()
            out += b" "
        out += b"0"
        out += b"\n" if len(out) % 2 else b" \n"
        assert len(out) % 2 == 0
        return bytes(out)

    forced = [line([(False, v), (s, 8), (t, 20)])
              for v in (2, 4, 6) for s in (False, True) for t in (False, True)]
    pos = line([(False, 2), (False, 4), (False, 6)])
    neg = line([(True, 2), (True, 4), (True, 6)])
    assert len(pos) == len(neg)
    body = [pos] * (clauses - len(forced))
    if flip is not None:
        body[flip] = neg
    return head + b"".join(forced) + b"".join(body), len(head), len(b"".join(forced)), len(pos)


# A word must be able to hold a whole clause record, so test large w.
for w in (256, 512, 1024):
    W = w // 8
    for j in (3, 4, 5):
        data, hl, nf, rec = build(j)
        padded = data + b"\0" * (-len(data) % W)
        words = [int.from_bytes(padded[i:i + W], "little") for i in range(0, len(padded), W)]
        assert len(data) == hl + nf + (10 ** j - 12) * rec
        start = hl + nf   # forced clauses are longer than tail clauses
        full = range(-(-start // W), len(data) // W)
        Q = 1 << w
        low_norm = sum(1 for i in full if min(words[i], Q - words[i]) < 10 * Q // 256)
        uncovered = 0
        for i in full:
            c = -(-(i * W - start) // rec)          # first clause starting in word i
            if not (start + c * rec >= i * W and start + (c + 1) * rec <= (i + 1) * W):
                uncovered += 1
        i = full[len(full) // 2]
        c = -(-(i * W - start) // rec)
        other = build(j, flip=c)[0]
        changed = {p // W for p, (a, b) in enumerate(zip(data, other)) if a != b}
        print(f"w={w} j={j} odd_words={sum(v & 1 for v in words)} "
              f"distinct_words={len(set(words) | {0})} full_tail_words={len(full)} "
              f"below_norm={low_norm} without_whole_clause={uncovered} "
              f"words_changed_by_flip={len(changed)} same_length={len(other) == len(data)}")
