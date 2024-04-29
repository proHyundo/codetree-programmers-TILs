from itertools import combinations
from collections import deque


# N, K = map(int, input().split())
# arr = [1,2,3,4,5,6,7,8,9,10,11,12]
# combies = list(combinations(arr, N))
# ans = 0
# for c in combies:
#     if sum(c) == K:
#         ans += 1
#
# print(ans)

def dfs(n, sm, cnt):
    global ans
    # 종료조건 : n에 관련된 수식
    if n == INDEX:
        if sm == K and cnt == CNT:
            ans += 1
        return
    dfs(n+1, sm+lst[n], cnt+1)
    dfs(n+1, sm, cnt)

CNT, K = map(int, input().split())
lst = [n for n in range(1, 13)]
INDEX = 12
ans = 0
dfs(0, 0, 0)
print(ans)
