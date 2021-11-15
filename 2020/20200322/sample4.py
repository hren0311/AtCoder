import collections

N = int(input())
num_list = list(map(int,input().split()))
memo = [0]*(N+1)
memo_flg = [False]*(N+1)
counter = [0] * (N+1)
counter_ans = [0] * (N+1)

for i in num_list:
    counter[i] += 1
for i in range(N+1):
    counter_ans[i] = (counter[i]*(counter[i]-1))//2

all_sum = sum(counter_ans)
def calc(k):
    num = num_list[k]
    
    if(memo_flg[num] is True):
        return memo[num]
    ans = 0
    
    wrong = counter_ans[num]
    c = counter[num]-1
    right = (c*(c-1))//2
    
    ans = all_sum - wrong + right
    memo[num] = ans
    memo_flg[num] = True
    return ans

[print(calc(i)) for i in range(N)]
