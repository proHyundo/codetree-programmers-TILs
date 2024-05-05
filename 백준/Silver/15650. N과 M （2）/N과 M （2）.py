N, M = map(int, input().split())
ans = []


def dfs(n, cnt, lst):
    if n > N:
        if cnt == M:
            ans.append(lst)
        return

    dfs(n+1, cnt+1, lst + [n])
    dfs(n+1, cnt, lst)


dfs(1, 0, [])
for ele in ans:
    print(*ele)
