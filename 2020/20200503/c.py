n,m = map(int,input().split())
hei = list(map(int,input().split()))
bestT = [True for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    if(hei[a-1] == hei[b-1]):
        bestT[a-1] = False
        bestT[b-1] = False
        continue
    if(hei[a-1] > hei[b-1]):
        bestT[b-1] = False
    else:
        bestT[a-1] = False

ans = sum(bestT)
print(ans)