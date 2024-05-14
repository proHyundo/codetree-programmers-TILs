"""
5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리
"""
from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [
        [] for _ in range(V + 1)
    ]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    S, G = map(int, input().split())


    def dfs(s, e):
        # (1) q, visited 생성
        q = deque()
        visited = [0] * (V+1)

        # (2) q 초기데이터 삽입, visited 표시
        q.append(s)
        visited[s] = 1

        while q:
            current = q.popleft()
            if current == e:
                return visited[e] - 1

            for nx in adj[current]:  # 연결된 노드들
                if visited[nx] == 0:  # 미방문 노드인 경우
                    q.append(nx)
                    visited[nx] = visited[current] + 1  # 방문할 노드까지의 거리는 현재 노드에서 + 1

        return 0

    print(f'#{test_case}', dfs(S, G))
