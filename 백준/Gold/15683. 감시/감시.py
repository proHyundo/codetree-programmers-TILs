N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cctv = []

# 주어진 arr 에서 cctv 유형 및 좌표를 cctv 리스트에 저장
for i in range(N):
    for j in range(M):
        if arr[i][j] in (1, 2, 3, 4, 5):
            cctv.append((arr[i][j], i, j))

cctv_len = len(cctv)
ans = N * M

dxys = {
    1: [[(0, 1)], [(1, 0)], [(0, -1)], [(-1, 0)]],
    2: [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
    3: [[(0, 1), (-1, 0)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
    4: [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],
    5: [[(0, -1), (-1, 0), (0, 1), (1, 0)]]
}


def calculate(tdirection):  # cctv 정보와 방향정보
    v = [
        [False] * M for _ in range(N)
    ]
    for index, tcctv in enumerate(cctv):  # 각 cctv 마다 순회
        c_type, sx, sy = tcctv
        d_num = tdirection[index]  # 특정 cctv가 선택한 방향 번호

        for dx, dy in dxys[c_type][d_num]:
            cx, cy = sx, sy
            while True:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 6:
                    v[nx][ny] = True
                    cx, cy = nx, ny
                else:
                    break

    cnt = 0
    for i in range(N):
        for j in range(M):
            if not v[i][j] and arr[i][j] == 0:
                cnt += 1

    return cnt


def dfs(n, directions):
    global ans
    if n == cctv_len:
        ans = min(ans, calculate(directions))
        return

    # cctv의 방향 결정
    d, x, y = cctv[n]
    if d in (1, 3, 4):
        for i in range(4):
            dfs(n+1, directions+[i])
    elif d == 2:
        for i in range(2):
            dfs(n+1, directions+[i])
    else:
        dfs(n+1, directions+[0])


dfs(0, [])
print(ans)
