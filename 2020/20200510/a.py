s = input()
t = input()
a = len(s)
b = len(t)
if((a+1)!=b):
    print('No')
else:
    if(s[0:a]==t[0:a]):
        print('Yes')
    else:
        print('No')