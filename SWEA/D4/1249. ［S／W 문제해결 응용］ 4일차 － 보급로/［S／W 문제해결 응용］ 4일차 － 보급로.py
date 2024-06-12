from collections import deque

T = int(input())


def bfs():
    q = deque()
    q.append((0, 0))
    v[0][0] = 0

    while q:
        ci, cj = q.popleft()

        for di, dj in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] > v[ci][cj] + board[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + board[ni][nj]

    return v[N - 1][N - 1]


for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    v = [
        [99999] * N for _ in range(N)
    ]
    print(f'#{test_case}', bfs())
