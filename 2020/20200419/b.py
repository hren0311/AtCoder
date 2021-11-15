n,m = map(int,input().split())
day = list(map(int,input().split()))
all_s = sum(day)

ans = n-all_s

if(ans<0):
    print(-1)
else:
    print(ans)