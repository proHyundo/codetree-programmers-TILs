from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
time = 0


def bfs(x, y):
    q = deque()
    q.append((x, y))
    v[x][y] = True

    while q:
        ci, cj = q.popleft()
        for di, dj in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and board[ni][nj] > 0:
                v[ni][nj] = True
                q.append((ni, nj))


while True:
    melt = [[0] * M for _ in range(N)]
    # 얼음 녹이기
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if board[i][j] > 0:
                ocean = 0
                for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < M and board[nx][ny] < 1:
                        ocean += 1
                melt[i][j] = board[i][j] - ocean

    board = melt.copy()

    # 덩어리 개수 체크
    v = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if board[i][j] > 0 and not v[i][j]:
                bfs(i, j)
                cnt += 1

    if cnt == 0:  # 덩어리 0개 : 0 출력 후 종료
        print(0)
        break
    elif cnt >= 2:  # 덩어리 2개 : time 출력 후 종료
        print(time + 1)
        break
    else:  # 그 외 : 그 다음 순회
        time += 1
