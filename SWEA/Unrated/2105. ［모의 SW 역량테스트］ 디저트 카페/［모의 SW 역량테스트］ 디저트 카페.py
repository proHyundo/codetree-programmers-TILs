T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = [
        list(map(int, input().split())) for _ in range(N)
    ]
    cd = 0
    dxs = [1, 1, -1, -1, 1]
    dys = [1, -1, -1, 1, 1]
    ans = -1
    
    
    def dfs(n, ci, cj, _set):
        global ans
        if n > 3:  # n -> 방향 정보
            return
        if n == 3 and si == ci and sj == cj:
            ans = max(ans, len(_set))
            return
    
        for d in range(2):
            ni, nj = ci + dxs[n+d], cj + dys[n+d]
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] not in _set:
                _set.add(board[ni][nj])
                dfs(n+d, ni, nj, _set)
                _set.remove(board[ni][nj])
    
    
    for si in range(N-2):
        for sj in range(N-1):
            dfs(0, si, sj, set())
    
    print(f'#{test_case}', ans)
