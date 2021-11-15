N, M = map(int,input().split())

ans1 = (M*(M-1))//2
ans2 = (N*(N-1))//2

ans = ans1+ans2
print(ans)