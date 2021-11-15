n = int(input())
A = [int(x) for x in input().split()]

ans = 0
isOK = True
for i in range(n,-1,-1):
    limit = 2**i
    if(limit<A[i]):
        isOK = False
        break
    if(i==n):
        ans += A[i]
        pre = A[i]
        continue
    if((pre+A[i]) > limit):
        target = (pre+1)//2 + A[i]
        if(target > limit):
            isOK = False
            break
        else:
            target = limit
    else:
        target = pre+A[i]
        
    ans += target
    pre = target

if(isOK):
    print(ans)
else:
    print(-1)