# Exact parity-filter capacity with adaptive record reads

Independent 3sat.live research note — 2026-11-27. Manuscript proof, not independently refereed or Lean-checked. Priority unestablished. Companion to [the upstream collision-pair note](https://github.com/aeyakovenko/3sat/blob/713aebb1888f7f3300b4dc21bf0ea5863480423a/notes/odd-filters-on-collision-pairs.md).

## Result

Let t >= 3 records take values from an alphabet of size at least t. A deterministic decision algorithm may read at most r distinct whole records (0 <= r <= t) and query the parity of equal pairs in at most s chosen edge subsets. Queries and reads may be interleaved adaptively. Promise at most three equal pairs (zero is allowed). Then for every integer s >= 7, such an algorithm exists if and only if

    min(t-r, t-2) <= 2^(s-1).

The same equivalence holds even under the narrower promise that all equality classes have size at most two. In particular without raw reads the exact capacity is 2^(s-1)+2. This is a statement about a specified query model, not unrestricted RAM runtime, unique-witness isolation, or a risk engine security theorem. No external circuit lower bound is needed.

## Reduction to edge labels

Follow an algorithm on an all-distinct list, and freeze its transcript. Let r' <= r be the number of distinct inspected rows. All parity answers on this transcript are zero. Let P be the inspected rows and G the complete graph with the edges internal to P deleted. Label each edge by the s-bit vector recording whether it occurs in each parity mask on this path (pad with zero masks as needed). Every matching of one, two or three edges of G is realized by a list with the same inspected values: pair the endpoints, keep the pinned values, and choose fresh distinct symbols for all other classes. The alphabet assumption suffices. If its edge labels XOR to zero, the algorithm follows exactly the same transcript and incorrectly rejects. Thus each such matching must have nonzero XOR. For the larger promise one must also detect triangles with at most one pinned vertex. The lower bound below uses only matchings.

## Construction

Write H=2^(s-1). Assign each color a different vector in the affine hyperplane of F_2^s whose first coordinate is one. If t-r <= H, first read r rows. Return positive if two read values agree. Otherwise assign every edge of G to one of its unread endpoints, using one star color per unread vertex. If t-2 <= H instead, one may skip all reads and color K_t by t-3 successive stars and one final triangle. Each color is an intersecting family of edges. A single edge or three edges have odd first coordinate, and two disjoint edges have distinct labels. These are all nonempty equality graphs with at most three edges (three edges can be a matching or a triangle). Asking all label coordinates decides the problem. This construction is nonadaptive after reading the selected rows.

## Local lemmas

Consider any edge labeling into F_2^s which detects every matching of size one through three. Each label is nonzero and its color class is pairwise intersecting. Such a class is a star or a triangle: two incident edges ab, ac force any edge not incident to a to be bc, and no further distinct edge intersects all three. Call a star large if it has at least four edges.

1. Choose one large-star label for each distinct center, and call the resulting set S. It is sum-free. If three distinct chosen labels XOR to zero, remove the other two centers from each star's leaf set. Each set still contains at least two leaves. If their union has at least three elements, Hall's theorem gives three distinct representatives, hence a zero-XOR three-edge matching. Otherwise all three leaf sets equal the same two-element set. Each original star then must contain both of the deleted centers as leaves to attain size four. The center-to-center edges would have multiple labels, impossible. Repeated labels cannot form a zero-sum triple since no label is zero. In particular |S| <= H, by disjointness of S and x+S for x in S.

2. If two chosen large stars have different centers c,d, an edge ab disjoint from c,d cannot have label x+y, where x,y are the star labels. Remove a,b and the other center from each leaf set. Both sets are nonempty. Failure to choose different leaves requires both sets to be the same singleton, which forces the edge cd to occur in both stars. Impossible. The two selected star edges and ab would otherwise give a zero-XOR matching.

3. A sum-free subset S of F_2^s with |S|>2H/3 lies in one nonzero affine hyperplane C, and S+S equals its underlying subspace U. For a self-contained proof let f be the indicator of S, alpha=|S|/2^s, and use normalized real Fourier coefficients on F_2^s. Parseval gives sum of squared coefficients alpha. The sum of cubed coefficients is the normalized number of x,y with x,y,x+y in S, hence zero. If m is the smallest nontrivial coefficient, then -alpha^3 >= m(alpha-alpha^2), so m <= -alpha^2/(1-alpha). The negative coset C of a character attaining m contains fraction (alpha-m)/2 >= alpha/[2(1-alpha)] > 1/4 of the whole group in S. Thus more than half of C is in S. Its translate by each u in U intersects it, proving U is contained in S+S. Sum-freeness excludes all elements of U from S, proving S is contained in C and hence S+S=U.

## Obstruction on K_(H+3) with at most one missing edge

Suppose a valid label table exists on such a graph, with H>=64. Choose the large-star representatives as above. Write h=|S| and a=H-h>=0. Delete the h centers. Every surviving color class has at most three edges, since the center of every originally large star was deleted. The h chosen labels are gone. The remaining graph has at least binom(a+3,2)-1 edges (at most one edge was missing initially), and at most 2H-1-h=H-1+a nonzero labels. Consequently

    binom(a+3,2)-1 <= 3(H-1+a)
    a^2-a+10 <= 6H.

If a>=H/3 then a^2-a+10 >= H^2/9-H/3+10 > 6H for H>=64 (equivalently H^2-57H+90>0). Thus h>2H/3. By lemma 3, S occupies the coset C and S+S=U. Every surviving edge is disjoint from all chosen centers. A nonzero label in U would be x+y for distinct x,y in S and is forbidden by lemma 2. Only labels in C can remain. Since h of them disappeared, at most a survive, each on at most three edges. Hence

    binom(a+3,2)-1 <= 3a
    a^2-a+4 <= 0,

contradicting a(a-1)>=0 for any nonnegative integer a.

## Adaptive lower bound

If min(t-r,t-2)>H, then also min(t-r',t-2)>H for the all-distinct transcript. There are at least H+1 unread rows and at least H+3 rows total. Choose H+3 vertices with at most two pinned vertices: if at least H+3 unread exist take those; if H+2 unread exist add one pin; if H+1 unread exist add two pins. The induced graph is K_(H+3) minus at most one edge. Restrict the path labels to it. Every matching of one through three is feasible with the pinned observations held fixed, contradicting the obstruction. This proves the exact adaptive statement. In particular, for min(t-r,t-2)>64 the minimum parity query count is 1+ceil(log2(min(t-r,t-2))) by monotonicity. Smaller filter counts are not determined by this theorem.

## Reproducibility and limitations

Run `python research/three-pair-adaptive-audit.py` from the repository root. Finite tests check the explicit constructions for small cases, sample boundary matchings, and check the arithmetic inequalities for s=7 through 12. They are not evidence of an unrestricted lower bound, nor a substitute for the general proof. No Lean compiler was available for this contribution. The manuscript extends the upstream two-pair exact adaptive tradeoff and fixed-k asymptotics. A limited source check found no exact three-pair adaptive statement; novelty against all graph-code literature is not established.

## Open discussion

Can the cutoff s>=7 be removed? Can analogous dense-label arguments price four-pair detection? The result shows that access to r raw rows has an exact effect on a restricted parity verifier, even if it chooses tests adaptively. It does not price native indexed RAM reads, which may solve list distinctness by radix sorting. A central question is whether any related obstruction survives a richer verification model.

Independent project: https://3sat.live — public explorer of the upstream research, not affiliated with the original author. This note is separate from the upstream journal.
