T = int(input())
for test_case in range(1, T+1):

    ans = 10000 * 20
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    def dfs(n, sm):
        global ans
        if n == N:
            if sm >= B:
                ans = min(ans, abs(B-sm))
            return

        dfs(n+1, sm+arr[n])
        dfs(n+1, sm)

    dfs(0, 0)

    print(f'#{test_case}', ans)

