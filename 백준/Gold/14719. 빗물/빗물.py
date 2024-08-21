import sys
input = sys.stdin.readline

H, W = map(int, input().split())
board = [
    [0] * W for _ in range(H)
]
for j, w in enumerate(list(map(int, input().split()))):
    for i in range(H-w, H):
        board[i][j] = 1

# for row in board:
#     print(*row)

def find_start(x):
    for y in range(0, W-1):
        if board[x][y] == 1:
            return y
    return False

def find_end(x):
    for y in range(W-1, 0, -1):
        if board[x][y] == 1:
            return y
    return False

answer = 0
for h in range(H):
    # 시작 점 찾기
    start = find_start(h)
    # 끝 점 찾기
    end = find_end(h)
    if type(start) is int and 0 < end != start:
        # print('h, start, end', h, start, end)
        # 시작 부터 끝 점 까지 순회하면서 벽이 아니면 cnt
        for j in range(start+1, end):
            if board[h][j] == 0:
                answer += 1

print(answer)