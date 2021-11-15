move = ((0,1),(1,0),(-1,0),(0,-1))
def search():
    global mapl
    global searched
    mapl = [[int(x) for x in input().split()] for j in range(h)]
    searched = [[False for i in range(w)] for j in range(h)]
    cnt=0
    for y in range(h):
        for x in range(w):
            if(searched[y][x] or mapl[y][x]==0):
                continue
            cnt+=1
            bfs(y,x,h,w)
    return cnt

def bfs(y,x,h,w):
    s_queue = [[y,x]]
    while(len(s_queue)>0):
        y,x = s_queue.pop()
        for a,b in move:
            ny = y + a
            nx = x + b
            if(ny<0 or ny>=h or nx<0 or nx>=w or mapl[ny][nx]==0):
                continue
            if(searched[ny][nx]):
                continue
            s_queue.append([ny,nx])
            searched[ny][nx] = True

while True:
    w,h = map(int,input().split())
    if(w==0 and h==0):
        break
    print(search())
    

