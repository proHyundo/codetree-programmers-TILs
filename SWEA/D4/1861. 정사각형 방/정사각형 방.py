from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    rooms = [
        list(map(int, input().split())) for _ in range(N)
    ]
    visited = [[0] * N for _ in range(N)]


    def bfs(i, j):
        q = deque()
        q.append((i, j))

        while q:
            ci, cj = q.popleft()
            if visited[ci][cj] > 0:
                visited[i][j] += visited[ci][cj]
                return visited[i][j]

            for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
                ni, nj = ci + dx, cj + dy
                if 0 <= ni < N and 0 <= nj < N and rooms[ci][cj] + 1 == rooms[ni][nj]:
                    q.append((ni, nj))
                    visited[i][j] += 1

        return visited[i][j]


    max_val = 0
    ans = 1000000  # 방 번호
    for si in range(N):
        for sj in range(N):
            result = bfs(si, sj)
            if result != 0:
                if max_val == result:
                    ans = min(ans, rooms[si][sj])
                    max_val = result
                elif max_val < result:
                    ans = rooms[si][sj]
                    max_val = result

    print(f'#{test_case}', ans, max_val+1)
