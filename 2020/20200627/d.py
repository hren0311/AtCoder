n,m,k = map(int,input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
Asum = [0]*(n+1)
Bsum = [0]*(m+1)

a_s = 0
for i in range(1,n+1):
    a_s += A[i-1]
    Asum[i] = a_s
b_s = 0
for i in range(1,m+1):
    b_s += B[i-1]
    Bsum[i] = b_s

t = 0
a_i=0
b_i=0
cnt = 0
while(t < k):
    
    if(a_i==(n+1) and b_i==(m+1)):
        break
    if(a_i==0 and b_i==0):
        if(Asum[a_i+1]<Bsum[b_i+1]):
            a_i += 1
        else:
            b_i += 1
    
    if(b_i==m):
        t = Asum[a_i] + Bsum[m]
        if(t > k):
            break
        a_i += 1
        cnt += 1    
        continue
    if(a_i==n):
        t = Asum[n] + Bsum[b_i]
        if(t > k):
            break
        b_i += 1
        cnt += 1 
        continue
    if(Asum[a_i]>Bsum[b_i]):
        
        t = Asum[a_i] + Bsum[b_i]
        
        if(t > k):
            break
        b_i += 1
        cnt += 1
    else:
        t = Asum[a_i] + Bsum[b_i]
        
        if(t > k):
            break
        a_i += 1
        cnt += 1


print(cnt)


    

