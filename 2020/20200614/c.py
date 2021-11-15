x,n = map(int,input().split())
l = [int(x) for x in input().split()]
mp = [False]*101
for i in range(n):
    mp[l[i]] = True

#xがリストになければ
if(mp[x]==False):
    print(x)
    exit()

#xより小さい整数 (x-1)から0まで
for i in range(x-1,-1,-1):
    if(i==0):
        bottom_savei = 0
        bottom_abs = abs(x) 
        break
    if(mp[i]==False):
        bottom_savei = i
        bottom_abs = abs(x-i)
        break

#xより大きい整数 (x+1)から101まで
for i in range(x+1,102):
    if(i==101):
        top_savei = 101
        top_abs = abs(101 - x)
        break
    if(mp[i]==False):
        top_savei = i
        top_abs = abs(x-i)
        break
    
if(bottom_abs <= top_abs):
    print(bottom_savei)
else:
    print(top_savei)
