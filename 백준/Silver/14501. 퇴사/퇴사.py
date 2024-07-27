N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0
def dfs(n, t_sm, p_sm):
    global ans

    if n >= N:
        if t_sm <= N:
            ans = max(ans, p_sm)
        return

    t, p = lst[n]
    if n + t <= N:
        dfs(n+t, t_sm + t, p_sm + p)
    dfs(n+1, t_sm, p_sm)

dfs(0, 0, 0)
print(ans)