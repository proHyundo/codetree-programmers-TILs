R, C, N = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

def simulate_bomb_explosion(current_board):
    temp_board = [['O'] * C for _ in range(R)]
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    for i in range(R):
        for j in range(C):
            if current_board[i][j] == 'O':
                temp_board[i][j] = '.'
                for dx, dy in zip(dxs, dys):
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < R and 0 <= ny < C:
                        temp_board[nx][ny] = '.'

    return temp_board

if N == 1:
    # 초기 상태 출력
    for row in board:
        print(*row, sep='')
elif N % 2 == 0:
    # N이 짝수일 경우 격자판은 폭탄으로 가득 참
    for _ in range(R):
        print('O' * C)
else:
    # N이 홀수일 경우, 두 단계의 폭발 상태를 계산
    first_explosion = simulate_bomb_explosion(board)
    second_explosion = simulate_bomb_explosion(first_explosion)

    if N % 4 == 3:
        # N % 4 == 3인 경우 첫 번째 폭발 상태 출력
        result = first_explosion
    else:
        # N % 4 == 1인 경우 두 번째 폭발 상태 출력
        result = second_explosion

    for row in result:
        print(*row, sep='')