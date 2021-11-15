H,W = map(int,input().split())
table =[[0] for i in range(H)]
for i in range(H):
    table[i] = list(input())


def search(x,y):
    min_num = 100000
    if(table[x][y]=='.'):
        num = 0
    else:
        num = 1
    if(x!=(H-1)):
        return search(x+1,y) + num
    if(y!=(W-1)):
        return search(x,y+1) + num
    

    return 

    
