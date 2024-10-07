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

        if 0 <= cur-1 <= 100000 and (memo[cur-1] == sys.maxsize or memo[cur-1] > memo[cur]+1):
            memo[cur-1] = memo[cur] + 1
            q.append(cur-1)
        if 0 <= cur*2 <= 100000 and (memo[cur*2] == sys.maxsize or memo[cur*2] > memo[cur]):
            memo[cur*2] = memo[cur]
            q.append(cur*2)
        if 0 <= cur+1 <= 100000 and (memo[cur+1] == sys.maxsize or memo[cur+1] > memo[cur]+1):
            memo[cur+1] = memo[cur] + 1
            q.append(cur+1)

    return -1


print(bfs(N))