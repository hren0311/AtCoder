n,m,x = map(int,input().split())
goods = [list(map(int,input().split())) for i in range(n)]
from itertools import combinations as comb
minm=float('INF')
def check(l):
    suml = [0]*(m+1)
    for j in l:
        good = goods[j]
        for s in range(0,m+1):
            suml[s] += good[s]
    for j in range(1,m+1):
        if(suml[j]<x):
            return None
    return suml[0]

ok = False
for i in range(1,n+1):
    
    for l in comb(range(n),i):
        num = check(l)
        if(num is None):
            continue
        if(minm>num):
            minm = num
            ok = True
if(ok):
    print(minm)
else:
    print(-1)
        
