
from collections import deque
N, K = map(int, input().split())
memo = [-1] * 100001

def bfs(start):
    q = deque()
    q.append(start)
    memo[start] = 0

    while q:
        cur = q.popleft()
        if cur == K:
            return memo[cur]

        if 0 <= cur-1 <= 100000 and memo[cur-1] == -1:
            memo[cur-1] = memo[cur] + 1
            q.append(cur-1)
        if 0 <= cur*2 <= 100000 and memo[cur*2] == -1:
            memo[cur*2] = memo[cur] + 0
            q.appendleft(cur*2)
        if 0 <= cur+1 <= 100000 and memo[cur+1] == -1:
            memo[cur+1] = memo[cur] + 1
            q.append(cur+1)

    return -1


print(bfs(N))