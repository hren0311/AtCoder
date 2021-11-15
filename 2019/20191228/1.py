N, A, B = map(int,input().split())

if (B-A) % 2 == 0:
    ans = (B-A) // 2
else:
    if (A-1) < (N-B):
        count = A
        a = 1
        b = B - count
        count += (b-a)//2
    else:
        count = (N-B) + 1
        a = A + count
        b = N
        count += (b-a)//2
    ans = count

print(ans)
        