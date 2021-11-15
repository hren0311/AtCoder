n = int(input())
x = 100

for i in range(1,1000000):
    x = x + x//100
    if(x >= n):
        print(i)
        break