a,b,c,k = map(int,input().split())
if((a+b)>=k):
    if(a>=k):
        print(k)
    else:
        print(a)
else:
    s = k - a - b
    print(a+s*-1)