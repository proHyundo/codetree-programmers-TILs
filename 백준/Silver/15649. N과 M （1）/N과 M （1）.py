N, M = map(int, input().split())
ans = []
visited = [False] * (N+1)


def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return
    for num in range(1, N+1):
        if not visited[num]:
            visited[num] = True
            dfs(n+1, lst+[num])
            visited[num] = False


dfs(0, [])
for ele in ans:
    print(*ele)
