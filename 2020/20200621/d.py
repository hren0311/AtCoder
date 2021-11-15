n = int(input())
A = [int(x) for x in input().split()]
sumA = sum(A)
counter = [0]*(10**5+1)
for i in range(n):
    counter[A[i]] += 1

q = int(input())

queue = [list(map(int,input().split())) for i in range(q)]

for b,c in queue:    
    b_cnt = counter[b]
    sumA -= (b*b_cnt)
    counter[b] = 0
    sumA += c*(b_cnt)
    counter[c] += b_cnt
    print(sumA)
    