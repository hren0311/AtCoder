n,m,q = map(int,input().split())
cd = 0
score_list = [list(map(int,input().split())) for i in range(q)]

def sum_d(l):
    s = 0
    
    for a,b,c,d in score_list:
        
        if (l[b-1] - l[a-1])==c:
            s += d
    return s

def f(l,ans):
    if(len(l)==n):
        return sum_d(l)

    if(len(l)==0):
        num=1
    else:
        num=l[-1]

    while(num <= m):
        ret = f(l+[num],ans)
        if(ans < ret):
            ans = ret
        num += 1

    return ans

ans = f([],ans=0)
print(ans)