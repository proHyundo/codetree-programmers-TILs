from collections import deque

N, M = map(int, input().split())
board = [
    list(map(int, input())) for _ in range(N)
]
v = [
    [0] * M for _ in range(N)
]


def bfs(si, sj, ei, ej):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        if ci == ei and cj == ej:
            return v[ci][cj]

        for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            nx, ny = ci + dx, cj + dy
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1 and v[nx][ny] == 0:
                q.append((nx, ny))
                v[nx][ny] = v[ci][cj] + 1

    return 0


print(bfs(0, 0, N - 1, M - 1))
