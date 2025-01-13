N, M, I = map(int, input().split())
board = [
    list(map(int, input().split())) for _ in range(N)
]

ix, iy = map(int, input().split())

for _ in range(M):
    a, b, c, d = map(int, input().split())
    board[a-1][b-1] = 's' # 출발
    board[c-1][d-1] = 'e' # 목적


