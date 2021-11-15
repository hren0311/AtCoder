a,b,n = map(int,input().split())
ma = 0

if(n<b):
    ma = (a*n)//b - (a* (n//b))
else:
    ma = (a*(b-1))//b - (a*((b-1)//b))
    

print(ma)