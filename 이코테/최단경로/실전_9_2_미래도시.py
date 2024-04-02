# 문제 이름: 미래 도시
# 해결 날짜: 240402
# 소요 시간: 35분
# 시간 복잡도: [해결책의 시간 복잡도 삽입, 예: O(n), O(n^2) 등]
# 난이도: 중
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: [문제 해결에 접근한 방식을 간략히 설명. 여기에는 사용된 알고리즘, 데이터 구조 및 주목할 만한 최적화가 포함될 수 있음.]
# 코멘트: [문제나 해결책과 관련된 추가 코멘트나 비고 사항.]
import heapq
import sys

# 반복해서 입력을 받아야 하는 경우 sys.stdin.readline 사용이 input() 보다 더 빠름
input = sys.stdin.readline

# N : 노드 개수, M : 간선 개수
N, M = map(int, input().split())

# 인접 리스트로 그래프 표현
graph = [
    [] for i in range(N+1)
]
distance = [sys.maxsize] * (N+1)

# 양방향 간선이라 v1, v2 모두 저장
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append((v2, 1))
    graph[v2].append((v1, 1))

X, K = map(int, input().split())
ans = -1


def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start)) # start 노드는 자기 자신이라 이동비용 0
    distance[start] = 0
    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))


# 1번 노드에서 K번 노드까지 최단 거리
dijkstra(1)
ans = distance[K] if distance[K] != sys.maxsize else -1

# K번 노드에서 X번 노드까지 최단 거리
distance = [sys.maxsize] * (N+1)
dijkstra(K)
ans = ans + distance[X] if distance[X] != sys.maxsize else -1

print(ans)
