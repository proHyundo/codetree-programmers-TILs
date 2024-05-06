N, M = map(int, input().split())
ans = []


def dfs(n, start, lst):
    if n == M:
        ans.append(lst)
        return

    for i in range(start, N+1):
        dfs(n+1, i, lst+[i])


dfs(0, 1, [])
for ele in ans:
    print(*ele)
