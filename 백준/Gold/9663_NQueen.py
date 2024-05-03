N = int(input())
visited = [
    [False] * N for _ in range(N)
]
ans = 0
dxs = [-1, 1, -1, 1]
dys = [1, 1, -1, -1]


def possible(x, y):
    # 가로, 세로 확인
    for i in range(N):
        if visited[x][i] or visited[i][y]:
            return False
    # 대각선
    for dx, dy in zip(dxs, dys):
        temp_x, temp_y = x, y
        while True:
            nx, ny = temp_x + dx, temp_y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny]:
                    return False
            else:
                break
            temp_x, temp_y = nx, ny
    return True


def dfs(n):
    global ans
    if n == N:
        print('ans', ans)
        ans += 1
        return
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and possible(i, j):
                print(i, j)
                visited[i][j] = True
                dfs(n+1)
                print(i, j, 'back')
                visited[i][j] = False


dfs(0)
print(ans)
