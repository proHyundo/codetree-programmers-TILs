from collections import deque
import sys

N, M, K, X = map(int, input().split())
graph = [
    [] for _ in range(N + 1)
]

# 도로 입력
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)

distances = [-1] * (N+1)
que = deque([X])
distances[X] = 0

while que:
    now = que.popleft()
    for next_node in graph[now]:
        if distances[next_node] == -1:
            que.append(next_node)
            distances[next_node] = distances[now] + 1


valid = False
for index, d in enumerate(distances):
    if d == K:
        print(index)
        valid = True
if valid is False:
    print(-1)