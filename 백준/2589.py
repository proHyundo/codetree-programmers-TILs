from collections import deque
N, M = map(int, input().split())
board = [
    list(input()) for _ in range(N)
]

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited = [
        [0] * M for _ in range(N)
    ]
    visited[sx][sy] = 1
    cnt = 0

    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 'L' and visited[nx][ny] == 0:  # 방문하지 않았다면 더 탐색
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx, ny))
                cnt = max(cnt, visited[nx][ny])

    return cnt - 1

ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            ans = max(ans, bfs(i, j))


print(ans)