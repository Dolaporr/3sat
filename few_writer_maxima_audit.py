"""Exhaust menus, histogram reconstruction, and perturbations of actual maxima."""

from collections import defaultdict, deque
from itertools import permutations, product


def histogram(names, width):
    counts = [0] * width
    for name in names:
        counts[name] += 1
    return tuple(counts)


def decode(menus, counts):
    """Decode a histogram in the common-order model, or reject it."""
    width = len(counts)
    if sum(counts) != len(menus) or any(h < 0 for h in counts):
        return None
    incidence = [[] for _ in counts]
    for row, menu in enumerate(menus):
        if not menu:
            return None
        for label in menu:
            incidence[label].append(row)
    degree = list(map(len, incidence))
    left = list(counts)
    if any(h > d for h, d in zip(left, degree)):
        return None
    queue = deque(v for v in range(width) if left[v] == degree[v] > 0)
    names = [None] * len(menus)
    while queue:
        v = queue.popleft()
        if degree[v] == 0 or left[v] != degree[v]:
            continue
        for row in incidence[v]:
            if names[row] is not None:
                continue
            names[row] = v
            left[v] -= 1
            for u in menus[row]:
                degree[u] -= 1
                if left[u] > degree[u]:
                    return None
                if u != v and left[u] == degree[u] > 0:
                    queue.append(u)
    return tuple(names) if all(v is not None for v in names) else None


def verify_noise(menus, actual, proposal, width):
    first = histogram(actual, width)
    second = histogram(proposal, width)
    distance = sum(max(0, a - b) for a, b in zip(first, second))
    illegal = sum(v not in menu for v, menu in zip(proposal, menus))
    wrong = sum(a != b for a, b in zip(actual, proposal))
    upper = (width - 1) * distance + width * illegal
    assert wrong <= upper
    return wrong, upper


def check_fibers():
    hist_tests = noise_tests = 0
    for width, rows in ((1, 2), (2, 3), (3, 3), (4, 2)):
        labels = range(width)
        subsets = [tuple(x for x in labels if mask & (1 << x))
                   for mask in range(1, 1 << width)]
        histograms = {histogram(xs, width) for xs in product(labels, repeat=rows)}
        for menus in product(subsets, repeat=rows):
            fibers = defaultdict(list)
            for allocation in product(*menus):
                fibers[histogram(allocation, width)].append(allocation)
            extrema = {tuple(max(menu, key=order.index) for menu in menus)
                       for order in permutations(labels)}
            for h in histograms:
                decoded = decode(menus, h)
                if len(fibers[h]) == 1:
                    assert decoded == fibers[h][0] and decoded in extrema
                else:
                    assert decoded is None
                    assert all(word not in extrema for word in fibers[h])
                hist_tests += 1
            actual = tuple(map(max, menus))
            for proposed in product(labels, repeat=rows):
                verify_noise(menus, actual, proposed, width)
                noise_tests += 1
    return hist_tests, noise_tests


def sharp_examples():
    tests = 0
    for width in range(2, 9):
        for distance, illegal in product(range(5), repeat=2):
            menus = []
            actual = []
            proposed = []
            for hi in range(1, width):
                for _ in range(distance + illegal):
                    menus.append((hi - 1, hi))
                    actual.append(hi)
                    proposed.append(hi - 1)
            for _ in range(illegal):
                menus.append((0,))
                actual.append(0)
                proposed.append(width - 1)
            got, bound = verify_noise(menus, actual, proposed, width)
            assert got == bound == (width - 1) * distance + width * illegal
            tests += 1
    return tests


def suffixes():
    tests = 0
    for j in range(1, 10):
        length = 1 << j
        for sign in (0, 1):
            replies = [sign ^ (i % 2) for i in range(length)]
            assert histogram(replies, 2) == (length // 2, length // 2)
            for i, reply in enumerate(replies):
                assert sign == reply ^ (i % 2)
                tests += 1
    return tests


if __name__ == "__main__":
    fiber_count, noise_count = check_fibers()
    print(f"{fiber_count} exact histogram decoding and fiber tests")
    print(f"{noise_count} perturbations of ordered menu maxima")
    print(f"{sharp_examples()} jointly sharp configurations")
    print(f"{suffixes()} suffix sign recoveries")
