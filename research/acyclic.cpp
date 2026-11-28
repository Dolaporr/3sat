// Exhaustive acyclic four-slot census on the same 2-bit ISA.
// Data sources 0..3 = constants, 4..6 = registers; branch predicates EQ/LT/SLT and complements.
#include <array>
#include <vector>
#include <string>
#include <map>
#include <iostream>
#include <cassert>
#include <cstdint>
using namespace std;
using U=unsigned;
struct State{array<array<int,3>,16> r{};array<int,16> m{};};
struct Op{int kind,a,b,d,k;};
int src(int i,const array<int,3>&r){return i<4?i:r[i-4];}
int sw(int x){return x<2?x:x-4;}
int val(int op,int a,int b){switch(op){case 0:return a&b;case 1:return a|b;case 2:return a^b;case 3:return a+b;case 4:return a-b;case 5:return a*b;case 6:return a<<b;case 7:return a>>b;case 8:return sw(a)>>b;case 9:return a<<(b%2);case 10:return a>>(b%2);case 11:return sw(a)>>(b%2);case 12:return (a<<(b%2))|(a>>(2-b%2));case 13:return a==b;case 14:return a<b;case 15:return sw(a)<sw(b);case 16:return a!=b;case 17:return a>=b;default:return sw(a)>=sw(b);}}
State apply(State s,Op o){for(int z=0;z<16;z++){auto&r=s.r[z];int a=src(o.a,r),b=src(o.b,r);if(o.kind==1)s.m[z]=(s.m[z]&~(3<<(2*a)))|(b<<(2*a));else r[o.d]=(o.kind==0?(s.m[z]>>(2*a)):val(o.k,a,b))&3;}return s;}
string desc(Op o){return to_string(o.kind)+","+to_string(o.a)+","+to_string(o.b)+","+to_string(o.d)+","+to_string(o.k);}
map<U,string> predicates(const State&s,int regs){map<U,string> p;for(int i=0;i<4+regs;i++)for(int j=0;j<4+regs;j++)for(int k=0;k<3;k++){U a=0;for(int z=0;z<16;z++){int x=src(i,s.r[z]),y=src(j,s.r[z]);if(k==0?x==y:k==1?x<y:sw(x)<sw(y))a|=1u<<z;}string d=to_string(k)+","+to_string(i)+","+to_string(j);p[a]=d+",0";p[a^65535]=d+",1";}return p;}
vector<Op> loads(int regs){vector<Op> o;for(int a=0;a<4+regs;a++)for(int d=0;d<=regs;d++)o.push_back({0,a,0,d,0});return o;}
vector<Op> nonloads(int regs){vector<Op> o;for(int a=0;a<4+regs;a++)for(int b=0;b<4+regs;b++){o.push_back({1,a,b,0,0});for(int k=0;k<19;k++)for(int d=0;d<=regs;d++)o.push_back({2,a,b,d,k});}return o;}
int main(){State ini;U target=0;for(int z=0;z<16;z++){ini.m[z]=z;if(!((z&3)&(z>>2))&&(z>>2)!=3)target|=1u<<z;}vector<U> dom={5570,5572,5576,5584,6020,6080,7048,21952};map<U,string> hits;uint64_t verdicts=0;
auto check=[&](U v,string msg){++verdicts;for(U d:dom)if(!hits.count(d)&&!((v^target)&d)){hits[d]=msg;cout<<"domain "<<d<<" witness "<<msg<<" verdict "<<v<<"\n";}};
auto last=[&](const State& s,int regs,string prefix){for(auto [v,p]:predicates(s,regs))check(v,prefix+" branch "+p);};
// Explicitly include a pre-read data operation below.
// With one branch and <=3 data ops, two loads are needed on these domains.
for(int a=0;a<2;a++){Op A={0,a,0,0,0};auto s=apply(ini,A);string pa=desc(A);last(s,1,pa);
 auto p1=predicates(s,1);
 for(auto B:loads(1)){auto t=apply(s,B);int nr=B.d==1?2:1;string pb=pa+" / "+desc(B);last(t,nr,pb);auto p2=predicates(t,nr);
 // Two branches: both after both reads, or first branch between reads.
 for(auto [p,d]:p2)for(auto [q,e]:p2){check(p&q,pb+" AND "+d+" ; "+e);check((p&q)^65535,pb+" NAND "+d+" ; "+e);}
 for(auto [p,d]:p1)for(auto [q,e]:p2){check(p&q,pa+" early branch "+d+" / "+desc(B)+" / "+e);check((p&q)^65535,pa+" early NAND "+d+" / "+desc(B)+" / "+e);}
 // The first branch may skip the second load and join at the final branch.
 // Evaluate the SAME final predicate on both register states.
 for(int i=0;i<4+nr;i++)for(int j=0;j<4+nr;j++)for(int k=0;k<3;k++){
 U before=0,after=0;for(int z=0;z<16;z++){int x=src(i,s.r[z]),y=src(j,s.r[z]);if(k==0?x==y:k==1?x<y:sw(x)<sw(y))before|=1u<<z;x=src(i,t.r[z]);y=src(j,t.r[z]);if(k==0?x==y:k==1?x<y:sw(x)<sw(y))after|=1u<<z;}
 for(auto [p,d]:p1){U v=(p&after)|((p^65535)&before);check(v,pa+" skip-load mux "+d+" / "+desc(B)+" / "+to_string(k)+","+to_string(i)+","+to_string(j)+",0");check(v^65535,pa+" skip-load mux "+d+" / "+desc(B)+" / "+to_string(k)+","+to_string(i)+","+to_string(j)+",1");}
 }
 for(auto C:loads(nr))last(apply(t,C),nr+(C.d==nr),pb+" / "+desc(C));
 for(auto C:nonloads(nr))last(apply(t,C),nr+(C.kind==2&&C.d==nr),pb+" / "+desc(C));
 }
 for(auto B:nonloads(1)){auto t=apply(s,B);int nr=1+(B.kind==2&&B.d==1);string pb=pa+" / "+desc(B);for(auto C:loads(nr))last(apply(t,C),nr+(C.d==nr),pb+" / "+desc(C));}
}
// Before the first load a single data instruction has only constant sources.
// Enumerate all stores and ALU operations (deduplicate constant ALU result).
vector<Op> initial;for(int a=0;a<4;a++)for(int b=0;b<4;b++)initial.push_back({1,a,b,0,0});for(int a=0;a<4;a++)initial.push_back({2,a,0,0,1});
for(auto A:initial){auto s=apply(ini,A);int nr=A.kind==2?1:0;for(auto B:loads(nr)){auto t=apply(s,B);int n2=nr+(B.d==nr);for(auto C:loads(n2))last(apply(t,C),n2+(C.d==n2),desc(A)+" / "+desc(B)+" / "+desc(C));}}
for(auto d:dom)if(!hits.count(d))cout<<"domain "<<d<<" no acyclic witness in enumerated class\n";cout<<"Verdict tables tested (with repetitions): "<<verdicts<<"\n";
}
