n,k = map(int,input().split())
okashi = [0 for i in range(n+1)]

for i in range(k):
    d = int(input())
    if(d==1):
        oka = int(input())
        okashi[oka] += 1
    else:
        oka = list(map(int,input().split()))
        
        for j in oka:
            okashi[j] += 1
c = 0
for i in okashi:
    if(i==0):
        c+=1
print(c-1)