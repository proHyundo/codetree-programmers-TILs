T = int(input())
for test_case in range(1, T+1):

    N = int(input())
    p = [
        list(map(int, input().split())) for _ in range(N)
    ]
    v = [False] * N
    ans = 0

    def dfs(n, sm):
        global ans
        if ans >= sm:
            return

        if n == N:
            ans = max(ans, sm)
            return

        for i in range(N):
            if not v[i]:
                v[i] = True
                dfs(n+1, sm * (p[n][i] / 100))
                v[i] = False

    dfs(0, 100)
    print(f'#{test_case}', format(ans, '.6f'))
