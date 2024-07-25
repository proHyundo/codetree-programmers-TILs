from collections import deque

N, K = map(int, input().split())
R = 100001
v = [False] * R
c = [0] * R

def bfs(start, end):
    q = deque()
    q.append(start)

    while q:
        cur = q.popleft()
        if cur == end:
            return v[end]

        for nxt in (cur-1, cur+1, cur*2):
            if 0 <= nxt < R and not v[nxt]:
                v[nxt] = v[cur] + 1
                q.append(nxt)
                c[nxt] = cur

total_cnt = bfs(N, K)
paths = []

def find_path(end):
    before = end
    for _ in range(total_cnt+1):
        paths.append(before)
        before = c[before]


find_path(K)
print(total_cnt if total_cnt else 0)
print(*paths[::-1])