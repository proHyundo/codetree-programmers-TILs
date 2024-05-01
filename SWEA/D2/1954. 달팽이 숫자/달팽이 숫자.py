T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ans = [
        [0] * N for _ in range(N)
    ]
    
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
    
    
    def dfs(num, x, y, dir):
        if num > N ** 2:
            return
        ans[x][y] = num
        for i in range(4):
            ndir = (dir + i) % 4
            nx, ny = x+dxs[ndir], y+dys[ndir]
            if 0 <= nx < N and 0 <= ny < N and ans[nx][ny] == 0:
                dfs(num+1, nx, ny, ndir)
                return
    
    dfs(1, 0, 0, 0)

    print(f'#{test_case}')
    for row in ans:
        print(*row)
