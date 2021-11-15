x,y = map(int,input().split())

a = (y-2*x) 

if(a >= 0):
    if(a%2==0):
        if((x-a//2)>=0):
            print('Yes')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')