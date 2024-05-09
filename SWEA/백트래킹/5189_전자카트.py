"""
파이썬 SW문제해결 응용_구현 - 02 완전 검색
5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트 D3
"""
T = int(input())
for test_case in range(1, T+1):

    N = int(input())
    board = [
        list(map(int, input().split())) for _ in range(N)
    ]
    visited = [False] * (N+1)
    ans = 99999


    def dfs(n, sm, last):
        global ans
        if sm >= ans:
            return

        if n == N-1:
            ans = min(ans, sm + board[last-1][0])
            return

        for i in range(2, N+1):
            if not visited[i]:
                visited[i] = True
                dfs(n+1, sm + board[last-1][i-1], i)
                visited[i] = False


    dfs(0, 0, 1)
    print(f'#{test_case}', ans)
