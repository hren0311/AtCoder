n, k = map(int,input().split())

A = [int(x) for x in input().split()]

ans = n
sumA = sum(A)
A_f = A[0]
A_e = A[-1]
for i in range(k):
    ans += (sumA * 2 + n)
    sumA = ans