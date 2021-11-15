n,k = map(int,input().split())

def f(a,b):
    s = a//b 
    a = a-s*b
    ans = min(a,abs(a-b))
    return ans


if(n%k==0):
    print(0)
else:
    print(f(n,k))
