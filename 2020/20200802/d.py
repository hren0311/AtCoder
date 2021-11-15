n = int(input())

l = list(input())

begin = 0
end = n-1

cnt = 0
while(True):
    
    if(end==-1):
        break
    if(begin==n):
        break
    for i in range(begin,end+1):
        w_place = i
        if(l[w_place]=='W'):
            begin=w_place
            break
        if(i==end):
            begin=end
    for j in range(end,begin-1,-1):
        r_place = j
        if(l[r_place]=='R'):
            end=r_place
            break
        if(j==begin):
            end=begin
    if(begin>=end):
        break
    else:
        cnt += 1
        l[begin] = 'R'
        l[end] = 'W'
    begin += 1
    end -= 1

print(cnt)
