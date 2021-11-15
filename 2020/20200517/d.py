n,m = map(int,input().split())
mp = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    mp[a].append(b)
    mp[b].append(a)

queue = []
dist = [float('INF')]*(n+1)
pre = [-1]*(n+1)
dist[0] = 0
dist[1] = 0
queue.append(1)

while(len(queue)>0):
    now = queue.pop(0)
    for nx in mp[now]:
        if dist[nx]!= float('INF'):
            continue
        dist[nx] = dist[now] + 1
        pre[nx] = now
        queue.append(nx)
print('Yes')
for i in range(2,n+1):
    print(pre[i])
