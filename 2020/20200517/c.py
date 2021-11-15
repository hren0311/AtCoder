a,b,h,m = map(int,input().split())
import math
minutes = h*60+m
s1 = m/60

s2 = minutes/720

sita = s1-s2

sita *= math.pi*2

c = a**2 + b**2 - 2*a*b*math.cos(sita)
c = math.sqrt(c)
print(c)