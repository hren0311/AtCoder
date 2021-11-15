n=int(input())

for i in range(1,15):
    x = 1000*i - n
    if(0 <= x and x < 1000):
        print(x)
        exit()