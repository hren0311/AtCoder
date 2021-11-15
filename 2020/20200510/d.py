n,k = map(int,input().split())
mp = list(map(int,input().split()))
save = []
isSaved = [False]*(n+1)
s_queue = [[1,0]]
while(len(s_queue)>0):
    i,cnt = s_queue.pop()
    if(cnt==k):
        break
    if(isSaved[i]):
        last=mp[i-1]
        break
    nexti = mp[i-1]
    isSaved[i] = True
    save.append(nexti)
    s_queue.append([nexti,cnt+1])


ls = len(save)

if(k<=ls):
    print(save[k-1])
else:
    for i in range(ls):
        if(save[i]==last):
            si = i
    k -= si
    save = save[si:]
    ls = len(save)
    amari = k%ls
    print(save[amari-1])
