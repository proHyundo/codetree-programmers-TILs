from collections import deque

M, N = map(int, input().split())
board = [
    list(map(int, input().split())) for _ in range(N)
]

q = deque([])

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

ans = 0

for x in range(N):
    for y in range(M):
        if board[x][y] == 1:
            q.append([x, y])

def bfs():
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = dx + cx, dy + cy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = board[cx][cy] + 1
                q.append([nx, ny])

bfs()

for row in board:
    for v in row:
        if v == 0:
            print(-1)
            exit(0)
        else:
            ans = max(ans, v)

print(ans - 1)