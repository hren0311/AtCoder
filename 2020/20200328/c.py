k,n = map(int,input().split())
mp = [int(x) for x in input().split()]
a = []
for i in range(n):
    if(i==(n-1)):
        last = k - mp[i] + mp[0]
        a.append(last)
        break
    a.append(mp[i+1] - mp[i])

ml = max(a)
print(sum(a)-ml)