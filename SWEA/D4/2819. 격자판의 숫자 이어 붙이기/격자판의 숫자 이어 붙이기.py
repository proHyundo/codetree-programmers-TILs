T = int(input())
for test_case in range(1, T+1):
    board = [
        list(input().split()) for _ in range(4)
    ]
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    ans = set()


    def dfs(n, s, x, y):
        if n == 7:
            ans.add(s)  # set 자료형 이기 때문에 'if s not in ans:' 으로 검사할 필요 없음.
            return
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                dfs(n+1, s+board[nx][ny], nx, ny)


    for i in range(4):
        for j in range(4):
            dfs(1, board[i][j], i, j)  # 이미 문자 1개는 골라진 상태이다.

    print(f'#{test_case}', len(ans))