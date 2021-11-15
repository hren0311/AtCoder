import copy
N = int(input())
num_list = list(map(int,input()))
num_list2 = []
for i in range(N):
    if(i != 0):
        if(len(num_list2)==0 or len(num_list2)==1):
            break
        num_list = copy.copy(num_list2)
        num_list2 = []
    for j in range(len(num_list)-1):
        num = num_list[j] - num_list[j+1]
        if num == 0:
            continue
            
        num_list2.append(abs(num))
        
if(len(num_list2)==0):
    print(0)
else:
    print(num_list2[0])
