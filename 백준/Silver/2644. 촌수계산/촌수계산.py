from collections import deque
n = int(input())
t1, t2 = map(int, input().split())
m = int(input())

adj = [[] for _ in range(n+1)]
checked = [0] * (n+1)

for _ in range(m):
    i, j = map(int, input().split())
    adj[i].append(j)
    adj[j].append(i)


def bfs(start, end):
    q = deque()
    q.append(start)
    checked[start] = 1

    while q:
        current = q.popleft()

        if current == end:
            return checked[end] - 1

        for nxt in adj[current]:
            if checked[nxt] == 0:
                q.append(nxt)
                checked[nxt] = checked[current] + 1

    return -1


print(bfs(t1, t2))


