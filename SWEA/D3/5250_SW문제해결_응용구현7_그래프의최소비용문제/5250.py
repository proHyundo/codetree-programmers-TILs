from collections import deque

T = int(input())


def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        cx, cy = q.popleft()
        if (cx, cy) == (N - 1, N - 1):  # 또 다른 경로가 있을 수 있으니 continue
            continue

        for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N:  # 범위 안
                add_val = 0
                if board[nx][ny] > board[cx][cy]:  # 더 높은 높이
                    add_val = board[nx][ny] - board[cx][cy] + 1
                else:
                    add_val = 1

                if visited[nx][ny] > visited[cx][cy] + add_val:  # 최소 값으로 변경될 때 만 que 삽입
                    q.append((nx, ny))
                    visited[nx][ny] = visited[cx][cy] + add_val

    return visited[N-1][N-1] - 1


for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [
        [99999] * N for _ in range(N)
    ]
    print(f'#{test_case}', bfs())

