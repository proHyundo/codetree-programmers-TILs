from collections import deque
N = int(input())  # 컴퓨터 수
M = int(input())  # 네트워크 수
adj = [
    [] for _ in range(N+1)
]
ans = [False] * (N+1)

for _ in range(M):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)


def bfs():
    q = deque()
    q.append(1)
    ans[1] = True
    cnt = 0

    while q:
        cur = q.popleft()
        cnt += 1

        for nx in adj[cur]:
            if not ans[nx]:
                q.append(nx)
                ans[nx] = True
    return cnt - 1

print(bfs())
