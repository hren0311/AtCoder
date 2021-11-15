n = int(input())
ans = 1
l = [int(x) for x in input().split()]
limit = 10**18
if(0 in l):
    print(0)
    exit()

for x in l:
    x = int(x)
    ans *= x

    if(ans > limit):
        print(-1)
        exit()    

print(ans)
