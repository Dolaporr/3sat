from itertools import combinations
from random import Random
from functools import reduce
from operator import xor

# Vertices 0,...,r-1 have already been read and are distinct.
def labels(t,r,s):
    H=1 << (s-1)
    u=t-r
    assert min(u,t-2)<=H and t>=3
    out={}
    for i,j in combinations(range(t),2):
        if j<r: continue
        if u<=H:
            color=(i if i>=r else j)-r
        else:
            color=min(i,t-3)
        assert 0<=color<H
        out[i,j]=H+color
    return out

def check(t,r,s):
    table=labels(t,r,s)
    n=0
    for k in (1,2,3):
        for es in combinations(table,k):
            if len({v for e in es for v in e})!=2*k: continue
            assert reduce(xor,(table[e] for e in es),0)!=0
            n+=1
    for a,b,c in combinations(range(t),3):
        if sum(v<r for v in (a,b,c))>1: continue
        assert table[a,b]^table[a,c]^table[b,c]
        n+=1
    return n

n=sum(check(t,r,s) for s in range(1,5) for t in range(3,11) for r in range(t+1) if min(t-r,t-2)<=1<<(s-1))
print('Exhaustive construction checks (small t, all allowed pin counts):',n)
rng=Random(20261127)
n=0
for s in range(7,10):
    H=1<<(s-1)
    for t,r in [(H+2,0),(H+2,2),(H+4,4),(H+16,16)]:
        table=labels(t,r,s)
        es=list(table)
        for _ in range(2000):
            chosen=rng.sample(es,3)
            if len({v for e in chosen for v in e})!=6: continue
            assert reduce(xor,(table[e] for e in chosen),0)!=0
            n+=1
print('Randomized boundary three-matching checks:',n)
for s in range(7,13):
    H=1<<(s-1)
    for a in range(H+1):
        if a*3>=H:
            assert (a+3)*(a+2)//2-1>3*(H-1+a)
        assert (a+3)*(a+2)//2-1>3*a
print('Integer inequalities: verified at s=7,...,12')
