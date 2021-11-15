n,m,k = map(int,input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
import sys
sys.setrecursionlimit(10**6)
maxc = 0
a_i=0
b_i=0
def dfs(a_i,b_i,t,cnt):
    global maxc
    
    if(a_i==n and b_i==m):
        maxc = m+n
        return
    if(k < t):
        maxc = max(maxc,cnt-1)
        return 
    if(a_i < n):
        dfs(a_i+1,b_i,A[a_i]+t,cnt+1)

    if(b_i < m):
        dfs(a_i,b_i+1,B[b_i]+t,cnt+1)



        
dfs(0,0,0,0)
print(maxc)