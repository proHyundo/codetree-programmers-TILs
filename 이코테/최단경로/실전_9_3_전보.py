# 문제 이름: 전보
# 해결 날짜: 240403
# 소요 시간: 18분
# 시간 복잡도: [해결책의 시간 복잡도 삽입, 예: O(n), O(n^2) 등]
# 난이도: 중
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: [문제 해결에 접근한 방식을 간략히 설명. 여기에는 사용된 알고리즘, 데이터 구조 및 주목할 만한 최적화가 포함될 수 있음.]
# 코멘트: 아직 다익스트라 풀이법에 익숙해지고 있는 중
import heapq
import sys

input = sys.stdin.readline
N, M, C = map(int, input().split())
graph = [
    [] for _ in range(N+1)
]
for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

distance = [sys.maxsize] * (N+1)

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0
    while que:
        dist, current_node = heapq.heappop(que)
        if distance[current_node] < dist:
            continue
        for node in graph[current_node]:
            through_cost = dist + node[1]
            if through_cost < distance[node[0]]:
                distance[node[0]] = through_cost
                heapq.heappush(que, (through_cost, node[0]))

dijkstra(C)

print(distance)
count = 0
total = 0

for d in distance:
    if d != sys.maxsize and d != 0:
        count += 1
        total = max(total, d)

print(count, total)