n,d = map(int,input().split())
cnt = 0
import math
for i in range(n):
    x,y = map(int,input().split())
    a = math.sqrt(x**2+y**2)
    if(a<=d):
        cnt += 1

print(cnt)