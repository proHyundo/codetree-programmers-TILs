# 문제 이름: 미래도시 - 플로이드워셜 풀이
# 해결 날짜: [YY-MM-DD 형식으로 날짜 삽입]
# 소요 시간: [문제를 해결하는데 걸린 시간 삽입, 예: 45분]
# 시간 복잡도: [해결책의 시간 복잡도 삽입, 예: O(n), O(n^2) 등]
# 난이도: [난이도 수준 삽입, 예: 상, 중, 하]
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: [문제 해결에 접근한 방식을 간략히 설명. 여기에는 사용된 알고리즘, 데이터 구조 및 주목할 만한 최적화가 포함될 수 있음.]
# 코멘트: [문제나 해결책과 관련된 추가 코멘트나 비고 사항.]

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [
    [sys.maxsize] * N for _ in range(N)
]

for i in range(N):
    for j in range(N):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    v1, v2 = map(int, input().split())
    v1, v2 = v1-1, v2-1
    graph[v1][v2] = 1
    graph[v2][v1] = 1

X, K = map(int, input().split())

for k in range(N):
    for s in range(N):
        for e in range(N):
            graph[s][e] = min(graph[s][e], graph[s][k] + graph[k][e])

print(graph)
print(graph[0][K-1] + graph[K-1][X-1])