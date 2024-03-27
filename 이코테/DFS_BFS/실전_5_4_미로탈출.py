# 문제 이름: 미로탈출
# 해결 날짜: 240327
# 소요 시간: 35m
# 시간 복잡도: O(n)
# 난이도: 중
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: 최단거리를 구할 것이기 때문에 BFS 사용. 현재 좌표를 기억해야할 것이고, deque에 append 할 때 이동 횟수를 증가시키면 될 듯.
# 코멘트: BFS 구현은 잘 했으나, 최단거리를 구할 때 board에 그대로 기록하면 되는 것을 떠올리지 못함
from collections import deque

N, M = map(int, input().split())

board = [
    list(map(int, input())) for _ in range(N)
]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def possible(x, y):
    if 0 <= x < N and 0 <= y < M and board[x][y] == 1:
        return True
    return False

def bfs(x, y):
    global board
    que = deque([(x, y)])

    while que:
        cx, cy = que.popleft()
        if cx == N - 1 and cy == M - 1:
            return
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if possible(nx, ny):
                que.append((nx, ny))
                board[nx][ny] = board[cx][cy] + 1


bfs(0, 0)

print(board[N-1][M-1])


