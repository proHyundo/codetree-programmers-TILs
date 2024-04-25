import copy
import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
board = [
    list(map(int, input().split())) for _ in range(n)
]

candidates = []
max_safe_cnt = 0
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            candidates.append((i, j))


def dfs(x, y):
    global temp_board
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and temp_board[nx][ny] == 0:
            temp_board[nx][ny] = 2
            dfs(nx, ny)


def get_safe_cnt(tb):
    cnt = 0
    for row in tb:
        cnt += row.count(0)
    return cnt


for selected in list(combinations(candidates, 3)):
    temp_board = copy.deepcopy(board)
    for x, y in selected:
        temp_board[x][y] = 1

    for i in range(n):
        for j in range(m):
            if temp_board[i][j] == 2:
                dfs(i, j)

    max_safe_cnt = max(max_safe_cnt, get_safe_cnt(temp_board))

print(max_safe_cnt)