# 문제 이름: 음료수얼려먹기
# 해결 날짜: 240327
# 소요 시간: 30m
# 시간 복잡도: O(n^3)
# 난이도: 하
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: 방문처리를 위해 checked 리스트를 생성했지만, 불필요함을 알게 되었음.
# 코멘트: 답안은 DFS 기법을 사용했지만, 나의 풀이는 BFS 기법 사용. 모든 정점을 탐색해야하기 때문에 어떤걸 사용해도 무방하지만, 교재에서
# BFS 기법이 일반적으로 더 빠르다 해서 BFS를 선택함. 그러나 구현 난이도는 DFS가 더 쉬운거 같음.

from collections import deque

n, m = map(int, input().split())

_board = [
    list(map(int, input())) for _ in range(n)
]
_checked = [
    [False] * m for _ in range(n)
]
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
ans = 0


def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False


def bfs(board, x, y):
    global _checked
    # 범위 내 & 방문한 적 없음 & 칸막이 아님
    if in_range(x, y) and _checked[x][y] == False and board[x][y] == 0:
        queue = deque([(x, y)])
        _checked[x][y] = True

        while queue:
            cx, cy = queue.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = cx + dx, cy + dy
                if in_range(nx, ny) and _checked[nx][ny] == False and board[nx][ny] == 0:
                    queue.append((nx, ny))
                    _checked[nx][ny] = True
        return True
    else:
        return False


for i in range(n):
    for j in range(m):
        if bfs(_board, i, j):
            ans += 1

print(ans)
