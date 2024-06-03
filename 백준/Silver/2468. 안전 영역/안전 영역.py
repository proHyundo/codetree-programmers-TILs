from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 1
rain_max = max(map(max, board))


def bfs(x, y):
    q = deque()
    q.append((x, y))
    v[x][y] = True
    r = 0
    while q:
        ci, cj = q.popleft()
        r += 1

        for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            nx, ny = ci + dx, cj + dy
            if 0 <= nx < N and 0 <= ny < N and not v[nx][ny] and board[nx][ny] > h:
                v[nx][ny] = True
                q.append((nx, ny))

    return r


for h in range(1, rain_max + 1):
    v = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not v[i][j] and board[i][j] > h:
                bfs(i, j)
                cnt += 1
    ans = max(ans, cnt)

print(ans)
