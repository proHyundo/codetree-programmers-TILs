# 2 : 1, 3
# 4 : 3, 5
# 6 : 5, 7
# 9 : 8
# 10 : 11
# 12 : 11
# ---
# 2 : 1, 3
# 4 : 3, 5
# 6 : 5, 7, 8
# 9 : 7, 8, 9
# 10 : 8, 11
# 12 : 11

N, K = map(int, input().split())
HP_lst = list(input())
answer = 0

for i, target in enumerate(HP_lst):
    if target == 'P':
        start = max(0, i-K)
        end = min(N, i+K+1)
        for j in range(start, end):
            if HP_lst[j] == 'H':
                answer += 1
                HP_lst[j] = 'D'
                break

print(answer)
