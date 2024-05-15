from collections import deque

for _ in range(10):
    test_case = int(input())
    board = [
        list(map(int, input())) for _ in range(16)
    ]
    visited = [[0] * 16 for _ in range(16)]


    def find_start():
        for i in range(16):
            for j in range(16):
                if board[i][j] == 2:
                    return (i, j)
        return (-1, -1)


    si, sj = find_start()


    def bfs(si, sj):
        q = deque()
        q.append((si, sj))
        visited[si][sj] = 1

        while q:
            ci, cj = q.popleft()

            if board[ci][cj] == 3:
                return visited[ci][cj] - 1

            for dx, dy in zip([0,1,0,-1], [1,0,-1,0]):
                ni, nj = ci + dx, cj + dy
                if 0 <= ni < 16 and 0 <= nj < 16 and visited[ni][nj] == 0 and board[ni][nj] != 1:
                    visited[ni][nj] = visited[ci][cj] + 1
                    q.append((ni, nj))

        return 0

    print(f'#{test_case}', 1 if bfs(si, sj) != 0 else 0)


