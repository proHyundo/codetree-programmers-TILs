from collections import deque

n, m = map(int, input().split())

indegree = [0] * (n + 1)            # 진입차수
adj = [[] for _ in range(n + 1)]    # 그래프를 인접리스트로 표현
for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        result.append(cur)

        for i in adj[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()
