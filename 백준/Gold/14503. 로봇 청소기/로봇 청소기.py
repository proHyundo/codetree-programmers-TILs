
def solve():
    N, M = map(int, input().split())
    cx, cy, _dir = map(int, input().split())  # 현재 좌표 (R, C) 방향 D (0, 1, 2, 3) (북, 동, 남, 서)
    board = [list(map(int, input().split())) for _ in range(N)]  # 0 청소 안됨, 1 벽
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]
    cnt = 0

    while True:
        if board[cx][cy] == 0:  # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
            board[cx][cy] = 2
            cnt += 1
            # print(cx, cy)

        flag = False
        for dx, dy in zip(dxs, dys):  # 현재 칸의 주변 4칸 빈칸 탐색
            nx, ny = cx + dx, cy + dy
            if board[nx][ny] == 0:
                flag = True
                break

        if flag:  # 빈 칸이 있는 경우, 반시계 방향으로 회전
            for i in range(-1, -5, -1):
                n_dir = (_dir + i + 4) % 4
                nx, ny = cx + dxs[n_dir], cy + dys[n_dir]
                if board[nx][ny] == 0:  # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
                    cx, cy, _dir = nx, ny, n_dir
                    break
        else:  # 빈 칸이 없는 경우
            temp_dir = (_dir + 2) % 4
            nx, ny = cx + dxs[temp_dir], cy + dys[temp_dir]
            if board[nx][ny] != 1:  # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
                cx, cy = nx, ny
            else:
                # for i, r in enumerate(board):
                #     print(i, '>', *r)
                return cnt

    return cnt


print(solve())

