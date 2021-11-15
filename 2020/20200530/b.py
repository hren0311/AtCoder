t = list(input())
ln = len(t)
pre = ""
for i in range(ln):
    if(t[i]=='?'):
        t[i] = 'D'
print(''.join(t))  