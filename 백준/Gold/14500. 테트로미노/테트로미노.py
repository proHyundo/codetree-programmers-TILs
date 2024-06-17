N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
v = [[False] * M for _ in range(N)]

dictionary = {
    0: [(0, 1), (0, 2), (-1, 1)],
    1: [(0, 1), (0, 2), (1, 1)],
    2: [(1, 0), (2, 0), (1, 1)],
    3: [(1, 0), (2, 0), (1, -1)],
    4: [(0, -1), (0, -2), (1, -1)],
    5: [(0, -1), (0, -2), (-1, -1)],
    6: [(-1, 0), (-2, 0), (-1, 1)],
    7: [(-1, 0), (-2, 0), (-1, -1)]
}

def dfs(n, ci, cj, sm):
    global ans
    if sm + (1000 * (4 - n)) < ans:
        return

    if n == 4:
        ans = max(ans, sm)
        return

    for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
        nx, ny = ci + dx, cj + dy
        if 0 <= nx < N and 0 <= ny < M and not v[nx][ny]:
            v[nx][ny] = True
            dfs(n + 1, nx, ny, sm + arr[nx][ny])
            v[nx][ny] = False


def check_8(ci, cj, sm):
    global ans
    for i in range(8):
        temp = sm
        for dx, dy in dictionary[i]:
            nx, ny = ci + dx, cj + dy
            if 0 <= nx < N and 0 <= ny < M:
                temp += arr[nx][ny]
            else:
                break
        ans = max(ans, temp)


for i in range(N):
    for j in range(M):
        v[i][j] = True
        dfs(1, i, j, arr[i][j])
        v[i][j] = False
        check_8(i, j, arr[i][j])

print(ans)
