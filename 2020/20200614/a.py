l = list(map(int,input().split()))

for i in range(1,6):
    if l[i-1]==0:
        print(i)
        exit()