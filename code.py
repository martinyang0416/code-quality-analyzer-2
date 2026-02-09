import collections
from math import factorial
def comb(n,r):
    return factorial(n)//factorial(n-r)//factorial(r)
n,a,b=map(int,input().split())
v=list(map(int,input().split()))
v.sort(reverse=True)
c=collections.Counter(v)
k=min(v[:a])
if c[max(v)]<a:
    ans=comb(c[k],v[:a].count(k))
else:
    ans=0
    for i in range(a,min(b,c[k])+1):
        ans+=comb(c[k],i)
print(sum(v[:a])/a)
print(ans)