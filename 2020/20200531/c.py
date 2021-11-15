a,b = input().split()

a = int(a)
b_str = b[0] + b[2] + b[3]

b = int(b_str)

ans = (a*b)//100
print(ans)