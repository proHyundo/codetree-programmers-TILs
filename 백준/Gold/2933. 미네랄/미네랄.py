import sys
from collections import deque

R, C = map(int, input().split())
cave = [
    list(input()) for _ in range(R)
]
N = int(input())


def from_left(y):
    for i in range(C):
        if cave[y][i] == 'x':
            cave[y][i] = '.'
            return


def from_right(y):
    for i in range(C - 1, -1, -1):
        if cave[y][i] == 'x':
            cave[y][i] = '.'
            return


def find_cluster():
    q = deque()
    # 바닥 긁어서 올라가기 위함
    for i in range(C):
        if cave[R - 1][i] == 'x':
            q.append((R - 1, i))

    while q:
        cx, cy = q.popleft()
        for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < R and 0 <= ny < C and cave[nx][ny] == 'x' and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

    cluster = []
    for i in range(R - 1, -1, -1):
        for j in range(C):
            if cave[i][j] == 'x' and not visited[i][j]:
                cluster.append((i, j))

    if len(cluster) > 0:
        return cluster, True
    else:
        return cluster, False


def move(cluster):
    down_min = sys.maxsize
    for cx, cy in cluster:
        cnt = 0
        for i in range(cx + 1, R):
            if cave[i][cy] == '.':
                cnt += 1
            if cave[i][cy] == 'x' and visited[i][cy] == True:
                break
        down_min = min(down_min, cnt)
    for x, y in cluster:
        cave[x][y] = '.'
        cave[x + down_min][y] = 'x'


for index, height in enumerate(list(map(int, input().split()))):
    # 1. 파괴
    if index % 2 == 0:  # 왼쪽
        from_left(R - height)
    else:
        from_right(R - height)
    # 2. 클러스터 확인
    visited = [
        [False] * C for _ in range(R)
    ]
    clusters, is_cluster = find_cluster()
    # 3. 이동
    if is_cluster:
        move(clusters)


for row in cave:
    print(*row, sep='')