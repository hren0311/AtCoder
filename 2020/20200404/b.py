n,m = map(int,input().split())
a = list(map(int,input().split()))
limit = sum(a) * (1/(4*m))
ans=0
for i in range(n):
    if(a[i]<limit):
        continue
    ans += 1
if(ans >=m):
    print('Yes')
else:
    print('No')