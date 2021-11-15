N, M, V ,P = map(int,input().split())
score = list(map(int,input().split()))
score.sort(reverse=True)
score_candidate = score[P:]

count = P
if V > (N-P):
    score_num = score[N-V-1]
    for num in score_candidate:
        if score_num <= num + M:
            count += 1
else:
    score_num = score[P-1] 
    for num in score_candidate:
        if score_num <= num + M:
            count += 1

print(count)