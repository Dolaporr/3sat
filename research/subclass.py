# Reproduce the upstream two-direct-load subclass coverage.
from itertools import product

def src(i,z): return i if i<4 else (z>>(2*(i-4)))&3
def signed(x): return x if x<2 else x-4
def vals(a,b):
    return (a&b,a|b,a^b,a+b,a-b,a*b,a<<b,a>>b,signed(a)>>b,a<<(b%2),a>>(b%2),signed(a)>>(b%2),(a<<(b%2))|(a>>(2-b%2)),int(a==b),int(a<b),int(signed(a)<signed(b)),int(a!=b),int(a>=b),int(signed(a)>=signed(b)))
pred=set(); tabs=set()
for i,j in product(range(6),repeat=2):
    pairs=[(src(i,z),src(j,z)) for z in range(16)]
    for k in range(3):
        p=sum(1<<z for z,(a,b) in enumerate(pairs) if (a==b,a<b,signed(a)<signed(b))[k]); pred.update((p,p^65535))
    for k in range(19): tabs.add(tuple(vals(a,b)[k]&3 for a,b in pairs))
predictions=set()
def add(p): predictions.update((p,p^65535))
for p,q in product(pred,repeat=2): add(p&q)
for t,b,p in product(tabs,range(6),pred): add(sum(1<<z for z in range(16) if p>>(t[z]+4*src(b,z))&1))
assert (len(pred),len(tabs),len(predictions))==(32,119,1162)
target=sum(1<<z for z in range(16) if not((z&3)&(z>>2)) and z>>2!=3)
covered=bytearray(65536)
for p in predictions: covered[65535^target^p]=1
for s in range(65535,0,-1):
    if covered[s]:
        x=s
        while x:
            bit=x&-x;covered[s^bit]=1;x^=bit
small=[s for s in range(65536) if s.bit_count()<=5]; assert all(covered[s] for s in small)
missing=[s for s in range(65536) if s.bit_count()==6 and not covered[s]]
assert missing==[5570,5572,5576,5584,6020,6080,7048,21952]
for m in missing:
    rows=[(z&3,z>>2,bool(target>>z&1)) for z in range(16) if m>>z&1]
    assert {v for p,n,v in rows if p==0}=={False,True}
    assert any(p==q and v!=w for p,n,v in rows for q,k,w in rows)
    assert any(n==k and v!=w for p,n,v in rows for q,k,w in rows)
print('Subclass predictions:',len(predictions),'covered suites of size <=5:',len(small))
print('Remaining six-input domains:',missing)
