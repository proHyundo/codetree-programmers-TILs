from collections import deque

N, L, R = map(int, input().split())  # 차가 L 이상 R 이하
arr = [list(map(int, input().split())) for _ in range(N)]


def bfs(si, sj, v):
    sm = 0
    cnt = 0
    targets = []
    q = deque()
    q.append((si, sj))
    v[si][sj] = True

    while q:
        ci, cj = q.popleft()
        targets.append((ci, cj))
        sm += arr[ci][cj]
        cnt += 1

        for di, dj in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and not v[ni][nj] and L <= abs(arr[ci][cj] - arr[ni][nj]) <= R:
                v[ni][nj] = True
                q.append((ni, nj))

    if cnt == 1:
        return False
    else:
        value = sm // cnt
        for i, j in targets:
            arr[i][j] = value
        return True


def sol():
    ans = 0
    while True:
        visited = [
            [False] * N for _ in range(N)
        ]
        find_flag = False
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    if bfs(i, j, visited):
                        find_flag = True

        if find_flag:
            ans += 1
            continue

        return ans


print(sol())
