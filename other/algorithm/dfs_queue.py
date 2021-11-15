#最速ではない
r,c = map(int,input().split())
sy,sx = [int(x)-1 for x in input().split()] 
gy,gx = [int(x)-1 for x in input().split()] 
mapl = [list(input()) for i in range(r)]
s_queue = []
searched = [[-1 for i in range(c)] for i in range(r)]
move = ((1,0),(0,1),(-1,0),(0,-1))
def bfs():
    s_queue.append([sy,sx])
    searched[sy][sx] = 0
    while(len(s_queue)>0):
        y,x = s_queue.pop() #先入れ後だし
        
        for m in move:
            ny,nx = y+m[0],x+m[1]
            if(0>ny or ny>=r or 0>nx or nx>=c or mapl[ny][nx]=='#'):
                continue
            if([ny,nx] in s_queue):
                continue
            if(searched[ny][nx]>=0):
                continue
            searched[ny][nx] = searched[y][x] + 1
            s_queue.append([ny,nx])
            if(ny==gy and nx==gx):
                return searched[ny][nx]

print(bfs())