N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

ans = []


def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return

    for i in range(N):
        dfs(n+1, lst + [nums[i]])


dfs(0, [])
for ele in ans:
    print(*ele)
