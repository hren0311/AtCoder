k = int(input())
if(k==1 or k==7):
    print(1)
    exit()
if(k%2==0):
    print(-1)
    exit()
x = 7
ans = None
for i in range(2,10**6+5):
    nex_x = 10*x+7
    nex_x = nex_x%k
    if(nex_x==0):
        ans = i
        break
    x = nex_x
    
if(ans is None):
    print(-1)
else:
    print(ans)