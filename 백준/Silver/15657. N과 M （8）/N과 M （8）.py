N, M = map(int, input().split())
nums = sorted(list(map(int, input().split()))) # 9 8 7 1
ans = []


def dfs(n, start, lst):
    if n == M:
        ans.append(lst)
        return

    for i in range(start, N):   # 0~4
        dfs(n+1, i, lst + [nums[i]])


dfs(0, 0, [])
for ele in ans:
    print(*ele)