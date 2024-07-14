N, M = map(int, input().split())  # 상1 하2 좌3 우4
board = [list(map(int, input().split())) for _ in range(N)]
b_cnt = [0, 0, 0, 0]
shark = (N + 1) // 2 - 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(M):
    D, S = map(int, input().split())

    # 블리자드 마법 수행 - 파괴된 것은 0으로
    for i in range(1, S + 1):
        board[dx[D-1] * i + shark][dy[D-1] * i + shark] = 0

    for row in board:
        print(*row)

    # 1차원 배열로 변환
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    dir = 0
    ci = cj = shark
    flat = [board[ci][cj]]

    for i in range(N*2 - 1):
        for _ in range(i//2+1):
            ni, nj = ci + dx[i%4], cj + dy[i%4]
            if board[ni][nj] != 0:
                flat.append(board[ni][nj])
            ci, cj = ni, nj
            print(i, ci, cj)
        dir += 1

    print('=======================')
    print(flat)
    flat_del = []

    # 순회하면서 연속 4개인 것들을 집계하고, 폭파된 것은 리스트에서 제거
    cnt = 1
    for i in range(1, len(flat)):
        if flat[i] == flat[i-1]:    # 연속되면 연속 개수 증가
            cnt += 1
        else:                       # 연속되지 않으면
            # print('같지않음', flat[i], flat[i-1], cnt)
            if cnt >= 4:            # 연속 개수가 4개 이상인 경우 압축 반영
                b_cnt[flat[i-1]] += cnt
                flat_del.append(flat[i - 1])
            else:
                for _ in range(cnt):
                    flat_del.append(flat[i - 1])
            cnt = 1
    if cnt > 1:
        b_cnt[flat[len(flat) - 1]] += cnt
        flat_del.append(flat[len(flat) - 1])

    print(flat_del)

    group_lst = []
    cnt = 1
    for i in range(1, len(flat_del)):
        if flat_del[i] == flat_del[i-1]:
            cnt += 1
        else:
            if cnt >= 2:
                group_lst.append(cnt)
                group_lst.append(flat_del[i-1])
            else:
                group_lst.append(1)
                group_lst.append(flat_del[i-1])
            cnt = 1
    if cnt > 1:
        group_lst.append(cnt)
        group_lst.append(flat_del[len(flat_del) - 1])

    print(group_lst)