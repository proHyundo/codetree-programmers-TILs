from collections import deque

T = int(input())


def bfs(start):
    q = deque()
    q.append(start)
    v[0] = 0

    while q:
        i = q.popleft()
        for st, et, wt in adj[i]:
            if v[et] > v[st] + wt:
                q.append(et)
                v[et] = v[st] + wt

    return v[N]


for test_case in range(1, T + 1):
    N, E = map(int, input().split())  # 노드 개수, 간선 개수
    adj = [
        [] for _ in range(N+1)
    ]
    v = [10000] * (N+1)
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((s, e, w))

    print(f'#{test_case}', bfs(0))

