from collections import deque

N = int(input())
board = [
    list(map(int, input().split())) for _ in range(N)
]
visited = [
    [False] * N for _ in range(N)
]


def bfs(cij, num):
    q = deque()
    q.append(cij)
    while q:
        ci, cj = q.popleft()
        for di, dj in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 1 and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = True
                board[ni][nj] = num


group_num = 2
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            board[i][j] = group_num
            bfs((i, j), group_num)
            group_num += 1

visited = [
    [0] * N for _ in range(N)
]
answer = 99999


def get_min_bfs(cij, target):
    q = deque()
    q.append(cij)
    while q:
        ci, cj = q.popleft()
        if board[ci][cj] != 0 and board[ci][cj] != target:
            return_val = visited[ci][cj] - 1
            visited[ci][cj] = 0
            return return_val
        for di, dj in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] != target:
                if visited[ni][nj] == 0 or visited[ci][cj] + 1 < visited[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[ci][cj] + 1

    return 99999


for i in range(N):
    for j in range(N):
        if board[i][j] != 0 and visited[i][j] == 0:
            answer = min(answer, get_min_bfs((i, j), board[i][j]))


print(answer)
