N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0


def dfs(n, p_sm):
    global ans
    if n > N:
        return
    if n == N:
        ans = max(ans, p_sm)
        return

    # 하부 함수 호출, 선택하는 경우와 안하는 경우. 선택하기 위해서는 N을 초과해서는 안됨.
    t, p = lst[n]
    if n + t <= N:
        dfs(n + t, p_sm + p)
    dfs(n + 1, p_sm)


dfs(0, 0)
print(ans)
