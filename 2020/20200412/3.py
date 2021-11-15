from math import gcd
k = int(input())
ans=0
memo = [[0]*201 for i in range(201)]
ismemo = [[False]*201 for i in range(201)] 
for x in range(1,k+1):
    for y in range(1,k+1):
        for z in range(1,k+1):
            
            ans += gcd(gcd(x,y),z)
print(ans)