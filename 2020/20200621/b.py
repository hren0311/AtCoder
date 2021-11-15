n, k = map(int,input().split())
l = [int(x) for x in input().split()]
l.sort()

cnt = 0
for i in range(k):
    cnt += l[i]
print(cnt)