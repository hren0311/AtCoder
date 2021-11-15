n = int(input())
dic = {}
def f(num):
    while(num%2==0):
        num //= 2
        if(dic.get(2) is None):
            dic[2] = 1
        else:
            dic[2] += 1
    s = 3
    while((s*s) <= num):
        if((num % s)==0):
            if(dic.get(s) is None):
                dic[s] = 1
            else:
                dic[s] += 1
            num //= s
        else:
            s += 2

    
    if num != 1:
        if(dic.get(num) is None):
            dic[num] = 1
        else:
            dic[num] += 1


f(n)

l = []
for x,y in dic.items():
    cnt = 1
    if(y==1):
        l.append(x)
        continue
    while(y >= cnt):
        l.append((x**cnt))
        y -= cnt
        cnt += 1

print(len(l))
    


