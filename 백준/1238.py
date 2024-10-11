import sys
import heapq
N, M, X = map(int, input().split())

# X -> node
adj_forward = [
    [] for _ in range(N+1)
]
# node -> X
adj_backward = [
    [] for _ in range(N+1)
]
answer = 0

for _ in range(M):
    s, e, t = map(int, input().split())
    adj_forward[s].append((e, t))
    adj_backward[e].append((s,t))

def dijk(s, edges):
    hq = []
    heapq.heappush(hq, (0, s))
    times = [sys.maxsize] * (N+1)
    times[s] = 0

    while hq:
        t, node = heapq.heappop(hq)
        if times[node] < t:
            continue

        for nxt, time in edges[node]:
            if times[nxt] > t + time:
                times[nxt] = t + time
                heapq.heappush(hq, (nxt, t+time))

forward = dijk(X, adj_forward)
backward = dijk(X, adj_backward)

for f, b in zip(forward, backward):
    answer = max(answer, f+b)

print(answer)