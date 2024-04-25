# 문제 이름: [문제 이름 삽입]
# 해결 날짜: [YY-MM-DD 형식으로 날짜 삽입]
# 소요 시간: [문제를 해결하는데 걸린 시간 삽입, 예: 45분]
# 시간 복잡도: [해결책의 시간 복잡도 삽입, 예: O(n), O(n^2) 등]
# 난이도: [난이도 수준 삽입, 예: 상, 중, 하]
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: 최대 8*8 보드이니까, 64개의 요소이고, 바이러스는 최소 2개이니, 벽의 조합 개수는 62 C 3 = 22만개
# 10의 6승 미만이면 시간복잡도가 크지 않음을 알 수 있다.
# 코멘트: 해당 풀이는 효율성 검사를 통과하지 못할 것 같다.

# DFS 으로 풀어야 할 것 같음
# 재귀
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
