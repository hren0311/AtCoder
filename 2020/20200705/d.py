n = int(input())
l = list(map(int,input().split()))
l_sort = sorted(l,reverse=True)
l_len = len(l)
if(l_len%2==0):
    ans = sum(l_sort[:(l_len//2)-1])+sum(l_sort[1:(l_len//2)])+l_sort[(l_len//2)-1]
else:
    ans = sum(l_sort[:(l_len//2)])+sum(l_sort[1:(l_len//2)+1])

print(ans)
