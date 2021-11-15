n = int(input())

l = [int(x) for x in input().split()]
mp = [1]*n


for i in range(n):
    for j in range(i+1,n):
        if(mp[j]==0):
            continue
        if(l[j]==l[i]):
            mp[i] = 0
            mp[j] = 0
            continue
        if(l[j]%l[i]==0):
            mp[j] = 0
            continue

print(sum(mp))