n = int(input())
h_l = list(map(int,input().split()))
cnt = 0
for i in range(n):
    h_i = h_l[i]
    for j in range(i,n):
        if((j-i)==(h_l[j]+h_i)):
            cnt += 1

print(cnt)