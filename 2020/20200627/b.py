s = input()
t = input()
cnt = 0
l = len(s)
for i in range(l):
    if(s[i]==t[i]):
        continue
    cnt += 1
print(cnt)