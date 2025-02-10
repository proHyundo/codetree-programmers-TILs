from collections import deque

N, M = map(int, input().split())

# visited[100] 의 값이 정답. 이동횟수 저장
visited = [0] * 101
# board 이동 좌표 안내
board = [i for i in range(101)]
# 사다리, 뱀 세팅
for _ in range(N+M):
    a, b = map(int, input().split())
    board[a] = b

def bfs(v):
    q = deque([v])
    visited[v] = 1

    while q:
        current = q.popleft()
        for i in range(1, 7):
            nxt = current + i   # 주사위로 이동할 좌표

            if nxt > 100:   # 100 넘으면 이동 불가
                continue

            moved_index = board[nxt]    # 이동한 좌표

            if visited[moved_index] == 0:   # 첫 방문
                q.append(moved_index)
                visited[moved_index] = visited[current] + 1

                if moved_index == 100:
                    return

bfs(1)  # 1에서 시작
print(visited[100] - 1)