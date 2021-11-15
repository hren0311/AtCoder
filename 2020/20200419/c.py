n= int(input())
syain = list(map(int,input().split()))
ans = [0 for i in range(n+1)]
for x in syain:
    ans[x] += 1

for i in range(1,n+1):
    print(ans[i])