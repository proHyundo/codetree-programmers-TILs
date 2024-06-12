from collections import deque
import sys


def solution(n, edge):
    answer = 0
    adj = [[] for _ in range(n + 1)]
    v = [sys.maxsize] * (n + 1)
    for n1, n2 in edge:
        adj[n1].append(n2)
        adj[n2].append(n1)

    def bfs():
        q = deque()
        q.append(1)
        v[1] = 0

        while q:
            cur = q.popleft()
            for nxt in adj[cur]:
                if v[nxt] == sys.maxsize:
                    q.append(nxt)
                    v[nxt] = v[cur] + 1

        max_val = max(v[1:])
        return v.count(max_val)


    return bfs()