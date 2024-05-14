"""
5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리
"""
import collections
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [
        list(map(int, input())) for _ in range(N)
    ]

    _start = _end = (-1, -1)
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                _start = (i, j)
            if board[i][j] == 3:
                _end = (i, j)

    def dfs(s, e):
        q = collections.deque()
        visited = [
            [0] * N for _ in range(N)
        ]
        q.append(s)
        visited[s[0]][s[1]] = 1

        while q:
            current = q.popleft()

            if current == e:
                return visited[current[0]][current[1]] - 2

            for dx, dy in zip([0,1,0,-1], [1,0,-1,0]):
                nx, ny = current[0] + dx, current[1] + dy
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and board[nx][ny] != 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[current[0]][current[1]] + 1

        return 0

    print(f'#{test_case}', dfs(_start, _end))