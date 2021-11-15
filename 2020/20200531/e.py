n = int(input())

l = [list(map(int,input().split())) for i in range(n)]
l.sort(key=lambda x: x[0])
if(n%2==0):
    i = n//2 - 1
    min1 = l[i][0]
    min2 = l[i+1][0]
    l.sort(key=lambda x: x[1])
    max1 = l[i][1]
    max2 = l[i+1][1]
    s1 = max1 - min1 + 1
    
    s2 = max2 - min2 + 1
    if((max1-max2) > 0):
        amari = max1 - max2
    ans = (s1*s2)//2
    print(ans)
else:
    i = (n+1)//2-1
    min1 = l[i][0]
    l.sort(key=lambda x: x[1])
    max1 = l[i][1]
    s = max1 - min1 + 1

    print(s)


