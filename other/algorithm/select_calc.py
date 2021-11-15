def choose(n,k):
    x,y = 1,1
    if(n//2 < k):
        k = n - k
    for i in range(1,k+1):
        x *= (n-i+1)
        y *= i
      
    return x//y

#ただしmodは素数
def choose_mod(n,k,mod):
    x,y = 1,1
    if(n//2 < k):
        k = n - k
    for i in range(1,k+1):
        x *= (n-i+1)
        x %= mod
        y *= i
        y %= mod
    
    x *= pow(y,mod-2,mod)
    x %= mod
    return x

print(choose(8,2))
print(choose(8,6))

print(choose_mod(8,2,10**9+7))
print(choose_mod(8,6,10**9+7))
print(choose_mod(10**9,8,10**9+7))