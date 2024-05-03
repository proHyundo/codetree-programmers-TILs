T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    ans = 99 * N
    arr = [
        list(map(int, input().split())) for _ in range(N)
    ]
    visited = [False] * N


    def dfs(n, sm):
        global ans
        if ans <= sm:  # 가지치기
            return

        if n == N:
            ans = min(ans, sm)
            return
        for j in range(N):
            if not visited[j]:
                visited[j] = True
                dfs(n+1, sm+arr[n][j])
                visited[j] = False


    dfs(0, 0)
    print(f'#{test_case}', ans)

