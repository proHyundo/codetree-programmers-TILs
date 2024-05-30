from collections import deque
import sys

N, K = map(int, input().split())
coordinate = [0] * 100001
ans = sys.maxsize


def bfs():
    q = deque()
    q.append(N)

    while q:
        cur = q.popleft()

        if cur == K:
            return coordinate[K]

        for nx in (cur-1, cur+1, cur*2):
            if 0 <= nx <= 100000 and coordinate[nx] == 0:
                coordinate[nx] = coordinate[cur] + 1
                q.append(nx)

print(bfs())
