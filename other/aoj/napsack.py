N,W = map(int,input().split())
prod = [list(map(int,input().split())) for i in range(N)]
used = [[] for i in range(W+1)]
dp = [0]*(W+1)
for i in range(1,W+1):
    dp[i] = 0
    for j in range(N):
        w = prod[j][1]
        weight = (i-w)
        if(weight<0):
            continue
        
        if(j in used[weight]):
            continue
        

        dp[i] = max(dp[i],dp[weight]+prod[j][0])
        

        
    print(i,dp)
        
    
print(dp[W])

