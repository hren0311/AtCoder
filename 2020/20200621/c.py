s = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())

num = 0
cnt = 1
while((num+pow(26,cnt)) < n):
    num += pow(26,cnt)
    cnt += 1

n -= num
n -= 1

ans = ""
while(cnt > 0):
    a = n // pow(26,cnt-1)
    n -= (pow(26,cnt-1)*a)
    cnt -= 1
    ans = ans + s[a]
print(ans)