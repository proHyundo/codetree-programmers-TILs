import sys
from collections import deque
N, K = map(int, input().split())
memo = [sys.maxsize] * 100001

def bfs(start):
    q = deque()
    q.append(start)
    memo[start] = 0

    while q:
        cur = q.popleft()
        if cur == K:
            return memo[cur]

        for nxt in [cur-1, cur+1]:
            if 0 < nxt <= 100000:
                q.append(nxt)
                memo[nxt] = min(memo[nxt], memo[cur] + 1)

        magic = cur * 2
        if 0 < magic <= 100000:
            q.append(magic)
            memo[magic] = min(memo[magic], memo[cur])

    return -1


print(bfs(N))