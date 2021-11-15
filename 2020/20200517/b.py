k = int(input())
s = input()
ls = len(s)
if(ls <= k):
    print(s)
else:
    print(s[:k]+'...')
