from collections import deque


def solution(n, computers):
    answer = 0
    adj = [[] for _ in range(n + 1)]
    visited = [1] + [0] * n

    for i in range(n):
        for j in range(n):
            if i < j and computers[i][j] == 1:
                adj[i + 1].append(j + 1)
                adj[j + 1].append(i + 1)

    def bfs(start):
        q = deque()
        q.append(start)
        visited[start] = 1

        while q:
            node = q.popleft()
            for nxt in adj[node]:
                if visited[nxt] == 0:
                    q.append(nxt)
                    visited[nxt] = 1

    for i in range(1, n + 1):
        if visited[i] == 0 and len(adj[i]) > 0:
            print(i)
            bfs(i)
            answer += 1

    print(adj)
    print(visited)

    answer += visited.count(0)
    return answer

"""
2 번 째 풀이
from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False] * n

    def bfs(start):
        q = deque()
        q.append(start)
        visited[start] = True

        while q:
            cur_node = q.popleft()
            for nxt_node in range(n):
                if computers[cur_node][nxt_node] == 1 and cur_node != nxt_node and not visited[nxt_node]:
                    visited[nxt_node] = True
                    q.append(nxt_node)

    for node in range(n):
        if visited[node]:
            continue
        answer += 1
        bfs(node)

    return answer
"""
