# 문제 이름: [문제 이름 삽입]
# 해결 날짜: [YY-MM-DD 형식으로 날짜 삽입]
# 소요 시간: [문제를 해결하는데 걸린 시간 삽입, 예: 45분]
# 시간 복잡도: [해결책의 시간 복잡도 삽입, 예: O(n), O(n^2) 등]
# 난이도: [난이도 수준 삽입, 예: 상, 중, 하]
# 문제 URL: [해당되는 경우 문제의 URL 삽입]
# 해결 접근 방식: [문제 해결에 접근한 방식을 간략히 설명. 여기에는 사용된 알고리즘, 데이터 구조 및 주목할 만한 최적화가 포함될 수 있음.]
# 코멘트: [문제나 해결책과 관련된 추가 코멘트나 비고 사항.]
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


