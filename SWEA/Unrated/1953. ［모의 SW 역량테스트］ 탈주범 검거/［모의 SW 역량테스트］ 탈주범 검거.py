from collections import deque

structure = {
    1: ((0, 1), (1, 0), (-1, 0), (0, -1)),
    2: ((1, 0), (-1, 0)),
    3: ((0, 1), (0, -1)),
    4: ((0, 1), (-1, 0)),
    5: ((1, 0), (0, 1)),
    6: ((1, 0), (0, -1)),
    7: ((0, -1), (-1, 0))
}


def bfs(si, sj, time_limit):
    v = [
        [0] * M for _ in range(N)
    ]
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()

        #  가능한 방향 순회
        for dx, dy in structure[arr[ci][cj]]:
            nx, ny = ci + dx, cj + dy
            if 0 <= nx < N and 0 <= ny < M and v[nx][ny] == 0 and arr[nx][ny] != 0:
                for mx, my in structure[arr[nx][ny]]:
                    bx, by = nx + mx, ny + my
                    if bx == ci and by == cj:
                        q.append((nx, ny))
                        v[nx][ny] = v[ci][cj] + 1
                        break

    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < v[i][j] <= time_limit:
                cnt += 1
    return cnt


T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case}', bfs(R, C, L))
