x = int(input())
sign = ((1,1),(1,-1),(-1,1),(-1,-1))
isloop=True
for a in range(10**3):
    if(isloop==False):
        break
    for b in range(10**3):
        if(isloop==False):
            break
        for s1,s2 in sign:
            if(isloop==False):
                break
            a1 = s1*a
            b1 = s2*b
            if((a1**5)==(x+b1**5)):
                print(a1,b1)
                isloop=False
                break
            
        