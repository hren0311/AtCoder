h,w,k = map(int,input().split())

mp = [input() for i in range(h)]

mp_h = []
for i in range(h):
    cnt = 0
    for j in range(w):
        if(mp[i][j]=="#"):
            cnt+=1
    mp_h.append(cnt)

mp_w=[]
for i in range(w):
    cnt = 0
    for j in range(h):
        if(mp[j][i]=="#"):
            cnt+=1
    mp_w.append(cnt)

sum_all = sum(mp_w)

sub_sum = sum_all - k
if(sub_sum < 0):
    print(0)
    exit()


from itertools import combinations

lw = range(w)
lh = range(h)
l_w = [[x for x in combinations(lw,i)] for i in range(0,w+1)]   
l_h = [[x for x in combinations(lh,i)] for i in range(0,h+1)]

def check(t_w,t_h):
    
    t_sum = 0
    cnt = 0
    for x in t_w:
        t_sum += mp_w[x]
    for y in t_h:
        t_sum += mp_h[y]
    
    for x in t_w:
        for y in t_h:
            if(mp[y][x]=="#"):
                cnt += 1
    t_sum -= cnt
    
    if((sum_all-t_sum)==k):
        return True
    return False

#i個選ぶ，j個選ぶ
ans = 0
for i in range(w+1):
    if(i==0):
        target_w = []
    else:
        target_w = l_w[i-1]
    for j in range(h+1):
        if(j==0):
            target_h = []
        else:
            target_h = l_h[j-1]
        for t_w in target_w:
            for t_h in target_h:
                if(check(t_w,t_h)):
                    ans += 1
print(ans)