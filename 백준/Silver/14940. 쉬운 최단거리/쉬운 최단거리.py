from collections import deque

N, M = map(int, input().split())

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

board = [
    list(map(int, input().split())) for _ in range(N)
]

q = deque()
answer = [
    [-1] * M for _ in range(N)
]
visited = [
    [False] * M for _ in range(N)
]


for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            q.append((i, j))
            visited[i][j] = True
            answer[i][j] = 0
        elif board[i][j] == 0:
            answer[i][j] = 0


while q:
    i, j = q.popleft()

    for dx, dy in zip(dxs, dys):
        nx, ny = dx + i, dy + j
        if 0 <= nx < N and 0 <= ny < M and board[i][j] != 0 and not visited[nx][ny] and board[nx][ny] == 1:
            visited[nx][ny] = True
            answer[nx][ny] = answer[i][j] + 1
            q.append((nx, ny))

for row in answer:
    print(*row, sep=' ')