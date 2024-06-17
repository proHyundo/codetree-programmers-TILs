from collections import deque


def solution(n, results):
    answer = 0
    win_adj = [[] for _ in range(n + 1)]
    lose_adj = [[] for _ in range(n + 1)]
    for row in results:
        win_adj[row[0]].append(row[1])
        lose_adj[row[1]].append(row[0])

    def bfs(start):
        v = [False] * (n+1)

        q = deque()
        q.append(start)
        v[start] = True

        while q:
            cur = q.popleft()
            for nxt in win_adj[cur]:
                if not v[nxt]:
                    q.append(nxt)
                    v[nxt] = True

        q.append(start)

        while q:
            cur = q.popleft()
            for nxt in lose_adj[cur]:
                if not v[nxt]:
                    q.append(nxt)
                    v[nxt] = True

        return v.count(True) == n

    ans = 0
    for i in range(1, n+1):
        if bfs(i):
            ans += 1

    return ans


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
