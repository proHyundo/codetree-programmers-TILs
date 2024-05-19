n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 0

for i in range(n-1):
    for j in range(m-1):
        area = [board[i][j], board[i][j+1], board[i+1][j], board[i+1][j+1]]
        area.sort()
        answer = max(answer, sum(area[1:]))


for i in range(n-2):
    for j in range(m):
        answer = max(answer, board[i][j] + board[i+1][j] + board[i+2][j])

for i in range(n):
    for j in range(m-2):
        answer = max(answer, board[i][j] + board[i][j+1] + board[i][j+2])

print(answer)