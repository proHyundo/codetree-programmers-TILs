# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2

import heapq
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
start = int(input())
graph = [
    [] for _ in range(N+1)
]

for _ in range(M):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((v2, cost))

distance = [sys.maxsize] * (N+1)


def dijkstra(node):
    q = []
    heapq.heappush(q, (0, node))
    distance[node] = 0
    while q:
        dist, current_node = heapq.heappop(q)
        print('distance :', distance, '\t dist:', dist, '\t current_node :', current_node)
        if distance[current_node] < dist:
            print('pass: distance[current_node]>', distance[current_node], 'dist>', dist)
            continue
        for v in graph[current_node]:
            move_cost = dist + v[1]  # v를 통과할 경우 비용
            if move_cost < distance[v[0]]:  # v에 이미 존재한 기존 비용
                distance[v[0]] = move_cost
                heapq.heappush(q, (move_cost, v[0]))

dijkstra(start)

print(distance)
